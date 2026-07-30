---
name: assertion-reachable-finder
description: "Detects reachable unreachable!()/unimplemented!()/todo!()/assert!() in non-test code"
category: testing-and-qa
source_repo: trailofbits/skills
source_path: "plugins/rust-review/prompts/general/assertion-reachable-finder.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/rust-review/prompts/general/assertion-reachable-finder.md
---


**Finding ID Prefix:** `ASSERTREACH`.

**Gates:**

1. Macro: `unreachable!`, `unimplemented!`, `todo!`, `assert!`, `assert_eq!`, `assert_ne!`, `panic!`, or `debug_assert!` in `release` builds (note: `debug_assert!` is no-op in release; OOS unless `debug-assertions = true`).
2. Not gated by `#[cfg(test)]` / `#[cfg(debug_assertions)]`.
3. Has at least one reachable control-flow path from a `pub fn` or trait-impl method, OR the condition can be falsified by untrusted input.

**FPs:**

- Exhaustiveness markers where the compiler-checked match makes the branch genuinely unreachable (verify by reading the match's arms).
- Asserts inside `#[cfg(test)]` modules.

**Patch:** replace `unreachable!`/`assert!` with structured error returns.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/rust-review/prompts/general/assertion-reachable-finder.md`
