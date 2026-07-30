---
name: systems-debug-optimized
description: "You own an intermittent data-corruption incident in our sharded key-value store. Work in /srv/kvstore and use the logs in /var/log/kvstore. Under concurrent writes, roughly once every few million operations, a record is observed with a value that was written for a different key. Your task is to reproduce that cross-key bleed, identify the exact code mechanism, implement the fix, and leave a regression test"
category: prompt-engineering
source_repo: muratcankoylan/Agent-Skills-for-Context-Engineering
source_path: "examples/long-horizon-prompt-lab/ui/prompts/systems-debug-optimized.txt"
source_url: https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/HEAD/examples/long-horizon-prompt-lab/ui/prompts/systems-debug-optimized.txt
---
You own an intermittent data-corruption incident in our sharded key-value
store. Work in /srv/kvstore and use the logs in /var/log/kvstore. Under concurrent
writes, roughly once every few million operations, a record is observed with a value
that was written for a different key. Your task is to reproduce that cross-key bleed,
identify the exact code mechanism, implement the fix, and leave a regression test
that would have caught it.

Do not optimize for a plausible post-mortem. Optimize for a causal demonstration.

WHAT COUNTS AS SOLVED

The incident is solved only when all of these artifacts exist:

1. A deterministic test or fault-injection harness that triggers cross-key bleed on
   a clean checkout in 20 of 20 runs under a controlled schedule. The schedule must
   be legal under the deployed runtime and memory model, reachable without test-only
   state mutation, and match the production incident in code path, shard state,
   ownership epoch, retry state, and observed failure mode.
2. A code-level causal explanation connecting the triggering schedule and state
   transition to the wrong key/value association.
3. A minimal fix that eliminates the reproduced failure.
4. An external reproducer that fails 20/20 on the pinned parent commit and passes
   100/100 on the fixed commit under the identical recorded schedule, plus a
   predeclared four-thread-count by three-seed stress matrix with every cell passing.
5. A fresh-context review that keeps the reproducer unchanged, reverts only the
   production-code fix, recovers the 20/20 failure, and confirms that the fix removes
   the cause rather than hiding the symptom.

If the verified cause is outside the repository (for example a runtime, filesystem,
hardware, or operational mechanism), completion may substitute an externally
replayable causal demonstration plus an owned-system configuration or containment
change. The same before/after/revert evidence is required, and fault injection must
exercise the verified non-code cause in regression.

"Root cause" means the specific mechanism whose activation is sufficient to reproduce
the corruption and whose correction prevents that same reproduction. "Fixed" does
not mean the observed frequency became lower. Retries, checksums, dropped writes, or
extra validation that merely masks the bad association are not fixes. The fixed build
must execute the same workload and reach the same precondition while preserving
acknowledged writes, concurrency, retries, and shard movement. It must introduce no
new errors or timeouts and must pass the unchanged availability, durability,
throughput, and latency acceptance gates. Preventing the trigger from running does
not count as a fix.

NON-SOLUTIONS

Do not return any of the following as completion:

- a hypothesis list, probability ranking, or narrative without a triggering test;
- "probably a race," "network issue," "clock skew," or "data drift" without the
  responsible code path and state transition;
- a stress test that sometimes fails but cannot control the failing interleaving;
- a mitigation that reduces incidence while the deterministic reproduction remains;
- a mechanism explaining only a different corruption mode; or
- a post-mortem without the reproduction, patch, and regression evidence.

INVESTIGATION POLICY

Start by pinning the current commit and turning the symptom into an executable
invariant. In the reproducer, every write uses a globally unique payload encoding its
key ID, request ID, and write generation. At the visibility point guaranteed by the
store's documented consistency model, after a defined quiescence barrier, cross-key
bleed occurs if the API response or durable record for key K contains a payload whose
encoded key is not K. Preserve key, payload provenance, shard, request ID, retry
generation, ownership epoch, and thread/task identity in the trace. Identify the first
layer where key and payload provenance diverge: API lookup, cache, serialization,
routing, or durable storage. A different latent defect with the same outward symptom
does not count as reproduction of this incident.

Build investigation/verified-ledger.md. Every entry must link to a command, log,
trace, test result, or diff from the current session. Record both supporting and
falsifying evidence. At the start of every later session, read the ledger and, if a
reproducer exists, rerun the smallest verified reproducer before doing new work.

Explore independent mechanism families: buffer or object reuse, serialization and
key/value framing, shard routing and ownership transfer, retry/idempotency behavior,
ABA or generation reuse, and unsynchronized publication. Use deterministic schedulers,
barriers, fault injection, and targeted tracing to turn timing hypotheses into
controlled interleavings. Do not keep pushing one theory after evidence falsifies it.
Before declaring the investigation blocked, produce evidence on at least four
materially different mechanism families.

ADVERSARIAL REVIEW

The runtime must launch the final reviewer in a separate context with read-only access
to candidate artifacts and no access to the investigation history. Give it the pinned
parent commit, original production log spans and traces, the predeclared incident
signature, reproducer, candidate trace, causal explanation, fix, and regression test.
Require the reviewer to:

- reproduce the failure 20/20 before the fix;
- apply the fix and observe 0/100 under the identical failing schedule, then pass
  every cell of the separate thread-count by scheduling-seed matrix;
- revert only the fix and recover the failure;
- check for ABA, lost-update, retry, and memory-lifetime explanations that the patch
  may merely perturb rather than correct;
- verify that the test detects cross-key bleed rather than a generic timeout or
  dropped write; and
- compare the candidate trace with the original production evidence and reject a
  reproducer whose code path, shard state, ownership epoch, retry state, or first
  divergence layer does not match; and
- trace every post-mortem claim to a run, log span, code location, or diff.

DELIVERABLES AND RETURN RULE

Return only after the reproduction, causal mechanism, minimal patch, regression
matrix, and fresh-context audit all pass. The final response must link to those
artifacts and explain the causal chain from triggering interleaving to the incorrect
key/value association at the API, cache, serialization, routing, or storage layer
where it first occurs, in enough detail for another engineer to reproduce it.

If the external runtime budget ends first, label the result INCOMPLETE. Return the
verified ledger, smallest reproducer achieved, falsified hypotheses, and exact next
experiment. Do not promote a likely explanation to root cause.

External search is limited to documented language, runtime, storage-engine, and
library semantics. A similar public bug is background evidence only; it is not the
answer unless its mechanism is reproduced in this codebase.

---

**Source:** [`muratcankoylan/Agent-Skills-for-Context-Engineering`](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) → `examples/long-horizon-prompt-lab/ui/prompts/systems-debug-optimized.txt`
