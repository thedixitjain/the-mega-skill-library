---
name: add-index
description: "Add database indexes to improve query performance with migration safety."
category: backend-and-data
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/database-optimizer/commands/add-index.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/database-optimizer/commands/add-index.md
---
Add database indexes to improve query performance with migration safety.

## Steps


1. Identify the query patterns that need indexing:
2. Choose the index type:
3. Design the index:
4. Create the migration:
5. Estimate the impact:
6. Deploy safely:

## Format


```
Table: <table name>
Index: <index name>
Columns: <column list>
Type: <B-tree|Hash|GIN|GiST>
```


## Rules

- Always use CONCURRENTLY for production index creation.
- Name indexes descriptively: idx_table_column1_column2.
- Do not create redundant indexes (check existing indexes first).

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/database-optimizer/commands/add-index.md`
