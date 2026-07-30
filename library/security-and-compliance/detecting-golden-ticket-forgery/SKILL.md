---
name: detecting-golden-ticket-forgery
description: "Detect Kerberos Golden Ticket forgery by analyzing Windows Event ID 4769 for RC4 encryption downgrades (0x17), abnormal ticket lifetimes, and krbtgt account anomalies in Splunk and Elastic SIEM"
category: security-and-compliance
source_repo: mukul975/Anthropic-Cybersecurity-Skills
source_path: "skills/detecting-golden-ticket-forgery/SKILL.md"
source_url: https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/HEAD/skills/detecting-golden-ticket-forgery/SKILL.md
---


# Detecting Golden Ticket Forgery

## Overview

A Golden Ticket attack (MITRE ATT&CK T1558.001) involves forging a Kerberos Ticket Granting Ticket (TGT) using the krbtgt account NTLM hash, granting unrestricted access to any service in the Active Directory domain. This skill detects Golden Ticket usage by analyzing Event ID 4769 for RC4 encryption type (0x17) in environments enforcing AES, identifying tickets with abnormal lifetimes exceeding domain policy, correlating TGS requests with missing corresponding TGT requests (Event ID 4768), and detecting krbtgt password age anomalies.


## When to Use

- When investigating security incidents that require detecting golden ticket forgery
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Windows Domain Controller with Kerberos audit logging enabled
- Splunk or Elastic SIEM ingesting Windows Security event logs
- Python 3.8+ for offline event log analysis
- Knowledge of domain Kerberos encryption policy (AES vs RC4)

## Steps

1. Audit domain Kerberos encryption policy to establish AES-only baseline
2. Forward Event IDs 4768 and 4769 to SIEM platform
3. Detect RC4 (0x17) encryption in TGS requests where AES is enforced
4. Identify TGS requests without corresponding TGT requests (forged ticket indicator)
5. Alert on ticket lifetimes exceeding MaxTicketAge domain policy
6. Monitor krbtgt account password age and last reset date
7. Correlate findings with host/user context for risk scoring

## Expected Output

JSON report with Golden Ticket indicators including RC4 downgrades, orphaned TGS requests, abnormal ticket lifetimes, and risk-scored alerts with MITRE ATT&CK technique mapping.

---

**Source:** [`mukul975/Anthropic-Cybersecurity-Skills`](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) → `skills/detecting-golden-ticket-forgery/SKILL.md`
