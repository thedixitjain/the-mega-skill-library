---
name: query-and-file
description: "Use this prompt when answering a question from the wiki and saving the result."
category: prompt-engineering
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/wiki-builder/templates/prompts/query-and-file.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/wiki-builder/templates/prompts/query-and-file.md
---
# Query And File

Use this prompt when answering a question from the wiki and saving the result.

Task:

- Read `wiki.config.md`, `sources.md`, and relevant wiki pages.
- Answer the user's question with source-grounded reasoning.
- If the answer should persist, create or update a page under `wiki/questions/`, `derived/briefs/`, or another configured location.
- Update `wiki/index.md` if the answer becomes an important entry point.
- Update `logs/maintenance-log.md` for material additions.

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/wiki-builder/templates/prompts/query-and-file.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/wiki-builder/templates/prompts/query-and-file.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/wiki-builder/templates/prompts/query-and-file.md`
