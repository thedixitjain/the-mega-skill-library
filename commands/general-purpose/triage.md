---
name: triage
description: "Triage open GitHub issues on jayminwest/overstory: classify, prioritize, label, deduplicate, and identify issues that should be closed. Apply labels directly to GitHub issues. Return a consolidated report to the developer."
category: general-purpose
source_repo: jayminwest/overstory
source_path: ".claude/commands/triage.md"
source_url: https://github.com/jayminwest/overstory/blob/HEAD/.claude/commands/triage.md
---
## intro

Triage open GitHub issues on `jayminwest/overstory`: classify, prioritize, label, deduplicate, and identify issues that should be closed. Apply labels directly to GitHub issues. Return a consolidated report to the developer.

**Argument:** `$ARGUMENTS` — optional issue number(s) to triage (e.g., `5` or `5 8 12`). If empty, triage all open issues.

**Delegation principle:** You are a coordinator, not a solo worker. Spawn parallel subagents for every phase that can be parallelized. Minimize serial work. Use the Task tool aggressively.

## label-taxonomy

Use these predefined labels when classifying issues. Each issue gets exactly one `area:` label, one `priority:` label, one `difficulty:` label, and optionally one `focus:` label.

### Area labels (one required — matches src/ subsystem boundaries)
- `area:runtimes` — Runtime adapters and spawning (src/runtimes/, src/worktree/). Covers Claude, Pi, Copilot, Codex, Gemini, Sapling, OpenCode, plus new adapter requests (Cursor, Fireworks, etc.)
- `area:agent-lifecycle` — Agent identity, sessions, checkpoint/resume, sling command (src/agents/, src/sessions/)
- `area:communication` — Mail system, nudge, tracker integration, dispatch protocol (src/mail/, src/tracker/)
- `area:merge` — Merge queue, tiered conflict resolution (src/merge/)
- `area:observability` — Status, dashboard, inspect, trace, logs, feed, replay, costs, metrics, watchdog (src/events/, src/metrics/, src/logging/, src/watchdog/, src/insights/)
- `area:coordination` — Coordinator, lead hierarchy, groups, multi-agent orchestration (src/commands/coordinator.ts, src/commands/group.ts)
- `area:initialization` — ov init, bootstrap, config loading/validation, ov doctor (src/config.ts, src/commands/init.ts, src/doctor/)
- `area:infrastructure` — Hooks, guard rules, worktree management, CLI framework (src/agents/hooks-deployer.ts, src/agents/guard-rules.ts, src/commands/hooks.ts)
- `area:docs` — Documentation, README, examples, guides

### Priority labels (one required)
- `priority:critical` — Blocks users or breaks core functionality
- `priority:high` — Significant improvement, clear path to implement
- `priority:medium` — Useful but not urgent, well-scoped
- `priority:low` — Nice-to-have, unclear scope, or minimal impact
- `priority:backlog` — Deferred indefinitely

### Difficulty labels (one required)
- `difficulty:starter` — Good first issue, well-scoped, minimal context needed
- `difficulty:moderate` — Requires understanding of 1-2 subsystems
- `difficulty:complex` — Cross-cutting, architectural, or high-risk

### Focus labels (optional — cross-cutting concerns and current hot zones)
- `focus:headless-mode` — The `-p` flag transition from interactive tmux TUI to headless spawning
- `focus:copilot` — Copilot runtime-specific issues (model aliases, hooks, auto-detection)
- `focus:windows` — Windows/WSL2 support (mprocs, psmux, SessionBackend abstraction)
- `focus:reliability` — Stall detection, recovery, cleanup, session DB hygiene
- `focus:sandbox` — Process isolation (Seatbelt on macOS, Landlock on Linux, containers)

## steps

### 1. Ensure labels exist on the repo

Before triaging, verify all labels from the taxonomy exist on the GitHub repo. Run:
```bash
gh label list --repo jayminwest/overstory --json name
```

For any missing labels, create them:
```bash
gh label create "<label-name>" --repo jayminwest/overstory --description "<description>" --color "<hex>"
```

Use these colors:
- `area:*` — `0075ca` (blue)
- `priority:critical` — `b60205` (red)
- `priority:high` — `d93f0b` (orange)
- `priority:medium` — `fbca04` (yellow)
- `priority:low` — `c2e0c6` (light green)
- `priority:backlog` — `d4c5f9` (lavender)
- `difficulty:*` — `bfd4f2` (light blue)
- `focus:*` — `e4e669` (olive)

