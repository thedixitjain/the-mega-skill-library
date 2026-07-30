---
name: analyzing-network-packets-with-scapy
description: "Craft, send, sniff, and dissect network packets using Scapy for protocol analysis, network reconnaissance, and traffic anomaly detection in authorized security testing"
category: security-and-compliance
source_repo: mukul975/Anthropic-Cybersecurity-Skills
source_path: "skills/analyzing-network-packets-with-scapy/SKILL.md"
source_url: https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/HEAD/skills/analyzing-network-packets-with-scapy/SKILL.md
---


# Analyzing Network Packets with Scapy

## Overview

Scapy is a Python packet manipulation library that enables crafting, sending, sniffing, and dissecting network packets at granular protocol layers. This skill covers using Scapy for security-relevant tasks including TCP/UDP/ICMP packet crafting, pcap file analysis, protocol field extraction, SYN scan implementation, DNS query analysis, and detecting anomalous traffic patterns such as unusually fragmented packets or malformed headers.


## When to Use

- When investigating security incidents that require analyzing network packets with scapy
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Python 3.8+ with `scapy` library installed (`pip install scapy`)
- Root/administrator privileges for raw socket operations (sniffing, sending)
- Npcap (Windows) or libpcap (Linux) for packet capture
- Authorization to perform packet operations on target network

## Steps

1. Read and parse pcap/pcapng files with `rdpcap()` for offline analysis
2. Extract protocol layers (IP, TCP, UDP, DNS, HTTP) and field values
3. Compute traffic statistics: top talkers, protocol distribution, port frequency
4. Detect SYN flood patterns by analyzing TCP flag ratios
5. Identify DNS exfiltration indicators via query length and entropy analysis
6. Craft custom probe packets for authorized network testing
7. Export findings as structured JSON report

## Expected Output

JSON report containing packet statistics, protocol distribution, top source/destination IPs, detected anomalies (SYN floods, DNS tunneling indicators, fragmentation attacks), and per-flow summaries.

---

**Source:** [`mukul975/Anthropic-Cybersecurity-Skills`](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) → `skills/analyzing-network-packets-with-scapy/SKILL.md`
