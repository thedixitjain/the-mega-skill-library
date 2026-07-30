---
name: rules
description: "Use when the user asks about Codex Rules behavior, injected project rules, supported rule file locations, matching, or environment configuration."
category: ai-agents-and-harness
source_repo: code-yeongyu/oh-my-openagent
source_path: "packages/omo-codex/plugin/components/rules/skills/rules/SKILL.md"
source_url: https://github.com/code-yeongyu/oh-my-openagent/blob/HEAD/packages/omo-codex/plugin/components/rules/skills/rules/SKILL.md
---
# Codex Rules

Codex Rules is automatic once the plugin is enabled. It injects:

- static project instructions on `SessionStart` and `UserPromptSubmit`
- matching file-specific rules after Codex `apply_patch` by default

Dynamic `PostToolUse` output is injected as additional context and is deduplicated per plugin data session. Codex Rules does not rewrite tool output.

Supported project sources:

- `CONTEXT.md`
- `.omo/rules/**/*.md`
- `.claude/rules/**/*.md`
- `.cursor/rules/**/*.md`
- `.github/instructions/**/*.md`
- `.github/copilot-instructions.md`

Supported environment knobs:

- `CODEX_RULES_DISABLED=1`
- `CODEX_RULES_MODE=both|static|dynamic|off`
- `CODEX_RULES_MAX_RULE_CHARS=<number>`
- `CODEX_RULES_MAX_RESULT_CHARS=<number>`
- `CODEX_RULES_ENABLED_SOURCES=CONTEXT.md,.omo/rules`

The legacy `PI_RULES_*` variables are accepted as fallbacks for users migrating from `pi-rules`.

---

**Source:** [`code-yeongyu/oh-my-openagent`](https://github.com/code-yeongyu/oh-my-openagent) → `packages/omo-codex/plugin/components/rules/skills/rules/SKILL.md`
