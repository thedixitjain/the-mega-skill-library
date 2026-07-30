---
name: smart-spawn
description: "Intelligently spawn agents based on workload analysis."
category: ai-agents-and-harness
source_repo: ruvnet/RuView
source_path: ".claude/commands/automation/smart-spawn.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/automation/smart-spawn.md
---
# smart-spawn

Intelligently spawn agents based on workload analysis.

## Usage
```bash
npx claude-flow automation smart-spawn [options]
```

## Options
- `--analyze` - Analyze before spawning
- `--threshold <n>` - Spawn threshold
- `--topology <type>` - Preferred topology

## Examples
```bash
# Smart spawn with analysis
npx claude-flow automation smart-spawn --analyze

# Set spawn threshold
npx claude-flow automation smart-spawn --threshold 5

# Force topology
npx claude-flow automation smart-spawn --topology hierarchical
```

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/automation/smart-spawn.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/automation/smart-spawn.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/automation/smart-spawn.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/automation/smart-spawn.md`
