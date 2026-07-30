---
name: task-orchestrate
description: "Orchestrate complex tasks across the swarm."
category: ai-agents-and-harness
source_repo: ruvnet/ruflo
source_path: ".claude/commands/coordination/task-orchestrate.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/coordination/task-orchestrate.md
---
# task-orchestrate

Orchestrate complex tasks across the swarm.

## Usage
```bash
npx claude-flow task orchestrate [options]
```

## Options
- `--task <description>` - Task description
- `--strategy <type>` - Orchestration strategy
- `--priority <level>` - Task priority (low, medium, high, critical)

## Examples
```bash
# Orchestrate development task
npx claude-flow task orchestrate --task "Implement user authentication"

# High priority task
npx claude-flow task orchestrate --task "Fix production bug" --priority critical

# With specific strategy
npx claude-flow task orchestrate --task "Refactor codebase" --strategy parallel
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/coordination/task-orchestrate.md`

**Also appears in:** `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/coordination/task-orchestrate.md`
