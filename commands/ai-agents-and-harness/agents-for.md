---
name: agents-for
description: "List pentest-ai agents relevant to a domain or tag (web, ad, cloud, mobile, recon, etc.)."
category: ai-agents-and-harness
source_repo: 0xSteph/pentest-ai-agents
source_path: "commands/agents-for.md"
source_url: https://github.com/0xSteph/pentest-ai-agents/blob/HEAD/commands/agents-for.md
---
Filter the pentest-ai agent catalog by the domain or tag below and return a focused list.

Filter:
$ARGUMENTS

Match against this taxonomy. A single argument may match multiple tags (e.g., "ad" matches both "active-directory" and "windows"). Return every agent that matches.

```
recon              → recon-advisor, osint-collector, vuln-scanner
osint              → osint-collector
web                → web-hunter, api-security, bug-bounty, bizlogic-hunter, vuln-scanner
api                → api-security, web-hunter, bug-bounty
ad / active-directory / windows → ad-attacker, credential-tester, privesc-advisor, recon-advisor
cloud / aws / azure / gcp → cloud-security, cicd-redteam
mobile / android / ios → mobile-pentester, reverse-engineer
wireless / wifi / bluetooth → wireless-pentester
social / phishing / se → social-engineer, phishing-operator
exploit / exploitation → exploit-guide, exploit-chainer, poc-validator, payload-crafter
payload / shellcode → payload-crafter, malware-analyst, reverse-engineer
re / reverse / reversing → reverse-engineer, malware-analyst, ctf-solver
malware / ir → malware-analyst, forensics-analyst, detection-engineer
forensics / dfir → forensics-analyst, malware-analyst
detection / blue / siem / sigma → detection-engineer, threat-modeler
threat / threat-model / stride → threat-modeler
stig / compliance / hardening → stig-analyst
priv-esc / privilege-escalation → privesc-advisor
creds / credentials / passwords / hash / cracking → credential-tester
business-logic / bizlogic → bizlogic-hunter
ci / cd / devsecops / pipeline → cicd-redteam
plan / planning / scope / roe → engagement-planner
report / reporting / writeup → report-generator
ctf / htb / hackthebox / tryhackme → ctf-solver
swarm / multi-agent / orchestrate → swarm-orchestrator
```

Output format:

```
**Agents for "<filter>"**:

| Agent | Why it matches | Tier |
|-------|----------------|------|
| <name> | <one-line relevance> | 1 or 2 |
| <name> | <one-line relevance> | 1 or 2 |

**Suggested first command** (in your shell):
> "<a one-line prompt the user can paste into Claude Code that will route to the top match>"
```

Tier 1 = advisory only. Tier 2 = can compose and execute commands with scope confirmation.

Tier 2 agents: recon-advisor, vuln-scanner, web-hunter, ad-attacker, exploit-chainer, poc-validator, bizlogic-hunter.

If the filter doesn't match anything in the taxonomy, return the closest matches, list the unmatched filter, and suggest 2–3 nearby tags from the taxonomy above.

---

**Source:** [`0xSteph/pentest-ai-agents`](https://github.com/0xSteph/pentest-ai-agents) → `commands/agents-for.md`
