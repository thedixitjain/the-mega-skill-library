import { existsSync, readFileSync, readdirSync, realpathSync, statSync } from "node:fs";
import { basename, dirname, join, sep } from "node:path";

export type PlanScope = "scoped" | "root" | "none";

export interface PlanPaths {
	cwd: string;
	scope: PlanScope;
	planPath?: string;
	progressPath?: string;
	findingsPath?: string;
	planDir?: string;
	planId?: string;
	attestationCandidates: string[];
}

export interface PlanStatus extends PlanPaths {
	exists: boolean;
	closed: boolean;
	totalPhases: number;
	completePhases: number;
	inProgressPhases: number;
	pendingPhases: number;
	firstLines50: string;
	headLines30: string;
	progressTail20: string;
}

function safeRead(path: string): string {
	try {
		return readFileSync(path, "utf-8");
	} catch {
		return "";
	}
}

function resolveNewestPlanDir(planRoot: string): string | undefined {
	if (!existsSync(planRoot)) return undefined;

	const dirs = readdirSync(planRoot, { withFileTypes: true })
		.filter((entry) => entry.isDirectory() && !entry.name.startsWith(".") && SLUG_RE.test(entry.name))
		.map((entry) => join(planRoot, entry.name))
		.filter((dir) => existsSync(join(dir, "task_plan.md")))
		.map((dir) => {
			let mtime = 0;
			try {
				// Rank by task_plan.md mtime, not the directory: editing a plan's contents does not bump the dir mtime, which let a completed plan lose to a stale sibling (#203).
				mtime = statSync(join(dir, "task_plan.md")).mtimeMs;
			} catch {
				mtime = 0;
			}
			return { dir, mtime };
		})
		.sort((a, b) => b.mtime - a.mtime);

	return dirs[0]?.dir;
}

// Same shape as the sh resolver's slug_is_valid: first char [A-Za-z0-9_],
// rest [A-Za-z0-9._-]. Blocks traversal tokens (no separators), hidden names,
// and whitespace before any path is built; keeps Pi resolution in lockstep
// with resolve-plan-dir.sh on the same trees.
const SLUG_RE = /^[A-Za-z0-9_][A-Za-z0-9._-]*$/;

// Containment (security A1.3 parity with the sh resolver): a scoped candidate
// must canonicalize to a path under the anchor, or a symlinked/junctioned
// slug dir could hand the hooks an arbitrary file outside the project. Fails
// closed on canonicalization failure, matching resolve-plan-dir.sh.
function isWithinRoot(root: string, candidate: string): boolean {
	let rootReal: string;
	let candReal: string;
	try {
		rootReal = realpathSync(root);
		candReal = realpathSync(candidate);
	} catch {
		return false;
	}
	if (candReal === rootReal) return true;
	return candReal.startsWith(rootReal.endsWith(sep) ? rootReal : rootReal + sep);
}

const ANCHOR_WALK_CAP = 10;

// The Pi session cwd follows the live shell, so an agent that cd's into a
// subdirectory used to lose the project's plan entirely: resolution found
// nothing, recitation went dark, and the "No task_plan.md found" warning
// fired on every write/edit (#208). Anchor resolution walks parents until a
// directory carries planning state (.planning/ or task_plan.md). A .git
// boundary without planning state, or the depth cap, stops the walk so a
// plan outside the repository can never leak into the session. Exported so
// runtime consumers that take a directory (attachment gate, mode config,
// script cwds) resolve from the same anchor as the plan itself.
export function resolveAnchor(cwd: string): string {
	let dir = cwd;
	for (let depth = 0; depth < ANCHOR_WALK_CAP; depth++) {
		if (existsSync(join(dir, ".planning")) || existsSync(join(dir, "task_plan.md"))) {
			return dir;
		}
		const parent = dirname(dir);
		if (existsSync(join(dir, ".git")) || parent === dir) {
			return cwd;
		}
		dir = parent;
	}
	return cwd;
}

