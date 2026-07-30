---
name: dgx-spark-preflight
description: "Preflight a DGX Spark system for an ML training or inference workload and emit env-report.json"
category: data-science-and-ml
source_repo: wshobson/agents
source_path: "plugins/dgx-spark-ops/commands/spark-preflight.md"
source_url: https://github.com/wshobson/agents/blob/HEAD/plugins/dgx-spark-ops/commands/spark-preflight.md
---


# DGX Spark Preflight

Verify this DGX Spark system is ready for: $ARGUMENTS

<Task>
subagent_type: dgx-spark-ops-engineer
prompt: |
  Run a full preflight for the planned workload: $ARGUMENTS
  1. Confirm hardware identity (GB10/aarch64/CUDA 13) and stack per the spark-environment-setup skill.
  2. Execute checks G1–G10 from the spark-training-gotchas skill; record each check's result using the check vocabulary (pass/fail/warn/skip/info).
  3. Compute memory headroom for the workload with the spark-memory-thermal-ops worksheets.
  4. Write env-report.json to the current directory (schema in agent instructions) and summarize verdict: ready | ready-with-warnings | blocked, with the blocking gotcha named.
</Task>

Report the verdict and any warnings to the user. If blocked, present the specific fix from the gotcha's FIX entry before suggesting anything else.

---

**Source:** [`wshobson/agents`](https://github.com/wshobson/agents) → `plugins/dgx-spark-ops/commands/spark-preflight.md`
