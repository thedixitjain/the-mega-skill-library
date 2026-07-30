---
name: prompt-optimize-legacy-shim
description: "Legacy slash-entry shim for the prompt-optimizer skill. Prefer the skill directly."
category: prompt-engineering
source_repo: affaan-m/ECC
source_path: "legacy-command-shims/commands/prompt-optimize.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/legacy-command-shims/commands/prompt-optimize.md
---
# Prompt Optimize (Legacy Shim)

Use this only if you still invoke `/prompt-optimize`. The maintained workflow lives in `skills/prompt-optimizer/SKILL.md`.

## Canonical Surface

- Prefer the `prompt-optimizer` skill directly.
- Keep this file only as a compatibility entry point.

## Arguments

`$ARGUMENTS`

## Delegation

Apply the `prompt-optimizer` skill.
- Keep it advisory-only: optimize the prompt, do not execute the task.
- Return the recommended ECC components plus a ready-to-run prompt.
- If the user actually wants direct execution, say so and tell them to make a normal task request instead of staying inside the shim.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `legacy-command-shims/commands/prompt-optimize.md`
