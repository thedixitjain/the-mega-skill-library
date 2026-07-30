import { mkdirSync, mkdtempSync, rmSync, symlinkSync, utimesSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterEach, describe, expect, it } from "vitest";
import { readPlanStatus, resolvePlanPaths } from "../plan.ts";
import { planLabel } from "../runtime.ts";

// Issue #208: the Pi session cwd follows the live shell. Before v3.8.1 an
// agent that cd'd into a subdirectory lost the project's plan entirely
// (scope=none, recitation dark, "No task_plan.md found" warning on every
// write/edit). Resolution now anchors on the nearest ancestor with planning
// state, bounded by a .git repository boundary and a depth cap.

const tempRoots: string[] = [];

function makeWorkspace(): string {
	const cwd = mkdtempSync(join(tmpdir(), "pwf-pi-anchor-"));
	tempRoots.push(cwd);
	return cwd;
}

function writeScopedPlan(root: string, id: string, content: string): void {
	const planDir = join(root, ".planning", id);
	mkdirSync(planDir, { recursive: true });
	writeFileSync(join(planDir, "task_plan.md"), content);
}

function writeRootPlan(root: string, content: string): void {
	writeFileSync(join(root, "task_plan.md"), content);
}

afterEach(() => {
	while (tempRoots.length > 0) {
		const root = tempRoots.pop();
		if (root) rmSync(root, { recursive: true, force: true });
	}
});

describe("resolvePlanPaths anchor walk (#208)", () => {
	it("resolves the ancestor scoped plan from a subdirectory", () => {
		const root = makeWorkspace();
		writeScopedPlan(root, "2026-07-21-demo", "# Task Plan: demo\n### Phase 1\n- **Status:** in_progress\n");
		const sub = join(root, "src", "nested");
		mkdirSync(sub, { recursive: true });

		const paths = resolvePlanPaths(sub);
		expect(paths.scope).toBe("scoped");
		expect(paths.planId).toBe("2026-07-21-demo");

		const status = readPlanStatus(sub);
		expect(status.exists).toBe(true);
	});

	it("resolves the ancestor root plan from a subdirectory", () => {
		const root = makeWorkspace();
		writeRootPlan(root, "# Task Plan: rooty\n### Phase 1\n- **Status:** complete\n");
		const sub = join(root, "lib");
		mkdirSync(sub, { recursive: true });

		const paths = resolvePlanPaths(sub);
		expect(paths.scope).toBe("root");
		expect(paths.planPath).toBe(join(root, "task_plan.md"));
	});

	it("does not walk past a .git repository boundary", () => {
		const outer = makeWorkspace();
		writeScopedPlan(outer, "2026-07-21-outer", "# Task Plan: outer\n");
		const repo = join(outer, "inner-repo");
		mkdirSync(join(repo, ".git"), { recursive: true });
		const sub = join(repo, "src");
		mkdirSync(sub, { recursive: true });

		// From inside inner-repo (which has no plan), the outer plan must not
		// leak in: the .git boundary stops the walk.
		expect(resolvePlanPaths(sub).scope).toBe("none");
		expect(resolvePlanPaths(repo).scope).toBe("none");
	});

	it("keeps slug-beats-root precedence at the anchor (documented since v2.40.0)", () => {
		const root = makeWorkspace();
		writeRootPlan(root, "# Task Plan: FRESH ROOT\n### Phase 1\n- **Status:** complete\n");
		writeScopedPlan(root, "2026-01-01-stale-old", "# Task Plan: STALE OLD\n### Phase 1\n- **Status:** in_progress\n");

		const paths = resolvePlanPaths(root);
		expect(paths.scope).toBe("scoped");
		expect(paths.planId).toBe("2026-01-01-stale-old");
	});

	it("still reports none when no ancestor carries planning state", () => {
		const root = makeWorkspace();
		const sub = join(root, "plain", "dir");
		mkdirSync(sub, { recursive: true });
		expect(resolvePlanPaths(sub).scope).toBe("none");
		expect(readPlanStatus(sub).exists).toBe(false);
	});

	it("respects an explicit PLAN_ID pin from a subdirectory", () => {
		const root = makeWorkspace();
		writeScopedPlan(root, "2026-07-21-pinned", "# Task Plan: pinned\n");
		writeScopedPlan(root, "2026-07-21-newer", "# Task Plan: newer\n");
		const sub = join(root, "deep");
		mkdirSync(sub, { recursive: true });

		const previous = process.env.PLAN_ID;
		process.env.PLAN_ID = "2026-07-21-pinned";
		try {
			const paths = resolvePlanPaths(sub);
			expect(paths.scope).toBe("scoped");
			expect(paths.planId).toBe("2026-07-21-pinned");
		} finally {
			if (previous === undefined) delete process.env.PLAN_ID;
			else process.env.PLAN_ID = previous;
		}
	});
});

