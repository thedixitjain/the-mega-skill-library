---
name: makefile-review-command
description: "Audit Makefiles for best practices and portability."
category: security-and-compliance
source_repo: athola/claude-night-market
source_path: "plugins/pensive/commands/makefile-review.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/pensive/commands/makefile-review.md
---
# Makefile Review Command

Audit Makefiles for best practices and portability.

## Usage

```bash
/makefile-review
```

## What It Does

1. **Context Mapping**: Find all Make files
2. **Dependency Graph**: Analyze targets
3. **Deduplication**: Find repeated recipes
4. **Portability Check**: Cross-platform safety
5. **Evidence Logging**: Document findings

## Scope

- Target organization
- Recipe duplication
- Variable usage
- PHONY declarations
- Cross-platform compatibility

## Output

- Dependency analysis
- Deduplication opportunities
- Portability issues
- Best practice gaps
- Recommendations

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/pensive/commands/makefile-review.md`
