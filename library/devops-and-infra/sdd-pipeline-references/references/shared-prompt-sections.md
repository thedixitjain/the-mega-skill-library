# Shared Prompt Sections

Common reusable sections. Each agent references these via `cache_control` markers.

---

## § 1. Output Language Rule

```
Priority: PLAN.md > Language: → CLAUDE.md ## Language → en (default)

On dispatch: pass resolved language code in <context><language> field
Section headers (##) are also written in the resolved language (refer to language mapping table)
```

---

## § 2. Build and Lint Commands

```bash
# Auto-detect Build (execute only if script exists)
if [ -f "package.json" ]; then
  if node -e "const p=JSON.parse(require('fs').readFileSync('package.json','utf8')); process.exit(p.scripts&&p.scripts.build?0:1)" 2>/dev/null; then
    npm run build 2>&1 || bun run build 2>&1 || yarn build 2>&1
  fi
elif [ -f "Cargo.toml" ]; then
  cargo build 2>&1
elif [ -f "go.mod" ]; then
  go build ./... 2>&1
elif [ -f "pyproject.toml" ] || [ -f "setup.py" ]; then
  python -m py_compile $(find . -maxdepth 3 -name "*.py" -not -path "*/venv/*" 2>/dev/null) 2>&1
elif [ -f "Makefile" ]; then
  make build 2>&1 || make 2>&1
fi

# Auto-detect Lint (execute only if script exists)
if [ -f "package.json" ]; then
  if node -e "const p=JSON.parse(require('fs').readFileSync('package.json','utf8')); process.exit(p.scripts&&p.scripts.lint?0:1)" 2>/dev/null; then
    npm run lint 2>&1 || bun run lint 2>&1 || true
  fi
elif [ -f "pyproject.toml" ]; then
  ruff check . 2>&1 || python -m flake8 . 2>&1 || true
fi
```

- If build/lint scripts do not exist → **skip (treat as N/A)**.
- On build/lint failure, always fix before reporting.

---

## § 3. WORK and TASK File Path Patterns

```
works/{WORK_ID}/
  ├─ Requirement.md                 # Created by Specifier (mandatory)
  ├─ PLAN.md
  ├─ PROGRESS.md
  ├─ TASK-00.md               # No WORK prefix
  ├─ TASK-00_progress.md      # Separator: underscore
  ├─ TASK-00_result.md        # Separator: underscore
  └─ TASK-01.md ...
```

- WORK ID: `WORK-NN` (e.g., `WORK-03`)
- TASK ID: `TASK-NN` (e.g., `TASK-00`) — WORK prefix must NOT be included

---

## § 4. File System Discovery Scripts

```
# Find latest WORK with incomplete TASKs
# Use Glob tool: pattern "works/WORK-*/" → list all WORK directories (sorted)
# For each WORK (descending), compare:
#   Glob "works/WORK-NN/TASK-*.md" (exclude *_result.md, *_progress.md) → TOTAL
#   Glob "works/WORK-NN/TASK-*_result.md" → DONE
# First WORK where DONE < TOTAL is the active WORK

# List all WORKs
# Use Glob tool: pattern "works/WORK-*/"

# TASK completion status
# TOTAL = count of Glob "works/${WORK_ID}/TASK-??.md"
# DONE  = count of Glob "works/${WORK_ID}/TASK-*_result.md"
```

---

## § 5. Task Result XML Format

```xml
<task-result work="{WORK_ID}" task="{TASK_ID}" agent="{agent}" status="{PASS|FAIL}">
  <summary>{1-2 line summary}</summary>
  <files-changed>
    <file action="{created|modified|deleted}" path="{path}">{description}</file>
  </files-changed>
  <verification>
    <check name="{type}" status="{PASS|FAIL|N/A}">{details}</check>
  </verification>
  <notes>{notes for next steps}</notes>
</task-result>
```

---

## § 7. PLAN.md Required Meta-Information — 7 Fields

→ `{REFERENCES_DIR}/file-content-schema.md` § 1 reference

| Field | Required | Description |
|-------|----------|-------------|
| `> Created:` | ✅ | YYYY-MM-DD |
| `> Requirement:` | ✅ | `REQ-XXX` or user request text |
| `> Execution-Mode:` | ✅ | `direct` / `pipeline` / `full` |
| `> Project:` | ✅ | Project name |
| `> Tech Stack:` | ✅ | Detected tech stack |
| `> Language:` | ✅ | Language code (`ko`, `en`, etc.) |
| `> Status:` | ✅ | Always starts as `PLANNED` |

---

## § 8. WORK-LIST.md Update Rules

File: `works/WORK-LIST.md`

