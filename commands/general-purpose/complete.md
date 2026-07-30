---
name: complete
description: "Complete a partially implemented feature by filling gaps and ensuring production readiness."
category: general-purpose
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/feature-dev/commands/complete.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/feature-dev/commands/complete.md
---
Complete a partially implemented feature by filling gaps and ensuring production readiness.

## Steps


1. Assess the current state of the feature:
2. Identify remaining work:
3. Complete each missing piece:
4. Harden the implementation:
5. Write missing tests and verify coverage.
6. Update documentation:
7. Run the full test suite and fix any regressions.

## Format


```
Feature: <name>
Completion Status: <before>% -> <after>%
Gaps Filled:
  - <gap>: <what was added>
```


## Rules

- Treat incomplete features as bugs that need fixing.
- Focus on making the feature shippable, not perfect.
- Every public API must have error handling and validation.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/feature-dev/commands/complete.md`
