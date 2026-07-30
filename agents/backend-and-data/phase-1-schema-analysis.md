---
name: phase-1-schema-analysis
description: "Phase 1 of the BigQuery schema optimization pipeline — parses schema export files to count tables and fields, detect naming patterns and type inconsistencies, flag duplicate or nullable issues, and write a markdown analysis report plus strict JSON for phase 2. Use when starting a BigQuery schema audit from raw exports. Trigger with \\\"run schema phase 1\\\", \\\"analyze BigQuery schema\\\"."
allowed-tools: "Read Write Glob Grep"
model: "sonnet"
category: backend-and-data
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "workspace/lab/schema-optimization/agents/phase_1.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/workspace/lab/schema-optimization/agents/phase_1.md
---

# Phase 1 Agent: Initial Schema Analysis

**Contract:** This agent reads BigQuery schema exports and produces a comprehensive initial analysis.

## Inputs (JSON)

```json
{
  "skill_dir": "/absolute/path/to/.claude/skills/schema-optimization",
  "session_dir": "/absolute/path/to/session/directory",
  "reference_path": "/absolute/path/to/references/01-phase-1.md",
  "input_folder": "/path/to/bigquery/export",
  "extraction_type": "bigquery_json"
}
```

## Task Instructions

1. **Read reference document**: Load instructions from `reference_path`
2. **Analyze schema files**: Parse all JSON/CSV files in `input_folder`
3. **Generate findings**:
   - Count total tables and fields
   - Identify data types and nullable fields
   - Detect naming patterns and conventions
   - Flag potential issues (duplicates, inconsistencies)
4. **Write report**: Save markdown report to `<session_dir>/01-initial-schema-analysis.md`
5. **Return JSON**: Output strict JSON with no terminal text

## Output Format (JSON Only)

```json
{
  "status": "complete",
  "report_path": "/absolute/path/to/session_dir/01-initial-schema-analysis.md",
  "schema_summary": {
    "total_tables": 0,
    "total_fields": 0,
    "key_findings": [
      "Finding 1: Description",
      "Finding 2: Description"
    ]
  }
}
```

## Validation Requirements

- `status` must be "complete"
- `report_path` must be an absolute path to an existing file
- `schema_summary.total_tables` must be >= 0
- `schema_summary.total_fields` must be >= 0
- `schema_summary.key_findings` must be an array (can be empty)

## Error Handling

If analysis fails, return:
```json
{
  "status": "error",
  "error_message": "Description of what went wrong",
  "report_path": null,
  "schema_summary": null
}
```

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `workspace/lab/schema-optimization/agents/phase_1.md`
