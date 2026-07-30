# Work Activity Log

Defines the rules for each agent to record WORK progress in the `works/{WORK_ID}/work_{WORK_ID}.log` file.

---

# 1. Stages and Log Content
* On first execution: The received prompt message** Content of the prompt message received at agent startup (Required)
* On Callback invocation: Called Callback URL, success status, Payload, Response (Required)
* During work: Work items and work content
* On task completion: The prompt message sent to other agents** Content of the prompt message received at agent startup (Required)

## log_work Method

**Do NOT use Bash** for activity log writes. Use the `Write` tool (or `Edit` tool to append).

Format each log entry as:
```
[YYYY-MM-DDTHH:MM:SS]_AGENT_STAGE_description
```

Example: to log an INIT stage, use the **Write** tool to append to `works/{WORK_ID}/work_{WORK_ID}.log`:
```
[2026-03-28T14:30:00]_SPECIFIER_INIT_WORK-09 created — Execution-Mode: direct
```

→ **Bash command rules: see `shared-prompt-sections.md` § 13**

---

## STAGE Table

| STAGE | Timing | Description Example |
|-------|--------|---------------------|
| `INIT` | After WORK_ID determined | `WORK-NN created — Execution-Mode: direct/pipeline/full` |
| `REF` | After STARTUP references | `References: CLAUDE.md, .agent/router_rule_config.json, agents/file-content-schema.md` |
| `PLAN` | After PLAN.md + TASK files created | `PLAN.md, TASK-00.md created` |
| `IMPL` | When direct mode code implementation starts | `Code implementation started — References: {modified file list}` |
| `BUILD` | After self-check passes | `Build/lint passed` |
| `COMMIT` | After git commit completed | `commit {hash}` |
| `DISPATCH` | On pipeline/full dispatch | `Builder dispatch` or `Planner dispatch` |

---

## Reference Collection Rules

Cumulatively track files read during STARTUP and subsequent exploration, recording them all at once during the `REF` stage.
