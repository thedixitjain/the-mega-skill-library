---
name: rust-data-driven-game-content
description: "Move Rust game monsters, items, loot, effects, spawn weights, level gates, and balance numbers into validated data files using Serde-friendly schemas. Use when replacing hard-coded spawn functions, adding RON or JSON content templates, or making game content editable without recompiling."
category: backend-and-data
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/LVTD-LLC/skills/skills/rust-data-driven-game-content/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/LVTD-LLC/skills/skills/rust-data-driven-game-content/SKILL.md
---


# Rust Data Driven Game Content

Use this skill to move game content out of Rust code and into validated data
files. Keep schemas small, explicit, and aligned with components the game can
actually spawn.

## Core Workflow

1. Identify repeated hard-coded spawn data.
2. Design a Serde-friendly schema for entities, effects, spawn levels, and
   weights.
3. Load data at startup or level generation with clear errors.
4. Convert templates into component bundles through one spawn boundary.
5. Add validation for missing fields, impossible levels, invalid effects, and
   empty spawn tables.
6. Keep balance changes in data and behavior changes in Rust systems.

## Read Next

Read `references/data-driven-content-patterns.md` for schema design,
RON/Serde notes, spawn weighting, validation, and review checks.

## Source Notes

Guidance is transformed and paraphrased from *Hands-On Rust* Chapters 13, 14,
and 15 and from the official companion source repository. Current crate context
was checked against Serde and RON docs. Verify the target project's chosen data
format and dependency versions before editing.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/LVTD-LLC/skills/skills/rust-data-driven-game-content/SKILL.md`
