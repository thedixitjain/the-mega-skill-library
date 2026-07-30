---
name: claw-command-legacy-shim
description: "Legacy slash-entry shim for the nanoclaw-repl skill. Prefer the skill directly."
category: general-purpose
source_repo: affaan-m/ECC
source_path: "legacy-command-shims/commands/claw.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/legacy-command-shims/commands/claw.md
---
# Claw Command (Legacy Shim)

Use this only if you still reach for `/claw` from muscle memory. The maintained implementation lives in `skills/nanoclaw-repl/SKILL.md`.

## Canonical Surface

- Prefer the `nanoclaw-repl` skill directly.
- Keep this file only as a compatibility entry point while command-first usage is retired.

## Arguments

`$ARGUMENTS`

## Delegation

Apply the `nanoclaw-repl` skill and keep the response focused on operating or extending `scripts/claw.js`.
- If the user wants to run it, use `node scripts/claw.js` or `npm run claw`.
- If the user wants to extend it, preserve the zero-dependency and markdown-backed session model.
- If the request is really about long-running orchestration rather than NanoClaw itself, redirect to `dmux-workflows` or `autonomous-agent-harness`.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `legacy-command-shims/commands/claw.md`
