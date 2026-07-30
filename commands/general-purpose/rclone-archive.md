---
name: rclone-archive
description: "Perform an action on an archive."
category: general-purpose
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_archive.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_archive.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_archive/](https://rclone.org/commands/rclone_archive/)
# rclone archive

Perform an action on an archive.

## Synopsis

Perform an action on an archive. Requires the use of a
subcommand to specify the protocol, e.g.

    rclone archive list remote:file.zip

Each subcommand has its own options which you can see in their help.

See [rclone archive create](/commands/rclone_archive_create/) for the
archive formats supported.


```
rclone archive <action> [opts] <source> [<destination>] [flags]
```

## Options

```
  -h, --help   help for archive
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone](/commands/rclone/)	 - Show help for rclone commands, flags and backends.
* [rclone archive create](/commands/rclone_archive_create/)	 - Archive source file(s) to destination.
* [rclone archive extract](/commands/rclone_archive_extract/)	 - Extract archives from source to destination.
* [rclone archive list](/commands/rclone_archive_list/)	 - List archive contents from source.


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_archive.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_archive.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_archive.md`
