---
name: nw-plugin-validator
description: "Use to validate Claude Code plugin structure and schema during DISTILL/DELIVER verification when deliverabletype is plugin. Validates plugin manifest, directory layout, hook/command/agent registration, and Claude Code plugin schema compliance. No existing agent knows the plugin schema. Runs on Haiku for cost efficiency."
category: ai-agents-and-harness
source_repo: nWave-ai/nWave
source_path: "docs/reference/agents/nw-plugin-validator.md"
source_url: https://github.com/nWave-ai/nWave/blob/HEAD/docs/reference/agents/nw-plugin-validator.md
---
# nw-plugin-validator

Use to validate Claude Code plugin structure and schema during DISTILL/DELIVER verification when deliverable_type is `plugin`. Validates plugin manifest, directory layout, hook/command/agent registration, and Claude Code plugin schema compliance. No existing agent knows the plugin schema. Runs on Haiku for cost efficiency.

**Wave:** Other
**Model:** haiku
**Max turns:** 20
**Tools:** Read, Glob, Grep

## Skills

- [nw-agent-creation-workflow](../skills/nw-agent-creation-workflow.md) — Detailed 5-phase workflow for creating agents - from requirements analysis through validation and iterative refinement

---

**Source:** [`nWave-ai/nWave`](https://github.com/nWave-ai/nWave) → `docs/reference/agents/nw-plugin-validator.md`
