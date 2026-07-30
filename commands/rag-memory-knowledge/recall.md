---
name: recall
description: "Quick semantic recall — searches all memory namespaces with MMR diversity and recency weighting"
category: rag-memory-knowledge
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-rag-memory/commands/recall.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-rag-memory/commands/recall.md
---

$ARGUMENTS

Semantic recall across all memory namespaces using HNSW vector search with MMR diversity reranking.

```bash
npx @claude-flow/cli@latest memory search --query "$ARGUMENTS" --limit 5
```

For richer results when ruvector is available:
```bash
npx ruvector search "$ARGUMENTS" --hybrid --limit 5
```

This searches across patterns, tasks, solutions, feedback, security, and claude-memories namespaces. Results are ranked by composite score: cosine similarity * MMR diversity * recency decay.

If no arguments provided, show recent memory entries:
```bash
npx @claude-flow/cli@latest memory list --limit 10
```

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-rag-memory/commands/recall.md`
