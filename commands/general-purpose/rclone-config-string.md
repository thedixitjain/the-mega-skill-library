---
name: rclone-config-string
description: "Print connection string for a single remote."
category: general-purpose
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_config_string.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_config_string.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_config_string/](https://rclone.org/commands/rclone_config_string/)
# rclone config string

Print connection string for a single remote.

## Synopsis

Print a connection string for a single remote.

The [connection strings](/docs/#connection-strings) can be used
wherever a remote is needed and can be more convenient than using the
config file, especially if using the RC API.

Backend parameters may be provided to the command also.

Example:

```sh
$ rclone config string s3:rclone --s3-no-check-bucket
:s3,access_key_id=XXX,no_check_bucket,provider=AWS,region=eu-west-2,secret_access_key=YYY:rclone
```

**NB** the strings are not quoted for use in shells (eg bash,
powershell, windows cmd). Most will work if enclosed in "double
quotes", however connection strings that contain double quotes will
require further quoting which is very shell dependent.



```
rclone config string <remote> [flags]
```

## Options

```
  -h, --help   help for string
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone config](/commands/rclone_config/)	 - Enter an interactive configuration session.


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_config_string.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_config_string.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_config_string.md`
