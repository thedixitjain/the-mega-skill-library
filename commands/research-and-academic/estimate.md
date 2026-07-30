---
name: estimate
description: "Estimate effort and time for development tasks using structured sizing methodology."
category: research-and-academic
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/plan/commands/estimate.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/plan/commands/estimate.md
---
Estimate effort and time for development tasks using structured sizing methodology.

## Steps


1. Read the task or feature description and identify all sub-tasks.
2. For each sub-task, assess complexity:
3. Estimate effort using T-shirt sizing:
4. Apply risk multipliers:
5. Sum estimates and add 20% buffer for integration and testing.
6. Present optimistic, expected, and pessimistic estimates.

## Format


```
Task: <description>
Sub-tasks:
  - <task> [Size] [Risk: multiplier] = <estimate>
Total: <sum>
```


## Rules

- Never give a single point estimate; always provide a range.
- Include testing time in every estimate.
- Flag tasks where the estimate confidence is low.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/plan/commands/estimate.md`
