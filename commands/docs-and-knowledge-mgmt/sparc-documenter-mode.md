---
name: sparc-documenter-mode
description: "Documentation with batch file operations for comprehensive docs."
category: docs-and-knowledge-mgmt
source_repo: ruvnet/RuView
source_path: ".claude/commands/sparc/documenter.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/sparc/documenter.md
---
# SPARC Documenter Mode

## Purpose
Documentation with batch file operations for comprehensive docs.

## Activation

### Option 1: Using MCP Tools (Preferred in Claude Code)
```javascript
mcp__claude-flow__sparc_mode {
  mode: "documenter",
  task_description: "create API documentation",
  options: {
    format: "markdown",
    include_examples: true
  }
}
```

### Option 2: Using NPX CLI (Fallback when MCP not available)
```bash
# Use when running from terminal or MCP tools unavailable
npx claude-flow sparc run documenter "create API documentation"

# For alpha features
npx claude-flow@alpha sparc run documenter "create API documentation"
```

### Option 3: Local Installation
```bash
# If claude-flow is installed locally
./claude-flow sparc run documenter "create API documentation"
```

## Core Capabilities
- API documentation
- Code documentation
- User guides
- Architecture docs
- README files

## Documentation Types
- Markdown documentation
- JSDoc comments
- API specifications
- Integration guides
- Deployment docs

## Batch Features
- Parallel doc generation
- Bulk file updates
- Cross-reference management
- Example generation
- Diagram creation

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/sparc/documenter.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/sparc/documenter.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/sparc/documenter.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/sparc/documenter.md`
