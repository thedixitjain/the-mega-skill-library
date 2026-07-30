---
name: out-of-bounds-index-finder
description: "Detects vec[i] / arr[i] / slice[i] with attacker-controlled index in safe Rust"
category: prompt-engineering
source_repo: trailofbits/skills
source_path: "plugins/rust-review/prompts/general/out-of-bounds-index-finder.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/rust-review/prompts/general/out-of-bounds-index-finder.md
---


**Finding ID Prefix:** `OOBIDX`.

**Gates:**

1. Bracket-indexing on `Vec`, `&[T]`, `[T; N]`, or types implementing `Index` where indexing panics on OOB.
2. The index integer is derived from untrusted input (taint trace).
3. No prior `if idx < v.len()` check on a reachable path; OR the bounds-check arithmetic is itself overflow-prone.

**FPs:**

- Index is a constant.
- Immediately follows `.get(idx).is_some()` (caller already validated).
- Container is statically a fixed-size array and index is bounded by `const N`.

**Patch:** replace `v[i]` with `v.get(i).ok_or(Error::OutOfRange)?`.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/rust-review/prompts/general/out-of-bounds-index-finder.md`
