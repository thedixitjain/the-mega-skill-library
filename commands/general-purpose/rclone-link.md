---
name: rclone-link
description: "Generate public link to file/folder."
category: general-purpose
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_link.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_link.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_link/](https://rclone.org/commands/rclone_link/)
# rclone link

Generate public link to file/folder.

## Synopsis

Create, retrieve or remove a public link to the given file or folder.

```console
rclone link remote:path/to/file
rclone link remote:path/to/folder/
rclone link --unlink remote:path/to/folder/
rclone link --expire 1d remote:path/to/file
```

If you supply the --expire flag, it will set the expiration time
otherwise it will use the default (100 years). **Note** not all
backends support the --expire flag - if the backend doesn't support it
then the link returned won't expire.

Use the --unlink flag to remove existing public links to the file or
folder. **Note** not all backends support "--unlink" flag - those that
don't will just ignore it.

If successful, the last line of the output will contain the
link. Exact capabilities depend on the remote, but the link will
always by default be created with the least constraints - e.g. no
expiry, no password protection, accessible without account.

```
rclone link remote:path [flags]
```

## Options

```
      --expire Duration   The amount of time that the link will be valid (default off)
  -h, --help              help for link
      --unlink            Remove existing public link to file/folder
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone](/commands/rclone/)	 - Show help for rclone commands, flags and backends.


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_link.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_link.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_link.md`
