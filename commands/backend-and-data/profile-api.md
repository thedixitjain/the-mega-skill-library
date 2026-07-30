---
name: profile-api
description: "Profile an API endpoint to identify performance bottlenecks and optimization opportunities."
category: backend-and-data
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/performance-monitor/commands/profile-api.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/performance-monitor/commands/profile-api.md
---


Profile an API endpoint to identify performance bottlenecks and optimization opportunities.

## Steps

1. Identify the target endpoint (URL, method, and payload).
2. Analyze the handler code path:
   - Map all database queries executed per request.
   - Identify external API calls and their expected latency.
   - Check for synchronous blocking operations.
   - Look for N+1 query patterns.
3. Measure baseline performance:
   - Send sample requests and measure response time.
   - Check memory allocation during request handling.
   - Identify the slowest operations in the call chain.
4. Check for common performance issues:
   - Missing database indexes for frequently queried columns.
   - Unbounded result sets without pagination.
   - Redundant data fetching (loading full objects when only IDs needed).
   - Missing caching for expensive computations.
   - Large response payloads without compression.
5. Suggest optimizations ranked by expected impact:
   - Add database indexes.
   - Implement caching layer.
   - Batch database queries.
   - Add pagination.
   - Enable response compression.
6. Estimate performance improvement for each suggestion.

## Format

```
Profile: <METHOD> <endpoint>
Baseline: <response time>ms (P50), <P99>ms (P99)

Bottlenecks:
  1. [HIGH] <description> - estimated <N>ms savings
  2. [MEDIUM] <description> - estimated <N>ms savings

Optimizations:
  1. <specific action to take>
  2. <specific action to take>

Expected improvement: <N>% faster response time
```

## Rules

- Profile with realistic data volumes, not empty databases.
- Measure P50, P95, and P99 latencies, not just averages.
- Identify the single biggest bottleneck before suggesting broad optimizations.
- Never suggest premature optimization for endpoints under 100ms.
- Consider read vs write path optimizations separately.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/performance-monitor/commands/profile-api.md`
