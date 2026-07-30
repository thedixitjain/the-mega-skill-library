---
name: cluster-layout-safety
description: "Undefined behavior from in-memory type layout the compiler does not always reject: references to fields of #[repr(packed)] structs (including implicit borrows via auto-deref). Common in wire-format and C-layout-matched structs, independent of whether the crate uses FFI."
category: frontend-and-design
source_repo: trailofbits/skills
source_path: "plugins/rust-review/prompts/clusters/layout-safety.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/rust-review/prompts/clusters/layout-safety.md
---


# Cluster: Type layout safety

Undefined behavior from in-memory type layout the compiler does not always reject: references to fields of `#[repr(packed)]` structs (including implicit borrows via auto-deref). Common in wire-format and C-layout-matched structs, independent of whether the crate uses FFI.

ID prefixes: `PACKEDREF`.

## Phase A

```
rg seed: "#\[repr\([^\]]*packed"
rg seed: "&(?:mut\s+)?[\w.]+\.(?:\w+|\d+)"
```

Run finders in declared order.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/rust-review/prompts/clusters/layout-safety.md`
