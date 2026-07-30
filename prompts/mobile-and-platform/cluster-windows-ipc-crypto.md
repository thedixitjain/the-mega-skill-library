---
name: cluster-windows-ipc-crypto
description: "Three Windows-only bug classes around named-pipe security, CryptoAPI misuse, and Windows heap/alloc specifics."
category: mobile-and-platform
source_repo: trailofbits/skills
source_path: "plugins/c-review/prompts/clusters/windows-ipc-crypto.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/c-review/prompts/clusters/windows-ipc-crypto.md
---


# Cluster: Windows — IPC, crypto, allocator

Three Windows-only bug classes around named-pipe security, CryptoAPI misuse, and Windows heap/alloc specifics.

ID prefixes: `NAMEDPIPE`, `WINCRYPTO`, `WINALLOC`.

---

## Phase A — Seed targets

```
rg seed: "\\b(CreateNamedPipe[AW]?|ConnectNamedPipe|ImpersonateNamedPipeClient|SetNamedPipeHandleState)\\s*\\("
rg seed: "\\b(CryptAcquireContext[AW]?|CryptGenKey|CryptGenRandom|CryptEncrypt|CryptDecrypt|CryptHashData|CryptSignHash|CryptVerifySignature|BCrypt\\w+|NCrypt\\w+)\\s*\\("
rg seed: "\\b(HeapAlloc|HeapFree|HeapReAlloc|HeapCreate|HeapDestroy|VirtualAlloc|VirtualFree|VirtualProtect|LocalAlloc|LocalFree|GlobalAlloc|GlobalFree)\\s*\\("
rg seed: "\\bSECURITY_DESCRIPTOR\\b|\\bSetSecurityDescriptor\\w+\\s*\\("
```

Keep as `win_ipc_sites`.

---

## Phase B — Passes in order

1. **`NAMEDPIPE` — Named-pipe security**
   Missing `PIPE_REJECT_REMOTE_CLIENTS`, weak DACL on pipe, impersonation without `SECURITY_IDENTIFICATION`.

2. **`WINCRYPTO` — CryptoAPI misuse**
   Deprecated algorithms (`CALG_MD5`, `CALG_DES`), `rand()` for keys, missing `CryptGenRandom`/`BCryptGenRandom`.

3. **`WINALLOC` — Windows allocator specifics**
   Mismatched alloc/free pairs (`HeapAlloc` freed with `LocalFree`), `VirtualProtect` race, W^X violations.

---

## Deconfliction

Mostly disjoint. `WINCRYPTO` never merges with the others.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/c-review/prompts/clusters/windows-ipc-crypto.md`
