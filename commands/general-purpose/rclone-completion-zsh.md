---
name: rclone-completion-zsh
description: "Output zsh completion script for rclone."
category: general-purpose
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_completion_zsh.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_completion_zsh.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_completion_zsh/](https://rclone.org/commands/rclone_completion_zsh/)
# rclone completion zsh

Output zsh completion script for rclone.

## Synopsis

Generates a zsh autocompletion script for rclone.

This writes to /usr/share/zsh/vendor-completions/_rclone by default so will
probably need to be run with sudo or as root, e.g.

```console
sudo rclone completion zsh
```

Logout and login again to use the autocompletion scripts, or source
them directly

```console
autoload -U compinit && compinit
```

If you supply a command line argument the script will be written
there.

If output_file is "-", then the output will be written to stdout.

```
rclone completion zsh [output_file] [flags]
```

## Options

```
  -h, --help   help for zsh
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone completion](/commands/rclone_completion/)	 - Output completion script for a given shell.


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_completion_zsh.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_completion_zsh.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_completion_zsh.md`
