---
name: openproject
description: "Use the OpenProject plugin MCP tools to inspect projects and manage work packages in a configured OpenProject instance."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/varaprasadreddy9676/team-codex-plugins/skills/openproject/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/varaprasadreddy9676/team-codex-plugins/skills/openproject/SKILL.md
---


# OpenProject

Use this skill when the user wants to read or update data in OpenProject.

## Before use

- Prefer the plugin MCP tools from the `openproject` server.
- Confirm connectivity first with `server_info` or `get_current_user`.
- If the task creates or updates work packages, resolve the project and type
  first with `list_projects` and `list_project_types`.

## Workflow

1. Check connection state with `server_info`.
2. Discover the target project with `list_projects`.
3. When needed, inspect allowed types via `list_project_types`.
4. Use `search_work_packages` or `get_work_package` to gather context before
   making changes.
5. Prefer `create_work_package`, `update_work_package`, and
   `comment_on_work_package` for mutations.
6. Return the resulting work package id, subject, and API link in the answer.

## Configuration

The plugin reads:

- `OPENPROJECT_BASE_URL`
- `OPENPROJECT_API_TOKEN`
- `OPENPROJECT_ACCESS_TOKEN`

OpenProject documents API v3 authentication with Bearer tokens, API tokens, and
OAuth2. A personal API token in `OPENPROJECT_API_TOKEN` is the simplest setup.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/varaprasadreddy9676/team-codex-plugins/skills/openproject/SKILL.md`
