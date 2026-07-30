---
name: agent-spawning
description: "Guide to spawning agents with Claude Code's Task tool."
category: ai-agents-and-harness
source_repo: ruvnet/ruflo
source_path: ".claude/commands/agents/agent-spawning.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/agents/agent-spawning.md
---
# agent-spawning

Guide to spawning agents with Claude Code's Task tool.

## Using Claude Code's Task Tool

**CRITICAL**: Always use Claude Code's Task tool for actual agent execution:

```javascript
// Spawn ALL agents in ONE message
Task("Researcher", "Analyze requirements...", "researcher")
Task("Coder", "Implement features...", "coder")
Task("Tester", "Create tests...", "tester")
```

## MCP Coordination Setup (Optional)

MCP tools are ONLY for coordination:
```javascript
mcp__claude-flow__swarm_init { topology: "mesh" }
mcp__claude-flow__agent_spawn { type: "researcher" }
```

## Best Practices
1. Always spawn agents concurrently
2. Use Task tool for execution
3. MCP only for coordination
4. Batch all operations

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/agents/agent-spawning.md`

**Also appears in:** `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/agents/agent-spawning.md`
