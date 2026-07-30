# Agent Flow — Main Claude Orchestration Guide

> **All agent invocations are performed by Main Claude.**
> Sub-agents only return results (dispatch XML or task-result XML) after completing their work.
> Main Claude receives return values and invokes the next agent.

---

## Pipeline Flow

```
[] tag detected → invoke specifier
    │
    Check specifier return value
    │
    ├─ Assumed (direct) → specifier creates Requirement.md + PLAN.md + TASK-00
    │                      → returns builder dispatch XML
    │                      → execute § direct procedure
    │
    └─ Delegated (pipeline/full) → specifier creates Requirement.md only
                                    → returns planner dispatch XML
                                    → execute § planner-driven procedure
```

---

## Direct Mode (Specifier Assumes Planner)

```
1. Invoke specifier → creates Requirement.md + PLAN.md + TASK-00 + returns builder dispatch XML
2. ⛔ STOP — Present summary to user and WAIT for approval (do NOT invoke builder)
3. Invoke builder (dispatch XML as prompt) — includes self-check
4. Invoke verifier+committer (builder result as prompt) — verify then commit in one spawn
```

> Verifier+Committer combined: single spawn performs verification, then creates result.md and git commit.

---

## Pipeline Mode (Separate Planner Invocation)

```
1. Invoke specifier+planner (single spawn) → creates Requirement.md + PLAN.md + TASK-NN + determines execution-mode
2. ⛔ STOP — Present Requirement.md + PLAN.md + TASK list and WAIT for approval
3. Invoke builder (per-TASK dispatch XML as prompt)
4. Invoke verifier+committer (builder result as prompt) — verify then commit in one spawn
```

> Specifier+Planner combined: specifier.md role first (Requirement.md), then planner.md role (PLAN.md + TASKs) in one spawn.

---

## Full Mode (With Scheduler)

```
1. Invoke specifier+planner (single spawn) → Requirement.md + PLAN.md + TASKs + execution-mode: full
2. ⛔ STOP — Present Requirement.md + PLAN.md + TASK list and WAIT for approval
3. Invoke scheduler → DAG analysis + READY TASK + returns builder dispatch XML
4. Invoke builder (dispatch XML as prompt) → implementation
5. Invoke verifier+committer (builder result as prompt) → verify then commit in one spawn
6. If incomplete TASKs remain, return to step 3
```

Parallel execution: When scheduler returns multiple READY TASKs, invoke builders concurrently.

---

## Resuming Existing WORK

Resume pipeline for a WORK that already has PLAN.md + TASKs:

```
1. Invoke scheduler → check READY TASKs + return builder dispatch XML
2. Invoke builder → implementation
3. Invoke verifier+committer → verify then commit in one spawn
4. If incomplete TASKs remain, return to step 1
```

---

## Combined Agent Invocation

### Specifier+Planner (single spawn)

When invoking specifier in pipeline/full mode, include both agent definitions:

```
Prompt to agent:
  "You will perform two roles in sequence.

   Role 1 — Specifier: Read specifier.md and create Requirement.md.
   Role 2 — Planner: Read planner.md and create PLAN.md + TASK files.

   Execute Role 1 first, then Role 2. Return the combined result."
```

- Use specifier's model (opus) for the spawn
- Agent reads both specifier.md and planner.md from REFERENCES_DIR
- Returns: Requirement.md + PLAN.md + TASK files + execution-mode

### Verifier+Committer (single spawn)

When invoking verification after builder completes:

```
Prompt to agent:
  "You will perform two roles in sequence.

   Role 1 — Verifier: Read verifier.md and verify build/lint/test.
   Role 2 — Committer: Read committer.md and create result.md + git commit.

   Execute Role 1 first. If verification PASSES, execute Role 2.
   If verification FAILS, skip Role 2 and return FAIL result."
```

- Use verifier's model (haiku) for the spawn
- Agent reads both verifier.md and committer.md from REFERENCES_DIR
- On PASS: returns verification result + commit hash
- On FAIL: returns verification failure only (no commit)

---

## Agent Role Summary

| Agent | Role | Model | Combined With |
|-------|------|-------|---------------|
| specifier | Requirement analysis | opus | + planner (pipeline/full) |
| planner | PLAN + TASK decomposition | opus | combined into specifier spawn |
| scheduler | DAG management + dispatch | haiku | standalone |
| builder | Code implementation | sonnet | standalone |
| verifier | Build/lint/test verification | haiku | + committer |
| committer | Result report + git commit | haiku | combined into verifier spawn |

---

## Sub-agent Spawn Count by Mode

| Mode | Spec+Plan | Scheduler | Builder | Veri+Commit | Total |
|------|:---------:|:---------:|:-------:|:-----------:|:-----:|
| direct | 1 (assumed) | — | 1 | 1 | **3** |
| pipeline | 1 (combined) | — | 1 | 1 | **3** |
| full (N TASKs) | 1 (combined) | 1 | N | N | **2 + 2N** |

**Before vs After (6 TASKs):**

| | Before | After | Reduction |
|---|:---:|:---:|:---:|
| Spawns | 2 + 3×6 = 20 | 2 + 2×6 = 14 | **-30%** |

---

## Approval Gates (CRITICAL)

> **MUST STOP and wait for explicit user approval before invoking the next agent.**
> Do NOT proceed until the user says "approve", "승인", "proceed", "go ahead", or equivalent.
> The only exception is auto mode — when the user's original message contains "auto" or "자동으로".

