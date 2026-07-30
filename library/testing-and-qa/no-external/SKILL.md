---
name: no-external
description: "Skill that operates purely on local state"
category: testing-and-qa
source_repo: garrytan/gbrain
source_path: "test/fixtures/brain-first-skills/no-external/SKILL.md"
source_url: https://github.com/garrytan/gbrain/blob/HEAD/test/fixtures/brain-first-skills/no-external/SKILL.md
---


# no-external

This skill rotates log files locally. No external APIs, no brain queries.
Trivially exempt from brain-first compliance because there's nothing
to consult.

## How

Read the log path from config, rename to .log.1, truncate the active file.

---

**Source:** [`garrytan/gbrain`](https://github.com/garrytan/gbrain) → `test/fixtures/brain-first-skills/no-external/SKILL.md`
