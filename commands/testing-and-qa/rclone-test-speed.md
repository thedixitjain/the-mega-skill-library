---
name: rclone-test-speed
description: "Run a speed test to the remote"
category: testing-and-qa
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_test_speed.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_test_speed.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_test_speed/](https://rclone.org/commands/rclone_test_speed/)
# rclone test speed

Run a speed test to the remote

## Synopsis

Run a speed test to the remote.

This command runs a series of uploads and downloads to the remote, measuring
and printing the speed of each test using varying file sizes and numbers of
files.

Test time can be innaccurate with small file caps and large files. As it
uses the results of an initial test to determine how many files to use in
each subsequent test.

It is recommended to use -q flag for a simpler output. e.g.:

    rclone test speed remote: -q

**NB** This command will create and delete files on the remote in a randomly
named directory which will be automatically removed on a clean exit.

You can use the --json flag to only print the results in JSON format.

```
rclone test speed <remote> [flags]
```

## Options

```
      --ascii                Fill files with random ASCII printable bytes only
      --chargen              Fill files with a ASCII chargen pattern
      --file-cap int         Maximum number of files to use in each test (default 100)
  -h, --help                 help for speed
      --json                 Output only results in JSON format
      --large SizeSuffix     Size of large files (default 1Gi)
      --medium SizeSuffix    Size of medium files (default 10Mi)
      --pattern              Fill files with a periodic pattern
      --seed int             Seed for the random number generator (0 for random) (default 1)
      --small SizeSuffix     Size of small files (default 1Ki)
      --sparse               Make the files sparse (appear to be filled with ASCII 0x00)
      --test-time Duration   Length for each test to run (default 15s)
      --zero                 Fill files with ASCII 0x00
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone test](/commands/rclone_test/)	 - Run a test command


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_test_speed.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_test_speed.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_test_speed.md`
