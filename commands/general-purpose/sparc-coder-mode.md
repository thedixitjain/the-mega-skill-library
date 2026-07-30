---
name: sparc-coder-mode
description: "Autonomous code generation with batch file operations."
category: general-purpose
source_repo: ruvnet/RuView
source_path: ".claude/commands/sparc/coder.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/sparc/coder.md
---
# SPARC Coder Mode

## Purpose
Autonomous code generation with batch file operations.

## Activation

### Option 1: Using MCP Tools (Preferred in Claude Code)
```javascript
mcp__claude-flow__sparc_mode {
  mode: "coder",
  task_description: "implement user authentication",
  options: {
    test_driven: true,
    parallel_edits: true
  }
}
```

### Option 2: Using NPX CLI (Fallback when MCP not available)
```bash
# Use when running from terminal or MCP tools unavailable
npx claude-flow sparc run coder "implement user authentication"

# For alpha features
npx claude-flow@alpha sparc run coder "implement user authentication"
```

### Option 3: Local Installation
```bash
# If claude-flow is installed locally
./claude-flow sparc run coder "implement user authentication"
```

## Core Capabilities
- Feature implementation
- Code refactoring
- Bug fixes
- API development
- Algorithm implementation

## Batch Operations
- Parallel file creation
- Concurrent code modifications
- Batch import updates
- Test file generation
- Documentation updates

## Code Quality
- ES2022 standards
- Type safety with TypeScript
- Comprehensive error handling
- Performance optimization
- Security best practices

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/sparc/coder.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/sparc/coder.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/sparc/coder.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/sparc/coder.md`
