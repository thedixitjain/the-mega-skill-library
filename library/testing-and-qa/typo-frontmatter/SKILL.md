---
name: typo-frontmatter
description: "Skill with typo in brain_first declaration"
category: testing-and-qa
source_repo: garrytan/gbrain
source_path: "test/fixtures/brain-first-skills/typo-frontmatter/SKILL.md"
source_url: https://github.com/garrytan/gbrain/blob/HEAD/test/fixtures/brain-first-skills/typo-frontmatter/SKILL.md
---


# typo-frontmatter

The maintainer tried to opt out but used kebab-case `brain-first` instead
of canonical snake_case `brain_first`. The analyzer should surface a
typo hint AND still flag the skill (because the exempt declaration
didn't land).

## How

Call web_search and perplexity for fresh data.

---

**Source:** [`garrytan/gbrain`](https://github.com/garrytan/gbrain) → `test/fixtures/brain-first-skills/typo-frontmatter/SKILL.md`
