---
name: investigate-cluster
description: "Triage a failed or slow Databricks cluster by fanning out parallel root-cause threads over its live event stream and returning the single most-likely cause with evidence."
category: security-and-compliance
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/databricks-cluster-forensics/commands/investigate-cluster.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/databricks-cluster-forensics/commands/investigate-cluster.md
---


# /investigate-cluster

Diagnoses one broken or anomalous Databricks cluster by invoking the
`cluster-event-investigator` subagent.

## Usage

```
/investigate-cluster <cluster_id> [symptom]
```

- `<cluster_id>` — the cluster to triage.
- `[symptom]` — optional, e.g. "never started", "died at 12 min", "randomly slow".

## What it does

Pulls the cluster's spec + event stream (`databricks-workspace-mcp` `clusters_get`
/ `clusters_events`, or a pasted `clusters.events` JSON in advisory mode), then runs
parallel investigation threads — provisioning, network/NPIP, init-script, driver,
spot/shuffle — and aggregates to the most-likely cause. It names the failure with
its actual `termination_reason.code` and cites the disambiguating check from
`references/termination-codes.md`. Read-only: it diagnoses, never restarts the cluster.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/databricks-cluster-forensics/commands/investigate-cluster.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/databricks-pack/skills/databricks-cluster-forensics/commands/investigate-cluster.md`
