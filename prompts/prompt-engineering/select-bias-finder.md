---
name: select-bias-finder
description: "Detects tokio::select!/futures::select! relying on nondeterministic poll order when correctness requires deterministic branch priority"
category: prompt-engineering
source_repo: trailofbits/skills
source_path: "plugins/rust-review/prompts/general/select-bias-finder.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/rust-review/prompts/general/select-bias-finder.md
---


**Finding ID Prefix:** `SELECTBIAS`.

**Gates:**

1. `tokio::select! { ... }` **or** `futures::select! { ... }` macro.
2. The branches include a "cancellation" branch (e.g., `_ = shutdown.recv() => ...`) AND a "work" branch.
3. The poll order is non-deterministic — `tokio::select!` without a `biased;` line, or `futures::select!` (which is always pseudo-random; its ordered form is the **separate** `futures::select_biased!` macro, not a `biased;` keyword) — AND correctness requires the cancellation branch to win when both are ready.

**Patch:** for `tokio::select!`, add `biased;` as the first line of the block **and** place the cancellation/priority branch **first** — `biased;` polls top-to-bottom, so it only makes the cancellation branch win if that branch is physically first (`biased;` with the work branch on top makes the *work* branch win, the opposite of the intent). For `futures::select!`, switch to `futures::select_biased!` (there is **no** `biased;` keyword in futures-rs) **and** place the cancellation branch first. Or restructure to use a dedicated priority channel.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/rust-review/prompts/general/select-bias-finder.md`
