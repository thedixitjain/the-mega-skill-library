---
name: audit-photon-fallback
description: "Find Databricks queries paying the Photon DBU premium while silently falling back to the Spark engine, and surface the plan seam + UDF-rewrite fix."
category: security-and-compliance
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/databricks-cluster-forensics/commands/audit-photon-fallback.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/databricks-cluster-forensics/commands/audit-photon-fallback.md
---


# /audit-photon-fallback

Audits whether Photon is earning its ~2x DBU premium or silently falling back to
Spark (pain D02).

## Usage

```
/audit-photon-fallback
```

## What it does

1. Reads recent `system.query.history` via the CLI Statement Execution API
   (needs `DATABRICKS_WAREHOUSE_ID` + the `system.query` grant chain) to find the
   slowest recent statements.
2. Inspects their physical plans for the "Photon does not support" seam and the
   `ColumnarToRow` / `RowToColumnar` boundaries that mark a fallback.
3. Confirms the cluster is Photon (`runtime_engine` via `clusters_get`).
4. Reports the queries paying the premium without the speedup and the fix — per
   `references/photon-eligibility-and-fallback.md`, usually rewriting a UDF as a
   native SQL expression so Photon engages, or turning Photon off for that workload.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/databricks-cluster-forensics/commands/audit-photon-fallback.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/databricks-pack/skills/databricks-cluster-forensics/commands/audit-photon-fallback.md`
