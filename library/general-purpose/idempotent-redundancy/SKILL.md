---
name: idempotent-redundancy
description: "Idempotent Redundancy"
category: general-purpose
source_repo: parcadei/Continuous-Claude-v3
source_path: ".claude/skills/idempotent-redundancy/SKILL.md"
source_url: https://github.com/parcadei/Continuous-Claude-v3/blob/HEAD/.claude/skills/idempotent-redundancy/SKILL.md
---


# Idempotent Redundancy

When adding redundant paths (fallbacks, belt-and-suspenders), make them idempotent.

## Pattern

Redundancy without idempotency causes loops, churn, or data corruption.

## DO
- Use `_is_merge: true` for Braintrust updates
- Check if value exists before writing (fallback only if missing)
- Use atomic write/rename for file operations
- Make reconciliation steps safe to run repeatedly

## DON'T
- Write unconditionally in fallback paths
- Allow multiple writers to overwrite each other
- Fire "repair" actions that can trigger more repairs

## Source Sessions
- a541f08a: "Redundancy is good only if idempotent"
- 1c21e6c8: "Belt-and-suspenders, but make it idempotent"
- 6a9f2d7a: "Idempotent repair hooks"

---

**Source:** [`parcadei/Continuous-Claude-v3`](https://github.com/parcadei/Continuous-Claude-v3) → `.claude/skills/idempotent-redundancy/SKILL.md`
