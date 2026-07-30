# fable-orchestration

A drop-in [Claude Code](https://claude.com/claude-code) skill for prompting **Claude Fable 5** to orchestrate a build correctly and cheaply.

Fable 5 is the most capable model but the most expensive — so don't run everything on it. Make **Fable the architect** and let **Opus 4.8** do the token-heavy work.

**The loop:** Opus 4.8 researches → **Fable architects** → Opus 4.8 executes → Opus 4.8 verifies. Fable only touches the middle step, so you pay its rate only for the thinking that needs it.

## Install

Drop `SKILL.md` into your project's `.claude/skills/fable-orchestration/` (or `~/.claude/skills/fable-orchestration/` for global). Claude Code loads it automatically.

## What's inside

- **Two ways to wire it** — advisor mode (`/advisor fable`, Opus as executor) or architect-and-delegate (Fable plans, parallel Opus 4.8 agents build).
- **Effort as the cost lever** — match `/effort` to task difficulty; Fable on `low` often beats prior models at `max`.
- **A paste-in prompt kit** — 9 ready-to-use instruction blocks (act-don't-overplan, delegate, verify, boundaries, and more).
- **Hard don'ts** — the failure modes that silently reroute Fable to Opus (e.g. asking it to "explain your reasoning").

See [`SKILL.md`](SKILL.md) for the full skill.
