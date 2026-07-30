---
name: hunting-credential-stuffing-attacks
description: "'Detects credential stuffing attacks by analyzing authentication logs for login velocity anomalies, ASN diversity, password spray patterns, and geographic distribution of failed logins. Uses statistical analysis on Splunk or raw log data. Use when investigating account takeover campaigns or building detection rules for auth abuse. '"
category: security-and-compliance
source_repo: mukul975/Anthropic-Cybersecurity-Skills
source_path: "skills/hunting-credential-stuffing-attacks/SKILL.md"
source_url: https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/HEAD/skills/hunting-credential-stuffing-attacks/SKILL.md
---


# Hunting Credential Stuffing Attacks


## When to Use

- When investigating security incidents that require hunting credential stuffing attacks
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Familiarity with security operations concepts and tools
- Access to a test or lab environment for safe execution
- Python 3.8+ with required dependencies installed
- Appropriate authorization for any testing activities

## Instructions

Analyze authentication logs to detect credential stuffing by identifying patterns
of distributed login failures, high IP diversity, and suspicious ASN distribution.

```python
import pandas as pd
from collections import Counter

# Load auth logs
df = pd.read_csv("auth_logs.csv", parse_dates=["timestamp"])

# Credential stuffing indicator: many IPs trying few accounts
ip_per_account = df[df["status"] == "failed"].groupby("username")["source_ip"].nunique()
accounts_under_attack = ip_per_account[ip_per_account > 50]
```

Key detection indicators:
1. High unique source IPs per failed username
2. Low success rate across many accounts (< 1%)
3. ASN concentration from cloud/proxy providers
4. Geographic impossibility (same account, distant locations)
5. User-agent uniformity across distributed IPs

## Examples

```python
# Password spray: one password tried across many accounts
spray = df[df["status"] == "failed"].groupby(["source_ip", "password_hash"]).agg(
    accounts=("username", "nunique")).reset_index()
sprays = spray[spray["accounts"] > 10]
```

---

**Source:** [`mukul975/Anthropic-Cybersecurity-Skills`](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) → `skills/hunting-credential-stuffing-attacks/SKILL.md`