### 2. Fetch open issues

- If `$ARGUMENTS` contains issue number(s), fetch only those
- Otherwise: `gh issue list --repo jayminwest/overstory --state open --limit 100 --json number,title,body,author,labels,createdAt,updatedAt,comments`
- If there are no open issues, say so and stop

### 3. Spawn triage team (parallel subagents)

Use the Task tool to spawn **parallel agents** — one per issue (or batch 2-3 per agent if there are many). Each agent receives a single issue (or small batch) and performs the full triage below.

**Each triage agent should:**

#### a. Analyze the issue
- Read the full issue body and all comments: `gh issue view <number> --json title,body,author,labels,comments,createdAt,updatedAt`
- Search the codebase for related code using Grep/Glob on keywords, file paths, function names mentioned
- Check for related open PRs: `gh pr list --state open --search "<keywords>"`

#### b. Classify
- **Type:** `bug` | `feature` | `task` | `epic` (use existing GH labels `bug`/`enhancement` where they map)
- **Area label:** Pick the single best `area:*` from the taxonomy (required)
- **Priority label:** Pick one `priority:*` label (required)
- **Difficulty label:** Pick one `difficulty:*` label (required)
- **Focus label:** Pick a `focus:*` label if a cross-cutting concern applies (optional)

#### c. Assess quality
Determine if the issue is actionable or should be closed. Flag for closure if:
- **Too vague:** No clear problem statement or acceptance criteria
- **Too broad:** Scope is unbounded, should be split into multiple issues
- **Duplicate:** Another open issue covers the same work (cite the duplicate)
- **Stale:** Old issue that references code/architecture that no longer exists
- **Wontfix:** Doesn't align with overstory's direction (agent orchestration, Bun-native, zero runtime deps)

For issues flagged for closure, draft a **suggested closing comment** (polite, specific, actionable — e.g., suggest how to refile if too vague).

#### d. Deduplicate against other GitHub issues
- Compare against ALL other open issues in the current batch
- Flag pairs that describe the same underlying work
- Recommend which to keep and which to close-as-duplicate

#### e. Return structured result
Each agent returns:
```
Issue: #<number> — <title>
Author: <login>
Type: bug | feature | task | epic
Priority: priority:<x>
Labels: area:<x>, difficulty:<x>, [focus:<x>]
Scope: Small (1-2 files) | Medium (3-5 files) | Large (6+ files)
Action: LABEL | CLOSE
Close reason: (if CLOSE) too-vague | too-broad | duplicate | stale | wontfix
Suggested comment: (if CLOSE) "<draft comment>"
Summary: 2-3 sentence assessment
Related files: key files/subsystems affected
Duplicate of: #<number> (if applicable)
```

### 4. Consolidate results

After all triage agents complete, consolidate into a single report.

### 5. Spawn a dedup verification agent

Spawn one additional agent to cross-check all duplicate pairs identified by the triage agents. This agent should:
- Read both issues in each flagged pair
- Confirm or reject the duplicate determination
- Look for duplicates the individual agents may have missed (issues triaged by different agents)

### 6. Apply labels to GitHub issues

For every issue with `Action: LABEL`, apply the classified labels:
```bash
gh issue edit <number> --repo jayminwest/overstory --add-label "area:<x>,priority:<x>,difficulty:<x>" [--add-label "focus:<x>"]
```

Do NOT label or modify issues with `Action: CLOSE` — those are presented to the developer for manual decision.

### 7. Present final report

#### Summary table (sorted by priority, then type)

| # | Title | Type | Priority | Area | Difficulty | Focus | Scope | Action |
|---|-------|------|----------|------|------------|-------|-------|--------|

#### Issues to close (with suggested comments)

For each issue recommended for closure:
- **Issue:** `#<number> — <title>`
- **Reason:** too-vague | too-broad | duplicate | stale | wontfix
- **Suggested comment:**
  > <draft comment for the developer to copy-paste or edit>

#### Duplicate clusters

Group issues that cover overlapping work. Recommend which to keep.

#### Cross-cutting observations

- Themes across the issue landscape
- Areas accumulating the most issues
- Suggestions for issues that should exist but don't

#### Labels applied

List each issue number and the labels that were applied to it.

---

**Source:** [`jayminwest/overstory`](https://github.com/jayminwest/overstory) → `.claude/commands/triage.md`
