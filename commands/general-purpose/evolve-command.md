---
name: evolve-command
description: "Analyze instincts and suggest or generate evolved structures"
category: general-purpose
source_repo: affaan-m/ECC
source_path: ".opencode/commands/evolve.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/.opencode/commands/evolve.md
---
# Evolve Command

Analyze and evolve instincts in continuous-learning-v2: $ARGUMENTS

## Your Task

Run:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/continuous-learning-v2/scripts/instinct-cli.py" evolve $ARGUMENTS
```

If `CLAUDE_PLUGIN_ROOT` is unavailable, use:

```bash
python3 ~/.claude/skills/continuous-learning-v2/scripts/instinct-cli.py evolve $ARGUMENTS
```

## Supported Args (v2.1)

- no args: analysis only
- `--generate`: also generate files under `evolved/{skills,commands,agents}`

## Behavior Notes

- Uses project + global instincts for analysis.
- Shows skill/command/agent candidates from trigger and domain clustering.
- Shows project -> global promotion candidates.
- With `--generate`, output path is:
  - project context: `~/.claude/homunculus/projects/<project-id>/evolved/`
  - global fallback: `~/.claude/homunculus/evolved/`

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `.opencode/commands/evolve.md`
