---
name: orchestrate-command-legacy-shim
description: "Legacy slash-entry shim for dmux-workflows and autonomous-agent-harness. Prefer the skills directly."
category: ai-agents-and-harness
source_repo: affaan-m/ECC
source_path: "legacy-command-shims/commands/orchestrate.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/legacy-command-shims/commands/orchestrate.md
---
# Orchestrate Command (Legacy Shim)

Use this only if you still invoke `/orchestrate`. The maintained orchestration guidance lives in `skills/dmux-workflows/SKILL.md` and `skills/autonomous-agent-harness/SKILL.md`.

## Canonical Surface

- Prefer `dmux-workflows` for parallel panes, worktrees, and multi-agent splits.
- Prefer `autonomous-agent-harness` for longer-running loops, governance, scheduling, and control-plane style execution.
- Keep this file only as a compatibility entry point.

## Arguments

`$ARGUMENTS`

## Delegation

Apply the orchestration skills instead of maintaining a second workflow spec here.
- Start with `dmux-workflows` for split/parallel execution.
- Pull in `autonomous-agent-harness` when the user is really asking for persistent loops, governance, or operator-layer behavior.
- Keep handoffs structured, but let the skills define the maintained sequencing rules.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `legacy-command-shims/commands/orchestrate.md`
