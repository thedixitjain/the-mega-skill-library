---
name: cluster-static-hygiene
description: "Project-wide hardening rules. ID prefixes: CARGOLINT, MSRV, DEPRECAPI."
category: prompt-engineering
source_repo: trailofbits/skills
source_path: "plugins/rust-review/prompts/clusters/static-hygiene.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/rust-review/prompts/clusters/static-hygiene.md
---


# Cluster: Static hygiene

Project-wide hardening rules. ID prefixes: `CARGOLINT`, `MSRV`, `DEPRECAPI`.

Missing `// SAFETY:` / `# Safety` documentation is covered by the `SAFETYDOC` pass in **unsafe-boundary** — do not re-audit here.

## Phase A

Read `Cargo.toml`, `rust-toolchain.toml`, `clippy.toml` if present.

```
rg seed: "unsafe_code|missing_docs|warnings"
rg seed: "mem::uninitialized"  # deprecated API (DEPRECAPI); the modern `MaybeUninit::uninit().assume_init()` is a UNINITREAD/memory-safety concern, not seeded here
```

Run finders in declared order.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/rust-review/prompts/clusters/static-hygiene.md`
