---
name: sparc-debugger-mode
description: "Systematic debugging with TodoWrite and Memory integration."
category: engineering-core
source_repo: ruvnet/RuView
source_path: ".claude/commands/sparc/debugger.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/sparc/debugger.md
---
# SPARC Debugger Mode

## Purpose
Systematic debugging with TodoWrite and Memory integration.

## Activation

### Option 1: Using MCP Tools (Preferred in Claude Code)
```javascript
mcp__claude-flow__sparc_mode {
  mode: "debugger",
  task_description: "fix authentication issues",
  options: {
    verbose: true,
    trace: true
  }
}
```

### Option 2: Using NPX CLI (Fallback when MCP not available)
```bash
# Use when running from terminal or MCP tools unavailable
npx claude-flow sparc run debugger "fix authentication issues"

# For alpha features
npx claude-flow@alpha sparc run debugger "fix authentication issues"
```

### Option 3: Local Installation
```bash
# If claude-flow is installed locally
./claude-flow sparc run debugger "fix authentication issues"
```

## Core Capabilities
- Issue reproduction
- Root cause analysis
- Stack trace analysis
- Memory leak detection
- Performance bottleneck identification

## Debugging Workflow
1. Create debugging plan with TodoWrite
2. Systematic issue investigation
3. Store findings in Memory
4. Track fix progress
5. Verify resolution

## Tools Integration
- Error log analysis
- Breakpoint simulation
- Variable inspection
- Call stack tracing
- Memory profiling

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/sparc/debugger.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/sparc/debugger.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/sparc/debugger.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/sparc/debugger.md`
