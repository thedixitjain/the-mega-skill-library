---
name: e2e-command-legacy-shim
description: "Legacy slash-entry shim for the e2e-testing skill. Prefer the skill directly."
category: testing-and-qa
source_repo: affaan-m/ECC
source_path: "legacy-command-shims/commands/e2e.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/legacy-command-shims/commands/e2e.md
---
# E2E Command (Legacy Shim)

Use this only if you still invoke `/e2e`. The maintained workflow lives in `skills/e2e-testing/SKILL.md`.

## Canonical Surface

- Prefer the `e2e-testing` skill directly.
- Keep this file only as a compatibility entry point.

## Arguments

`$ARGUMENTS`

## Delegation

Apply the `e2e-testing` skill.
- Generate or update Playwright coverage for the requested user flow.
- Run only the relevant tests unless the user explicitly asked for the entire suite.
- Capture the usual artifacts and report failures, flake risk, and next fixes without duplicating the full skill body here.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `legacy-command-shims/commands/e2e.md`
