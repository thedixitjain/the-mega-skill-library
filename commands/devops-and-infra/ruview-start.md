---
name: ruview-start
description: "Get started with RuView — pick the fastest path (Docker demo, repo build, or live ESP32) and walk through it."
category: devops-and-infra
source_repo: ruvnet/RuView
source_path: "plugins/ruview/commands/ruview-start.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/plugins/ruview/commands/ruview-start.md
---


# /ruview-start

Onboard the user onto RuView (WiFi-DensePose).

1. Invoke the **`ruview-quickstart`** skill.
2. If `$ARGUMENTS` names a tier (`docker`, `build`, `hardware`), go straight to it; otherwise ask which hardware they have:
   - **No hardware** → Tier 0: `docker run -p 3000:3000 ruvnet/wifi-densepose:latest`, open `http://localhost:3000`.
   - **Want to build from source** → Tier 1: `cd v2 && cargo test --workspace --no-default-features`, then `python archive/v1/data/proof/verify.py`.
   - **Have an ESP32-S3 / C6** → Tier 2: hand off to `/ruview-flash` then `/ruview-provision`, then `cargo run -p wifi-densepose-sensing-server`.
3. Warn about the gotchas: ESP32-C3 / original ESP32 unsupported; single node = limited spatial resolution; camera-free pose is modest (use camera-supervised for 92.9% PCK@20).
4. Point to next steps: `/ruview-app`, `/ruview-train`, `/ruview-advanced`, `/ruview-verify`, and the `ruview-configure` skill.

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `plugins/ruview/commands/ruview-start.md`
