---
name: ruview-advanced
description: "Use advanced RuView capabilities — multistatic sensing, cross-viewpoint fusion, RF tomography, persistent field model, intention signals, adversarial detection, mesh security."
category: security-and-compliance
source_repo: ruvnet/RuView
source_path: "plugins/ruview/commands/ruview-advanced.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/plugins/ruview/commands/ruview-advanced.md
---


# /ruview-advanced

Drive RuView's research-grade / multi-node features.

1. Invoke the **`ruview-advanced-sensing`** skill.
2. Route on `$ARGUMENTS`:
   - **multistatic** (ADR-029) — `wifi-densepose-signal/src/ruvsense/multistatic.rs`, `phase_align.rs`, `coherence_gate.rs`; neighbours' APs as illuminators.
   - **cross-viewpoint** (ADR-016 viewpoint) — `wifi-densepose-ruvector/src/viewpoint/`; needs 2+ nodes; `node scripts/mesh-graph-transformer.js`.
   - **tomography** — `ruvsense/tomography.rs` (ISTA L1 voxel solver) + cross-viewpoint geometry; through-wall volumetric.
   - **field-model** (ADR-030) — `ruvsense/field_model.rs`, SVD room eigenstructure persisted to RVF (Cognitum Seed); residual = perturbation.
   - **intention** — `ruvsense/intention.rs`, 200–500 ms pre-movement lead signals.
   - **adversarial** — `ruvsense/adversarial.rs`, physically-impossible-signal + multi-link consistency checks.
   - **security** (ADR-032) — mesh hardening: adversarial gate + coherence quarantine + Ed25519 witness chain; run a security review (`docs/security-audit-wasm-edge-vendor.md`), see `/ruview-verify`.
3. Validate: `cd v2 && cargo test -p wifi-densepose-signal --no-default-features && cargo test -p wifi-densepose-ruvector --no-default-features`, then `python archive/v1/data/proof/verify.py`.

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `plugins/ruview/commands/ruview-advanced.md`
