---
name: docs-command-legacy-shim
description: "Legacy slash-entry shim for the documentation-lookup skill. Prefer the skill directly."
category: docs-and-knowledge-mgmt
source_repo: affaan-m/ECC
source_path: "legacy-command-shims/commands/docs.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/legacy-command-shims/commands/docs.md
---
# Docs Command (Legacy Shim)

Use this only if you still reach for `/docs`. The maintained workflow lives in `skills/documentation-lookup/SKILL.md`.

## Canonical Surface

- Prefer the `documentation-lookup` skill directly.
- Keep this file only as a compatibility entry point.

## Arguments

`$ARGUMENTS`

## Delegation

Apply the `documentation-lookup` skill.
- If the library or the question is missing, ask for the missing part.
- Use live documentation through Context7 instead of training data.
- Return only the current answer and the minimum code/example surface needed.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `legacy-command-shims/commands/docs.md`
