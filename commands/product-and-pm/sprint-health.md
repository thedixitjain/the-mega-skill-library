---
name: sprint-health
description: "Sprint health scoring and velocity analysis for agile teams. Usage: /sprint-health <analyze|velocity> [options]"
category: product-and-pm
source_repo: alirezarezvani/claude-skills
source_path: "commands/sprint-health.md"
source_url: https://github.com/alirezarezvani/claude-skills/blob/HEAD/commands/sprint-health.md
---


# /sprint-health

Score sprint health across delivery, quality, and team metrics with velocity trend analysis.

## Usage

```
/sprint-health analyze <sprint_data.json>                    Full sprint health score
/sprint-health velocity <sprint_data.json>                   Velocity trend analysis
```

## Input Format

```json
{
  "sprint_name": "Sprint 24",
  "committed_points": 34,
  "completed_points": 29,
  "stories": {"total": 12, "completed": 10, "carried_over": 2},
  "blockers": [{"description": "API dependency", "days_blocked": 3}],
  "ceremonies": {"planning": true, "daily": true, "review": true, "retro": true}
}
```

## Examples

```
/sprint-health analyze sprint-24.json
/sprint-health velocity last-6-sprints.json
/sprint-health analyze sprint-24.json --format json
```

## Scripts
- `project-management/skills/scrum-master/scripts/sprint_health_scorer.py` — Sprint health scorer (`<data_file> [--format text|json]`)
- `project-management/skills/scrum-master/scripts/velocity_analyzer.py` — Velocity analyzer (`<data_file> [--format text|json]`)

## Skill Reference
> `project-management/skills/scrum-master/SKILL.md`

---

**Source:** [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) → `commands/sprint-health.md`
