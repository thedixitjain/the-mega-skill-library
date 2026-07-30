<!-- Harvested from https://github.com/openai/openai-cookbook/blob/HEAD/examples/agents_sdk/sandboxed-code-migration/repo_fixtures/support_reply_service/README.md -->
> **Source:** [`openai/openai-cookbook`](https://github.com/openai/openai-cookbook) → `examples/agents_sdk/sandboxed-code-migration/repo_fixtures/support_reply_service/README.md`

# Customer Support Reply Bot

This tiny package drafts a support-agent reply with the OpenAI Python client.

The current implementation still uses Chat Completions through a small wrapper
in `customer_support_bot/client.py`. The migration target is in `MIGRATION.md`.
