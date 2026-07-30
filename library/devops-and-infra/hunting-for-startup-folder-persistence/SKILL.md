---
name: hunting-for-startup-folder-persistence
description: "Detect T1547.001 startup folder persistence by monitoring Windows startup directories for suspicious file creation, analyzing autoruns entries, and using Python watchdog for real-time filesystem monitoring."
category: devops-and-infra
source_repo: mukul975/Anthropic-Cybersecurity-Skills
source_path: "skills/hunting-for-startup-folder-persistence/SKILL.md"
source_url: https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/HEAD/skills/hunting-for-startup-folder-persistence/SKILL.md
---


# Hunting for Startup Folder Persistence

## Overview

Attackers use Windows startup folders for persistence (MITRE ATT&CK T1547.001 — Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder). Files placed in `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup` or `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup` execute automatically at user logon. This skill scans startup directories for suspicious files, monitors for real-time changes using Python watchdog, and analyzes file metadata to detect persistence implants.


## When to Use

- When investigating security incidents that require hunting for startup folder persistence
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Python 3.9+ with `watchdog`, `pefile` (optional for PE analysis)
- Access to Windows startup folders (user and all-users)
- Windows Event Logs for Event ID 4663 correlation (optional)

## Steps

1. Enumerate all files in user and system startup directories
2. Analyze file types, creation timestamps, and digital signatures
3. Flag suspicious file extensions (.bat, .vbs, .ps1, .lnk, .exe)
4. Check for recently created files (< 7 days) as potential implants
5. Monitor startup folders in real-time using watchdog FileSystemEventHandler
6. Correlate with known legitimate startup entries
7. Generate threat hunting report with T1547.001 MITRE mapping

## Expected Output

- JSON report listing all startup folder contents with risk scores, file metadata, and suspicious indicators
- Real-time monitoring alerts for new file creation in startup directories

---

**Source:** [`mukul975/Anthropic-Cybersecurity-Skills`](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) → `skills/hunting-for-startup-folder-persistence/SKILL.md`
