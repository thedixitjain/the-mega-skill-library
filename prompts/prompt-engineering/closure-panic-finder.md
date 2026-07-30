---
name: closure-panic-finder
description: "Detects user-supplied closures that can panic across unsafe scaffolding, causing leaks or double-free during unwind"
category: prompt-engineering
source_repo: trailofbits/skills
source_path: "plugins/rust-review/prompts/general/closure-panic-finder.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/rust-review/prompts/general/closure-panic-finder.md
---


**Finding ID Prefix:** `CLOSUREPANIC`.

**Gates:**

1. Library API accepts `F: FnOnce(...)` / `F: FnMut(...)` / `F: Fn(...)`.
2. The library invokes `f(...)` between two unsafe operations (e.g., `ptr::read` then `f(x)` then `ptr::write` to complete a move).
3. If `f` panics, the in-between state has duplicated ownership / leaked allocation / poisoned invariant with no `catch_unwind` guard.

**Patch:** make the unsafe pair panic-safe — restructure so no user closure runs between the `ptr::read` and the completing `ptr::write` (read/write atomically), or guard the half-moved value with `scopeguard::guard(...)` + `ScopeGuard::into_inner` (dismiss-on-success) or a `ManuallyDrop` so the fix-up runs only on the unwind path. Do **not** use bare `scopeguard::defer!`: it runs its body on *every* scope exit (success **and** unwind) with no dismiss, so it cannot complete a move without double-running on the success path.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/rust-review/prompts/general/closure-panic-finder.md`
