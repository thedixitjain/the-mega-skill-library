---
name: awesome-cursorrules-postgresql
description: "PostgreSQL production rules. Safe migrations, parameterized queries, TIMESTAMPTZ, proper indexing strategy."
category: backend-and-data
source_repo: PatrickJS/awesome-cursorrules
source_path: "rules/postgresql.mdc"
source_url: https://github.com/PatrickJS/awesome-cursorrules/blob/HEAD/rules/postgresql.mdc
---

# PostgreSQL Rules

Expert PostgreSQL developer. Safe migrations, parameterized queries, proper indexing.

## Schema
- TIMESTAMPTZ for all timestamps (not TIMESTAMP without timezone)
- UUID for public IDs, BIGSERIAL for internal keys
- NOT NULL by default — nullable only when intentional
- FK with explicit ON DELETE behavior
- Check constraints for domain invariants

## Queries
- Parameterized always — never string interpolation
- SELECT explicit columns, never SELECT *
- LIMIT on all potentially large result sets
- EXPLAIN ANALYZE before shipping complex queries

## Indexes
- Index every FK column
- CREATE INDEX CONCURRENTLY for live tables (non-blocking)
- Partial indexes for frequently filtered subsets
- Remove unused indexes

## Migrations
- Versioned files: V001__create_table.sql
- Large column additions: multi-step with backfill
- Test rollback before deploying

## Transactions
- Explicit BEGIN/COMMIT for multi-statement changes
- statement_timeout to prevent runaway queries
- SELECT ... FOR UPDATE for row locking

## Forbidden
- No SELECT *
- No string-interpolated SQL
- No schema changes during peak traffic
- No plaintext passwords in DB
- No TRUNCATE in app code

---

**Source:** [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) → `rules/postgresql.mdc`
