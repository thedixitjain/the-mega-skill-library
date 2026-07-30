---
name: swarm-monitor
description: "Real-time swarm monitoring."
category: ai-agents-and-harness
source_repo: ruvnet/RuView
source_path: ".claude/commands/monitoring/swarm-monitor.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/monitoring/swarm-monitor.md
---
# swarm-monitor

Real-time swarm monitoring.

## Usage
```bash
npx claude-flow swarm monitor [options]
```

## Options
- `--interval <ms>` - Update interval
- `--metrics` - Show detailed metrics
- `--export` - Export monitoring data

## Examples
```bash
# Start monitoring
npx claude-flow swarm monitor

# Custom interval
npx claude-flow swarm monitor --interval 5000

# With metrics
npx claude-flow swarm monitor --metrics
```

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/monitoring/swarm-monitor.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/monitoring/swarm-monitor.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/monitoring/swarm-monitor.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/monitoring/swarm-monitor.md`
