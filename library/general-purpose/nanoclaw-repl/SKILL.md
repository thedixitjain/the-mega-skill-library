---
name: nanoclaw-repl
description: "Operate and extend NanoClaw v2, ECC's zero-dependency session-aware REPL built on claude -p."
category: general-purpose
source_repo: affaan-m/ECC
source_path: "skills/nanoclaw-repl/SKILL.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/skills/nanoclaw-repl/SKILL.md
---
# NanoClaw REPL

Use this skill when running or extending `scripts/claw.js`.

## Capabilities

- persistent markdown-backed sessions
- model switching with `/model`
- dynamic skill loading with `/load`
- session branching with `/branch`
- cross-session search with `/search`
- history compaction with `/compact`
- export to md/json/txt with `/export`
- session metrics with `/metrics`

## Operating Guidance

1. Keep sessions task-focused.
2. Branch before high-risk changes.
3. Compact after major milestones.
4. Export before sharing or archival.

## Extension Rules

- keep zero external runtime dependencies
- preserve markdown-as-database compatibility
- keep command handlers deterministic and local

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `skills/nanoclaw-repl/SKILL.md`

**Also appears in:** `hashgraph-online/awesome-codex-plugins/plugins/Colin4k1024/tsp/skills/nanoclaw-repl/SKILL.md`
