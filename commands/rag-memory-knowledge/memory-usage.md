---
name: memory-usage
description: "Manage persistent memory storage."
category: rag-memory-knowledge
source_repo: ruvnet/ruflo
source_path: ".claude/commands/memory/memory-usage.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/memory/memory-usage.md
---
# memory-usage

Manage persistent memory storage.

## Usage
```bash
npx claude-flow memory usage [options]
```

## Options
- `--action <type>` - Action (store, retrieve, list, clear)
- `--key <key>` - Memory key
- `--value <data>` - Data to store (JSON)

## Examples
```bash
# Store memory
npx claude-flow memory usage --action store --key "project-config" --value '{"api": "v2"}'

# Retrieve memory
npx claude-flow memory usage --action retrieve --key "project-config"

# List all keys
npx claude-flow memory usage --action list
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/memory/memory-usage.md`

**Also appears in:** `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/memory/memory-usage.md`
