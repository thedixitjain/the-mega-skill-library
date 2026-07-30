---
name: perf-check
description: "Run a Maestro-style performance assessment for hotspots, regressions, and optimization planning"
category: engineering-core
source_repo: josstei/maestro-orchestrate
source_path: "claude/skills/perf-check/SKILL.md"
source_url: https://github.com/josstei/maestro-orchestrate/blob/HEAD/claude/skills/perf-check/SKILL.md
---



# Maestro Perf Check

Call `get_skill_content` with resources: ["architecture"].

## Protocol

Before delegating, call `get_skill_content` with resources: ["delegation"] and follow the returned methodology.

## Workflow

1. Define the performance target or pain point
2. Establish the current baseline from available code, metrics, or reproducible commands
3. Identify likely hotspots, structural bottlenecks, and hot loops through code analysis
4. Prioritize fixes by expected impact versus implementation cost
5. Report measurement gaps when hard evidence is unavailable and propose a validation plan

## Constraints

- Avoid optimization advice that is disconnected from the observed bottleneck
- Distinguish measured issues from inferred ones

---

**Source:** [`josstei/maestro-orchestrate`](https://github.com/josstei/maestro-orchestrate) → `claude/skills/perf-check/SKILL.md`
