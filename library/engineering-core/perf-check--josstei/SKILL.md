---
name: perf-check
description: "Run a Maestro-style performance assessment for hotspots, regressions, and optimization planning"
category: engineering-core
source_repo: josstei/maestro-orchestrate
source_path: "plugins/maestro/skills/perf-check/SKILL.md"
source_url: https://github.com/josstei/maestro-orchestrate/blob/HEAD/plugins/maestro/skills/perf-check/SKILL.md
---


Read `../../references/runtime-guide.md`.
Call `get_skill_content` with resources: ["architecture", "delegation"].
Call `get_agent` with agents: ["performance-engineer"].

## Workflow

1. Define the performance target or pain point
2. Establish the current baseline from available code, metrics, or reproducible commands
3. Identify likely hotspots, structural bottlenecks, and hot loops through code analysis
4. Prioritize fixes by expected impact versus implementation cost
5. Report measurement gaps when hard evidence is unavailable and propose a validation plan

---

**Source:** [`josstei/maestro-orchestrate`](https://github.com/josstei/maestro-orchestrate) → `plugins/maestro/skills/perf-check/SKILL.md`
