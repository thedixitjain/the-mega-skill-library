---
name: sparc-batch-executor-mode
description: "Parallel task execution specialist using batch operations."
category: general-purpose
source_repo: ruvnet/RuView
source_path: ".claude/commands/sparc/batch-executor.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/sparc/batch-executor.md
---
# SPARC Batch Executor Mode

## Purpose
Parallel task execution specialist using batch operations.

## Activation

### Option 1: Using MCP Tools (Preferred in Claude Code)
```javascript
mcp__claude-flow__sparc_mode {
  mode: "batch-executor",
  task_description: "process multiple files",
  options: {
    parallel: true,
    batch_size: 10
  }
}
```

### Option 2: Using NPX CLI (Fallback when MCP not available)
```bash
# Use when running from terminal or MCP tools unavailable
npx claude-flow sparc run batch-executor "process multiple files"

# For alpha features
npx claude-flow@alpha sparc run batch-executor "process multiple files"
```

### Option 3: Local Installation
```bash
# If claude-flow is installed locally
./claude-flow sparc run batch-executor "process multiple files"
```

## Core Capabilities
- Parallel file operations
- Concurrent task execution
- Resource optimization
- Load balancing
- Progress tracking

## Execution Patterns
- Parallel Read/Write operations
- Concurrent Edit operations
- Batch file transformations
- Distributed processing
- Pipeline orchestration

## Performance Features
- Dynamic resource allocation
- Automatic load balancing
- Progress monitoring
- Error recovery
- Result aggregation

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/sparc/batch-executor.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/sparc/batch-executor.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/sparc/batch-executor.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/sparc/batch-executor.md`
