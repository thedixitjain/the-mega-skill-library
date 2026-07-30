---
name: rclone-deletefile
description: "Remove a single file from remote."
category: general-purpose
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_deletefile.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_deletefile.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_deletefile/](https://rclone.org/commands/rclone_deletefile/)
# rclone deletefile

Remove a single file from remote.

## Synopsis

Remove a single file from remote.  Unlike `delete` it cannot be used to
remove a directory and it doesn't obey include/exclude filters - if the
specified file exists, it will always be removed.

```
rclone deletefile remote:path [flags]
```

## Options

```
  -h, --help   help for deletefile
```

Options shared with other commands are described next.
See the [global flags page](/flags/) for global options not listed here.

### Important Options

Important flags useful for most commands

```text
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)
```

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone](/commands/rclone/)	 - Show help for rclone commands, flags and backends.


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_deletefile.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_deletefile.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_deletefile.md`
