---
name: implementing-deception-based-detection-with-canarytoken
description: "Deploy and monitor Canary Tokens via the Thinkst Canary API for deception-based breach detection using web bug tokens, DNS tokens, document tokens, and AWS key tokens."
category: devops-and-infra
source_repo: mukul975/Anthropic-Cybersecurity-Skills
source_path: "skills/implementing-deception-based-detection-with-canarytoken/SKILL.md"
source_url: https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/HEAD/skills/implementing-deception-based-detection-with-canarytoken/SKILL.md
---


# Implementing Deception-Based Detection with Canarytoken

## Overview

Canary Tokens are lightweight tripwire mechanisms that alert when an attacker accesses a resource. This skill uses the Thinkst Canary REST API to programmatically create tokens (web bugs, DNS tokens, MS Word documents, AWS API keys), deploy them to strategic locations, monitor for triggered alerts, and generate deception coverage reports.


## When to Use

- When deploying or configuring implementing deception based detection with canarytoken capabilities in your environment
- When establishing security controls aligned to compliance requirements
- When building or improving security architecture for this domain
- When conducting security assessments that require this implementation

## Prerequisites

- Thinkst Canary Console or canarytokens.org account
- API auth token from Canary Console
- Python 3.9+ with `requests`
- File system access for deploying document and file tokens

## Steps

1. Authenticate to the Canary Console API using auth_token
2. Create web bug (HTTP) tokens for embedding in documents and web pages
3. Create DNS tokens for monitoring DNS resolution attempts
4. Create MS Word document tokens for file share deployment
5. List all active tokens and their trigger history
6. Query recent alerts for triggered token events
7. Generate deception coverage report with deployment recommendations

## Expected Output

- JSON report listing all deployed Canary Tokens, trigger history, alert details, and coverage analysis
- Deployment map showing token types across network segments

---

**Source:** [`mukul975/Anthropic-Cybersecurity-Skills`](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) → `skills/implementing-deception-based-detection-with-canarytoken/SKILL.md`
