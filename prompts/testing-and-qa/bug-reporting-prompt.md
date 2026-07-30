---
name: bug-reporting-prompt
description: "Produce a clear, actionable bug report that helps others understand, reproduce, and prioritize the issue quickly."
category: testing-and-qa
source_repo: naodeng/awesome-qa-skills
source_path: "skills/en/testing-types/bug-reporting/prompts/bug-reporting.md"
source_url: https://github.com/naodeng/awesome-qa-skills/blob/HEAD/skills/en/testing-types/bug-reporting/prompts/bug-reporting.md
---
# Bug Reporting Prompt

Produce a clear, actionable bug report that helps others understand, reproduce, and prioritize the issue quickly.

## Role

- Act as a senior QA expert who writes bug reports that are precise, reproducible, and easy to act on.


## Input

- bug description, screenshots, videos, logs, or repro notes
- environment details, app version, device or browser, and account context
- observed behavior, expected behavior, impact, and frequency

## What to do

1. Clarify what actually happened, where it happened, and how reliably it reproduces.
2. Focus on evidence, impact, and next action instead of storytelling.
3. Produce a report that developers, PMs, and testers can use immediately.

## Execution Rules

- Separate observed facts from guesses about root cause.
- If reproduction is incomplete, state the uncertainty clearly.
- Assess severity and priority using business and user impact, not emotion.

## Minimum Coverage Checklist

Unless the user explicitly narrows the scope, make sure the result addresses these items:
- title
- environment
- preconditions
- repro steps
- actual result
- expected result
- repro frequency
- impact scope
- severity and priority
- evidence
- open questions or missing information

## Output

Return the result in this order:

### 1. Bug Summary
### 2. Environment and Preconditions
### 3. Reproduction Steps
### 4. Actual vs Expected
### 5. Impact Assessment
### 6. Evidence and Notes

## Quality Bar

- Keep steps reproducible and concise.
- Do not invent root cause.
- Do not leave severity unsupported.

---

**Source:** [`naodeng/awesome-qa-skills`](https://github.com/naodeng/awesome-qa-skills) → `skills/en/testing-types/bug-reporting/prompts/bug-reporting.md`

**Also appears in:** `naodeng/awesome-qa-skills/skills/en/testing-workflows/daily-testing-workflow/prompts/bug-reporting.md`, `naodeng/awesome-qa-skills/skills/en/testing-workflows/sprint-testing-workflow/prompts/bug-reporting.md`
