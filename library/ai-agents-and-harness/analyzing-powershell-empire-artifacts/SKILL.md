---
name: analyzing-powershell-empire-artifacts
description: "Detect PowerShell Empire framework artifacts in Windows event logs by identifying Base64 encoded launcher patterns, default user agents, staging URL structures, stager IOCs, and known Empire module signatures in Script Block Logging events."
category: ai-agents-and-harness
source_repo: mukul975/Anthropic-Cybersecurity-Skills
source_path: "skills/analyzing-powershell-empire-artifacts/SKILL.md"
source_url: https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/HEAD/skills/analyzing-powershell-empire-artifacts/SKILL.md
---


# Analyzing PowerShell Empire Artifacts

## Overview

PowerShell Empire is a post-exploitation framework consisting of listeners, stagers, and agents. Its artifacts leave detectable traces in Windows event logs, particularly PowerShell Script Block Logging (Event ID 4104) and Module Logging (Event ID 4103). This skill analyzes event logs for Empire's default launcher string (`powershell -noP -sta -w 1 -enc`), Base64 encoded payloads containing `System.Net.WebClient` and `FromBase64String`, known module invocations (Invoke-Mimikatz, Invoke-Kerberoast, Invoke-TokenManipulation), and staging URL patterns.


## When to Use

- When investigating security incidents that require analyzing powershell empire artifacts
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Python 3.9+ with access to Windows Event Log or exported EVTX files
- PowerShell Script Block Logging (Event ID 4104) enabled via Group Policy
- Module Logging (Event ID 4103) enabled for comprehensive coverage

## Key Detection Patterns

1. **Default launcher** — `powershell -noP -sta -w 1 -enc` followed by Base64 blob
2. **Stager indicators** — `System.Net.WebClient`, `DownloadData`, `DownloadString`, `FromBase64String`
3. **Module signatures** — Invoke-Mimikatz, Invoke-Kerberoast, Invoke-TokenManipulation, Invoke-PSInject, Invoke-DCOM
4. **User agent strings** — default Empire user agents in HTTP listener configuration
5. **Staging URLs** — `/login/process.php`, `/admin/get.php` and similar default URI patterns

## Output

JSON report with matched IOCs, decoded Base64 payloads, timeline of suspicious events, MITRE ATT&CK technique mappings, and severity scores.

---

**Source:** [`mukul975/Anthropic-Cybersecurity-Skills`](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) → `skills/analyzing-powershell-empire-artifacts/SKILL.md`
