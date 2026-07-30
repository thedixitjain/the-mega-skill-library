---
name: trailofbitsaudit-context
description: "Builds deep architectural context before vulnerability hunting"
allowed-tools: "Read Grep Glob Bash Task"
category: security-and-compliance
source_repo: trailofbits/skills
source_path: "plugins/audit-context-building/commands/audit-context.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/audit-context-building/commands/audit-context.md
---


# Build Audit Context

**Arguments:** $ARGUMENTS

Parse arguments:
1. **Codebase path** (required): Path to codebase to analyze
2. **Focus** (optional): `--focus <module>` for specific module analysis

Invoke the `audit-context-building` skill with these arguments for the full workflow.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/audit-context-building/commands/audit-context.md`
