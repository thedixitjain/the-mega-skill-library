---
name: compliant-callout
description: "External-lookup skill with canonical Convention callout"
category: testing-and-qa
source_repo: garrytan/gbrain
source_path: "test/fixtures/brain-first-skills/compliant-callout/SKILL.md"
source_url: https://github.com/garrytan/gbrain/blob/HEAD/test/fixtures/brain-first-skills/compliant-callout/SKILL.md
---


# compliant-callout

A skill that researches people via Perplexity but properly delegates to
the brain-first convention.

> **Convention:** see conventions/brain-first.md for the lookup chain (search → query → get_page → external).

## Phase 1: Research

Use Perplexity to find recent news about the person; cross-reference web_search
for primary sources.

---

**Source:** [`garrytan/gbrain`](https://github.com/garrytan/gbrain) → `test/fixtures/brain-first-skills/compliant-callout/SKILL.md`
