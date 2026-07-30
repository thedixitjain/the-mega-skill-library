# Context Handoff Policy

Sliding window context transfer rules between agents.

## Sliding Window

| Step Distance | Detail Level | Rule |
|---------------|-------------|------|
| Immediate (1 step) | `FULL` | All 4 fields transmitted |
| 2 steps back | `SUMMARY` | `what` field only, 1-3 lines |
| 3+ steps back | `DROP` | Omitted |

## Context-Handoff 4 Fields

| Field | FULL | SUMMARY | Content |
|-------|:----:|:-------:|---------|
| `what` | ✅ | ✅ | Summary of changes/verification (2-5 lines) |
| `why` | ✅ | ❌ | Decision rationale (2-4 lines) |
| `caution` | ✅ | ❌ | Caveats, conditional completion (1-3 lines) |
| `incomplete` | ✅ | ❌ | Incomplete items (1-2 lines, "None" if empty) |

## Pipeline Stage Input/Output

### Builder

Input: TASK spec + dependent TASK result.md context-handoff (sliding window)

Output:
```xml
<task-result status="PASS|FAIL">
  <context-handoff from="builder" detail-level="FULL">
    <what>Changes made</what><why>Rationale</why><caution>Caveats</caution><incomplete>Incomplete items</incomplete>
  </context-handoff>
</task-result>
```

### Verifier

Input: TASK spec + Builder context-handoff (FULL)

Output:
```xml
<task-result status="PASS|FAIL">
  <context-handoff from="verifier" detail-level="FULL">
    <what>Verification results</what><why>Judgment rationale</why><caution>Manual checks needed</caution><incomplete>Items that could not be verified</incomplete>
  </context-handoff>
</task-result>
```

### Committer

Input: Verifier context-handoff (FULL) + Builder context-handoff (SUMMARY) + progress.md (gate)

Processing:
1. progress.md gate: exists + Status=COMPLETED + Files changed is not empty
2. Gate passed → write result.md + git commit
3. Gate failed → return FAIL (triggers scheduler retry)

Output: → `{REFERENCES_DIR}/file-content-schema.md` § 4 reference

## Inter-TASK Dependency Transfer

- Immediate dependent TASK: context-handoff **FULL** (all 4 fields)
- 2 steps back: **SUMMARY** (what only)
- 3+ steps back: **DROP**

## Scheduler Dispatch

```xml
<!-- Verifier: Builder FULL -->
<dispatch to="verifier">
  <context-handoff from="builder" detail-level="FULL">...</context-handoff>
</dispatch>

<!-- Committer: Verifier FULL + Builder SUMMARY -->
<dispatch to="committer">
  <context-handoff from="verifier" detail-level="FULL">...</context-handoff>
  <context-handoff from="builder" detail-level="SUMMARY"><what>...</what></context-handoff>
</dispatch>

<!-- Next TASK Builder: dependency distance applied -->
<dispatch to="builder" task="TASK-YY">
  <previous-results>
    <context-handoff from="prev-task" task="TASK-XX" detail-level="FULL">...</context-handoff>
    <context-handoff from="prev-prev-task" task="TASK-WW" detail-level="SUMMARY"><what>...</what></context-handoff>
  </previous-results>
</dispatch>
```

## Committer Retry

1. Failure cause: progress.md not found / Status≠COMPLETED / No files changed
2. Re-dispatch to builder including existing progress.md
3. Maximum 2 retries (3 attempts total). 3 failures → TASK FAILED, pipeline halted
