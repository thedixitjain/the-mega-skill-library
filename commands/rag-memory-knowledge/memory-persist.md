---
name: memory-persist
description: "Persist memory across sessions."
category: rag-memory-knowledge
source_repo: ruvnet/ruflo
source_path: ".claude/commands/memory/memory-persist.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/.claude/commands/memory/memory-persist.md
---
# memory-persist

Persist memory across sessions.

## Usage
```bash
npx claude-flow memory persist [options]
```

## Options
- `--export <file>` - Export to file
- `--import <file>` - Import from file
- `--compress` - Compress memory data

## Examples
```bash
# Export memory
npx claude-flow memory persist --export memory-backup.json

# Import memory
npx claude-flow memory persist --import memory-backup.json

# Compressed export
npx claude-flow memory persist --export memory.gz --compress
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `.claude/commands/memory/memory-persist.md`

**Also appears in:** `ruvnet/ruflo/v3/@claude-flow/cli/.claude/commands/memory/memory-persist.md`
