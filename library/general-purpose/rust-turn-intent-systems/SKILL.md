---
name: rust-turn-intent-systems
description: "Build and review turn-based Rust game flow using turn-state enums, phase-specific schedules, intent messages, movement resolution, combat resolution, wait actions, and win/loss states. Use when implementing roguelike turns, tactical action order, ECS message entities, or decoupled input and action systems."
category: general-purpose
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/LVTD-LLC/skills/skills/rust-turn-intent-systems/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/LVTD-LLC/skills/skills/rust-turn-intent-systems/SKILL.md
---


# Rust Turn Intent Systems

Use this skill to make turn-based gameplay deterministic and easy to extend.
Separate decision systems from resolution systems: input and AI create intents;
movement, combat, inventory, and end-turn systems resolve them.

## Core Workflow

1. Define the allowed turn phases in one enum.
2. Run different system schedules or branches for input, player resolution,
   monster resolution, and terminal states.
3. Convert input and AI decisions into intent components or messages.
4. Resolve intents in shared systems so players and monsters use the same rules.
5. Remove or mark intents after processing.
6. Advance the turn state in one end-turn boundary.

## Read Next

Read `references/turn-intent-patterns.md` for phase design, intent messages,
ordering rules, and review checks.

## Source Notes

Guidance is transformed and paraphrased from *Hands-On Rust* Chapters 7, 8,
9, and 13 and from the official companion source repository. The patterns are
generalized for Rust ECS projects and do not require using Legion.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/LVTD-LLC/skills/skills/rust-turn-intent-systems/SKILL.md`
