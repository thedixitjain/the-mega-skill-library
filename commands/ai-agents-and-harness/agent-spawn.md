---
name: agent-spawn
description: "Spawn a new agent in the current swarm."
category: ai-agents-and-harness
source_repo: ruvnet/ruflo
source_path: ".claude/commands/coordination/agent-spawn.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/coordination/agent-spawn.md
---
# agent-spawn

Spawn a new agent in the current swarm.

## Usage
```bash
npx claude-flow agent spawn [options]
```

## Options
- `--type <type>` - Agent type (coder, researcher, analyst, tester, coordinator)
- `--name <name>` - Custom agent name
- `--skills <list>` - Specific skills (comma-separated)

## Examples
```bash
# Spawn coder agent
npx claude-flow agent spawn --type coder

# With custom name
npx claude-flow agent spawn --type researcher --name "API Expert"

# With specific skills
npx claude-flow agent spawn --type coder --skills "python,fastapi,testing"
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/coordination/agent-spawn.md`

**Also appears in:** `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/coordination/agent-spawn.md`
