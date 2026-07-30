---
name: msrv-mismatch-finder
description: "Detects missing MSRV declaration or use of features past the declared MSRV"
category: prompt-engineering
source_repo: trailofbits/skills
source_path: "plugins/rust-review/prompts/general/msrv-mismatch-finder.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/rust-review/prompts/general/msrv-mismatch-finder.md
---


**Finding ID Prefix:** `MSRV`.

**Gates:**

1. `Cargo.toml` has no `rust-version` field, OR
2. `rust-version` is set but the code uses post-MSRV features (e.g., `let-else` on `rust-version = 1.60`).

**Patch:** set explicit `rust-version`; pin in CI via `cargo +<msrv> check`.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/rust-review/prompts/general/msrv-mismatch-finder.md`
