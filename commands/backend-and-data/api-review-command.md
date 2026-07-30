---
name: api-review-command
description: "Evaluate public API surfaces against guidelines and exemplars."
category: backend-and-data
source_repo: athola/claude-night-market
source_path: "plugins/pensive/commands/api-review.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/pensive/commands/api-review.md
---
# API Review Command

Evaluate public API surfaces against guidelines and exemplars.

## Usage

```bash
/api-review
```

## What It Does

1. **Surface Inventory**: Catalog all exported APIs
2. **Exemplar Research**: Find best-practice references
3. **Consistency Audit**: Compare against guidelines
4. **Documentation Check**: Verify completeness
5. **Evidence Log**: Document findings

## Scope

- REST/GraphQL endpoints
- Library exports (pub, export)
- SDK functions
- CLI commands
- Configuration interfaces

## Output

- API surface inventory
- Consistency issues
- Documentation gaps
- Exemplar comparisons
- Action items with owners

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/pensive/commands/api-review.md`
