---
name: httpyac
description: "Configure VSCode httpYac extension for API testing"
category: testing-and-qa
source_repo: libukai/awesome-agent-skills
source_path: "plugins/vscode-extensions-toolkit/commands/httpyac.md"
source_url: https://github.com/libukai/awesome-agent-skills/blob/HEAD/plugins/vscode-extensions-toolkit/commands/httpyac.md
---


You are helping the user configure the VSCode httpYac extension for API testing and automation.

## Your Task

Guide the user through setting up httpYac for their project:

1. **Assess the project context**:
   - Check if this is a new httpYac setup or updating existing configuration
   - Identify the API documentation or endpoints to work with
   - Determine authentication requirements

2. **Create httpYac configuration**:
   - Set up `.vscode/settings.json` with httpYac settings
   - Create `.http` files for API endpoints
   - Configure environment variables in `http-client.env.json`
   - Set up pre-request scripts for authentication if needed

3. **Organize API tests**:
   - Structure `.http` files by feature or service
   - Implement request chaining with response data
   - Add documentation comments in `.http` files

4. **Provide usage guidance**:
   - Explain how to run requests
   - Show how to switch environments
   - Demonstrate request chaining and variable usage

Use the `vscode-httpyac-config` skill for detailed templates and best practices.

---

**Source:** [`libukai/awesome-agent-skills`](https://github.com/libukai/awesome-agent-skills) → `plugins/vscode-extensions-toolkit/commands/httpyac.md`
