---
name: rclone-config-encryption-remove
description: "Remove the config file encryption password"
category: security-and-compliance
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_config_encryption_remove.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_config_encryption_remove.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_config_encryption_remove/](https://rclone.org/commands/rclone_config_encryption_remove/)
# rclone config encryption remove

Remove the config file encryption password

## Synopsis

Remove the config file encryption password

This removes the config file encryption, returning it to un-encrypted.

If `--password-command` is in use, this will be called to supply the old config
password.

If the config was not encrypted then no error will be returned and
this command will do nothing.

```
rclone config encryption remove [flags]
```

## Options

```
  -h, --help   help for remove
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone config encryption](/commands/rclone_config_encryption/)	 - set, remove and check the encryption for the config file


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_config_encryption_remove.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_config_encryption_remove.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_config_encryption_remove.md`
