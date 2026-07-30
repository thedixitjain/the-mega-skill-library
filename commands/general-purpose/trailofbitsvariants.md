---
name: trailofbitsvariants
description: "Finds similar vulnerabilities using pattern-based analysis"
allowed-tools: "Read Grep Glob Bash Task"
category: general-purpose
source_repo: trailofbits/skills
source_path: "plugins/variant-analysis/commands/variants.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/variant-analysis/commands/variants.md
---


# Find Vulnerability Variants

**Arguments:** $ARGUMENTS

This command is context-driven. Use conversation context to understand:
1. The original bug/vulnerability that was found
2. The codebase to search

If context is unclear, ask for a description of the original vulnerability.

Invoke the `variant-analysis` skill for the full workflow.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/variant-analysis/commands/variants.md`
