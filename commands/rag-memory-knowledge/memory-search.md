---
name: memory-search
description: "Search through stored memory."
category: rag-memory-knowledge
source_repo: ruvnet/ruflo
source_path: ".claude/commands/memory/memory-search.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/memory/memory-search.md
---
# memory-search

Search through stored memory.

## Usage
```bash
npx claude-flow memory search [options]
```

## Options
- `--query <text>` - Search query
- `--pattern <regex>` - Pattern matching
- `--limit <n>` - Result limit

## Examples
```bash
# Search memory
npx claude-flow memory search --query "authentication"

# Pattern search
npx claude-flow memory search --pattern "api-.*"

# Limited results
npx claude-flow memory search --query "config" --limit 10
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/memory/memory-search.md`

**Also appears in:** `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/memory/memory-search.md`
