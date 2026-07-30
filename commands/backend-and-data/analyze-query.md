---
name: analyze-query
description: "Analyze database queries for performance issues using EXPLAIN plans and query patterns."
category: backend-and-data
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/database-optimizer/commands/analyze-query.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/database-optimizer/commands/analyze-query.md
---
Analyze database queries for performance issues using EXPLAIN plans and query patterns.

## Steps


1. Identify the slow or problematic query:
2. Run EXPLAIN (or EXPLAIN ANALYZE) on the query:
3. Analyze common performance issues:
4. Check for lock contention:
5. Suggest optimizations:
6. Estimate improvement from each suggestion.

## Format


```
Query: <simplified query>
Current Time: <execution time>
Issues Found:
  - <issue>: <impact>
```


## Rules

- Always use EXPLAIN ANALYZE for real execution statistics.
- Consider the query frequency when prioritizing optimizations.
- Test optimizations on a staging environment first.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/database-optimizer/commands/analyze-query.md`
