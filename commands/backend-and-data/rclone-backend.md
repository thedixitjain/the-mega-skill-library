---
name: rclone-backend
description: "Run a backend-specific command."
category: backend-and-data
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_backend.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_backend.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_backend/](https://rclone.org/commands/rclone_backend/)
# rclone backend

Run a backend-specific command.

## Synopsis

This runs a backend-specific command. The commands themselves (except
for "help" and "features") are defined by the backends and you should
see the backend docs for definitions.

You can discover what commands a backend implements by using

```console
rclone backend help remote:
rclone backend help <backendname>
```

You can also discover information about the backend using (see
[operations/fsinfo](/rc/#operations-fsinfo) in the remote control docs
for more info).

```console
rclone backend features remote:
```

Pass options to the backend command with -o. This should be key=value or key, e.g.:

```console
rclone backend stats remote:path stats -o format=json -o long
```

Pass arguments to the backend by placing them on the end of the line

```console
rclone backend cleanup remote:path file1 file2 file3
```

Note to run these commands on a running backend then see
[backend/command](/rc/#backend-command) in the rc docs.

```
rclone backend <command> remote:path [opts] <args> [flags]
```

## Options

```
  -h, --help                 help for backend
      --json                 Always output in JSON format
  -o, --option stringArray   Option in the form name=value or name
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

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_backend.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_backend.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_backend.md`
