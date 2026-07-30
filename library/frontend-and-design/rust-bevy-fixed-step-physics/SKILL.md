---
name: rust-bevy-fixed-step-physics
description: "Design and review Bevy fixed-step 2D physics loops with velocity components, deterministic movement, collision prediction, interpolation, impulses, and tweened presentation. Use when movement depends on frame rate, collision misses appear at high speed, physics and animation are tangled, or Bevy gameplay needs stable simulation steps."
category: frontend-and-design
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/LVTD-LLC/skills/skills/rust-bevy-fixed-step-physics/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/LVTD-LLC/skills/skills/rust-bevy-fixed-step-physics/SKILL.md
---


# Rust Bevy Fixed Step Physics

Use this skill to separate deterministic simulation from frame-rate-dependent
presentation in Bevy games.

## Core Workflow

1. Identify which movement must be deterministic and collision-safe.
2. Sample input in update systems, then apply movement in fixed-step systems.
3. Store velocity, acceleration, and intent explicitly in components/resources.
4. Predict or sweep movement before committing positions.
5. Emit physics/collision events; keep animation and particles as presentation.
6. Interpolate or tween visuals when fixed simulation looks choppy.

## Read Next

| Task | Load |
|------|------|
| Fix frame-rate-dependent movement | `guidelines.md`, `workflows/stabilize-physics.md` |
| Add fixed movement and collision prediction | `references/fixed-step-patterns.md` |
| Separate animation from physics | `references/fixed-step-patterns.md` |

## Source Notes

Guidance is transformed and paraphrased from Herbert Wolverson,
*Advanced Hands-On Rust*, especially Chapters 7 through 9 on movement,
collision, and smoothing. Examples are original skeletons.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/LVTD-LLC/skills/skills/rust-bevy-fixed-step-physics/SKILL.md`
