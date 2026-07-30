---
name: rclone-authorize
description: "Remote authorization."
category: security-and-compliance
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_authorize.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_authorize.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_authorize/](https://rclone.org/commands/rclone_authorize/)
# rclone authorize

Remote authorization.

## Synopsis

Remote authorization. Used to authorize a remote or headless
rclone from a machine with a browser. Use as instructed by rclone config.
See also the [remote setup documentation](/remote_setup).

The command requires 1-3 arguments:

- Name of a backend (e.g. "drive", "s3")
- Either a base64 encoded JSON blob obtained from a previous rclone config session
- Or a client_id and client_secret pair obtained from the remote service

Use --auth-no-open-browser to prevent rclone to open auth
link in default browser automatically.

Use --template to generate HTML output via a custom Go template. If a blank
string is provided as an argument to this flag, the default template is used.

```
rclone authorize <backendname> [base64_json_blob | client_id client_secret] [flags]
```

## Options

```
      --auth-no-open-browser   Do not automatically open auth link in default browser
  -h, --help                   help for authorize
      --template string        The path to a custom Go template for generating HTML responses
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone](/commands/rclone/)	 - Show help for rclone commands, flags and backends.


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_authorize.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_authorize.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_authorize.md`
