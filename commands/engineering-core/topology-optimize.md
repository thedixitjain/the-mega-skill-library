---
name: topology-optimize
description: "Optimize swarm topology for current workload."
category: engineering-core
source_repo: ruvnet/RuView
source_path: ".claude/commands/optimization/topology-optimize.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/optimization/topology-optimize.md
---
# topology-optimize

Optimize swarm topology for current workload.

## Usage
```bash
npx claude-flow optimization topology-optimize [options]
```

## Options
- `--analyze-first` - Analyze before optimizing
- `--target <metric>` - Optimization target
- `--apply` - Apply optimizations

## Examples
```bash
# Analyze and suggest
npx claude-flow optimization topology-optimize --analyze-first

# Optimize for speed
npx claude-flow optimization topology-optimize --target speed

# Apply changes
npx claude-flow optimization topology-optimize --target efficiency --apply
```

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/optimization/topology-optimize.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/optimization/topology-optimize.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/optimization/topology-optimize.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/optimization/topology-optimize.md`
