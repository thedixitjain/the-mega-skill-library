---
name: swarm-init
description: "Initialize a multi-agent swarm with anti-drift configuration. Use when starting a complex multi-file task that needs 3+ coordinated agents (feature implementation, refactor across modules, security audit). Skip for single-file edits or quick questions."
allowed-tools: "Bash(npx *) mcp__plugin_ruflo-core_ruflo__swarm_init mcp__plugin_ruflo-core_ruflo__swarm_status Task SendMessage"
category: ai-agents-and-harness
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-swarm/skills/swarm-init/SKILL.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-swarm/skills/swarm-init/SKILL.md
---

Initialize a hierarchical swarm for coordinated multi-agent work.

Via MCP: `mcp__plugin_ruflo-core_ruflo__swarm_init({ topology: "hierarchical", maxAgents: 8, strategy: "specialized" })`

Or via CLI:
```bash
npx @claude-flow/cli@latest swarm init --topology hierarchical --max-agents 8 --strategy specialized
```

Then spawn named agents in ONE message via Claude Code's `Task` tool with `name:` (for `SendMessage` addressability) and `run_in_background: true` (for parallel execution). Use `EnterWorktree` per agent for git-safe parallel work, and `SendMessage` for inter-agent coordination.

For larger teams (10+), use hierarchical-mesh topology:
```bash
npx @claude-flow/cli@latest swarm init --topology hierarchical-mesh --max-agents 15 --strategy specialized
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-swarm/skills/swarm-init/SKILL.md`
