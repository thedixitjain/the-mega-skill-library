---
name: test-skill
description: "Test Claude Code skills using RED/GREEN/REFACTOR TDD phases in fresh subagents to prevent priming bias."
category: testing-and-qa
source_repo: athola/claude-night-market
source_path: "plugins/abstract/commands/test-skill.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/abstract/commands/test-skill.md
---


# Test Skill

Runs skill validation via superpowers:test-driven-development while keeping the familiar `/test-skill` interface.

## When To Use

Use this command when you need to:
- Testing a skill through RED/GREEN/REFACTOR phases
- Validating skill behavior before deployment
- Running TDD checkpoints on skill development

## When NOT To Use

Avoid this command if:
- Evaluating skill quality metrics - use /skills-eval instead
- Creating new skills - use /create-skill instead
- Hardening against rationalization - use /bulletproof-skill

## How It Works

- Executes RED/GREEN/REFACTOR phases through `superpowers:test-driven-development`.
- Accepts the same arguments as the previous `/test-skill` command.
- Adds superpowers' reporting and enforcement of TDD checkpoints.

## Notes

- Behavior is backward compatible with prior `/test-skill` usage.
- Use `--phase` to target a single stage or run the full cycle without flags.

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/abstract/commands/test-skill.md`
