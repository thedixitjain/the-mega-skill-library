---
name: rclone-completion-fish
description: "Output fish completion script for rclone."
category: general-purpose
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_completion_fish.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_completion_fish.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_completion_fish/](https://rclone.org/commands/rclone_completion_fish/)
# rclone completion fish

Output fish completion script for rclone.

## Synopsis

Generates a fish autocompletion script for rclone.

This writes to /etc/fish/completions/rclone.fish by default so will
probably need to be run with sudo or as root, e.g.

```console
sudo rclone completion fish
```

Logout and login again to use the autocompletion scripts, or source
them directly

```console
. /etc/fish/completions/rclone.fish
```

If you supply a command line argument the script will be written
there.

If output_file is "-", then the output will be written to stdout.

```
rclone completion fish [output_file] [flags]
```

## Options

```
  -h, --help   help for fish
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone completion](/commands/rclone_completion/)	 - Output completion script for a given shell.


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_completion_fish.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_completion_fish.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_completion_fish.md`
