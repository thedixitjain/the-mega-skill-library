---
name: rclone-rmdirs
description: "Remove empty directories under the path."
category: general-purpose
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_rmdirs.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_rmdirs.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_rmdirs/](https://rclone.org/commands/rclone_rmdirs/)
# rclone rmdirs

Remove empty directories under the path.

## Synopsis

This recursively removes any empty directories (including directories
that only contain empty directories), that it finds under the path.
The root path itself will also be removed if it is empty, unless
you supply the `--leave-root` flag.

Use command [rmdir](/commands/rclone_rmdir/) to delete just the empty
directory given by path, not recurse.

This is useful for tidying up remotes that rclone has left a lot of
empty directories in. For example the [delete](/commands/rclone_delete/)
command will delete files but leave the directory structure (unless
used with option `--rmdirs`).

This will delete `--checkers` directories concurrently so
if you have thousands of empty directories consider increasing this number.

To delete a path and any objects in it, use the [purge](/commands/rclone_purge/)
command.

```
rclone rmdirs remote:path [flags]
```

## Options

```
  -h, --help         help for rmdirs
      --leave-root   Do not remove root directory if empty
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

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_rmdirs.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_rmdirs.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_rmdirs.md`
