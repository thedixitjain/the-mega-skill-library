---
name: mermaid
description: "Create entity relationship diagrams using Mermaid from SQL/database files"
allowed-tools: "Read, Write, Bash, Glob"
category: backend-and-data
source_repo: davepoon/buildwithclaude
source_path: "plugins/all-commands/commands/mermaid.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/all-commands/commands/mermaid.md
---


Create Mermaid entity relationship diagrams (ERD) from SQL migration files or database schemas.

## Process:

1. **Parse Arguments**:
   - First argument: Source path (SQL files or directory)
   - Second argument: Output path (optional, defaults to `docs/erd.md`)

2. **Find SQL/Schema Files**:
   - Look for SQL files: `*.sql`, `*.ddl`
   - Check common locations if no path provided:
     - `migrations/`, `db/migrations/`, `schema/`
     - `database/`, `sql/`
   - Support multiple database formats:
     - PostgreSQL, MySQL, SQLite
     - Migration files (Rails, Django, Flyway, etc.)

3. **Extract Schema Information**:
   - Parse CREATE TABLE statements
   - Extract table names, columns, and data types
   - Identify primary keys, foreign keys, and relationships
   - Handle indexes and constraints

4. **Generate Mermaid ERD**:
   ```mermaid
   erDiagram
     CUSTOMER ||--o{ ORDER : places
     ORDER ||--|{ LINE-ITEM : contains
     CUSTOMER {
       string name
       string email
       int id PK
     }
   ```

5. **Validate Diagram**:
   - If mermaid-cli is available: `npx -p @mermaid-js/mermaid-cli mmdc -i output.md -o temp.svg`
   - Alternative validation: Check syntax manually
   - Clean up temporary files

6. **Output Options**:
   - Single file with all entities
   - Separate files per schema/database
   - Include relationship descriptions

## Example Usage:
- `/mermaid migrations/` - Create ERD from all SQL files in migrations
- `/mermaid schema.sql docs/database-erd.md` - Create ERD from specific file
- `/mermaid "db/**/*.sql" erd/` - Create ERDs for all SQL files

Source: $ARGUMENTS

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/all-commands/commands/mermaid.md`

**Also appears in:** `davepoon/buildwithclaude/plugins/commands-miscellaneous/commands/mermaid.md`
