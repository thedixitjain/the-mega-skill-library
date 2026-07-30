---
name: root-level-skill-fixture
description: "| Minimal fixture skill for regression coverage of root-level SKILL.md discovery. Use when validating that find_skill_files picks up Anthropic-spec layout. Trigger with \"root level skill fixture\"."
allowed-tools: "Read"
category: testing-and-qa
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "tests/fixtures/root-level-skill-plugin/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/tests/fixtures/root-level-skill-plugin/SKILL.md
---


## Overview

Fixture skill used by `tests/test_root_level_skill_discovery.py`. It exists solely
to verify that the validator's batch walker (`find_skill_files`) picks up
plugins that follow the Anthropic-spec layout — SKILL.md at plugin root with no
`skills/<name>/` subdirectory.

## Prerequisites

None — this is a static fixture.

## Instructions

Do not invoke this skill. It is a test fixture only.

## Output

N/A.

## Error Handling

N/A.

## Examples

N/A.

## Resources

- `scripts/validate-skills-schema.py` — the function under test.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `tests/fixtures/root-level-skill-plugin/SKILL.md`
