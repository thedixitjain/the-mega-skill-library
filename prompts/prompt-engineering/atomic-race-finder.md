---
name: atomic-race-finder
description: "Detects non-atomic read-modify-write sequences on Atomic* types"
category: prompt-engineering
source_repo: trailofbits/skills
source_path: "plugins/rust-review/prompts/general/atomic-race-finder.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/rust-review/prompts/general/atomic-race-finder.md
---


**Finding ID Prefix:** `ATOMICRACE`.

**Bug shape:** `let v = a.load(Ordering::Acquire); if v == X { a.store(Y, Ordering::Release); }` — two independent ops; another thread can race between them.

**Gates:**

1. `Atomic*.load(...)` followed by conditional `Atomic*.store(...)` on the same variable, where the store is dependent on the load.
2. No `compare_exchange` / `compare_exchange_weak` / `fetch_update` in between.
3. The Atomic is shared (`Arc<Atomic*>`, `static`, or field of `Arc<...>`).

**FPs (reject):**

- Single-writer atomic: only one thread ever `store`s (others only `load`), so the load→store pair is never concurrent with another writer.
- The load/store pair sits inside a held `Mutex`/`RwLock` critical section — the lock, not the atomic, supplies atomicity (if the locking itself is wrong, that is `DLOCK`).
- An existing `compare_exchange` / `compare_exchange_weak` / `fetch_update` already performs the update atomically (gate 2 already excludes these — reconfirm before filing).

**Patch:** convert to `compare_exchange` loop or `fetch_update`.

**Search patterns:**

```
\.load\s*\(
\.store\s*\(
\.(compare_exchange(_weak)?|fetch_update)\s*\(
```

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/rust-review/prompts/general/atomic-race-finder.md`
