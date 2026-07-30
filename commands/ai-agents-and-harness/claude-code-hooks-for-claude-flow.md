---
name: claude-code-hooks-for-claude-flow
description: "Automatically coordinate, format, and learn from Claude Code operations using hooks."
category: ai-agents-and-harness
source_repo: ruvnet/RuView
source_path: ".claude/commands/hooks/overview.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/hooks/overview.md
---
# Claude Code Hooks for claude-flow

## Purpose
Automatically coordinate, format, and learn from Claude Code operations using hooks.

## Available Hooks

### Pre-Operation Hooks
- **pre-edit**: Validate and assign agents before file modifications
- **pre-bash**: Check command safety and resource requirements
- **pre-task**: Auto-spawn agents for complex tasks

### Post-Operation Hooks
- **post-edit**: Auto-format code and train neural patterns
- **post-bash**: Log execution and update metrics
- **post-search**: Cache results and improve search patterns

### MCP Integration Hooks
- **mcp-initialized**: Persist swarm configuration
- **agent-spawned**: Update agent roster
- **task-orchestrated**: Monitor task progress
- **neural-trained**: Save pattern improvements

### Session Hooks
- **notify**: Custom notifications with swarm status
- **session-end**: Generate summary and save state
- **session-restore**: Load previous session state

## Configuration
Hooks are configured in `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "^(Write|Edit|MultiEdit)$",
        "hooks": [{
          "type": "command",
          "command": "npx claude-flow hook pre-edit --file '${tool.params.file_path}'"
        }]
      }
    ]
  }
}
```

## Benefits
- 🤖 Automatic agent assignment based on file type
- 🎨 Consistent code formatting
- 🧠 Continuous neural pattern improvement
- 💾 Cross-session memory persistence
- 📊 Performance metrics tracking

## See Also
- [Pre-Edit Hook](./pre-edit.md)
- [Post-Edit Hook](./post-edit.md)
- [Session End Hook](./session-end.md)

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/hooks/overview.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/hooks/overview.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/hooks/overview.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/hooks/overview.md`
