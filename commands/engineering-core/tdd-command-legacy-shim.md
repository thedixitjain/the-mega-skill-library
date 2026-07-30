---
name: tdd-command-legacy-shim
description: "Legacy slash-entry shim for the tdd-workflow skill. Prefer the skill directly."
category: engineering-core
source_repo: affaan-m/ECC
source_path: "legacy-command-shims/commands/tdd.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/legacy-command-shims/commands/tdd.md
---
# TDD Command (Legacy Shim)

Use this only if you still invoke `/tdd`. The maintained workflow lives in `skills/tdd-workflow/SKILL.md`.

## Canonical Surface

- Prefer the `tdd-workflow` skill directly.
- Keep this file only as a compatibility entry point.

## Arguments

`$ARGUMENTS`

## Delegation

Apply the `tdd-workflow` skill.
- Stay strict on RED -> GREEN -> REFACTOR.
- Keep tests first, coverage explicit, and checkpoint evidence clear.
- Use the skill as the maintained TDD body instead of duplicating the playbook here.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `legacy-command-shims/commands/tdd.md`
