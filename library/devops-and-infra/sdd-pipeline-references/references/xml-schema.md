# Agent Communication XML Schema

XML communication format definition for uc-taskmanager agents.

---

## 1. Dispatch Format (Dispatcher → Receiver)

```xml
<dispatch to="{receiver}" work="{WORK_ID}" task="{TASK_ID}" execution-mode="{direct|pipeline|full}">
  <ref-cache>                                        <!-- optional -->
    <ref key="shared-prompt-sections">{file content}</ref>
    <ref key="file-content-schema">{file content}</ref>
    <ref key="xml-schema">{file content}</ref>
    <ref key="context-policy">{file content}</ref>
    <ref key="work-activity-log">{file content}</ref>
  </ref-cache>
  <references-dir>{absolute path to references directory}</references-dir>
  <context>
    <project>{project name}</project>
    <language>{lang_code}</language>
    <plan-file>works/{WORK_ID}/PLAN.md</plan-file>
  </context>
  <task-spec>
    <file>works/{WORK_ID}/TASK-XX.md</file>
    <title>{title}</title>
    <action>{implement|verify|commit|plan|route}</action>
    <description>{optional}</description>
  </task-spec>
  <previous-results>
    <result task="{TASK_ID}" status="{PASS|FAIL|SKIP}">{summary}</result>
  </previous-results>
  <cache-hint sections="{section1},{section2}"/>
</dispatch>
```

| Attribute | Value |
|-----------|-------|
| `to` | builder, verifier, committer, planner, scheduler, specifier |
| `task` | `TASK-NN` — WORK prefix must NOT be included |
| `execution-mode` | direct / pipeline / full (defaults to full if omitted) |

---

## 2. Task Result Format (Receiver → Dispatcher)

```xml
<task-result work="{WORK_ID}" task="{TASK_ID}" agent="{agent}" status="{PASS|FAIL}">
  <summary>{1-2 line summary}</summary>
  <files-changed>
    <file action="{created|modified|deleted}" path="{path}">{description}</file>
  </files-changed>
  <verification>
    <check name="{type}" status="{PASS|FAIL|N/A}">{output}</check>
  </verification>
  <notes>{notes}</notes>
  <ref-cache>                                        <!-- optional -->
    <ref key="shared-prompt-sections">{file content}</ref>
    <ref key="file-content-schema">{file content}</ref>
    <ref key="xml-schema">{file content}</ref>
    <ref key="context-policy">{file content}</ref>
    <ref key="work-activity-log">{file content}</ref>
  </ref-cache>
</task-result>
```

---

## 3. Dispatcher-Receiver Mapping

| Dispatcher | Receiver | execution-mode | Description |
|------------|----------|:--------------:|-------------|
| Specifier | Builder | `direct` | Assumed: single TASK implementation (Verifier skipped) |
| Specifier | Planner | `pipeline/full` | Delegated: complex WORK planning |
| Planner | Builder | `pipeline` | TASK implementation |
| Planner | Scheduler | `full` | DAG management + execution |
| Scheduler | Builder | `full` | N TASK implementation |
| Scheduler | Verifier | `full` | N TASK verification |
| Scheduler | Committer | `full` | N TASK commit |

---

## 4. Context-Handoff Element

```xml
<context-handoff from="{agent}" detail-level="{FULL|SUMMARY|DROP}">
  <what>{changes/verification details}</what>
  <why>{decision rationale}</why>       <!-- FULL only -->
  <caution>{caveats}</caution>          <!-- FULL only -->
  <incomplete>{incomplete items}</incomplete>  <!-- FULL only -->
</context-handoff>
```

| detail-level | Included Fields |
|:---:|---|
| `FULL` | what, why, caution, incomplete |
| `SUMMARY` | what only (1-3 lines) |
| `DROP` | Element omitted |

---

## 5. Agent Behavior by execution-mode

| Agent | direct | pipeline | full |
|-------|--------|----------|------|
| Specifier | Requirement.md + PLAN.md + TASK (assumed) | Requirement.md only → delegate to Planner | Requirement.md only → delegate to Planner |
| Planner | Not invoked (Specifier assumed) | PLAN.md + TASK + execution-mode | PLAN.md + TASK + execution-mode |
| Scheduler | Not invoked | Not invoked | DAG management + [B→V→C]×N |
| Builder | Normal execution (self-check) | Normal execution | Normal execution |
| Verifier | Not invoked | Normal execution | Normal execution |
| Committer | result.md+commit+callback | result.md+commit+callback | result.md+commit+callback |

Invariants (regardless of mode):

| Item | direct | pipeline/full |
|------|:---:|:---:|
| `works/WORK-NN/` directory | Specifier | Specifier |
| `Requirement.md` | Specifier | Specifier |
| `PLAN.md` | Specifier (assumed) | Planner |
| `TASK-XX.md` | Specifier (assumed) | Planner |
| `TASK-XX_result.md` | Committer | Committer |
| COMMITTER DONE callback | Committer | Committer |
| `WORK-LIST.md` IN_PROGRESS | Specifier | Specifier |

---

## 6. ref-cache Element Definition

`<ref-cache>` is an optional container element that carries pre-loaded reference file contents within dispatch and task-result XML. When present, receiving agents MUST use these contents instead of reading files from disk.

### Structure

```xml
<ref-cache>
  <ref key="{filename-without-extension}">{full file content}</ref>
  ...
</ref-cache>
```

| Element | Required | Description |
|---------|----------|-------------|
| `<ref-cache>` | Optional | Container for cached reference files. Omit entirely if no cache is available. |
| `<ref key="...">` | — | Individual reference file. `key` is the filename without extension (e.g., `shared-prompt-sections`). |

### Recognized Keys

| Key | Corresponding File |
|-----|--------------------|
| `shared-prompt-sections` | `{REFERENCES_DIR}/shared-prompt-sections.md` |
| `file-content-schema` | `{REFERENCES_DIR}/file-content-schema.md` |
| `xml-schema` | `{REFERENCES_DIR}/xml-schema.md` |
| `context-policy` | `{REFERENCES_DIR}/context-policy.md` |
| `work-activity-log` | `{REFERENCES_DIR}/work-activity-log.md` |

### Backward Compatibility

- Dispatch or task-result XML without `<ref-cache>` is fully valid — agents fall back to reading files from `REFERENCES_DIR`.
- Agents that do not yet support ref-cache simply ignore the element and read files normally.
- Partial ref-cache (only some keys present) is allowed — missing keys are read from disk.
