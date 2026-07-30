---
name: eval-command-legacy-shim
description: "Legacy slash-entry shim for the eval-harness skill. Prefer the skill directly."
category: ai-agents-and-harness
source_repo: affaan-m/ECC
source_path: "legacy-command-shims/commands/eval.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/legacy-command-shims/commands/eval.md
---
# Eval Command (Legacy Shim)

Use this only if you still invoke `/eval`. The maintained workflow lives in `skills/eval-harness/SKILL.md`.

## Canonical Surface

- Prefer the `eval-harness` skill directly.
- Keep this file only as a compatibility entry point.

## Arguments

`$ARGUMENTS`

## Delegation

Apply the `eval-harness` skill.
- Support the same user intents as before: define, check, report, list, and cleanup.
- Keep evals capability-first, regression-backed, and evidence-based.
- Use the skill as the canonical evaluator instead of maintaining a separate command-specific playbook.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `legacy-command-shims/commands/eval.md`
