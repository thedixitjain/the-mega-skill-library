---
name: vector-index-tuning
description: "Optimize vector index performance for latency, recall, and memory. Use when tuning HNSW parameters, selecting quantization strategies, or scaling vector search infrastructure."
category: rag-memory-knowledge
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/vector-index-tuning/SKILL.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/vector-index-tuning/SKILL.md
---


# Vector Index Tuning

Guide to optimizing vector indexes for production performance.

## Use this skill when

- Tuning HNSW parameters
- Implementing quantization
- Optimizing memory usage
- Reducing search latency
- Balancing recall vs speed
- Scaling to billions of vectors

## Do not use this skill when

- You only need exact search on small datasets (use a flat index)
- You lack workload metrics or ground truth to validate recall
- You need end-to-end retrieval system design beyond index tuning

## Instructions

1. Gather workload targets (latency, recall, QPS), data size, and memory budget.
2. Choose an index type and establish a baseline with default parameters.
3. Benchmark parameter sweeps using real queries and track recall, latency, and memory.
4. Validate changes on a staging dataset before rolling out to production.

Refer to `resources/implementation-playbook.md` for detailed patterns, checklists, and templates.

## Safety

- Avoid reindexing in production without a rollback plan.
- Validate changes under realistic load before applying globally.
- Track recall regressions and revert if quality drops.

## Resources

- `resources/implementation-playbook.md` for detailed patterns, checklists, and templates.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/vector-index-tuning/SKILL.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/vector-index-tuning/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/vector-index-tuning/SKILL.md`
