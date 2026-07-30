---
name: compliant-position
description: "Skill that runs gbrain search before external lookup"
category: testing-and-qa
source_repo: garrytan/gbrain
source_path: "test/fixtures/brain-first-skills/compliant-position/SKILL.md"
source_url: https://github.com/garrytan/gbrain/blob/HEAD/test/fixtures/brain-first-skills/compliant-position/SKILL.md
---


# compliant-position

This skill demonstrates position-relative compliance: the first brain
reference (gbrain search) appears strictly before the first external
reference (web_search), so the analyzer accepts it without requiring
the canonical callout.

## Workflow

1. Run `gbrain search "topic"` to find existing brain pages.
2. If brain answer is thin, fall back to web_search for fresh data.

---

**Source:** [`garrytan/gbrain`](https://github.com/garrytan/gbrain) → `test/fixtures/brain-first-skills/compliant-position/SKILL.md`
