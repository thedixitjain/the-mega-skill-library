---
name: hive-mind
description: "> Byzantine fault-tolerant consensus and distributed coordination. Queen-led hierarchical swarm management with multiple consensus strategies. Use when: distributed coordination, fault-tolerant operations, multi-agent consensus, collective decision making. Skip when: single-agent tasks, simple operations, local-only work."
category: ai-agents-and-harness
source_repo: ruvnet/ruflo
source_path: ".agents/skills/hive-mind/SKILL.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.agents/skills/hive-mind/SKILL.md
---


# Hive-Mind Skill

## Purpose
Byzantine fault-tolerant consensus and distributed swarm coordination.

## When to Trigger
- Multi-agent distributed tasks
- Fault-tolerant operations needed
- Collective decision making
- Complex coordination patterns

## Topologies

| Topology | Description | Use Case |
|----------|-------------|----------|
| `hierarchical` | Queen controls workers | Default, anti-drift |
| `mesh` | Fully connected peers | Research, exploration |
| `hierarchical-mesh` | Hybrid | Recommended for complex |
| `adaptive` | Dynamic based on load | Auto-scaling |

## Consensus Strategies

| Strategy | Tolerance | Use Case |
|----------|-----------|----------|
| `byzantine` | f < n/3 faulty | Untrusted environment |
| `raft` | f < n/2 faulty | Leader-based, consistent |
| `gossip` | Eventual | Large scale, availability |
| `crdt` | Conflict-free | Concurrent updates |
| `quorum` | Configurable | Tunable consistency |

## Commands

### Initialize Hive-Mind
```bash
npx claude-flow hive-mind init --topology hierarchical-mesh --consensus raft
```

### Spawn Queen
```bash
npx claude-flow hive-mind spawn --role queen --name coordinator
```

### Check Consensus Status
```bash
npx claude-flow hive-mind consensus --status
```

### View Sessions
```bash
npx claude-flow hive-mind sessions --active
```

## Best Practices
1. Use hierarchical for coding tasks (anti-drift)
2. Use raft consensus for consistency
3. Keep agent count under 8 for coordination
4. Run frequent checkpoints

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.agents/skills/hive-mind/SKILL.md`
