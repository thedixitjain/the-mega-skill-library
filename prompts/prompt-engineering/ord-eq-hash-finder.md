---
name: ord-eq-hash-finder
description: "Detects manual Ord/PartialOrd/Eq/PartialEq/Hash impls that violate required invariants"
category: prompt-engineering
source_repo: trailofbits/skills
source_path: "plugins/rust-review/prompts/general/ord-eq-hash-finder.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/rust-review/prompts/general/ord-eq-hash-finder.md
---


**Finding ID Prefix:** `ORDEQHASH`.

**Gates:**

1. Manual (non-derived) `impl Ord` / `impl PartialOrd` / `impl Eq` / `impl PartialEq` / `impl Hash` exists.
2. At least one invariant is checkable as violated by reading the impl: (a) `a == b ⟹ hash(a) == hash(b)`, (b) `Ord::cmp` total order consistency with `PartialOrd::partial_cmp`, (c) `Eq` reflexivity/symmetry/transitivity, (d) NaN handling for floats.

**Why:** violations corrupt `HashMap`/`BTreeMap` (collisions, missing keys, infinite loops in some std internals).

**Patch:** derive when possible; otherwise document invariant proofs and add property tests.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/rust-review/prompts/general/ord-eq-hash-finder.md`