describe("slug validation and containment parity with the sh resolver (v3.8.1)", () => {
	it("rejects a traversal PLAN_ID instead of escaping .planning", () => {
		const root = makeWorkspace();
		mkdirSync(join(root, "project", ".planning"), { recursive: true });
		mkdirSync(join(root, "outside"), { recursive: true });
		writeFileSync(join(root, "outside", "task_plan.md"), "# escaped");

		const previous = process.env.PLAN_ID;
		process.env.PLAN_ID = "../../outside";
		try {
			const paths = resolvePlanPaths(join(root, "project"));
			expect(paths.scope).not.toBe("scoped");
			expect(paths.planPath ?? "").not.toContain("outside");
		} finally {
			if (previous === undefined) delete process.env.PLAN_ID;
			else process.env.PLAN_ID = previous;
		}
	});

	it("rejects a PLAN_ID containing whitespace", () => {
		const root = makeWorkspace();
		writeScopedPlan(root, "plan a", "# spaced");
		writeScopedPlan(root, "plan-fallback", "# fallback");

		const previous = process.env.PLAN_ID;
		process.env.PLAN_ID = "plan a";
		try {
			const paths = resolvePlanPaths(root);
			expect(paths.planId).toBe("plan-fallback");
		} finally {
			if (previous === undefined) delete process.env.PLAN_ID;
			else process.env.PLAN_ID = previous;
		}
	});

	it("rejects a hidden .active_plan target and falls through", () => {
		const root = makeWorkspace();
		writeScopedPlan(root, ".hidden-plan", "# hidden");
		writeScopedPlan(root, "plan-a", "# visible");
		writeFileSync(join(root, ".planning", ".active_plan"), ".hidden-plan");

		const paths = resolvePlanPaths(root);
		expect(paths.planId).toBe("plan-a");
	});

	it("newest scan skips slug-invalid directory names", () => {
		const root = makeWorkspace();
		writeScopedPlan(root, "plan-valid", "# valid");
		const bad = join(root, ".planning", "plan invalid name");
		mkdirSync(bad, { recursive: true });
		writeFileSync(join(bad, "task_plan.md"), "# bad");
		const future = Date.now() / 1000 + 300;
		utimesSync(join(bad, "task_plan.md"), future, future);

		const paths = resolvePlanPaths(root);
		expect(paths.planId).toBe("plan-valid");
	});

	it("rejects a junctioned slug dir pointing outside the project", () => {
		const root = makeWorkspace();
		const outside = join(root, "outside-target");
		mkdirSync(outside, { recursive: true });
		writeFileSync(join(outside, "task_plan.md"), "# outside");
		const project = join(root, "project");
		mkdirSync(join(project, ".planning"), { recursive: true });
		try {
			symlinkSync(outside, join(project, ".planning", "2026-07-21-evil"), "junction");
		} catch {
			return; // junction creation not permitted on this runner; nothing to assert
		}

		const paths = resolvePlanPaths(project);
		expect(paths.scope).not.toBe("scoped");
	});

	it("sanitizes the injected plan label", () => {
		const status = {
			scope: "scoped",
			planId: "evil`slug with spaces{and}stuff",
		} as unknown as Parameters<typeof planLabel>[0];
		const label = planLabel(status);
		expect(label.startsWith("plan: ")).toBe(true);
		expect(label.slice(6)).toMatch(/^[A-Za-z0-9._-]+$/);
	});
});
