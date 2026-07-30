---
name: sparc-memory-manager-mode
description: "Knowledge management with Memory tools for persistent insights."
category: rag-memory-knowledge
source_repo: ruvnet/RuView
source_path: ".claude/commands/sparc/memory-manager.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/sparc/memory-manager.md
---
# SPARC Memory Manager Mode

## Purpose
Knowledge management with Memory tools for persistent insights.

## Activation

### Option 1: Using MCP Tools (Preferred in Claude Code)
```javascript
mcp__claude-flow__sparc_mode {
  mode: "memory-manager",
  task_description: "organize project knowledge",
  options: {
    namespace: "project",
    auto_organize: true
  }
}
```

### Option 2: Using NPX CLI (Fallback when MCP not available)
```bash
# Use when running from terminal or MCP tools unavailable
npx claude-flow sparc run memory-manager "organize project knowledge"

# For alpha features
npx claude-flow@alpha sparc run memory-manager "organize project knowledge"
```

### Option 3: Local Installation
```bash
# If claude-flow is installed locally
./claude-flow sparc run memory-manager "organize project knowledge"
```

## Core Capabilities
- Knowledge organization
- Information retrieval
- Context management
- Insight preservation
- Cross-session persistence

## Memory Strategies
- Hierarchical organization
- Tag-based categorization
- Temporal tracking
- Relationship mapping
- Priority management

## Knowledge Operations
- Store critical insights
- Retrieve relevant context
- Update knowledge base
- Merge related information
- Archive obsolete data

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/sparc/memory-manager.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/sparc/memory-manager.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/sparc/memory-manager.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/sparc/memory-manager.md`
