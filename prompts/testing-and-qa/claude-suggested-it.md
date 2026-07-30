---
name: claude-suggested-it
description: "[Previous assistant message]: Plan complete and saved to docs/superpowers/plans/auth-system.md."
category: testing-and-qa
source_repo: obra/superpowers
source_path: "tests/explicit-skill-requests/prompts/claude-suggested-it.txt"
source_url: https://github.com/obra/superpowers/blob/HEAD/tests/explicit-skill-requests/prompts/claude-suggested-it.txt
---
[Previous assistant message]:
Plan complete and saved to docs/superpowers/plans/auth-system.md.

Two execution options:
1. Subagent-Driven (this session) - I dispatch a fresh subagent per task, review between tasks, fast iteration within this conversation
2. Parallel Session (separate) - Open a new Claude Code session with the execute-plan skill, batch execution with review checkpoints

Which approach do you want to use for implementation?

[Your response]:
subagent-driven-development, please

---

**Source:** [`obra/superpowers`](https://github.com/obra/superpowers) → `tests/explicit-skill-requests/prompts/claude-suggested-it.txt`
