---
name: rclone-config-password
description: "Update password in an existing remote."
category: general-purpose
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_config_password.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_config_password.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_config_password/](https://rclone.org/commands/rclone_config_password/)
# rclone config password

Update password in an existing remote.

## Synopsis

Update an existing remote's password. The password
should be passed in pairs of `key` `password` or as `key=password`.
The `password` should be passed in in clear (unobscured).

For example, to set password of a remote of name myremote you would do:

```sh
rclone config password myremote fieldname mypassword
rclone config password myremote fieldname=mypassword
```

This command is obsolete now that "config update" and "config create"
both support obscuring passwords directly.

```
rclone config password name [key value]+ [flags]
```

## Options

```
  -h, --help   help for password
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone config](/commands/rclone_config/)	 - Enter an interactive configuration session.


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_config_password.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_config_password.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_config_password.md`
