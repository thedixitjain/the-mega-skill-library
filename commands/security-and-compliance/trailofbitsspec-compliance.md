---
name: trailofbitsspec-compliance
description: "Verifies code implements specification requirements"
allowed-tools: "Read Write Grep Glob Bash WebFetch"
category: security-and-compliance
source_repo: trailofbits/skills
source_path: "plugins/spec-to-code-compliance/commands/spec-compliance.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/spec-to-code-compliance/commands/spec-compliance.md
---


# Verify Spec-to-Code Compliance

**Arguments:** $ARGUMENTS

Parse arguments:
1. **Spec document** (required): Path to specification (PDF, MD, DOCX, HTML, TXT, or URL)
2. **Codebase path** (required): Path to codebase to verify

Invoke the `spec-to-code-compliance` skill with these arguments for the full workflow.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/spec-to-code-compliance/commands/spec-compliance.md`
