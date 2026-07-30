---
name: sftp
description: "Configure VSCode SFTP for deploying static websites"
category: general-purpose
source_repo: libukai/awesome-agent-skills
source_path: "plugins/vscode-extensions-toolkit/commands/sftp.md"
source_url: https://github.com/libukai/awesome-agent-skills/blob/HEAD/plugins/vscode-extensions-toolkit/commands/sftp.md
---


You are helping the user configure the VSCode SFTP extension for deploying static websites to production servers.

## Your Task

Guide the user through setting up SFTP deployment:

1. **Gather server information**:
   - Server host, port, username
   - Authentication method (password or SSH key)
   - Remote deployment path
   - Local build output directory

2. **Create SFTP configuration**:
   - Set up `.vscode/sftp.json` with server details
   - Configure upload patterns and ignore rules
   - Set up automatic upload on save if desired

3. **Configure Nginx (if applicable)**:
   - Provide optimized Nginx configuration
   - Include security headers
   - Set up caching strategies
   - Configure compression

4. **Test deployment**:
   - Verify connection to server
   - Test file upload
   - Provide deployment workflow guidance

Use the `vscode-sftp-config` skill for detailed templates and best practices.

---

**Source:** [`libukai/awesome-agent-skills`](https://github.com/libukai/awesome-agent-skills) → `plugins/vscode-extensions-toolkit/commands/sftp.md`
