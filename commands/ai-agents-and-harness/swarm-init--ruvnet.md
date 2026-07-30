---
name: swarm-init
description: "Initialize a new swarm with specified topology."
category: ai-agents-and-harness
source_repo: ruvnet/ruflo
source_path: ".claude/commands/swarm/swarm-init.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/swarm/swarm-init.md
---
# swarm-init

Initialize a new swarm with specified topology.

## Usage
```bash
npx claude-flow swarm init [options]
```

## Options
- `--topology <type>` - Swarm topology (mesh, hierarchical, ring, star)
- `--max-agents <n>` - Maximum agents
- `--strategy <type>` - Distribution strategy

## Examples
```bash
npx claude-flow swarm init --topology mesh
npx claude-flow swarm init --topology hierarchical --max-agents 8
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/swarm/swarm-init.md`

**Also appears in:** `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/swarm/swarm-init.md`
