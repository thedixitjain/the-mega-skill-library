---
name: ruview-app
description: "Run a RuView sensing application — presence, vitals, pose, sleep, environment mapping, MAT, point cloud, or a novel RF app."
category: devops-and-infra
source_repo: ruvnet/RuView
source_path: "plugins/ruview/commands/ruview-app.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/plugins/ruview/commands/ruview-app.md
---


# /ruview-app

Launch a RuView application.

1. Invoke the **`ruview-applications`** skill.
2. Map `$ARGUMENTS` to an application; if empty, show the catalogue and ask. Quick mappings:
   - `presence` / `vitals` / `pose` / `environment` → `cd v2 && cargo run -p wifi-densepose-sensing-server` (live ESP32 sink) or the Docker demo for simulated CSI; for environment also `--build-index env`.
   - `sleep` → `examples/sleep/` + `node scripts/apnea-detector.js`.
   - `mat` (Mass Casualty Assessment) → `wifi-densepose-mat` crate, `docs/wifi-mat-user-guide.md`.
   - `pointcloud` → `python scripts/mmwave_fusion_bridge.py` (camera depth + CSI + mmWave).
   - novel RF → `scripts/passive-radar.js`, `material-classifier.js`, `device-fingerprint.js`, `mincut-person-counter.js`.
3. If no hardware: fall back to `docker run -p 3000:3000 ruvnet/wifi-densepose:latest` or `python examples/ruview_live.py`.
4. Help pick the right modality (through-wall → presence/activity; stationary subject → vitals/sleep; need skeletons → pose, train it for accuracy; search & rescue → MAT; best accuracy → 2+ nodes + cross-viewpoint fusion via `/ruview-advanced`).

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `plugins/ruview/commands/ruview-app.md`
