# File Content Schema

Single source of truth for pipeline artifact file formats.

## COMPLIANCE

| Generated File | Reference Section | Violation Consequence |
|----------------|-------------------|----------------------|
| `PLAN.md` | § 1 | `parsePlanMd()` parsing failure, scheduler inoperable |
| `TASK-XX.md` | § 2 | `parseTaskFilename()` DB registration missed |
| `TASK-XX_progress.md` | § 3 | committer gate FAIL |
| `TASK-XX_result.md` | § 4 | context-handoff missing |
| `TASK-XX_result.md` (direct) | § 5 | result.md recognition failure |
| `PROGRESS.md` | § 6 | scheduler progress tracking inoperable |

---

## § 0. Requirement.md

Path: `works/{WORK_ID}/Requirement.md`

```markdown
# Requirement — WORK-NN

## Original Request
> User's exact input

## Functional Requirements
- FR-01: ...
- FR-02: ...

## Non-Functional Requirements
- NFR-01: ...

## Acceptance Criteria
- [ ] Verifiable criteria
```

Created by: Specifier (mandatory for all requests)

---

## § 1. PLAN.md

Path: `works/{WORK_ID}/PLAN.md`

```markdown
# WORK-01: {title}

> Created: {YYYY-MM-DD}
> Requirement: {REQ-XXX | user request text}
> Execution-Mode: {direct | pipeline | full}
> Project: {project name}
> Tech Stack: {stack}
> Language: {lang_code}
> Status: PLANNED

## Goal
{1-2 sentences}

## Task Dependency Graph
{ASCII diagram}

## Tasks

### TASK-00: {title}
- **Depends on**: (none)
- **Scope**: {description}
- **Files**:
  - `path/to/file` — {description}

### TASK-01: {title}
- **Depends on**: TASK-00
```

Title format: `# WORK-NN: title` — `# PLAN WORK-NN:` is prohibited (`parsePlanMd()` error)

---

## § 2. TASK-XX.md

Path: `works/{WORK_ID}/TASK-XX.md`

> `parseTaskFilename()` regex: `/^TASK-(\d+)\.md$/` — WORK prefix prohibited

```markdown
# TASK-XX: {title}

## WORK
{WORK_ID}: {WORK title}

## Dependencies
- TASK-YY (required)

## Scope
{description}

## Files
| Path | Action | Description |
|------|--------|-------------|
| `src/file.ts` | CREATE | description |

## Acceptance Criteria
- [ ] {criterion}

## Verify
```bash
{verification commands}
```
```

---

## § 3. TASK-XX_progress.md

Path: `works/{WORK_ID}/TASK-XX_progress.md`

```markdown
# TASK-XX Progress

- Status: {PENDING | STARTED | IN_PROGRESS | COMPLETED}
- Started: {ISO 8601}
- Updated: {ISO 8601}
- Files changed:
  - `path/to/file` — {CREATE | MODIFY | DELETE}
```

| Timing | Status |
|--------|--------|
| planner template | `PENDING` |
| builder starts | `STARTED` |
| file changes in progress | `IN_PROGRESS` |
| completed | `COMPLETED` |

committer gate: file exists + `Status: COMPLETED` + Files changed is not empty

---

## § 4. TASK-XX_result.md (full / pipeline)

Path: `works/{WORK_ID}/TASK-XX_result.md`

```markdown
# TASK-XX Result

> WORK: {WORK_ID} — {title}
> Completed: {YYYY-MM-DD HH:MM}
> Status: **DONE**

{## Summary | ## 요약 | ## サマリー}
{1-2 lines}

{## Completed Checklist | ## 완료 체크리스트 | ## 完了チェックリスト}
- [x] {item}

{## Verification Results | ## 검증 결과 | ## 検証結果}
- Build: ✅
- Lint: ✅
- Tests: ✅ (N passed)

{## Files Changed | ## 변경 파일 | ## 変更ファイル}
### Created
- `path` — {description}

{## Issues Encountered | ## 발생 이슈 | ## 発生した問題}
None

{## Notes for Subsequent Tasks | ## 후속 TASK 참고사항 | ## 後続タスクへの注記}
None

{## Context Handoff | ## 컨텍스트 핸드오프 | ## コンテキスト引き継ぎ}

### Builder Context (SUMMARY)
{builder what field 1-3 lines}

### Verifier Context (FULL)
{verifier context-handoff 4 fields}
```

| Section | en | ko | ja |
|---------|----|----|-----|
| Summary | `## Summary` | `## 요약` | `## サマリー` |
| Completed Checklist | `## Completed Checklist` | `## 완료 체크리스트` | `## 完了チェックリスト` |
| Verification Results | `## Verification Results` | `## 검증 결과` | `## 検証結果` |
| Files Changed | `## Files Changed` | `## 변경 파일` | `## 変更ファイル` |
| Issues Encountered | `## Issues Encountered` | `## 발생 이슈` | `## 発生した問題` |
| Notes for Subsequent Tasks | `## Notes for Subsequent Tasks` | `## 후속 TASK 참고사항` | `## 後続タスクへの注記` |
| Context Handoff | `## Context Handoff` | `## 컨텍스트 핸드오프` | `## コンテキスト引き継ぎ` |

---

## § 5. TASK-XX_result.md (direct mode)

```markdown
# TASK-00 Result

> WORK: WORK-NN — {title}
> Completed: {YYYY-MM-DD HH:MM}
> Execution-Mode: direct
> Status: **DONE**

## Summary
{1 line}

## Files Changed
- `{path}` — {description}

## Verification
- Build: PASS (self-check)
- Lint: PASS (self-check)
```

---

## § 6. PROGRESS.md

Path: `works/{WORK_ID}/PROGRESS.md`

```markdown
# {WORK_ID} Progress

> WORK: {title}
> Last updated: {timestamp}
> Mode: manual | auto

| TASK | Title | Status | Commit | Duration |
|------|-------|--------|--------|----------|
| TASK-00 | {title} | ✅ Done | abc1234 | 12min |
| TASK-01 | {title} | 🔄 In Progress | — | — |

## Log
- [10:00] TASK-00 started
- [10:12] TASK-00 verified ✅, committed abc1234
```

---

## § 7. File Naming Rules

| Type | Format | Created By |
|------|--------|------------|
| Requirement | `Requirement.md` | specifier |
| WORK plan | `PLAN.md` | planner / specifier |
| TASK plan | `TASK-NN.md` | planner / specifier |
| TASK progress | `TASK-NN_progress.md` | planner / specifier (template) / builder (update) |
| TASK result | `TASK-NN_result.md` | committer |
| WORK progress | `PROGRESS.md` | scheduler |

`WORK-NN-TASK-NN.md` format prohibited → `parseTaskFilename()` cannot recognize it.
