---
name: swarm-spawn
description: "Spawn agents in the swarm."
category: ai-agents-and-harness
source_repo: ruvnet/ruflo
source_path: ".claude/commands/swarm/swarm-spawn.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/swarm/swarm-spawn.md
---
# swarm-spawn

Spawn agents in the swarm.

## Usage
```bash
npx claude-flow swarm spawn [options]
```

## Options
- `--type <type>` - Agent type
- `--count <n>` - Number to spawn
- `--capabilities <list>` - Agent capabilities

## Examples
```bash
npx claude-flow swarm spawn --type coder --count 3
npx claude-flow swarm spawn --type researcher --capabilities "web-search,analysis"
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/swarm/swarm-spawn.md`

**Also appears in:** `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/swarm/swarm-spawn.md`
