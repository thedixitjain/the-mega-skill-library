---
name: rust-library-performance-features
description: "Optimize Rust libraries with criterion benchmarks, feature-flag matrices, cargo bench workflows, dependency gating, regression baselines, and evidence-driven API performance tradeoffs. Use when adding or reviewing Rust library benchmarks, cargo features, optional dependencies, or performance claims before publishing."
category: engineering-core
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/LVTD-LLC/skills/skills/rust-library-performance-features/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/LVTD-LLC/skills/skills/rust-library-performance-features/SKILL.md
---


# Rust Library Performance Features

Use this skill when a Rust library needs performance work that can be measured
and shipped behind clear Cargo feature boundaries.

## Core Workflow

1. Define the library operation and input sizes that matter to downstream users.
2. Add or repair benchmarks before optimizing.
3. Compare baseline and candidate implementations with the same harness.
4. Use Cargo features for optional capabilities and dependencies.
5. Test the feature matrix, including default features disabled.
6. Document performance claims with scope and measurement commands.

## Read Next

| Task | Load |
|------|------|
| Add benchmarks or optimize a hot path | `guidelines.md`, `workflows/benchmark-feature-matrix.md` |
| Review Cargo features and optional dependencies | `references/performance-feature-patterns.md` |
| Validate performance claims before release | `references/performance-feature-patterns.md` |

## Source Notes

Guidance is transformed and paraphrased from Herbert Wolverson,
*Advanced Hands-On Rust*, especially Chapters 2 and 3 on creating, testing,
optimizing, benchmarking, and feature-gating a library. Examples are original
skeletons.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/LVTD-LLC/skills/skills/rust-library-performance-features/SKILL.md`
