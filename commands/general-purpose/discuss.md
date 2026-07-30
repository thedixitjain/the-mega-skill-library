---
name: discuss
description: "Debate implementation approaches by presenting structured arguments for multiple options."
category: general-purpose
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/discuss/commands/discuss.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/discuss/commands/discuss.md
---
Debate implementation approaches by presenting structured arguments for multiple options.

## Steps


1. Clearly state the decision to be made and any constraints.
2. Identify at least 3 viable approaches to the problem.
3. For each approach, analyze:
4. Compare approaches against key criteria:
5. Present a recommendation with clear reasoning.
6. Identify what would change the recommendation (e.g., "if scale exceeds X, use option B").

## Format


```
Decision: <what needs to be decided>
Options:
  A. <approach> - Pros: [...] Cons: [...] Effort: <X>
  B. <approach> - Pros: [...] Cons: [...] Effort: <X>
```


## Rules

- Present at least 3 options; "do nothing" can be one of them.
- Be honest about trade-offs; no option is perfect.
- The recommendation must follow logically from the analysis.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/discuss/commands/discuss.md`
