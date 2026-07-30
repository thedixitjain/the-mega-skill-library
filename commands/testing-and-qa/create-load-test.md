---
name: create-load-test
description: "Create load test scenarios and scripts"
category: testing-and-qa
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/performance/load-test-runner/commands/create-load-test.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/performance/load-test-runner/commands/create-load-test.md
---

# Load Test Runner

Create comprehensive load test scenarios to validate application performance.

## Test Scenarios

1. **Baseline Load**: Normal traffic patterns
2. **Stress Test**: Identify breaking points
3. **Spike Test**: Sudden traffic increases
4. **Soak Test**: Extended duration testing
5. **Scalability Test**: Performance under growth

## Process

1. Analyze application endpoints and critical paths
2. Identify key user journeys to test
3. Create load test scripts (k6, JMeter, Artillery, etc.)
4. Define performance thresholds and SLOs
5. Generate test execution instructions

## Output

Provide:

- Load test scripts for chosen tool
- Test scenario descriptions
- Performance threshold definitions
- Execution instructions
- Result interpretation guidelines
- CI/CD integration suggestions

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/performance/load-test-runner/commands/create-load-test.md`
