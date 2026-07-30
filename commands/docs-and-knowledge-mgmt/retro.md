---
name: retro
description: "Analyze sprint retrospectives for patterns and action item tracking. Usage: /retro analyze <retro_data.json>. Slash command for Claude Code, Codex CLI, Gemini CLI."
category: docs-and-knowledge-mgmt
source_repo: alirezarezvani/claude-skills
source_path: "docs/commands/retro.md"
source_url: https://github.com/alirezarezvani/claude-skills/blob/HEAD/docs/commands/retro.md
---


# /retro

<div class="page-meta" markdown>
<span class="meta-badge">:material-console: Slash Command</span>
<span class="meta-badge">:material-github: <a href="https://github.com/alirezarezvani/claude-skills/tree/main/commands/retro.md">Source</a></span>
</div>


Analyze retrospective data for recurring themes, sentiment trends, and action item effectiveness.

## Usage

```
/retro analyze <retro_data.json>                             Full retrospective analysis
```

## Input Format

```json
{
  "sprint_name": "Sprint 24",
  "went_well": ["CI pipeline improvements", "Pair programming sessions"],
  "improvements": ["Too many meetings", "Flaky integration tests"],
  "action_items": [
    {"description": "Reduce standup to 10 min", "owner": "SM", "status": "done"},
    {"description": "Fix flaky tests", "owner": "QA Lead", "status": "in_progress"}
  ],
  "participants": 8
}
```

## Examples

```
/retro analyze sprint-24-retro.json
/retro analyze sprint-24-retro.json --format json
```

## Scripts
- `project-management/skills/scrum-master/scripts/retrospective_analyzer.py` — Retrospective analyzer (`<data_file> [--format text|json]`)

## Skill Reference
> `project-management/skills/scrum-master/SKILL.md`

---

**Source:** [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) → `docs/commands/retro.md`
