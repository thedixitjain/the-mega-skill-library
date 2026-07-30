---
name: feature-development
description: "Workflow command scaffold for feature-development in everything-claude-code."
category: general-purpose
source_repo: affaan-m/ECC
source_path: ".claude/commands/feature-development.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/.claude/commands/feature-development.md
---
# /feature-development

Use this workflow when working on **feature-development** in `everything-claude-code`.

## Goal

Standard feature implementation workflow

## Common Files

- `manifests/*`
- `schemas/*`
- `**/*.test.*`
- `**/api/**`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Add feature implementation
- Add tests for feature
- Update documentation

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `.claude/commands/feature-development.md`
