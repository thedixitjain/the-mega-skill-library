---
name: after-planning-flow
description: "Great, the plan is complete. I've saved it to docs/superpowers/plans/auth-system.md."
category: testing-and-qa
source_repo: obra/superpowers
source_path: "tests/explicit-skill-requests/prompts/after-planning-flow.txt"
source_url: https://github.com/obra/superpowers/blob/HEAD/tests/explicit-skill-requests/prompts/after-planning-flow.txt
---
Great, the plan is complete. I've saved it to docs/superpowers/plans/auth-system.md.

Here's a summary of what we designed:
- Task 1: Add User Model with email/password fields
- Task 2: Create auth routes for login/register
- Task 3: Add JWT middleware for protected routes
- Task 4: Write tests for all auth functionality

Two execution options:
1. Subagent-Driven (this session) - dispatch a fresh subagent per task
2. Parallel Session (separate) - open new Claude Code session

Which approach do you want?

---

subagent-driven-development, please

---

**Source:** [`obra/superpowers`](https://github.com/obra/superpowers) → `tests/explicit-skill-requests/prompts/after-planning-flow.txt`
