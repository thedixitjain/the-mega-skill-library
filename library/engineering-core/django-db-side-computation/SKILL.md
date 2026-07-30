---
name: django-db-side-computation
description: "Move Django performance-sensitive Python loops into database-side computation with annotations, aggregates, filtered aggregates, F expressions, functions, Subquery, OuterRef, Exists, Window expressions, db_default, and GeneratedField. Use when Django code counts, sums, filters, flags, ranks, or derives values in Python after fetching rows."
category: engineering-core
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/LVTD-LLC/skills/skills/django-db-side-computation/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/LVTD-LLC/skills/skills/django-db-side-computation/SKILL.md
---


# Django DB-Side Computation

Use this skill when Django fetches rows into Python to compute values the database can compute more efficiently or more consistently.

## Workflow

1. Identify the Python computation.
   - Counts, sums, min/max, booleans, latest related rows, rankings, denormalized totals, or per-row derived fields.
   - Confirm whether the computed value must be exact, current, and transactionally consistent.

2. Pick the SQL expression level.
   - `filter()`, `exclude()`, and `F()` for simple comparisons and updates.
   - `annotate()` and aggregates for per-object counts and totals.
   - Filtered aggregates for conditional counts and sums.
   - `Exists()` for yes/no related-row checks.
   - `Subquery()` with `OuterRef()` for latest or scalar related values.
   - `Window()` for ranks and running calculations.
   - `GeneratedField` for deterministic same-row computed columns when the database supports it.

3. Validate query shape.
   - Inspect generated SQL or `QuerySet.explain()`.
   - Clear unintended ordering before grouping when needed.
   - Confirm indexes support joins, filters, and ordering.

4. Decide whether the result should be stored.
   - Use annotations for request-time values.
   - Use generated fields for same-row deterministic values.
   - Use materialized views or denormalized tables when cross-row aggregate queries are too expensive and can be stale.

See [aggregation-patterns.md](references/aggregation-patterns.md) for Django expression examples.

## Safety Notes

- Database computation is not always faster; complex queries can overload the database or block OLTP work.
- Generated fields have database-specific restrictions and PostgreSQL supports only persisted generated columns.
- Subqueries and annotations can duplicate work if composed carelessly. Read the plan.

## Verification

Compare correctness against the old Python calculation on representative data, then measure SQL time and total response time.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/LVTD-LLC/skills/skills/django-db-side-computation/SKILL.md`
