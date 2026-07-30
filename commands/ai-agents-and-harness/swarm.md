---
name: swarm
description: "Main swarm orchestration command for Claude Flow."
category: ai-agents-and-harness
source_repo: ruvnet/ruflo
source_path: ".claude/commands/swarm/swarm.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/swarm/swarm.md
---
# swarm

Main swarm orchestration command for Claude Flow.

## Usage
```bash
npx claude-flow swarm <objective> [options]
```

## Options
- `--strategy <type>` - Execution strategy (research, development, analysis, testing)
- `--mode <type>` - Coordination mode (centralized, distributed, hierarchical, mesh)
- `--max-agents <n>` - Maximum number of agents (default: 5)
- `--claude` - Open Claude Code CLI with swarm prompt
- `--parallel` - Enable parallel execution

## Examples
```bash
# Basic swarm
npx claude-flow swarm "Build REST API"

# With strategy
npx claude-flow swarm "Research AI patterns" --strategy research

# Open in Claude Code
npx claude-flow swarm "Build API" --claude
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/swarm/swarm.md`
