---
name: bug-review-command
description: "Systematic bug detection with language-specific expertise."
category: general-purpose
source_repo: athola/claude-night-market
source_path: "plugins/pensive/commands/bug-review.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/pensive/commands/bug-review.md
---
# Bug Review Command

Systematic bug detection with language-specific expertise.

## Usage

```bash
/bug-review
```

## What It Does

1. **Language Detection**: Identify frameworks
2. **Reproduction Plan**: Document how to reproduce
3. **Defect Documentation**: Log all bugs found
4. **Fix Preparation**: Draft patches
5. **Verification Plan**: Outline testing

## Scope

- Logic errors
- API misuse
- Concurrency issues
- Resource leaks
- Validation gaps
- Security vulnerabilities

## Output

- Defect list with severity
- Root cause analysis
- Proposed fixes
- Test updates
- Evidence log

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/pensive/commands/bug-review.md`
