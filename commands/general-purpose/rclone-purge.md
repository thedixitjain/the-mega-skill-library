---
name: rclone-purge
description: "Remove the path and all of its contents."
category: general-purpose
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_purge.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_purge.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_purge/](https://rclone.org/commands/rclone_purge/)
# rclone purge

Remove the path and all of its contents.

## Synopsis

Remove the path and all of its contents.  Note that this does not obey
include/exclude filters - everything will be removed.  Use the
[delete](/commands/rclone_delete/) command if you want to selectively
delete files. To delete empty directories only, use command
[rmdir](/commands/rclone_rmdir/) or [rmdirs](/commands/rclone_rmdirs/).

The concurrency of this operation is controlled by the `--checkers` global flag.
However, some backends will implement this command directly, in which
case `--checkers` will be ignored.

**Important**: Since this can cause data loss, test first with the
`--dry-run` or the `--interactive`/`-i` flag.

```
rclone purge remote:path [flags]
```

## Options

```
  -h, --help   help for purge
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

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_purge.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_purge.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_purge.md`
