---
name: integration-test
description: "Generate integration tests verifying component interactions and real data flows."
category: testing-and-qa
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/test-writer/commands/integration-test.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/test-writer/commands/integration-test.md
---


Generate integration tests verifying component interactions and real data flows.

## Steps

1. Identify integration boundaries in the target module (database, APIs, message queues).
2. Detect the test framework and available test utilities (supertest, testcontainers, etc.).
3. Set up test infrastructure:
   - Database: Use test database or in-memory alternative.
   - APIs: Use test server or recorded responses.
   - Queues: Use in-process implementations.
4. For each integration point:
   - Test the complete request-response cycle.
   - Verify data persistence and retrieval.
   - Test error propagation across boundaries.
   - Verify retry and timeout behavior.
5. Add setup and teardown for shared resources.
6. Run tests and verify they pass in isolation and in sequence.

## Format

```
Generated: <N> integration tests in <file>
Infrastructure: <services required>

Tests:
  - <scenario>: <what it verifies>
```

## Rules

- Integration tests should exercise real code paths, not mocked abstractions.
- Clean up test data in teardown hooks to prevent test pollution.
- Use transactions or database snapshots for fast rollback.
- Set appropriate timeouts for network-dependent tests.
- Name files with `.integration.test` suffix to separate from unit tests.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/test-writer/commands/integration-test.md`
