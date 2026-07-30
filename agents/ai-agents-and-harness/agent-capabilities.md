---
name: agent-capabilities
description: "Matrix of agent capabilities and their specializations."
category: ai-agents-and-harness
source_repo: ruvnet/ruflo
source_path: ".claude/commands/agents/agent-capabilities.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/agents/agent-capabilities.md
---
# agent-capabilities

Matrix of agent capabilities and their specializations.

## Capability Matrix

| Agent Type | Primary Skills | Best For |
|------------|---------------|----------|
| coder | Implementation, debugging | Feature development |
| researcher | Analysis, synthesis | Requirements gathering |
| tester | Testing, validation | Quality assurance |
| architect | Design, planning | System architecture |

## Querying Capabilities
```bash
# List all capabilities
npx claude-flow agents capabilities

# For specific agent
npx claude-flow agents capabilities --type coder
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/agents/agent-capabilities.md`
