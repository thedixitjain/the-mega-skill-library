---
name: setup-rum
description: "Set up Real User Monitoring"
category: devops-and-infra
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/performance/real-user-monitoring/commands/setup-rum.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/performance/real-user-monitoring/commands/setup-rum.md
---

# Real User Monitoring Setup

Implement RUM to capture actual user performance experiences.

## Monitoring Metrics

1. **Core Web Vitals**: LCP, FID, CLS
2. **Page Load Metrics**: FCP, TTI, TTFB
3. **Custom Metrics**: Business-specific timing markers
4. **User Context**: Browser, device, geography, network
5. **Error Tracking**: Client-side errors and exceptions

## Process

1. Choose RUM platform (Google Analytics, Datadog RUM, New Relic, etc.)
2. Design instrumentation strategy
3. Implement tracking code
4. Configure data collection and sampling
5. Create analysis dashboards
6. Set up alerting for degraded experiences

## Output

Provide:

- RUM integration code for frontend
- Configuration for chosen platform
- Custom metric definitions
- Dashboard setup for Core Web Vitals
- Segmentation strategy (device, browser, geography)
- Alert rules for poor user experiences
- Privacy and compliance considerations

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/performance/real-user-monitoring/commands/setup-rum.md`
