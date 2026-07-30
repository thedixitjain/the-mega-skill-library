---
name: lossy-from-into-finder
description: "Detects From/Into and `as` casts that silently truncate or lose information across security boundaries"
category: prompt-engineering
source_repo: trailofbits/skills
source_path: "plugins/rust-review/prompts/general/lossy-from-into-finder.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/rust-review/prompts/general/lossy-from-into-finder.md
---


**Finding ID Prefix:** `LOSSYFROM`.

**Gates:**

1. `impl From<A> for B` (or `as` cast) where `B` cannot represent all `A` values (narrower integer, signed-to-unsigned, float-to-int).
2. The conversion site is on a security-relevant path: length field, capability check, authorization token, ID lookup.

**FPs:**

- Conversion is bounded by a prior explicit `< MAX` check.
- Using `TryFrom`/`try_into()` already.

**Patch:** prefer `TryFrom` + `?`.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/rust-review/prompts/general/lossy-from-into-finder.md`
