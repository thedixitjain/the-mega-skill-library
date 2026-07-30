---
name: real-time-view
description: "Real-time view of swarm activity."
category: devops-and-infra
source_repo: ruvnet/RuView
source_path: ".claude/commands/monitoring/real-time-view.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/monitoring/real-time-view.md
---
# real-time-view

Real-time view of swarm activity.

## Usage
```bash
npx claude-flow monitoring real-time-view [options]
```

## Options
- `--filter <type>` - Filter view
- `--highlight <pattern>` - Highlight pattern
- `--tail <n>` - Show last N events

## Examples
```bash
# Start real-time view
npx claude-flow monitoring real-time-view

# Filter errors
npx claude-flow monitoring real-time-view --filter errors

# Highlight pattern
npx claude-flow monitoring real-time-view --highlight "API"
```

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/monitoring/real-time-view.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/monitoring/real-time-view.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/monitoring/real-time-view.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/monitoring/real-time-view.md`
