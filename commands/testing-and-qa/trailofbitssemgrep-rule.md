---
name: trailofbitssemgrep-rule
description: "Creates Semgrep rules with test-first methodology"
allowed-tools: "Bash Read Write Edit Glob Grep WebFetch"
category: testing-and-qa
source_repo: trailofbits/skills
source_path: "plugins/semgrep-rule-creator/commands/semgrep-rule.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/semgrep-rule-creator/commands/semgrep-rule.md
---


# Create Semgrep Rule

**Arguments:** $ARGUMENTS

This command is context-driven. Use conversation context to understand:
1. The vulnerability or pattern to detect
2. The target language
3. Whether taint mode is appropriate

If context is unclear, ask for a description of the pattern to detect.

Invoke the `semgrep-rule-creator` skill for the full workflow.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/semgrep-rule-creator/commands/semgrep-rule.md`
