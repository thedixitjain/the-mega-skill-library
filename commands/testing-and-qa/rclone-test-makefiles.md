---
name: rclone-test-makefiles
description: "Make a random file hierarchy in a directory"
category: testing-and-qa
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_test_makefiles.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_test_makefiles.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_test_makefiles/](https://rclone.org/commands/rclone_test_makefiles/)
# rclone test makefiles

Make a random file hierarchy in a directory

```
rclone test makefiles <dir> [flags]
```

## Options

```
      --ascii                      Fill files with random ASCII printable bytes only
      --chargen                    Fill files with a ASCII chargen pattern
      --files int                  Number of files to create (default 1000)
      --files-per-directory int    Average number of files per directory (default 10)
      --flat                       If set create all files in the root directory
  -h, --help                       help for makefiles
      --max-depth int              Maximum depth of directory hierarchy (default 10)
      --max-file-size SizeSuffix   Maximum size of files to create (default 100)
      --max-name-length int        Maximum size of file names (default 12)
      --min-file-size SizeSuffix   Minimum size of file to create
      --min-name-length int        Minimum size of file names (default 4)
      --pattern                    Fill files with a periodic pattern
      --seed int                   Seed for the random number generator (0 for random) (default 1)
      --sparse                     Make the files sparse (appear to be filled with ASCII 0x00)
      --zero                       Fill files with ASCII 0x00
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone test](/commands/rclone_test/)	 - Run a test command


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_test_makefiles.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_test_makefiles.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_test_makefiles.md`
