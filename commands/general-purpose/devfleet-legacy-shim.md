---
name: devfleet-legacy-shim
description: "Legacy slash-entry shim for the claude-devfleet skill. Prefer the skill directly."
category: general-purpose
source_repo: affaan-m/ECC
source_path: "legacy-command-shims/commands/devfleet.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/legacy-command-shims/commands/devfleet.md
---
# DevFleet (Legacy Shim)

Use this only if you still call `/devfleet`. The maintained workflow lives in `skills/claude-devfleet/SKILL.md`.

## Canonical Surface

- Prefer the `claude-devfleet` skill directly.
- Keep this file only as a compatibility entry point while command-first usage is retired.

## Arguments

`$ARGUMENTS`

## Delegation

Apply the `claude-devfleet` skill.
- Plan from the user's description, show the DAG, and get approval before dispatch unless the user already said to proceed.
- Prefer polling status over blocking waits for long missions.
- Report mission IDs, files changed, failures, and next steps from structured mission reports.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `legacy-command-shims/commands/devfleet.md`
