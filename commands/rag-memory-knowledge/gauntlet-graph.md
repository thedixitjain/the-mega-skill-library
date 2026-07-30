---
name: gauntlet-graph
description: "Build, search, and query the code knowledge graph"
category: rag-memory-knowledge
source_repo: athola/claude-night-market
source_path: "plugins/gauntlet/commands/gauntlet-graph.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/gauntlet/commands/gauntlet-graph.md
---


# /gauntlet-graph

Manage the code knowledge graph.

## Subcommands

### `/gauntlet-graph build [dir]`

Build or update the graph for a directory (default: cwd).

Routes to: `Skill(gauntlet:graph-build)`

### `/gauntlet-graph search <query>`

Search the graph for code entities by name.

Routes to: `Skill(gauntlet:graph-search)`

### `/gauntlet-graph status`

Show graph statistics (node count, edge count,
last build time).

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/graph_query.py \
    --action status
```

## Routing Logic

Parse the user's arguments:

- No args or `build`: invoke `Skill(gauntlet:graph-build)`
- `search <query>`: invoke `Skill(gauntlet:graph-search)`
- `status`: run the status query directly and display

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/gauntlet/commands/gauntlet-graph.md`
