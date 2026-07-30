---
name: verification-command-legacy-shim
description: "Legacy slash-entry shim for the verification-loop skill. Prefer the skill directly."
category: general-purpose
source_repo: affaan-m/ECC
source_path: "legacy-command-shims/commands/verify.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/legacy-command-shims/commands/verify.md
---
# Verification Command (Legacy Shim)

Use this only if you still invoke `/verify`. The maintained workflow lives in `skills/verification-loop/SKILL.md`.

## Canonical Surface

- Prefer the `verification-loop` skill directly.
- Keep this file only as a compatibility entry point.

## Arguments

`$ARGUMENTS`

## Delegation

Apply the `verification-loop` skill.
- Choose the right verification depth for the user's requested mode.
- Run build, types, lint, tests, security/log checks, and diff review in the right order for the current repo.
- Report only the verdicts and blockers instead of maintaining a second verification checklist here.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `legacy-command-shims/commands/verify.md`
