---
name: rclone-completion-powershell
description: "Output powershell completion script for rclone."
category: general-purpose
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_completion_powershell.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_completion_powershell.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_completion_powershell/](https://rclone.org/commands/rclone_completion_powershell/)
# rclone completion powershell

Output powershell completion script for rclone.

## Synopsis

Generate the autocompletion script for powershell.

To load completions in your current shell session:

```console
rclone completion powershell | Out-File -Encoding utf8 "$HOME\Documents\PowerShell\rclone-completion.ps1"
```

Inspect the generated script, then dot-source it from your profile if you want completions
for every new session.
to your powershell profile.

If output_file is "-" or missing, then the output will be written to stdout.

```
rclone completion powershell [output_file] [flags]
```

## Options

```
  -h, --help   help for powershell
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone completion](/commands/rclone_completion/)	 - Output completion script for a given shell.


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_completion_powershell.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_completion_powershell.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_completion_powershell.md`
