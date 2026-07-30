# Harness Principles

This skill is built around one claim: a strong agent is not just a model with a tool list. It is a model wrapped in a coherent harness.

## What a harness is

A harness is the runtime layer that makes an agentic system executable, governable, and recoverable.

It usually owns:

- request assembly
- turn and tool loop execution
- tool exposure and permission gates
- memory and context maintenance
- transcript and recovery behavior
- extension points
- human control surfaces

## Why the harness matters more than the prompt

Prompts matter, but the harness determines:

- what information reaches the model
- what actions the model can take
- what state survives across turns
- how failures are handled
- whether humans can understand and steer the system

The more useful an agent looks in practice, the more likely its harness is doing the real heavy lifting.

## Request assembly is central

Claude Code suggests that the center of a harness is not only the tool loop. It is the combination of:

- assembling instruction sources
- injecting runtime context
- exposing tools as schemas or affordances
- normalizing message history into a stable model request

This is where product intent becomes machine behavior.

## The turn loop should stay legible

A good turn loop usually looks like:

1. gather context
2. produce a model turn
3. execute one or more actions
4. verify what happened
5. continue, compact, escalate, or stop

If the loop cannot be named clearly, it probably cannot be operated safely.

## Memory is a control problem

Memory is not a yes-or-no feature. It is a boundary design problem:

- what lives only for this turn
- what persists for this task
- what survives across sessions
- what is summarized or compacted
- what must remain auditable

The harness should make those boundaries explicit.

## Recovery is part of the design

Any useful agentic product will eventually face:

- partial success
- interrupted work
- stale context
- missing tool output
- user redirection

If the design has no transcript, no resumability, and no recovery story, the harness is incomplete.

## Human control is not optional

A practical harness should make room for:

- approvals
- visibility
- interruption
- auditability
- bounded autonomy

This is not just safety theater. It is part of how people trust and operate real agentic systems.

