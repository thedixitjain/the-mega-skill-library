---
name: hunting-for-process-injection-techniques
description: "Detect process injection techniques (T1055) including CreateRemoteThread, process hollowing, and DLL injection via Sysmon Event IDs 8 and 10 and EDR process telemetry"
category: general-purpose
source_repo: mukul975/Anthropic-Cybersecurity-Skills
source_path: "skills/hunting-for-process-injection-techniques/SKILL.md"
source_url: https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/HEAD/skills/hunting-for-process-injection-techniques/SKILL.md
---


# Hunting for Process Injection Techniques

## Overview

Process injection (MITRE ATT&CK T1055) allows adversaries to execute code in the address space of another process, enabling defense evasion and privilege escalation. This skill detects injection techniques via Sysmon Event ID 8 (CreateRemoteThread), Event ID 10 (ProcessAccess with suspicious access rights), and analysis of source-target process relationships to distinguish legitimate from malicious injection.


## When to Use

- When investigating security incidents that require hunting for process injection techniques
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Sysmon installed with Event IDs 8 and 10 enabled
- Process creation logs (Sysmon Event ID 1 or Windows 4688)
- Python 3.8+ with standard library
- JSON-formatted Sysmon event logs

## Steps

1. **Parse Sysmon Events** — Ingest Event IDs 1, 8, and 10 from JSON log files
2. **Detect CreateRemoteThread** — Flag Event ID 8 with suspicious source-target process pairs
3. **Analyze ProcessAccess Rights** — Identify Event ID 10 with dangerous access masks (PROCESS_VM_WRITE, PROCESS_CREATE_THREAD)
4. **Build Process Relationship Graph** — Map source-to-target injection relationships
5. **Filter Known Legitimate Pairs** — Exclude known benign injection patterns (AV, debuggers, system processes)
6. **Score Injection Severity** — Apply risk scoring based on source process, target process, and access rights
7. **Generate Hunt Report** — Produce structured report with MITRE sub-technique mapping

## Expected Output

- JSON report of detected injection events with severity scores
- Process injection relationship graph
- MITRE ATT&CK sub-technique mapping (T1055.001-T1055.012)
- False positive exclusion recommendations

---

**Source:** [`mukul975/Anthropic-Cybersecurity-Skills`](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) → `skills/hunting-for-process-injection-techniques/SKILL.md`
