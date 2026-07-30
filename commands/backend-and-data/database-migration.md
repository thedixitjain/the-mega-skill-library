---
name: database-migration
description: "Workflow command scaffold for database-migration in everything-claude-code."
category: backend-and-data
source_repo: affaan-m/ECC
source_path: ".claude/commands/database-migration.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/.claude/commands/database-migration.md
---
# /database-migration

Use this workflow when working on **database-migration** in `everything-claude-code`.

## Goal

Database schema changes with migration files

## Common Files

- `**/schema.*`
- `migrations/*`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Create migration file
- Update schema definitions
- Generate/update types

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `.claude/commands/database-migration.md`
