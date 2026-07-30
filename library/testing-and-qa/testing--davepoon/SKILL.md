---
name: testing
description: "Testing strategies and methodologies including TDD, E2E testing, and multi-framework support"
category: testing-and-qa
source_repo: davepoon/buildwithclaude
source_path: "plugins/cc-best/skills/testing/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/cc-best/skills/testing/SKILL.md
---


# Testing Skill

Comprehensive testing guidance covering:

- **TDD Workflow**: Red → Green → Refactor cycle with practical examples
- **Test Organization**: Unit / Integration / E2E test structure
- **Framework Support**: pytest, Jest, JUnit5, xUnit, Google Test
- **Mock Strategies**: Only mock external boundaries, not internal logic
- **Coverage Requirements**: 80%+ with meaningful assertions

## When Loaded

This skill is automatically injected when working with:

- `/cc-best:dev` — Implementation with tests
- `tdd-guide` agent — Test-driven development guidance
- `build-error-resolver` agent — Fixing test failures

## Key Rules

1. **Tests first** — Write failing test before implementation
2. **AAA pattern** — Arrange, Act, Assert in every test
3. **No shared mutable state** — Each test is independent
4. **Descriptive names** — `test_<feature>_<scenario>_<expected>`

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/cc-best/skills/testing/SKILL.md`
