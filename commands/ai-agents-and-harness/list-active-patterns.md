---
name: list-active-patterns
description: "This tool coordinates Claude Code's actions. It does NOT write code or create content."
category: ai-agents-and-harness
source_repo: ruvnet/RuView
source_path: ".claude/commands/monitoring/agents.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/monitoring/agents.md
---
# List Active Patterns

## 🎯 Key Principle
**This tool coordinates Claude Code's actions. It does NOT write code or create content.**

## MCP Tool Usage in Claude Code

**Tool:** `mcp__claude-flow__agent_list`

## Parameters
```json
{
  "swarmId": "current"
}
```

## Description
View all active cognitive patterns and their current focus areas

## Details
Filters:
- **all**: Show all defined patterns
- **active**: Currently engaged patterns
- **idle**: Available but unused patterns
- **busy**: Patterns actively coordinating tasks

## Example Usage

**In Claude Code:**
1. List all agents: Use tool `mcp__claude-flow__agent_list`
2. Get specific agent metrics: Use tool `mcp__claude-flow__agent_metrics` with parameters `{"agentId": "coder-123"}`
3. Monitor agent performance: Use tool `mcp__claude-flow__swarm_monitor` with parameters `{"interval": 2000}`

## Important Reminders
- ✅ This tool provides coordination and structure
- ✅ Claude Code performs all actual implementation
- ❌ The tool does NOT write code
- ❌ The tool does NOT access files directly
- ❌ The tool does NOT execute commands

## See Also
- Main documentation: /CLAUDE.md
- Other commands in this category
- Workflow examples in /workflows/

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/monitoring/agents.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/monitoring/agents.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/monitoring/agents.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/monitoring/agents.md`
