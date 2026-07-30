<!-- Harvested from https://github.com/openai/openai-cookbook/blob/HEAD/examples/agents_sdk/sandboxed-code-migration/repo_fixtures/case_summary_service/README.md -->
> **Source:** [`openai/openai-cookbook`](https://github.com/openai/openai-cookbook) → `examples/agents_sdk/sandboxed-code-migration/repo_fixtures/case_summary_service/README.md`

# Case summary service

Small offline fixture for the sandboxed migration cookbook.

The pre-migration service wraps a Chat Completions call and uses it to summarize
internal case notes. Tests use fakes; they should never call the network.
