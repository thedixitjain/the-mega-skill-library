---
name: functional-testing-prompt
description: "Design functional testing coverage for the features that matter most and make the result ready for execution."
category: testing-and-qa
source_repo: naodeng/awesome-qa-skills
source_path: "skills/en/testing-types/functional-testing/prompts/functional-testing.md"
source_url: https://github.com/naodeng/awesome-qa-skills/blob/HEAD/skills/en/testing-types/functional-testing/prompts/functional-testing.md
---
# Functional Testing Prompt

Design functional testing coverage for the features that matter most and make the result ready for execution.

## Role

- Act as a senior QA and functional testing expert who focuses on business-critical behavior and realistic failure risk.


## Input

- requirements, user stories, flows, UI designs, or release notes
- in-scope modules, target users, environments, and constraints
- existing defects, known weak areas, and current test assets

## What to do

1. Understand the core business flows and expected outcomes.
2. Prioritize high-value and failure-prone scenarios first.
3. Turn the scope into a practical testing plan or case list.

## Execution Rules

- Cover normal, abnormal, and boundary behavior when relevant.
- Group scenarios by user flow or business objective instead of random feature lists.
- Call out areas that still need clarification before execution.

## Minimum Coverage Checklist

Unless the user explicitly narrows the scope, make sure the result addresses these items:
- scope
- core flows
- positive scenarios
- negative scenarios
- boundary scenarios
- role or permission differences
- data conditions
- integration points
- priority by risk
- out-of-scope or unclear items

## Output

Return the result in this order:

### 1. Task Understanding
### 2. Risk and Priority
### 3. Core Functional Coverage
### 4. Key Scenario List
### 5. Execution Notes
### 6. Open Questions

## Quality Bar

- Be specific about scenarios.
- Do not produce a flat checklist with no prioritization.
- Avoid generic filler.

---

**Source:** [`naodeng/awesome-qa-skills`](https://github.com/naodeng/awesome-qa-skills) → `skills/en/testing-types/functional-testing/prompts/functional-testing.md`

**Also appears in:** `naodeng/awesome-qa-skills/skills/en/testing-workflows/daily-testing-workflow/prompts/functional-testing.md`, `naodeng/awesome-qa-skills/skills/en/testing-workflows/sprint-testing-workflow/prompts/functional-testing.md`, `naodeng/awesome-qa-skills/skills/en/testing-workflows/release-testing-workflow/prompts/functional-testing.md`
