---
name: sparc-architect-mode
description: "System design with Memory-based coordination for scalable architectures."
category: rag-memory-knowledge
source_repo: ruvnet/RuView
source_path: ".claude/commands/sparc/architect.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/sparc/architect.md
---
# SPARC Architect Mode

## Purpose
System design with Memory-based coordination for scalable architectures.

## Activation

### Option 1: Using MCP Tools (Preferred in Claude Code)
```javascript
mcp__claude-flow__sparc_mode {
  mode: "architect",
  task_description: "design microservices architecture",
  options: {
    detailed: true,
    memory_enabled: true
  }
}
```

### Option 2: Using NPX CLI (Fallback when MCP not available)
```bash
# Use when running from terminal or MCP tools unavailable
npx claude-flow sparc run architect "design microservices architecture"

# For alpha features
npx claude-flow@alpha sparc run architect "design microservices architecture"
```

### Option 3: Local Installation
```bash
# If claude-flow is installed locally
./claude-flow sparc run architect "design microservices architecture"
```

## Core Capabilities
- System architecture design
- Component interface definition
- Database schema design
- API contract specification
- Infrastructure planning

## Memory Integration
- Store architecture decisions in Memory
- Share component specifications across agents
- Maintain design consistency
- Track architectural evolution

## Design Patterns
- Microservices
- Event-driven architecture
- Domain-driven design
- Hexagonal architecture
- CQRS and Event Sourcing

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/sparc/architect.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/sparc/architect.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/sparc/architect.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/sparc/architect.md`
