---
name: last30days-skill-copilot-instructions
description: "This file contains Copilot-specific additions. See AGENTS.md for the shared cross-tool governance layer."
category: ai-agents-and-harness
source_repo: mvanhorn/last30days-skill
source_path: ".github/copilot-instructions.md"
source_url: https://github.com/mvanhorn/last30days-skill/blob/HEAD/.github/copilot-instructions.md
---
This file contains Copilot-specific additions. See AGENTS.md for the shared cross-tool governance layer.

# Copilot-specific guidance

## Test generation

- Prefer unittest.TestCase for generated tests to match the existing test suite.
- Mock external calls with unittest.mock.patch.

## Pull request reminders

Before suggesting a pull request:

- Confirm that pytest passes.
- For changes that belong in the next release notes, add a `changelog.d/<n>.<type>.md` fragment (do not edit `CHANGELOG.md` or bump version manifests). See `CONTRIBUTING.md` / `AGENTS.md` § Changelog and releases and fill the PR template’s Agent disclosure + Relationship sections.
- If changes were made anywhere under skills/last30days/, confirm the install copy has been refreshed with:

npx skills add . -g -y

## Vendor exclusion zone

- Never suggest changes to skills/last30days/scripts/lib/vendor/.
- Treat skills/last30days/scripts/lib/vendor/ as a no-touch zone.

## CI expectations

GitHub CI runs:

- pytest
- ruff

Generated changes should pass both before review is requested.

## CLI examples

When suggesting CLI usage examples for safe local testing, default to:

--emit=compact --mock

---

**Source:** [`mvanhorn/last30days-skill`](https://github.com/mvanhorn/last30days-skill) → `.github/copilot-instructions.md`
