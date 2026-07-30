---
name: rust-crate-publishing-readiness
description: "Prepare Rust crates for publishing with Cargo metadata, versioning, README and license checks, package dry-runs, feature verification, docs.rs readiness, examples, changelog notes, and secret-safe release gates. Use before cargo publish, crate release PRs, or sharing a reusable Rust library."
category: docs-and-knowledge-mgmt
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/LVTD-LLC/skills/skills/rust-crate-publishing-readiness/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/LVTD-LLC/skills/skills/rust-crate-publishing-readiness/SKILL.md
---


# Rust Crate Publishing Readiness

Use this skill before publishing or sharing a Rust crate. It focuses on the
consumer-facing package, not on deployment of a running service.

## Core Workflow

1. Verify package metadata, license, README, repository, and categories.
2. Check public API, feature flags, examples, and docs from a consumer's view.
3. Run tests, docs, formatting, and feature-matrix checks.
4. Run `cargo package` or `cargo publish --dry-run`.
5. Inspect packaged contents for missing files and accidental secrets.
6. Publish only from a clean, tagged, intentional release state.

## Read Next

| Task | Load |
|------|------|
| Prepare a crate release PR | `guidelines.md`, `workflows/prepare-crate-release.md` |
| Review Cargo metadata and package contents | `references/publishing-patterns.md` |
| Diagnose dry-run failures | `references/publishing-patterns.md` |

## Source Notes

Guidance is transformed and paraphrased from Herbert Wolverson,
*Advanced Hands-On Rust*, especially Chapter 15 on sharing libraries and the
earlier chapters on tests, docs, benchmarks, and features. Examples are
original skeletons.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/LVTD-LLC/skills/skills/rust-crate-publishing-readiness/SKILL.md`
