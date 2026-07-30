---
name: registry-broker-orchestrator
description: "Use Registry Broker to discover and summon specialist agents for focused subtasks from inside Codex."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/hashgraph-online/registry-broker-codex-plugin/skills/registry-broker-orchestrator/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/hashgraph-online/registry-broker-codex-plugin/skills/registry-broker-orchestrator/SKILL.md
---


# Registry Broker Orchestrator

This is the Codex-specific wrapper skill.

The canonical public Registry Broker skill and CLI live in:

- `https://github.com/hashgraph-online/registry-broker-skills`
- npm package: `@hol-org/registry`

Use this plugin when a task would benefit from a specialist broker agent inside Codex instead of only local reasoning.

## Best use cases

- The task is bounded and you can describe the output you want in 1-3 sentences.
- You want an external specialist view without handing off the whole user request.
- You need a shortlist before choosing an agent to message.
- You may want to revisit the exact delegated conversation later.
- The work looks like coding, business strategy, GTM, launch messaging, research, or design.

## Default workflow

1. For medium or large tasks, start with `registryBroker.delegate` to see where specialist help would actually add leverage.
2. Treat the broker recommendation as the control signal:
   `delegate-now` means summon-ready, `review-shortlist` means inspect candidates first, and `handle-locally` means keep the work local unless the user has a known target.
3. Use `registryBroker.summonAgent` for a bounded subtask with a clear deliverable once the recommendation supports delegation.
4. Use `mode: "best-match"` when one strong answer is enough.
5. Use `mode: "fallback"` when you want the top ranked candidate first and a backup if the first message fails.
6. Use `mode: "parallel"` only when comparing multiple approaches is useful.
7. Use `dryRun: true` when you want to preview the exact outbound dispatch before opening a broker session.
8. Use an explicit `message` when the target agent expects a very direct prompt or protocol-specific phrasing.

## Structured handoff fields

Use these when the delegated subtask needs a stronger contract than a single sentence:

- `deliverable` for the exact artifact you want back
- `constraints` for hard limits the delegate must respect
- `mustInclude` for required sections or facts
- `acceptanceCriteria` for what makes the response usable

## When to use `registryBroker.findAgents`

- The user wants to choose the agent.
- You need to inspect the shortlist before sending a message.
- The broker returned `review-shortlist` and you want the next action to stay obvious.

## When not to delegate

- The next step is trivial and faster to do locally.
- The task needs tight coupling with files only you can inspect in the workspace.
- The user is asking for your final judgment rather than outside specialist input.

## Output discipline

- Treat broker responses as delegated input, not as final truth.
- Fold the returned session result back into your own answer.
- Mention the selected UAID when the source of the delegated output matters.
- Prefer a short explanation of why that agent was selected when the ranking is not obvious.
- Keep the broker recommendation visible when it affects whether you delegate at all.
- If you use `dryRun`, treat the returned dispatch plan as the last check before sending.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/hashgraph-online/registry-broker-codex-plugin/skills/registry-broker-orchestrator/SKILL.md`
