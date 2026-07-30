---
name: analyze-logs
description: "Analyze logs for performance insights"
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/performance/log-analysis-tool/commands/analyze-logs.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/performance/log-analysis-tool/commands/analyze-logs.md
---

# Log Analysis Tool

Analyze application logs to identify performance issues and optimization opportunities.

## Analysis Areas

1. **Slow Requests**: Identify requests exceeding latency thresholds
2. **Error Patterns**: Detect recurring errors and exceptions
3. **Resource Warnings**: Find resource exhaustion warnings
4. **Query Performance**: Extract slow database queries from logs
5. **Traffic Patterns**: Analyze request patterns and spikes
6. **Exception Trends**: Track exception frequency over time

## Process

1. Define log aggregation strategy
2. Set up structured logging if not present
3. Configure log parsing and indexing
4. Create performance-focused log queries
5. Build log analysis dashboards
6. Set up log-based alerts

## Output

Provide:

- Structured logging implementation guide
- Log aggregation setup (ELK, Loki, CloudWatch, etc.)
- Performance analysis queries
- Dashboard configurations showing:
  - Slow request distribution
  - Error rate trends
  - Performance degradation events
- Alert rules based on log patterns
- Log retention and cost optimization recommendations

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/performance/log-analysis-tool/commands/analyze-logs.md`
