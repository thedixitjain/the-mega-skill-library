---
name: playwright-generate-test
description: "Generate a Playwright test based on a scenario using Playwright MCP"
category: testing-and-qa
source_repo: github/awesome-copilot
source_path: "skills/playwright-generate-test/SKILL.md"
source_url: https://github.com/github/awesome-copilot/blob/HEAD/skills/playwright-generate-test/SKILL.md
---
# Test Generation with Playwright MCP

Your goal is to generate a Playwright test based on the provided scenario after completing all prescribed steps.

## Specific Instructions

- You are given a scenario, and you need to generate a playwright test for it. If the user does not provide a scenario, you will ask them to provide one.
- DO NOT generate test code prematurely or based solely on the scenario without completing all prescribed steps.
- DO run steps one by one using the tools provided by the Playwright MCP.
- Only after all steps are completed, emit a Playwright TypeScript test that uses `@playwright/test` based on message history
- Save generated test file in the tests directory
- Execute the test file and iterate until the test passes

---

**Source:** [`github/awesome-copilot`](https://github.com/github/awesome-copilot) → `skills/playwright-generate-test/SKILL.md`
