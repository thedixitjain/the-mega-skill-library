---
name: rclone-archive-list
description: "List archive contents from source."
category: general-purpose
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_archive_list.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_archive_list.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_archive_list/](https://rclone.org/commands/rclone_archive_list/)
# rclone archive list

List archive contents from source.

## Synopsis


List the contents of an archive to the console, auto detecting the
format. See [rclone archive create](/commands/rclone_archive_create/)
for the archive formats supported.

For example:

```
$ rclone archive list remote:archive.zip
        6 file.txt
        0 dir/
        4 dir/bye.txt
```

Or with `--long` flag for more info:

```
$ rclone archive list --long remote:archive.zip
        6 2025-10-30 09:46:23.000000000 file.txt
        0 2025-10-30 09:46:57.000000000 dir/
        4 2025-10-30 09:46:57.000000000 dir/bye.txt
```

Or with `--plain` flag which is useful for scripting:

```
$ rclone archive list --plain /path/to/archive.zip
file.txt
dir/
dir/bye.txt
```

Or with `--dirs-only`:

```
$ rclone archive list --plain --dirs-only /path/to/archive.zip
dir/
```

Or with `--files-only`:

```
$ rclone archive list --plain --files-only /path/to/archive.zip
file.txt
dir/bye.txt
```

Filters may also be used:

```
$ rclone archive list --long archive.zip --include "bye.*"
        4 2025-10-30 09:46:57.000000000 dir/bye.txt
```

The [archive backend](/archive/) can also be used to list files. It
can be used to read only mount archives also but it supports a
different set of archive formats to the archive commands.


```
rclone archive list [flags] <source>
```

## Options

```
      --dirs-only    Only list directories
      --files-only   Only list files
  -h, --help         help for list
      --long         List extra attributtes
      --plain        Only list file names
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone archive](/commands/rclone_archive/)	 - Perform an action on an archive.


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_archive_list.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_archive_list.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_archive_list.md`