export function resolvePlanPaths(sessionCwd: string): PlanPaths {
	// All plan paths are built on the anchor (the nearest ancestor with
	// planning state), not the raw shell cwd. The returned cwd field carries
	// the anchor; runtime call sites that take a directory route through
	// resolveAnchor/anchorCwd so they land on the same plan.
	const cwd = resolveAnchor(sessionCwd);
	const planRoot = join(cwd, ".planning");

	const makeScoped = (planDir: string): PlanPaths => ({
		cwd,
		scope: "scoped",
		planDir,
		planId: basename(planDir),
		planPath: join(planDir, "task_plan.md"),
		progressPath: join(planDir, "progress.md"),
		findingsPath: join(planDir, "findings.md"),
		attestationCandidates: [join(planDir, ".attestation"), join(cwd, ".plan-attestation")],
	});

	const makeRoot = (): PlanPaths => ({
		cwd,
		scope: "root",
		planPath: join(cwd, "task_plan.md"),
		progressPath: join(cwd, "progress.md"),
		findingsPath: join(cwd, "findings.md"),
		attestationCandidates: [join(cwd, ".plan-attestation")],
	});

	const planId = process.env.PLAN_ID?.trim();
	if (planId && SLUG_RE.test(planId)) {
		const candidate = join(planRoot, planId);
		if (existsSync(join(candidate, "task_plan.md")) && isWithinRoot(cwd, candidate)) {
			return makeScoped(candidate);
		}
	}

	const activePlanFile = join(planRoot, ".active_plan");
	if (existsSync(activePlanFile)) {
		const activePlanId = safeRead(activePlanFile).trim();
		if (activePlanId && SLUG_RE.test(activePlanId)) {
			const candidate = join(planRoot, activePlanId);
			if (existsSync(join(candidate, "task_plan.md")) && isWithinRoot(cwd, candidate)) {
				return makeScoped(candidate);
			}
		}
	}

	const newest = resolveNewestPlanDir(planRoot);
	// Containment is checked on the winner only; a rejected winner falls
	// through to root/none (the safe direction) rather than promoting the
	// next-newest sibling.
	if (newest && isWithinRoot(cwd, newest)) {
		return makeScoped(newest);
	}

	const rootPlan = makeRoot();
	if (rootPlan.planPath && existsSync(rootPlan.planPath)) {
		return rootPlan;
	}

	return {
		cwd,
		scope: "none",
		attestationCandidates: [join(cwd, ".plan-attestation")],
	};
}

export function readPlanStatus(cwd: string): PlanStatus {
	const paths = resolvePlanPaths(cwd);
	if (!paths.planPath || !existsSync(paths.planPath)) {
		return {
			...paths,
			exists: false,
			closed: false,
			totalPhases: 0,
			completePhases: 0,
			inProgressPhases: 0,
			pendingPhases: 0,
			firstLines50: "",
			headLines30: "",
			progressTail20: "",
		};
	}

	const planContent = safeRead(paths.planPath);
	const closed = /<!--\s*pwf:\s*closed\s*-->/i.test(planContent);
	const lines = planContent.split("\n");

	const phaseRegex = /^###\s+Phase\b/i;
	const statusComplete = /\*\*Status:\*\*\s*complete\b/i;
	const statusInProgress = /\*\*Status:\*\*\s*in_progress\b/i;
	const statusPending = /\*\*Status:\*\*\s*pending\b/i;

	let total = 0;
	let complete = 0;
	let inProgress = 0;
	let pending = 0;

	for (const line of lines) {
		if (phaseRegex.test(line)) total += 1;
		if (statusComplete.test(line)) complete += 1;
		else if (statusInProgress.test(line)) inProgress += 1;
		else if (statusPending.test(line)) pending += 1;
	}

	if (complete + inProgress + pending === 0) {
		complete = (planContent.match(/\[complete\]/gi) || []).length;
		inProgress = (planContent.match(/\[in_progress\]/gi) || []).length;
		pending = (planContent.match(/\[pending\]/gi) || []).length;
	}

	let progressTail20 = "";
	if (paths.progressPath && existsSync(paths.progressPath)) {
		const progressLines = safeRead(paths.progressPath).split("\n");
		progressTail20 = progressLines.slice(-20).join("\n");
	}

	return {
		...paths,
		exists: true,
		closed,
		totalPhases: total,
		completePhases: complete,
		inProgressPhases: inProgress,
		pendingPhases: pending,
		firstLines50: lines.slice(0, 50).join("\n"),
		headLines30: lines.slice(0, 30).join("\n"),
		progressTail20,
	};
}

export function isAllPhasesComplete(status: PlanStatus): boolean {
	return status.exists && status.totalPhases > 0 && status.completePhases >= status.totalPhases;
}

export function isPlanIncomplete(status: PlanStatus): boolean {
	return status.exists && status.totalPhases > 0 && status.completePhases < status.totalPhases;
}

export function isSessionAttached(cwd: string, sessionId: string | undefined): boolean {
	const sessionsDir = join(cwd, ".planning", "sessions");
	if (!existsSync(sessionsDir)) return true;
	if (!sessionId) return false;
	return existsSync(join(sessionsDir, `${sessionId}.attached`));
}
