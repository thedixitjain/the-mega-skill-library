---
name: analyzing-azure-activity-logs-for-threats
description: "'Queries Azure Monitor activity logs and sign-in logs via azure-monitor-query to detect suspicious administrative operations, impossible travel, privilege escalation, and resource modifications. Builds KQL queries for threat hunting in Azure environments. Use when investigating suspicious Azure tenant activity or building cloud SIEM detections. '"
category: devops-and-infra
source_repo: mukul975/Anthropic-Cybersecurity-Skills
source_path: "skills/analyzing-azure-activity-logs-for-threats/SKILL.md"
source_url: https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/HEAD/skills/analyzing-azure-activity-logs-for-threats/SKILL.md
---


# Analyzing Azure Activity Logs for Threats


## When to Use

- When investigating security incidents that require analyzing azure activity logs for threats
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Familiarity with security operations concepts and tools
- Access to a test or lab environment for safe execution
- Python 3.8+ with required dependencies installed
- Appropriate authorization for any testing activities

## Instructions

Use azure-monitor-query to execute KQL queries against Azure Log Analytics workspaces,
detecting suspicious admin operations and sign-in anomalies.

```python
from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient
from datetime import timedelta

credential = DefaultAzureCredential()
client = LogsQueryClient(credential)

response = client.query_workspace(
    workspace_id="WORKSPACE_ID",
    query="AzureActivity | where OperationNameValue has 'MICROSOFT.AUTHORIZATION/ROLEASSIGNMENTS/WRITE' | take 10",
    timespan=timedelta(hours=24),
)
```

Key detection queries:
1. Role assignment changes (privilege escalation)
2. Resource group and subscription modifications
3. Key vault secret access from new IPs
4. Network security group rule changes
5. Conditional access policy modifications

## Examples

```python
# Detect new Global Admin role assignments
query = '''
AuditLogs
| where OperationName == "Add member to role"
| where TargetResources[0].modifiedProperties[0].newValue has "Global Administrator"
'''
```

---

**Source:** [`mukul975/Anthropic-Cybersecurity-Skills`](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) → `skills/analyzing-azure-activity-logs-for-threats/SKILL.md`
