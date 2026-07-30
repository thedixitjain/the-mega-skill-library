---
name: rclone-config-redacted
description: "Print redacted (decrypted) config file, or the redacted config for a single remote."
category: general-purpose
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_config_redacted.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_config_redacted.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_config_redacted/](https://rclone.org/commands/rclone_config_redacted/)
# rclone config redacted

Print redacted (decrypted) config file, or the redacted config for a single remote.

## Synopsis

This prints a redacted copy of the config file, either the
whole config file or for a given remote.

The config file will be redacted by replacing all passwords and other
sensitive info with XXX.

This makes the config file suitable for posting online for support.

It should be double checked before posting as the redaction may not be perfect.

```
rclone config redacted [<remote>] [flags]
```

## Options

```
  -h, --help   help for redacted
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone config](/commands/rclone_config/)	 - Enter an interactive configuration session.


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_config_redacted.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_config_redacted.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_config_redacted.md`
