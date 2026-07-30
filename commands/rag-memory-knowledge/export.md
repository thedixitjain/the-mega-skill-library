---
name: export
description: ">- Export research findings to a format compatible with memory-palace's knowledge-intake skill."
category: rag-memory-knowledge
source_repo: athola/claude-night-market
source_path: "plugins/tome/commands/export.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/tome/commands/export.md
---


# Export Command

Export research findings for memory-palace ingestion.

## Usage

```bash
# Export latest session
/tome:export

# Export specific session
/tome:export --session abc123
```

## What Happens

1. Loads the specified or latest research session
2. Formats findings as a knowledge-intake compatible
   markdown file with metadata frontmatter
3. Saves to `docs/research/export-{session}.md`
4. Output can be processed by memory-palace's
   `knowledge-intake` skill without reformatting

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/tome/commands/export.md`
