---
name: setup-monitoring
description: "Set up monitoring and alerting for application and infrastructure metrics."
category: devops-and-infra
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/monitoring-setup/commands/setup-monitoring.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/monitoring-setup/commands/setup-monitoring.md
---
Set up monitoring and alerting for application and infrastructure metrics.

## Steps


1. Define what to monitor:
2. Choose the monitoring stack:
3. Instrument the application:
4. Configure alerting rules:
5. Set up notification channels:
6. Create runbooks for each alert.
7. Test the monitoring by simulating failure scenarios.

## Format


```
Monitoring: <service name>
Stack: <tools used>
Metrics:
  - <metric name>: <type> (<threshold>)
```


## Rules

- Alert on symptoms (error rate), not causes (CPU usage).
- Every alert must have a runbook with resolution steps.
- Avoid alert fatigue: only alert on actionable conditions.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/monitoring-setup/commands/setup-monitoring.md`
