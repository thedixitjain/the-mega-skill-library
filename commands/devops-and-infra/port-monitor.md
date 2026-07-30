---
name: port-monitor
description: "Configure VSCode Port Monitor for development server monitoring"
category: devops-and-infra
source_repo: libukai/awesome-agent-skills
source_path: "plugins/vscode-extensions-toolkit/commands/port-monitor.md"
source_url: https://github.com/libukai/awesome-agent-skills/blob/HEAD/plugins/vscode-extensions-toolkit/commands/port-monitor.md
---


You are helping the user configure the VSCode Port Monitor extension for real-time port status monitoring.

## Your Task

Guide the user through setting up Port Monitor:

1. **Identify development environment**:
   - Determine which development servers are used (Vite, Next.js, Node.js, etc.)
   - Identify ports that need monitoring
   - Check for any port conflicts

2. **Create Port Monitor configuration**:
   - Set up `.vscode/settings.json` with port monitor settings
   - Configure ports to monitor
   - Set up auto-start behavior if desired
   - Configure notification preferences

3. **Provide environment-specific templates**:
   - Vite (default port 5173)
   - Next.js (default port 3000)
   - Node.js custom ports
   - Multiple concurrent servers

4. **Troubleshooting guidance**:
   - How to resolve port conflicts
   - How to check port status
   - How to restart servers

Use the `vscode-port-monitor-config` skill for detailed templates and best practices.

---

**Source:** [`libukai/awesome-agent-skills`](https://github.com/libukai/awesome-agent-skills) → `plugins/vscode-extensions-toolkit/commands/port-monitor.md`
