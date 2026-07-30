---
name: team
description: "[team-mode] Team-mode reference detected. Orchestrate via team tools (teamcreate -> teamtaskcreate + teamsendmessage); NEVER substitute with delegatetask — it is not equivalent. After every teamtaskupdate that completes or fails a task, re-check teamtasklist: if every task is terminal, run the closure sequence (teamshutdownrequest + teamapproveshutdown per active member, then teamdelete) in the same turn. Closing the team is the lead's responsibility, not the user's. If the team tools are absent, teammode is disabled — tell the user to set teammode.enabled=true and restart opencode."
category: prompt-engineering
source_repo: code-yeongyu/oh-my-openagent
source_path: "packages/prompts-core/prompts/mode/team.md"
source_url: https://github.com/code-yeongyu/oh-my-openagent/blob/HEAD/packages/prompts-core/prompts/mode/team.md
---
[team-mode]
Team-mode reference detected. Orchestrate via team_* tools (team_create -> team_task_create + team_send_message); NEVER substitute with delegate_task — it is not equivalent. After every team_task_update that completes or fails a task, re-check team_task_list: if every task is terminal, run the closure sequence (team_shutdown_request + team_approve_shutdown per active member, then team_delete) in the same turn. Closing the team is the lead's responsibility, not the user's. If the team_* tools are absent, team_mode is disabled — tell the user to set team_mode.enabled=true and restart opencode.

---

**Source:** [`code-yeongyu/oh-my-openagent`](https://github.com/code-yeongyu/oh-my-openagent) → `packages/prompts-core/prompts/mode/team.md`
