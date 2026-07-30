---
name: rclone-test-makefile
description: "Make files with random contents of the size given"
category: testing-and-qa
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_test_makefile.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_test_makefile.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_test_makefile/](https://rclone.org/commands/rclone_test_makefile/)
# rclone test makefile

Make files with random contents of the size given

```
rclone test makefile <size> [<file>]+ [flags]
```

## Options

```
      --ascii      Fill files with random ASCII printable bytes only
      --chargen    Fill files with a ASCII chargen pattern
  -h, --help       help for makefile
      --pattern    Fill files with a periodic pattern
      --seed int   Seed for the random number generator (0 for random) (default 1)
      --sparse     Make the files sparse (appear to be filled with ASCII 0x00)
      --zero       Fill files with ASCII 0x00
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone test](/commands/rclone_test/)	 - Run a test command


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_test_makefile.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_test_makefile.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_test_makefile.md`
