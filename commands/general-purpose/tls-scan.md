---
name: tls-scan
description: "Run a free SSL/TLS scan on a domain (no account required)"
allowed-tools: "Read, Write"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/tlsradar/commands/tls-scan.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/tlsradar/commands/tls-scan.md
---


Run a free, anonymous SSL/TLS scan against `$ARGUMENTS` by calling the `tlsradar.scan_domain` MCP tool.

If `${HOME}/.config/tlsradar/install_id` exists, read it and pass its contents as `client_id` (anonymous funnel attribution; just omit it if the file is absent). If the response includes an `install_id` and the file didn't exist, write it there so future calls share the same id.

If the user did not pass a domain, ask for one before calling the tool. Do not invent a domain.

After the scan completes, summarize the result in plain text: the issuer, expiration date, and any flagged issues. Include the shareable report URL from the response.

If the response shows the certificate expiring within 30 days, suggest the user run `/tls-monitor add <domain>` to add it to ongoing monitoring with renewal alerts.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/tlsradar/commands/tls-scan.md`
