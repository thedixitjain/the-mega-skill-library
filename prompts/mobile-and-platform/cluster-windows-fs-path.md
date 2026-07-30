---
name: cluster-windows-fs-path
description: "Three Windows-only bug classes around DLL search order, path handling, and installer TOCTOU. Share one inventory of Win32 FS/path APIs."
category: mobile-and-platform
source_repo: trailofbits/skills
source_path: "plugins/c-review/prompts/clusters/windows-fs-path.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/c-review/prompts/clusters/windows-fs-path.md
---


# Cluster: Windows — filesystem & path

Three Windows-only bug classes around DLL search order, path handling, and installer TOCTOU. Share one inventory of Win32 FS/path APIs.

ID prefixes: `DLLPLANT`, `WINPATH`, `INSTRACE`.

---

## Phase A — Seed targets

```
rg seed: "\\b(LoadLibrary[AW]?|LoadLibraryEx[AW]?|GetProcAddress|SetDllDirectory[AW]?|SetDefaultDllDirectories|AddDllDirectory)\\s*\\("
rg seed: "\\b(GetCurrentDirectory[AW]?|SetCurrentDirectory[AW]?|GetTempPath[AW]?|GetTempFileName[AW]?|PathCombine[AW]?|PathAppend[AW]?)\\s*\\("
rg seed: "\\b(CreateFile[AW]?|CreateDirectory[AW]?|DeleteFile[AW]?|MoveFile[AW]?|CopyFile[AW]?)\\s*\\("
rg seed: "\\bMAX_PATH\\b"                         # MAX_PATH usage (truncation candidates)
```

Keep as `win_fs_sites`.

---

## Phase B — Passes in order

1. **`DLLPLANT` — DLL search-order hijacking**
   `LoadLibrary("foo.dll")` without full path; missing `SetDefaultDllDirectories(LOAD_LIBRARY_SEARCH_SYSTEM32)`.

2. **`WINPATH` — Windows path handling**
   `MAX_PATH` truncation; missing `\\?\\` for long paths; reserved names (`CON`, `PRN`, `AUX`, `NUL`, `COM1`…).

3. **`INSTRACE` — Installer race conditions**
   Writable-by-users temp dirs used during install; signature verification before copy-to-privileged-dir.

---

## Deconfliction

1. `DLLPLANT` > `WINPATH` (if the path issue is specifically about unqualified DLL names).
2. `INSTRACE` > `WINPATH` (when the TOCTOU is the root cause).

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/c-review/prompts/clusters/windows-fs-path.md`
