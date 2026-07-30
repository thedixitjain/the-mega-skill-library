---
name: exempt-frontmatter
description: "Pure-infra skill that opts out via frontmatter"
category: testing-and-qa
source_repo: garrytan/gbrain
source_path: "test/fixtures/brain-first-skills/exempt-frontmatter/SKILL.md"
source_url: https://github.com/garrytan/gbrain/blob/HEAD/test/fixtures/brain-first-skills/exempt-frontmatter/SKILL.md
---


# exempt-frontmatter

This skill manages cron schedules. It does call web_search for time-zone
data and perplexity for cron syntax help — but the maintainer declared
`brain_first: exempt` because the skill is pure infrastructure that
doesn't consult brain knowledge.

## How

Use web_search for tz data, perplexity for cron syntax. Update the
crontab via the host system call.

---

**Source:** [`garrytan/gbrain`](https://github.com/garrytan/gbrain) → `test/fixtures/brain-first-skills/exempt-frontmatter/SKILL.md`
