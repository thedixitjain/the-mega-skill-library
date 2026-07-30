---
name: optimize-size
description: "Analyze and reduce code bundle size, dependency bloat, and binary footprint."
category: general-purpose
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/optimize/commands/optimize-size.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/optimize/commands/optimize-size.md
---
Analyze and reduce code bundle size, dependency bloat, and binary footprint.

## Steps


1. Measure the current size:
2. Identify the largest contributors:
3. Apply size reduction strategies:
4. Optimize assets:
5. Configure build optimizations:
6. Measure the result and compare against the baseline.

## Format


```
Before: <size>
After: <size>
Reduction: <percentage>
Changes:
```


## Rules

- Measure before and after with the same build configuration.
- Do not remove dependencies that are actually used at runtime.
- Verify functionality after removing or replacing dependencies.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/optimize/commands/optimize-size.md`
