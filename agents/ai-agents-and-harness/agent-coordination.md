---
name: agent-coordination
description: "Coordination patterns for multi-agent collaboration."
category: ai-agents-and-harness
source_repo: ruvnet/ruflo
source_path: ".claude/commands/agents/agent-coordination.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/agents/agent-coordination.md
---
# agent-coordination

Coordination patterns for multi-agent collaboration.

## Coordination Patterns

### Hierarchical
Queen-led with worker specialization
```bash
npx claude-flow swarm init --topology hierarchical
```

### Mesh
Peer-to-peer collaboration
```bash
npx claude-flow swarm init --topology mesh
```

### Adaptive
Dynamic topology based on workload
```bash
npx claude-flow swarm init --topology adaptive
```

## Best Practices
- Use hierarchical for complex projects
- Use mesh for research tasks
- Use adaptive for unknown workloads

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/agents/agent-coordination.md`

**Also appears in:** `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/agents/agent-coordination.md`
