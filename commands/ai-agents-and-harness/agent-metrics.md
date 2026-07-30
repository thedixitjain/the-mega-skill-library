---
name: agent-metrics
description: "View agent performance metrics."
category: ai-agents-and-harness
source_repo: ruvnet/RuView
source_path: ".claude/commands/monitoring/agent-metrics.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/monitoring/agent-metrics.md
---
# agent-metrics

View agent performance metrics.

## Usage
```bash
npx claude-flow agent metrics [options]
```

## Options
- `--agent-id <id>` - Specific agent
- `--period <time>` - Time period
- `--format <type>` - Output format

## Examples
```bash
# All agents metrics
npx claude-flow agent metrics

# Specific agent
npx claude-flow agent metrics --agent-id agent-001

# Last hour
npx claude-flow agent metrics --period 1h
```

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/monitoring/agent-metrics.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/monitoring/agent-metrics.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/monitoring/agent-metrics.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/monitoring/agent-metrics.md`
