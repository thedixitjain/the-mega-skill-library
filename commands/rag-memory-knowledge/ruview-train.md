---
name: ruview-train
description: "Train a RuView model — camera-free WiFlow pose, camera-supervised pose (92.9% PCK@20), RuVector embeddings, domain generalization, local SNN, with optional GPU on GCloud."
category: rag-memory-knowledge
source_repo: ruvnet/RuView
source_path: "plugins/ruview/commands/ruview-train.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/plugins/ruview/commands/ruview-train.md
---


# /ruview-train

Train, fine-tune, evaluate, or publish a RuView model.

1. Invoke the **`ruview-model-training`** skill.
2. Pick the track from `$ARGUMENTS`; if empty, ask which:
   - **camera-free** (Track A) — `cargo run -p wifi-densepose-sensing-server -- --pretrain --dataset data/csi/ --pretrain-epochs 50` then `-- --train --dataset data/mmfi/ --epochs 100 --save-rvf model.rvf`. ~84 s on M4 Pro, modest accuracy.
   - **camera-supervised** (Track B, ADR-079) — `python scripts/collect-ground-truth.py`, `python scripts/collect-training-data.py`, `node scripts/align-ground-truth.js`, then train on `data/paired/`, eval with `node scripts/eval-wiflow.js`. ~19 min, 92.9% PCK@20. Needs `data/pose_landmarker_lite.task`.
   - **embeddings** (Track C, AETHER ADR-024) — `wifi-densepose-train` + `wifi-densepose-ruvector`; `-- --model model.rvf --embed`, `-- --build-index env`.
   - **domain-gen** (Track D, MERIDIAN ADR-027) / **snn** (Track E) — `node scripts/snn-csi-processor.js --port 5006`; cognitum-seed-pretraining tutorial.
   - **gpu** — `gcloud config set project cognitum-20260110`; `bash scripts/gcloud-train.sh --gpu l4 --hours 2` (or `--gpu a100 --sweep`, `--dry-run` to smoke-test). VM auto-deletes unless `--keep-vm`.
3. After training: `cd v2 && cargo test --workspace --no-default-features`, `python archive/v1/data/proof/verify.py`. To publish: `python scripts/publish-huggingface.py`.
4. Hand off to `/ruview-verify` for the witness bundle.

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `plugins/ruview/commands/ruview-train.md`
