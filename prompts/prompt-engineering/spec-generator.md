---
name: spec-generator
description: "You are analyzing a skill/rule file for a coding agent (Claude Code). Your task: extract the observable behavioral sequence that an agent should follow when this skill is active."
category: prompt-engineering
source_repo: affaan-m/ECC
source_path: "skills/skill-comply/prompts/spec_generator.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/skills/skill-comply/prompts/spec_generator.md
---
<!-- markdownlint-disable MD007 -->
You are analyzing a skill/rule file for a coding agent (Claude Code).
Your task: extract the **observable behavioral sequence** that an agent should follow when this skill is active.

Each step should be described in natural language. Do NOT use regex patterns.

Output ONLY valid YAML in this exact format (no markdown fences, no commentary):

id: <kebab-case-id>
name: <Human readable name>
source_rule: <file path provided>
version: "1.0"

steps:
  - id: <snake_case>
    description: <what the agent should do>
    required: true|false
    detector:
      description: <natural language description of what tool call to look for>
      after_step: <step_id this must come after, optional — omit if not needed>
      before_step: <step_id this must come before, optional — omit if not needed>

scoring:
  threshold_promote_to_hook: 0.6

Rules:
- detector.description should describe the MEANING of the tool call, not patterns
  Good: "Write or Edit a test file (not an implementation file)"
  Bad: "Write|Edit with input matching test.*\\.py"
- Use before_step/after_step for skills where ORDER matters (e.g. TDD: test before impl)
- Omit ordering constraints for skills where only PRESENCE matters
- Mark steps as required: false only if the skill says "optionally" or "if applicable"
- 3-7 steps is ideal. Don't over-decompose
- IMPORTANT: Quote all YAML string values containing colons with double quotes
  Good: description: "Use conventional commit format (type: description)"
  Bad: description: Use conventional commit format (type: description)

Skill file to analyze:

---
{skill_content}
---

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `skills/skill-comply/prompts/spec_generator.md`

**Also appears in:** `hashgraph-online/awesome-codex-plugins/plugins/Colin4k1024/tsp/skills/skill-comply/prompts/spec_generator.md`
