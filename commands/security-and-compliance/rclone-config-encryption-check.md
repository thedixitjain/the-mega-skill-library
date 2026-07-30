---
name: rclone-config-encryption-check
description: "Check that the config file is encrypted"
category: security-and-compliance
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_config_encryption_check.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_config_encryption_check.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_config_encryption_check/](https://rclone.org/commands/rclone_config_encryption_check/)
# rclone config encryption check

Check that the config file is encrypted

## Synopsis

This checks the config file is encrypted and that you can decrypt it.

It will attempt to decrypt the config using the password you supply.

If decryption fails it will return a non-zero exit code if using
`--password-command`, otherwise it will prompt again for the password.

If the config file is not encrypted it will return a non zero exit code.

```
rclone config encryption check [flags]
```

## Options

```
  -h, --help   help for check
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone config encryption](/commands/rclone_config_encryption/)	 - set, remove and check the encryption for the config file


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_config_encryption_check.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_config_encryption_check.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_config_encryption_check.md`
