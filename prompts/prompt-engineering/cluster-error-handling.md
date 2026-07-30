---
name: cluster-error-handling
description: "ID prefixes: RESDISC, DROPPANIC, LOSSYFROM, LOSSYSTR, BUFFLUSH."
category: prompt-engineering
source_repo: trailofbits/skills
source_path: "plugins/rust-review/prompts/clusters/error-handling.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/rust-review/prompts/clusters/error-handling.md
---


# Cluster: Error handling flow

ID prefixes: `RESDISC`, `DROPPANIC`, `LOSSYFROM`, `LOSSYSTR`, `BUFFLUSH`.

## Phase A

```
rg seed: "let\s+_\s*=\s"
rg seed: "impl\b[^\n]*\bDrop\s+for"  # incl. generic/lifetime `impl<'a> Drop for` / `impl<T> Drop for`
rg seed: "impl\b[^\n]*\bFrom<[^\n]*>\s+for|impl\b[^\n]*\bInto<"  # incl. generic `impl<T> From<...> for` (the `\bFrom` boundary still excludes `TryFrom`)
rg seed: "\bas\s+\w"
rg seed: "from_utf8_lossy|to_string_lossy|to_str\(\)\s*\.unwrap_or"
rg seed: "BufWriter"
```

Run finders in declared order.

## Deconfliction

- `DROPPANIC` (panic risk *inside* an `impl Drop`) vs `DROPSKIP` (a `Drop` *skipped* via `mem::forget`/`ManuallyDrop`/`process::exit`, resource-handling) — different bugs on the same `impl Drop` site: a panic-in-Drop is `DROPPANIC`, a never-run Drop is `DROPSKIP`.
- A borrow panic inside `Drop` routes to `DROPPANIC`, **not** `REFCELLPANIC` (panic-dos); a `Mutex` poisoned by a panic in `Drop` is also `DROPPANIC`, not a concurrency-locking finding.
- `LOSSYFROM` covers **numeric** `as`/`From`/`Into` narrowing only — a pointer/reference `as` cast routes to `PTRCAST` (unsafe-boundary), not here.
- `LOSSYSTR` (lossy UTF-8 / OS-string / path conversion) vs `LOSSYFROM` (numeric) vs `UNWRAP` (`to_str().unwrap_or` masking a failure): file at the most specific.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/rust-review/prompts/clusters/error-handling.md`
