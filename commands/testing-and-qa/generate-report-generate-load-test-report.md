---
name: generate-report-generate-load-test-report
description: "Generate a detailed performance report from load test results."
category: testing-and-qa
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/load-tester/commands/generate-report.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/load-tester/commands/generate-report.md
---
# /generate-report - Generate Load Test Report

Generate a detailed performance report from load test results.

## Steps

1. Locate the most recent load test results in the project directory
2. Parse the raw results data (JSON, CSV, or stdout output)
3. Calculate key metrics: avg response time, p50, p95, p99 latency, throughput (req/s)
4. Calculate error rate breakdown by HTTP status code
5. Identify the slowest endpoints and their average response times
6. Compare results against SLA thresholds if defined in config
7. Generate performance trend charts as ASCII tables showing latency over time
8. Create a summary section with pass/fail status for each metric
9. Add recommendations based on findings (caching, connection pooling, query optimization)
10. Save the report as a markdown file with timestamp in the reports directory
11. If previous reports exist, include a comparison showing performance changes

## Rules

- Always include p99 latency as it reveals tail latency issues
- Flag any endpoint with response time exceeding 1 second as a concern
- Include request volume context (total requests, requests per second)
- Compare against previous baselines when available
- Format numbers consistently (2 decimal places for latency, whole numbers for counts)
- Include test configuration details (VUs, duration, ramp-up) in the report header

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/load-tester/commands/generate-report.md`
