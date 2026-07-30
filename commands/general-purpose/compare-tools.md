---
name: compare-tools
description: "Compare multiple developer tools side-by-side to make an informed selection decision."
category: general-purpose
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/tool-evaluator/commands/compare-tools.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/tool-evaluator/commands/compare-tools.md
---
Compare multiple developer tools side-by-side to make an informed selection decision.

## Steps


1. Define the comparison scope:
2. Select tools to compare (3-5 candidates):
3. Build a comparison matrix:
4. Weight criteria by importance to the project:
5. Score each tool on each criterion.
6. Calculate weighted totals and rank.
7. Provide a recommendation with migration cost considerations.

## Format


```
Comparison: <category>
Candidates: <tool list>

| Criterion    | Weight | Tool A | Tool B | Tool C |
```


## Rules

- Compare tools under identical conditions for fairness.
- Include the migration cost from the current tool.
- Note vendor lock-in risk for each option.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/tool-evaluator/commands/compare-tools.md`
