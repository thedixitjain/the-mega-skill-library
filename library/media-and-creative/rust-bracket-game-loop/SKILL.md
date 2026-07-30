---
name: rust-bracket-game-loop
description: "Build and review bracket-lib style Rust 2D game loops, state structs, game modes, input handling, rendering calls, and restart flow. Use when creating a small Rust game with bracket-lib, porting a tutorial loop, or debugging tick/update/render state behavior."
category: media-and-creative
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/LVTD-LLC/skills/skills/rust-bracket-game-loop/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/LVTD-LLC/skills/skills/rust-bracket-game-loop/SKILL.md
---


# Rust Bracket Game Loop

Use this skill to create or review a small Rust game loop, especially one built
with `bracket-lib` and an explicit game state. Keep `tick` as a coordinator:
read input, advance state, render, and dispatch to small helper functions.

## Core Workflow

1. Inspect the target project's `Cargo.toml`, edition, engine, and existing
   architecture before changing dependencies.
2. Create one state object that contains data preserved between frames.
3. Implement the engine trait or callback required by the project.
4. Route modes through an enum rather than scattered booleans.
5. Keep rendering and state mutation ordered and easy to trace.
6. Add a restart/reset path before adding many gameplay states.

## Read Next

Read `references/game-loop-patterns.md` for setup patterns, code skeletons,
mode routing, and review checks.

## Source Notes

Guidance is transformed and paraphrased from *Hands-On Rust* Chapter 3 and
the official companion source repository. Current crate context was checked
against `bracket-lib` documentation on docs.rs and the bracket-lib example
repository. Verify the target project's dependency versions before copying API
details.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/LVTD-LLC/skills/skills/rust-bracket-game-loop/SKILL.md`
