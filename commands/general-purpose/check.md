---
name: check
description: "Checks if the code is ready to be committed"
category: general-purpose
source_repo: tailcallhq/forgecode
source_path: ".forge/commands/check.md"
source_url: https://github.com/tailcallhq/forgecode/blob/HEAD/.forge/commands/check.md
---


- Run the `lint` and `test` commands and verify if everything is fine.
  <lint>cargo +nightly fmt --all; cargo +nightly clippy --fix --allow-staged --allow-dirty --workspace</lint>
  <test>cargo insta test --accept --unreferenced=delete</test>
- Fix every issue found in the process

---

**Source:** [`tailcallhq/forgecode`](https://github.com/tailcallhq/forgecode) → `.forge/commands/check.md`
