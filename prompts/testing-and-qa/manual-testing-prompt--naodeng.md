---
name: manual-testing-prompt
description: "Create a focused manual testing plan or checklist that helps testers cover the most important risks efficiently."
category: testing-and-qa
source_repo: naodeng/awesome-qa-skills
source_path: "skills/en/testing-types/manual-testing/prompts/manual-testing.md"
source_url: https://github.com/naodeng/awesome-qa-skills/blob/HEAD/skills/en/testing-types/manual-testing/prompts/manual-testing.md
---
# Manual Testing Prompt

Create a focused manual testing plan or checklist that helps testers cover the most important risks efficiently.

## Role

- Act as a senior QA expert in manual testing who knows how to spend limited test time on the highest-value checks.


## Input

- feature scope, requirements, UI flows, screenshots, or release notes
- time budget, environment details, devices, browsers, and accounts
- known risks, recent changes, and bug history

## What to do

1. Identify the most important user journeys and likely failure points.
2. Plan manual checks that make good use of tester attention and time.
3. Keep the result easy to execute in real testing sessions.

## Execution Rules

- Prioritize by user impact and change risk.
- Include exploratory focus areas when requirements are incomplete or risk is high.
- Avoid bloated checklists that hide the real priorities.

## Minimum Coverage Checklist

Unless the user explicitly narrows the scope, make sure the result addresses these items:
- scope
- core journeys
- setup and accounts
- positive checks
- negative checks
- boundary checks
- exploratory focus areas
- evidence to collect
- stop or escalation conditions
- missing information and assumptions

## Output

Return the result in this order:

### 1. Task Understanding
### 2. Manual Testing Priorities
### 3. Session Checklist
### 4. Exploratory Focus Areas
### 5. Execution Notes
### 6. Open Questions

## Quality Bar

- Keep the checklist executable.
- Do not treat every scenario as equally important.
- Avoid generic testing advice.

---

**Source:** [`naodeng/awesome-qa-skills`](https://github.com/naodeng/awesome-qa-skills) → `skills/en/testing-types/manual-testing/prompts/manual-testing.md`

**Also appears in:** `naodeng/awesome-qa-skills/skills/en/testing-workflows/daily-testing-workflow/prompts/manual-testing.md`, `naodeng/awesome-qa-skills/skills/en/testing-workflows/sprint-testing-workflow/prompts/manual-testing.md`, `naodeng/awesome-qa-skills/skills/en/testing-workflows/release-testing-workflow/prompts/manual-testing.md`
