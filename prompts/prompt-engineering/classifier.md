---
name: classifier
description: "You are classifying tool calls from a coding agent session against expected behavioral steps."
category: prompt-engineering
source_repo: affaan-m/ECC
source_path: "skills/skill-comply/prompts/classifier.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/skills/skill-comply/prompts/classifier.md
---
You are classifying tool calls from a coding agent session against expected behavioral steps.

For each tool call, determine which step (if any) it belongs to. A tool call can match at most one step.

Steps:
{steps_description}

Tool calls (numbered):
{tool_calls}

Respond with ONLY a JSON object mapping step_id to a list of matching tool call numbers.
Include only steps that have at least one match. If no tool calls match a step, omit it.

Example response:
{"write_test": [0, 1], "run_test_red": [2], "write_impl": [3, 4]}

Rules:
- Match based on the MEANING of the tool call, not just keywords
- A Write to "test_calculator.py" is a test file write, even if the content is implementation-like
- A Write to "calculator.py" is an implementation write, even if it contains test helpers
- A Bash running "pytest" that outputs "FAILED" is a RED phase test run
- A Bash running "pytest" that outputs "passed" is a GREEN phase test run
- Each tool call should match at most one step (pick the best match)
- If a tool call doesn't match any step, don't include it

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `skills/skill-comply/prompts/classifier.md`

**Also appears in:** `hashgraph-online/awesome-codex-plugins/plugins/Colin4k1024/tsp/skills/skill-comply/prompts/classifier.md`
