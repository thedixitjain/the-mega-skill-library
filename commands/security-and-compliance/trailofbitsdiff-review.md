---
name: trailofbitsdiff-review
description: "Performs security-focused differential review of code changes"
allowed-tools: "Read Write Grep Glob Bash"
category: security-and-compliance
source_repo: trailofbits/skills
source_path: "plugins/differential-review/commands/diff-review.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/differential-review/commands/diff-review.md
---


# Differential Security Review

**Arguments:** $ARGUMENTS

Parse arguments:
1. **Target** (required): PR URL, commit SHA, or diff path
2. **Baseline** (optional): `--baseline <ref>` for comparison reference

Invoke the `differential-review` skill with these arguments for the full workflow.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/differential-review/commands/diff-review.md`
