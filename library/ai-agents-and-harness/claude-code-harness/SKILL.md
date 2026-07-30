---
name: claude-code-harness
description: "Design a real harness for an agentic system using Claude Code-inspired patterns. Use when the user needs a harness blueprint, request assembly design, execution loop, tool runtime, memory layering, permission model, transcript or recovery strategy, or wants to turn a vague agent idea into a harness-level architecture. Do not use for generic product brainstorming, simple prompt writing, or isolated code generation."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/dadwadw233/claude-code-harness/skills/claude-code-harness/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/dadwadw233/claude-code-harness/skills/claude-code-harness/SKILL.md
---


# Claude Code Harness

Design the harness, not just the agent prompt.

This skill helps turn an agent idea into a harness blueprint that specifies:

- how a turn is assembled
- how the execution loop runs
- how tools are governed
- how memory survives boundaries
- how permissions and recovery are enforced
- how the system stays understandable to humans

## What to optimize for

Prefer harnesses that are:

- explicit rather than magical
- layered rather than blended
- recoverable rather than one-shot
- bounded rather than overpowered
- product-useful rather than architecturally theatrical

## Output contract

When this skill is active, default to a harness blueprint with these sections:

1. System goal and delegation boundary
2. Harness layers
3. Request assembly design
4. Turn loop design
5. Tool and capability runtime
6. Context and memory model
7. Permissions and safety gates
8. Transcript and recovery model
9. Extension surfaces
10. Implementation sequence

If the user is reviewing an existing design, lead with structural weaknesses and missing control planes.

## Workflow

### 1. Clarify whether the user needs a harness at all

Start by answering:

- what job is being delegated
- what state must survive across steps or turns
- whether the system needs tools, memory, recovery, or background work
- what would break if the model were only called once

If the workflow does not need a harness, say so directly.

### 2. Define the harness boundary

Separate:

- the model
- the harness runtime
- external tools and systems
- durable storage
- human operators

The harness is the layer that governs the model, not the model itself.

For a deeper framing, read `references/harness-principles.md`.

### 3. Design request assembly before discussing autonomy

Specify:

- what instruction sources exist
- which sources are durable versus per-turn
- how system context and user context enter the request
- how tool affordances are exposed
- what transcript normalization or message repair is required before model calls

If request assembly is vague, the harness is still vague.

### 4. Design the turn loop

Make the loop explicit:

- gather context
- decide or plan
- call tools or act
- verify progress
- continue, compact, escalate, or stop

Prefer a small, legible loop over a large “AI orchestration” story.

### 5. Treat tools as a runtime plane

For each tool or action surface, define:

- purpose
- invocation boundary
- inputs and outputs
- permission gates
- success criteria
- rollback or recovery story

Tools are not just capabilities. They are governance boundaries.

### 6. Treat memory as multiple layers

Separate at least these concerns when relevant:

- active turn context
- retrieved grounding
- working memory
- durable user or project memory
- summaries and compaction artifacts

Do not collapse memory into one implicit blob.

For reusable patterns, read `references/harness-pattern-language.md`.

### 7. Design safety and control into the runtime

Specify:

- approval points
- permission modes
- destructive action gates
- visibility into pending actions
- interruption and override behavior

The harness should make power legible before it makes power scalable.

### 8. Design persistence and recovery

Make explicit:

- what gets logged or transcripted
- what survives a new turn
- what survives a new session
- how partial work is resumed
- how compacted history preserves semantic continuity

If the system cannot recover from partial work, it is brittle.

### 9. End with implementation order

Translate the harness design into a build order:

- what must exist first
- what can be layered later
- what should be validated early
- what failure modes must be tested before expansion

Use `references/harness-blueprint-template.md` when a formal blueprint is required.

## Anti-patterns

Push back on these designs:

- prompt-only agents described as full systems
- lots of tools but no runtime governance
- memory with no boundaries or rewrite policy
- hidden background work with no transcript or user visibility
- retry loops with no stop conditions
- permissions handled as an afterthought
- extension systems added before the core loop is coherent

## Style guidance

- Be concrete about boundaries and data flow.
- Name missing runtime planes explicitly.
- Prefer fewer but stronger abstractions.
- If the design is performative rather than useful, say so.

## References

- Core framing: `references/harness-principles.md`
- Pattern language: `references/harness-pattern-language.md`
- Blueprint format: `references/harness-blueprint-template.md`
- Claude-derived lessons: `references/claude-code-derived-insights.md`

Load only the reference files you need and keep the final answer operational.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/dadwadw233/claude-code-harness/skills/claude-code-harness/SKILL.md`
