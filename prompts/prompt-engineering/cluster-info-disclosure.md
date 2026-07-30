---
name: cluster-info-disclosure
description: "Externally observable leaks of internal runtime state the compiler cannot catch: raw memory addresses reaching logs, API responses, serialized output, or error strings, defeating ASLR."
category: prompt-engineering
source_repo: trailofbits/skills
source_path: "plugins/rust-review/prompts/clusters/info-disclosure.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/rust-review/prompts/clusters/info-disclosure.md
---


# Cluster: Information disclosure

Externally observable leaks of internal runtime state the compiler cannot catch: raw memory addresses reaching logs, API responses, serialized output, or error strings, defeating ASLR.

ID prefixes: `PTREXPOSE`.

## Phase A

```
rg seed: "\bas\s+usize\b|\{[^{}]*:[^{}]*p\}|\.(addr|expose_provenance|expose_addr)\(\)"  # `{:p}` / `{ptr:p}` / `{0:p}` / `{:>16p}` pointer formats
```

Run finders in declared order.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/rust-review/prompts/clusters/info-disclosure.md`
