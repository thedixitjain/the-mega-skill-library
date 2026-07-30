---
name: rclone-config-encryption-set
description: "Set or change the config file encryption password"
category: security-and-compliance
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_config_encryption_set.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_config_encryption_set.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_config_encryption_set/](https://rclone.org/commands/rclone_config_encryption_set/)
# rclone config encryption set

Set or change the config file encryption password

## Synopsis

This command sets or changes the config file encryption password.

If there was no config password set then it sets a new one, otherwise
it changes the existing config password.

Note that if you are changing an encryption password using
`--password-command` then this will be called once to decrypt the
config using the old password and then again to read the new
password to re-encrypt the config.

When `--password-command` is called to change the password then the
environment variable `RCLONE_PASSWORD_CHANGE=1` will be set. So if
changing passwords programmatically you can use the environment
variable to distinguish which password you must supply.

Alternatively you can remove the password first (with `rclone config
encryption remove`), then set it again with this command which may be
easier if you don't mind the unencrypted config file being on the disk
briefly.

```
rclone config encryption set [flags]
```

## Options

```
  -h, --help   help for set
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone config encryption](/commands/rclone_config_encryption/)	 - set, remove and check the encryption for the config file


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_config_encryption_set.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_config_encryption_set.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_config_encryption_set.md`
