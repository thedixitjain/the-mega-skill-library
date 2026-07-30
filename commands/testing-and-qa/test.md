---
name: test
description: "Run TDD workflow — write failing tests, implement, verify. For bugs, use the Prove-It pattern."
category: testing-and-qa
source_repo: addyosmani/agent-skills
source_path: ".claude/commands/test.md"
source_url: https://github.com/addyosmani/agent-skills/blob/HEAD/.claude/commands/test.md
---
Invoke the agent-skills:test-driven-development skill.

For new features:
1. Write tests that describe the expected behavior (they should FAIL)
2. Implement the code to make them pass
3. Refactor while keeping tests green

For bug fixes (Prove-It pattern):
1. Write a test that reproduces the bug (must FAIL)
2. Confirm the test fails
3. Implement the fix
4. Confirm the test passes
5. Run the full test suite for regressions

For browser-related issues, also invoke agent-skills:browser-testing-with-devtools to verify with Chrome DevTools MCP.

---

**Source:** [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) → `.claude/commands/test.md`
