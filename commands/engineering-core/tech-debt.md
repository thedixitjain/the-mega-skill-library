---
name: tech-debt
description: "Scan, prioritize, and report technical debt. Usage: /tech-debt <scan|prioritize|report> [options]"
category: engineering-core
source_repo: alirezarezvani/claude-skills
source_path: "commands/tech-debt.md"
source_url: https://github.com/alirezarezvani/claude-skills/blob/HEAD/commands/tech-debt.md
---


# /tech-debt

Scan codebases for technical debt, score severity, and generate prioritized remediation plans.

## Usage

```
/tech-debt scan <project-dir>           Scan for debt indicators
/tech-debt prioritize <inventory.json>  Prioritize debt backlog
/tech-debt report <project-dir>         Full dashboard with trends
```

## Examples

```
/tech-debt scan ./src
/tech-debt scan . --format json
/tech-debt report . --format json --output debt-report.json
```

## Scripts
- `engineering/skills/tech-debt-tracker/scripts/debt_scanner.py` — Scan for debt patterns (`debt_scanner.py <directory> [--format json] [--output file]`)
- `engineering/skills/tech-debt-tracker/scripts/debt_prioritizer.py` — Prioritize debt backlog (`debt_prioritizer.py <inventory.json> [--framework cost_of_delay|wsjf|rice] [--format json]`)
- `engineering/skills/tech-debt-tracker/scripts/debt_dashboard.py` — Generate debt dashboard (`debt_dashboard.py [files...] [--input-dir dir] [--period weekly|monthly|quarterly] [--format json]`)

## Skill Reference
→ `engineering/skills/tech-debt-tracker/SKILL.md`

---

**Source:** [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) → `commands/tech-debt.md`
