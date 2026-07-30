---
name: extract-knowledge
description: "Rebuild the knowledge base from the current codebase"
category: rag-memory-knowledge
source_repo: athola/claude-night-market
source_path: "plugins/gauntlet/commands/gauntlet-extract.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/gauntlet/commands/gauntlet-extract.md
---


# Extract Knowledge

Invoke `Skill(gauntlet:extract)` to analyze the codebase and rebuild
`.gauntlet/knowledge.json`.

Arguments:

- No args: extract from current directory
- `<path>`: extract from specific directory

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/gauntlet/commands/gauntlet-extract.md`
