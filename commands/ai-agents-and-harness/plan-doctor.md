---
name: plan-doctor
description: "Self-check for the planning-with-files mechanisms that fail silently: plan resolution, hook injection, canonicalizer path shape, attestation state, install surfaces, and per-fire hook latency. Run it whenever hooks seem quiet or after installing on a new machine. Available since v3.6.0."
allowed-tools: "Bash"
category: ai-agents-and-harness
source_repo: OthmanAdi/planning-with-files
source_path: "commands/plan-doctor.md"
source_url: https://github.com/OthmanAdi/planning-with-files/blob/HEAD/commands/plan-doctor.md
---


Run the planning-with-files self-check against the current project directory.

Steps:
1. Run the doctor script from the project root:
   - Linux/macOS/Git Bash: `sh ${CLAUDE_PLUGIN_ROOT}/scripts/plan-doctor.sh`
   - Windows without Git Bash on PATH: locate Git Bash via `git.exe` (its `usr\bin\sh.exe` sibling) and run the same script with it.
2. Report the PASS/WARN/FAIL lines to the user verbatim — they are designed to be read as-is.
3. If any line reports FAIL, explain the matching remediation:
   - resolver FAIL → inspect `.planning/.active_plan` content and plan dir names.
   - injection FAIL with a resolving plan → the hooks are silently dark; upgrading past v3.6.0 fixes the Windows-native-coreutils realpath cause. Also check `PLANNING_DISABLED`.
   - tamper WARN → re-approve with `/plan-attest` if the plan edit was intentional.
4. Do not attempt automatic fixes; this command is diagnostic only.

Why this exists: the mechanisms this skill relies on (hook injection, plan resolution) exit 0 and stay silent by design when something is off, so a broken install looks identical to "no plan yet". The doctor makes the difference visible in one pass.

---

**Source:** [`OthmanAdi/planning-with-files`](https://github.com/OthmanAdi/planning-with-files) → `commands/plan-doctor.md`
