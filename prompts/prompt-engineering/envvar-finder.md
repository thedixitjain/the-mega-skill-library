---
name: envvar-finder
description: "Identifies environment variable injection"
category: prompt-engineering
source_repo: trailofbits/skills
source_path: "plugins/c-review/prompts/linux-userspace/envvar-finder.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/c-review/prompts/linux-userspace/envvar-finder.md
---


**Finding ID Prefix:** `ENVVAR` (e.g., ENVVAR-001, ENVVAR-002)

**Bug Patterns to Find:**

1. **Thread Safety Issues**
   - `getenv`/`setenv` not thread-safe in older glibc
   - Concurrent access without synchronization
   - Use secure_getenv where appropriate

2. **Attacker-Controlled Envvars**
   - Bash exported functions (Shellshock-style)
   - `LIBC_FATAL_STDERR_` manipulation
   - `LD_PRELOAD`, `LD_LIBRARY_PATH` in setuid
   - `PATH` manipulation

3. **Procfs Environment Leaks**
   - Child process reads parent env via `/proc/$pid/environ`
   - `setenv` leaves old value on stack (readable)
   - Sensitive data in environment

4. **Environment Inheritance**
   - Sensitive envvars passed to child processes
   - Not clearing environment before exec

**Common False Positives to Avoid:**

- **Non-setuid programs:** Many envvar attacks require setuid context
- **Internal configuration:** Envvars used for internal config not exposed to attackers
- **secure_getenv used:** Already using the secure version
- **Environment sanitized:** Program clears dangerous envvars at startup
- **Single-threaded:** Thread safety not a concern in single-threaded programs

**Search Patterns:**
```
getenv\s*\(|setenv\s*\(|putenv\s*\(|unsetenv\s*\(
secure_getenv\s*\(|clearenv\s*\(
LD_PRELOAD|LD_LIBRARY_PATH|PATH
environ\b|/proc/.*environ
execve\s*\(|execle\s*\(
```

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/c-review/prompts/linux-userspace/envvar-finder.md`
