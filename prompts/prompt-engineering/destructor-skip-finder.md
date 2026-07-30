---
name: destructor-skip-finder
description: "Detects process::exit, mem::forget, and ManuallyDrop bypassing Drop for values whose destructor performs security-relevant cleanup"
category: prompt-engineering
source_repo: trailofbits/skills
source_path: "plugins/rust-review/prompts/general/destructor-skip-finder.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/rust-review/prompts/general/destructor-skip-finder.md
---


**Finding ID Prefix:** `DROPSKIP`.

**Bug shape:** `std::process::exit`/`libc::exit`, `std::mem::forget`, or `ManuallyDrop` bypasses `Drop` for live values whose destructor performs security-relevant cleanup — committing/rolling back, flushing, releasing a lock, or closing a connection. The cleanup silently never runs. (DROPSKIP flags a present `Drop` bypassed by control flow; whether a secret has zeroize-on-drop at all is out of scope — see `zeroize-audit`. Distinct from `RAWFD`, which covers fd-specific lifecycle.)

**Gates:**

1. `process::exit`/`exit`/`mem::forget`/`ManuallyDrop` is reachable while values with a meaningful `Drop` are live (secret, DB/connection handle, transaction guard, lock guard, buffered writer).
2. Skipping that `Drop` has a security or correctness consequence.

**FPs:**

- No live value has a meaningful `Drop` at the skip point.
- The leak/skip is intentional and documented (`// SAFETY:` or equivalent comment) with an explicit handoff.
- Cleanup is performed explicitly before `exit`.

**Patch:** run cleanup explicitly before `process::exit`; avoid `process::exit` in library code; pair `mem::forget`/`ManuallyDrop` with an explicit equivalent cleanup and a justifying comment.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/rust-review/prompts/general/destructor-skip-finder.md`
