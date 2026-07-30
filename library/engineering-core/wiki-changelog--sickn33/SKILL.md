---
name: wiki-changelog
description: "Generate structured changelogs from git history. Use when user asks \\\"what changed recently\\\", \\\"generate a changelog\\\", \\\"summarize commits\\\" or user wants to understand recent development activity."
category: engineering-core
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/wiki-changelog/SKILL.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/wiki-changelog/SKILL.md
---


# Wiki Changelog

Generate structured changelogs from git history.

## When to Use
- User asks "what changed recently", "generate a changelog", "summarize commits"
- User wants to understand recent development activity

## Procedure

1. Examine git log (commits, dates, authors, messages)
2. Group by time period: daily (last 7 days), weekly (older)
3. Classify each commit: Features (🆕), Fixes (🐛), Refactoring (🔄), Docs (📝), Config (🔧), Dependencies (📦), Breaking (⚠️)
4. Generate concise user-facing descriptions using project terminology

## Constraints

- Focus on user-facing changes
- Merge related commits into coherent descriptions
- Use project terminology from README
- Highlight breaking changes prominently with migration notes

### When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/wiki-changelog/SKILL.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/wiki-changelog/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/wiki-changelog/SKILL.md`
