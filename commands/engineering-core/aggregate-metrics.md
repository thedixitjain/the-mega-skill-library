---
name: aggregate-metrics
description: "Aggregate performance metrics centrally"
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/performance/metrics-aggregator/commands/aggregate-metrics.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/performance/metrics-aggregator/commands/aggregate-metrics.md
---

# Metrics Aggregator

Implement centralized metrics aggregation for comprehensive performance visibility.

## Metric Categories

1. **Application Metrics**: Custom business and performance metrics
2. **System Metrics**: CPU, memory, disk, network
3. **Database Metrics**: Query performance, connections
4. **Cache Metrics**: Hit rates, memory usage
5. **Queue Metrics**: Message rates, processing times
6. **External Service Metrics**: Third-party API performance

## Process

1. Design metrics taxonomy and naming convention
2. Choose metrics platform (Prometheus, StatsD, CloudWatch, etc.)
3. Implement metric instrumentation
4. Configure aggregation and retention
5. Create visualization dashboards
6. Set up alerting on key metrics

## Output

Provide:

- Metrics instrumentation code
- Metric naming and tagging standards
- Collection configuration (Prometheus, etc.)
- Aggregation rules and retention policies
- Dashboard configurations (Grafana, etc.)
- Alert definitions for critical metrics

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/performance/metrics-aggregator/commands/aggregate-metrics.md`
