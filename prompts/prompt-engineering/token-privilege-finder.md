---
name: token-privilege-finder
description: "Detects privilege token vulnerabilities"
category: prompt-engineering
source_repo: trailofbits/skills
source_path: "plugins/c-review/prompts/windows-userspace/token-privilege-finder.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/c-review/prompts/windows-userspace/token-privilege-finder.md
---


**Finding ID Prefix:** `TOKPRIV` (e.g., TOKPRIV-001, TOKPRIV-002)

**Bug Patterns to Find:**

1. **Dangerous Privilege Enabling**
   - `SeDebugPrivilege` - bypasses all DACLs/SACLs
   - `SeBackupPrivilege` - complete filesystem access
   - `SeTcbPrivilege` - create tokens for other users
   - `SeAssignPrimaryTokenPrivilege` - replace process tokens

2. **Privilege Not Dropped**
   - High privilege enabled but never disabled
   - Privilege enabled for longer than necessary
   - Missing `AdjustTokenPrivileges` to disable

3. **Token Impersonation Issues**
   - `ImpersonateLoggedOnUser` without validation
   - `SetThreadToken` with untrusted token
   - Missing `RevertToSelf` after impersonation

4. **Service Privilege Issues**
   - Service running as SYSTEM when not required
   - Missing `LOCAL SERVICE` or `NETWORK SERVICE` usage
   - Improper service account configuration

5. **Handle/Token Leaks**
   - Token handle not closed after use
   - Token inherited by child process
   - Token accessible to lower-privilege code

**Common False Positives to Avoid:**

- **Immediately disabled:** Privilege enabled and disabled in same operation
- **Required for functionality:** Backup software needs SeBackupPrivilege
- **Security software:** Debugger/AV legitimately needs SeDebugPrivilege
- **Properly scoped:** Privilege enabled only for specific operation

**Search Patterns:**
```
AdjustTokenPrivileges\s*\(|LookupPrivilegeValue\s*\(
SeDebugPrivilege|SeBackupPrivilege|SeTcbPrivilege
SeAssignPrimaryTokenPrivilege|SeRestorePrivilege
ImpersonateLoggedOnUser|SetThreadToken|RevertToSelf
OpenProcessToken|OpenThreadToken|DuplicateToken
```

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/c-review/prompts/windows-userspace/token-privilege-finder.md`
