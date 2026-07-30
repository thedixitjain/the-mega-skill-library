---
name: workflow-select
description: "Automatically select optimal workflow based on task type."
category: general-purpose
source_repo: ruvnet/RuView
source_path: ".claude/commands/automation/workflow-select.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/automation/workflow-select.md
---
# workflow-select

Automatically select optimal workflow based on task type.

## Usage
```bash
npx claude-flow automation workflow-select [options]
```

## Options
- `--task <description>` - Task description
- `--constraints <list>` - Workflow constraints
- `--preview` - Preview without executing

## Examples
```bash
# Select workflow for task
npx claude-flow automation workflow-select --task "Deploy to production"

# With constraints
npx claude-flow automation workflow-select --constraints "no-downtime,rollback"

# Preview mode
npx claude-flow automation workflow-select --task "Database migration" --preview
```

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/automation/workflow-select.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/automation/workflow-select.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/automation/workflow-select.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/automation/workflow-select.md`
