---
name: rclone-test-info
description: "Discovers file name or other limitations for paths."
category: testing-and-qa
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_test_info.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_test_info.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_test_info/](https://rclone.org/commands/rclone_test_info/)
# rclone test info

Discovers file name or other limitations for paths.

## Synopsis

Discovers what filenames and upload methods are possible to write to the
paths passed in and how long they can be.  It can take some time.  It will
write test files into the remote:path passed in.  It outputs a bit of go
code for each one.

**NB** this can create undeletable files and other hazards - use with care!

```
rclone test info [remote:path]+ [flags]
```

## Options

```
      --all                    Run all tests
      --check-base32768        Check can store all possible base32768 characters
      --check-control          Check control characters
      --check-length           Check max filename length
      --check-normalization    Check UTF-8 Normalization
      --check-streaming        Check uploads with indeterminate file size
  -h, --help                   help for info
      --keep-test-files        Keep test files after execution
      --upload-wait Duration   Wait after writing a file (default 0s)
      --write-json string      Write results to file
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone test](/commands/rclone_test/)	 - Run a test command


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_test_info.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_test_info.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_test_info.md`