**Format:**
```
LAST_WORK_ID: WORK-XX

| WORK | 제목 | 상태 | 생성일 | 완료일 |
|------|------|------|--------|--------|
| WORK-NN | ... | IN_PROGRESS | YYYY-MM-DD | |
| WORK-MM | ... | DONE | YYYY-MM-DD | YYYY-MM-DD |
```

| Status | Meaning | Trigger |
|--------|---------|---------|
| `IN_PROGRESS` | WORK is being executed | specifier creates WORK |
| `DONE` | All TASKs completed, awaiting review/push | committer completes last TASK |
| `COMPLETED` | Archived to _COMPLETED/ | push merge (Main Claude batch processes all DONE) |

Rules:
- `LAST_WORK_ID` header tracks the highest WORK ID ever created
- **specifier**: on WORK creation, add IN_PROGRESS row + update `LAST_WORK_ID`
- **committer**: when last TASK is completed, change `IN_PROGRESS` → `DONE` and fill completion date (do NOT move folder or remove row)
- **Main Claude** (push procedure): move all DONE WORKs to `works/_COMPLETED/`, remove their rows from WORK-LIST.md

---

## § 9. Locale Detection

```
1. CLAUDE.md → check "Language: xx"
2. If not found, ask user for language
3. If not found, auto-detect system locale
   - Windows: powershell -c "[CultureInfo]::CurrentCulture.TwoLetterISOLanguageName"
   - Linux/Mac: locale | grep LANG | grep -oP '[a-z]{2}' | head -1
   - Fallback: "en"
```

---

## § 10. Callback Transmission Template

→ **Bash command rules: see § 13** — each step below is a separate tool call.

Replace `{CallbackType}` with the actual key name (e.g., `ProgressCallback`, `TaskCallback`).

**Step 1.** Use `Grep` tool to find `{CallbackType}:` line in CLAUDE.md. If not found, skip callback entirely.

**Step 2.** Use `Grep` tool to find `CallbackToken:` line in CLAUDE.md (optional).

**Step 3.** Send callback with a single `curl` command:
```bash
curl -s -X POST "CALLBACK_URL" -H "Content-Type: application/json" -H "X-Runner-Api-Key: TOKEN" -d '{"workId":"WORK-01","taskId":"TASK-00",...}'
```

Agent-specific payload fields:
- **ProgressCallback** (builder): `"status": "IN_PROGRESS"`, `"currentReasoning": "..."`
- **TaskCallback** (committer): `"status": "SUCCESS"`, `"commitHash": "${COMMIT_HASH}"`

---

## § 11. Project Discovery

```bash
# 1. Check CLAUDE.md language setting
grep -oP '(?<=Language:\s?)[a-z]{2}' CLAUDE.md 2>/dev/null

# 2. Tech stack
head -50 package.json 2>/dev/null
head -30 pyproject.toml 2>/dev/null
head -20 Cargo.toml 2>/dev/null
head -10 go.mod 2>/dev/null

# 3. Structure (when needed)
find . -maxdepth 3 -type f \( -name "*.md" -o -name "*.json" -o -name "*.toml" \) -not -path "*/node_modules/*" 2>/dev/null
```

---

## § 12. Progress File Gate Check

Gate conditions for `works/WORK-NN/TASK-XX_progress.md`:
- File exists at the expected path
- `Status: COMPLETED` line is present
- `## Files Changed` section is present and non-empty

On gate failure → return FAIL task-result immediately. Do not proceed to subsequent steps.

---

## § 13. Bash Command Rules

Bash commands MUST follow these rules for permission compatibility.

**MANDATORY:**
- One simple command per Bash call — NO compound commands (`&&`, `||`, `;`, `|`)
- NO `cd dir && command` — you are already in the project root
- NO multi-line scripts — split into separate Bash calls
- NO sub-shell expansions in arguments — e.g., `$(date ...)` inside `printf`
- Use relative paths from project root (e.g., `works/WORK-01/`) — NO absolute paths
- Use `git add file`, `git commit -m "msg"` — NO `git -C path` flag

**For file operations, prefer dedicated tools over Bash:**
- Read files → `Read` tool (NOT `cat`)
- Write/append files → `Write` tool (NOT `echo >>` or `printf >>`)
- Edit files → `Edit` tool (NOT `sed -i`)
- Search files → `Grep` tool (NOT `grep`)
- Find files → `Glob` tool (NOT `find`)

**Activity log example:**
```
WRONG: printf '[%s]_%s\n' "$(date ...)" "INIT" >> work.log
RIGHT: Use Write tool to append a line to the log file
```

**Git example:**
```
WRONG: cd /path/to/project && git add file && git commit -m "msg"
RIGHT: git add file        (one call)
       git commit -m "msg"  (next call)
```

---

## Version

- Created: 2026-03-10
- Updated: 2026-03-28