| Mode | Approvals | Timing | What to show user |
|------|:---------:|--------|-------------------|
| direct | 1 | After Specifier completes | Requirement.md + PLAN.md + TASK-00.md summary |
| pipeline/full | 1 | After Specifier+Planner completes | Requirement.md + PLAN.md + TASK list |
| auto-approve | 0 | — | Skip all approval gates |

> Note: pipeline/full now has **1 approval** (not 2), since specifier and planner run in one spawn.

**How to request approval:**
1. Present a summary of what the specifier+planner created (files, scope, execution-mode)
2. Ask: "Proceed?" or equivalent
3. **WAIT for user response** — do NOT invoke builder until approved

---

## Bash CLI Execution (Server Automation)

Run the pipeline independently without a conversation session. `claude -p` acts as Main Claude.

```bash
env -u CLAUDECODE -u ANTHROPIC_API_KEY claude -p \
  "[new-work] {task description}" \
  --dangerously-skip-permissions \
  --output-format stream-json \
  --verbose \
  2>&1 | tee /tmp/pipeline.log
```

| Option | Purpose |
|--------|---------|
| `env -u CLAUDECODE` | Bypass nested execution block |
| `env -u ANTHROPIC_API_KEY` | Use subscription auth (Max) instead of API key |
| `--dangerously-skip-permissions` | Skip permission prompts for unattended execution |
| `--output-format stream-json --verbose` | Streaming for real-time monitoring |

Resume interrupted pipeline:
```bash
env -u CLAUDECODE -u ANTHROPIC_API_KEY claude -p \
  "Resume WORK-XX pipeline." \
  --dangerously-skip-permissions
```

---

## References Directory Passing (REQUIRED)

Main Claude MUST pass the references directory path to every sub-agent invocation.
This allows sub-agents to locate their reference files regardless of installation method (npm or plugin).

**How to pass:**
- Prepend `REFERENCES_DIR={absolute_path}` at the top of the prompt for every Task tool call
- For npm installations: use `.claude/agents` (default, resolved from project root)
- For plugin installations: derive from the skill's "Base directory" (`{base_dir}/../sdd-pipeline/references`)

**Example:**
```
REFERENCES_DIR=C:/Users/me/.claude/plugins/cache/uc-taskmanager/abc123/skills/sdd-pipeline/references

<dispatch to="builder" ...>
  ...
</dispatch>
```

If REFERENCES_DIR is not available (e.g., npm installation without plugin), sub-agents fall back to `.claude/agents/`.

---

## Context Handoff (Sliding Window)

| Distance | Level | Content |
|----------|-------|---------|
| Previous | FULL | what + why + caution + incomplete |
| 2 steps back | SUMMARY | what 1-2 lines |
| 3+ steps | DROP | Not passed |

---

## ref-cache Chain Propagation

`<ref-cache>` carries pre-loaded reference file contents through the pipeline, eliminating redundant disk reads in each sub-agent.

### Rules

1. **First agent (typically specifier)** — no ref-cache available on dispatch. Reads reference files from `REFERENCES_DIR` normally.

2. **Agent returns task-result** — if the agent supports ref-cache, it includes `<ref-cache>` in its task-result XML containing all reference files it loaded.

3. **Main Claude propagates ref-cache** — when dispatching the next agent, copy the `<ref-cache>` block from the previous task-result into the new dispatch XML unchanged.

4. **Receiving agent skips file reads** — when `<ref-cache>` is present in the dispatch XML, the agent reads reference content from `<ref>` elements instead of reading files from disk.

5. **Missing ref-cache** — if a task-result does not contain `<ref-cache>` (agent does not support it yet), omit `<ref-cache>` from the next dispatch. The receiving agent falls back to reading files from disk.

### Flow Example

```
specifier+planner (no ref-cache in) → reads files → returns task-result with <ref-cache>
  ↓ Main Claude copies <ref-cache> into dispatch
builder (ref-cache in) → skips file reads → returns task-result with <ref-cache>
  ↓ Main Claude copies <ref-cache> into dispatch
verifier+committer (ref-cache in) → skips file reads → commit
```

### Phase 2: Selective Section Delivery

Instead of passing full reference files, Main Claude extracts only the sections each agent needs. This reduces dispatch token size by 50-70%.

**Main Claude reads reference files once at pipeline start**, then delivers condensed `<ref-cache>` per agent using this mapping:

| Agent | shared-prompt-sections | file-content-schema | xml-schema | context-policy | work-activity-log |
|-------|:---:|:---:|:---:|:---:|:---:|
| **specifier+planner** | §1,§2,§7,§8,§9,§11 | §0,§1,§2,§3 | §1,§3 | — | full |
| **scheduler** | §4,§8,§10 | §1,§6 | §1,§3,§4,§5 | full | full |
| **builder** | §1,§2,§10,§12 | §2,§3 | §1,§2,§4 | Builder section | full |
| **verifier+committer** | §1,§2,§8,§10,§12 | §3,§4,§5,§6,§7 | §1,§2,§4 | Verifier+Committer | full |

**Delivery format**: Condense each `<ref key="">` to contain only the needed sections, not the full file. Use one-line summaries for simple rules, keep full content only for templates and code blocks.

### Constraints

- **ref-cache does not replace REFERENCES_DIR** — always pass `REFERENCES_DIR` (or `<references-dir>`) in every dispatch regardless of ref-cache presence, for backward compatibility.
- **Agents may still read files** — if ref-cache content is insufficient, agents fall back to reading from disk.
