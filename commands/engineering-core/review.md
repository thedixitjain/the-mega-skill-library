---
name: review
description: "Conduct a five-axis code review — correctness, readability, architecture, security, performance"
category: engineering-core
source_repo: addyosmani/agent-skills
source_path: ".claude/commands/review.md"
source_url: https://github.com/addyosmani/agent-skills/blob/HEAD/.claude/commands/review.md
---
Invoke the agent-skills:code-review-and-quality skill.

Review the current changes (staged or recent commits) across all five axes:

1. **Correctness** — Does it match the spec? Edge cases handled? Tests adequate?
2. **Readability** — Clear names? Straightforward logic? Well-organized?
3. **Architecture** — Follows existing patterns? Clean boundaries? Right abstraction level?
4. **Security** — Input validated? Secrets safe? Auth checked? (Use security-and-hardening skill)
5. **Performance** — No N+1 queries? No unbounded ops? (Use performance-optimization skill)

Categorize findings as Critical, Important, or Suggestion.
Output a structured review with specific file:line references and fix recommendations.

---

**Source:** [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) → `.claude/commands/review.md`
