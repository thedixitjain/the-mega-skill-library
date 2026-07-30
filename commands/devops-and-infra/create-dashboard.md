---
name: create-dashboard
description: "Create monitoring dashboards with key metrics for service observability."
category: devops-and-infra
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/monitoring-setup/commands/create-dashboard.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/monitoring-setup/commands/create-dashboard.md
---
Create monitoring dashboards with key metrics for service observability.

## Steps


1. Define the dashboard audience and purpose:
2. Select the key metrics for the dashboard:
3. Design the dashboard layout:
4. Create each panel:
5. Add interactive elements:
6. Configure dashboard settings:
7. Test with real data across different scenarios.

## Format


```
Dashboard: <name>
Tool: <Grafana|Datadog|CloudWatch>
Panels: <count>
Key Metrics:
```


## Rules

- Keep dashboards focused: one dashboard per service or concern.
- Use consistent color coding (green=good, yellow=warning, red=critical).
- Include SLA target lines on all latency and error rate graphs.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/monitoring-setup/commands/create-dashboard.md`
