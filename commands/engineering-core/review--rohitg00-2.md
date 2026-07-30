---
name: review
description: "Perform an automated code review with categorized findings and severity ratings."
category: engineering-core
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/code-review-assistant/commands/review.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/code-review-assistant/commands/review.md
---
Perform an automated code review with categorized findings and severity ratings.

## Steps


1. Identify the scope of the review:
2. Review for correctness:
3. Review for security:
4. Review for maintainability:
5. Review for performance:
6. Assign severity to each finding:

## Format


```
Review: <scope>
Findings: <total count>
  [CRITICAL] <file>:<line> - <issue>
  [WARNING] <file>:<line> - <issue>
```


## Rules

- Read the full file context, not just the diff.
- Be specific: reference exact lines and suggest concrete fixes.
- Balance criticism with acknowledgment of good patterns.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/code-review-assistant/commands/review.md`
