---
name: agent-sort-legacy-shim
description: "Legacy slash-entry shim for the agent-sort skill. Prefer the skill directly."
category: ai-agents-and-harness
source_repo: affaan-m/ECC
source_path: "legacy-command-shims/commands/agent-sort.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/legacy-command-shims/commands/agent-sort.md
---
# Agent Sort (Legacy Shim)

Use this only if you still invoke `/agent-sort`. The maintained workflow lives in `skills/agent-sort/SKILL.md`.

## Canonical Surface

- Prefer the `agent-sort` skill directly.
- Keep this file only as a compatibility entry point.

## Arguments

`$ARGUMENTS`

## Delegation

Apply the `agent-sort` skill.
- Classify ECC surfaces with concrete repo evidence.
- Keep the result to DAILY vs LIBRARY.
- If an install change is needed afterward, hand off to `configure-ecc` instead of re-implementing install logic here.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `legacy-command-shims/commands/agent-sort.md`
