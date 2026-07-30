---
name: detecting-credential-dumping-techniques
description: "Detect LSASS credential dumping, SAM database extraction, and NTDS.dit theft using Sysmon Event ID 10, Windows Security logs, and SIEM correlation rules"
category: security-and-compliance
source_repo: mukul975/Anthropic-Cybersecurity-Skills
source_path: "skills/detecting-credential-dumping-techniques/SKILL.md"
source_url: https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/HEAD/skills/detecting-credential-dumping-techniques/SKILL.md
---


# Detecting Credential Dumping Techniques

## Overview

Credential dumping (MITRE ATT&CK T1003) is a post-exploitation technique where adversaries extract authentication credentials from OS memory, registry hives, or domain controller databases. This skill covers detection of LSASS memory access via Sysmon Event ID 10 (ProcessAccess), SAM registry hive export via reg.exe, NTDS.dit extraction via ntdsutil/vssadmin, and comsvcs.dll MiniDump abuse. Detection rules analyze GrantedAccess bitmasks, suspicious calling processes, and known tool signatures.


## When to Use

- When investigating security incidents that require detecting credential dumping techniques
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Sysmon v14+ deployed with ProcessAccess logging (Event ID 10) for lsass.exe
- Windows Security audit policy enabling process creation (Event ID 4688) with command line logging
- Splunk or Elastic SIEM ingesting Sysmon and Windows Security logs
- Python 3.8+ for log analysis

## Steps

1. Configure Sysmon to log ProcessAccess events targeting lsass.exe
2. Forward Sysmon Event ID 10 and Windows Event ID 4688 to SIEM
3. Create detection rules for known GrantedAccess patterns (0x1010, 0x1FFFFF)
4. Detect comsvcs.dll MiniDump and procdump.exe targeting LSASS PID
5. Alert on reg.exe SAM/SECURITY/SYSTEM hive export commands
6. Detect ntdsutil/vssadmin shadow copy creation for NTDS.dit theft
7. Correlate detections with user/host context for risk scoring

## Expected Output

JSON report containing detected credential dumping indicators with technique classification, severity ratings, process details, MITRE ATT&CK mapping, and Splunk/Elastic detection queries.

---

**Source:** [`mukul975/Anthropic-Cybersecurity-Skills`](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) → `skills/detecting-credential-dumping-techniques/SKILL.md`
