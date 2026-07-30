---
name: trailofbitsct-check
description: "Detects timing side-channels in cryptographic code"
allowed-tools: "Bash Read Grep Glob"
category: general-purpose
source_repo: trailofbits/skills
source_path: "plugins/constant-time-analysis/commands/ct-check.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/constant-time-analysis/commands/ct-check.md
---


# Check Constant-Time Properties

**Arguments:** $ARGUMENTS

Parse arguments:
1. **Source file** (required): Path to source file to analyze
2. **Flags** (optional): `--warnings`, `--json`, `--arch <arch>`, `--opt-level <level>`, `--func <pattern>`

Invoke the `constant-time-analysis` skill with these arguments for the full workflow.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/constant-time-analysis/commands/ct-check.md`
