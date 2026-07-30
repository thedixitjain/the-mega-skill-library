---
name: sparc-swarm-coordinator-mode
description: "Specialized swarm management with batch coordination capabilities."
category: ai-agents-and-harness
source_repo: ruvnet/RuView
source_path: ".claude/commands/sparc/swarm-coordinator.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/.claude/commands/sparc/swarm-coordinator.md
---
# SPARC Swarm Coordinator Mode

## Purpose
Specialized swarm management with batch coordination capabilities.

## Activation

### Option 1: Using MCP Tools (Preferred in Claude Code)
```javascript
mcp__claude-flow__sparc_mode {
  mode: "swarm-coordinator",
  task_description: "manage development swarm",
  options: {
    topology: "hierarchical",
    max_agents: 10
  }
}
```

### Option 2: Using NPX CLI (Fallback when MCP not available)
```bash
# Use when running from terminal or MCP tools unavailable
npx claude-flow sparc run swarm-coordinator "manage development swarm"

# For alpha features
npx claude-flow@alpha sparc run swarm-coordinator "manage development swarm"
```

### Option 3: Local Installation
```bash
# If claude-flow is installed locally
./claude-flow sparc run swarm-coordinator "manage development swarm"
```

## Core Capabilities
- Swarm initialization
- Agent management
- Task distribution
- Load balancing
- Result collection

## Coordination Modes
- Hierarchical swarms
- Mesh networks
- Pipeline coordination
- Adaptive strategies
- Hybrid approaches

## Management Features
- Dynamic scaling
- Resource optimization
- Failure recovery
- Performance monitoring
- Quality assurance

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `.claude/commands/sparc/swarm-coordinator.md`

**Also appears in:** `ruvnet/ruflo/.claude/commands/sparc/swarm-coordinator.md`, `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/sparc/swarm-coordinator.md`, `ruvnet/ruflo/v3/@claude-flow/mcp/.claude/commands/sparc/swarm-coordinator.md`
