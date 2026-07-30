---
name: rclone-cryptdecode
description: "Cryptdecode returns unencrypted file names."
category: general-purpose
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_cryptdecode.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_cryptdecode.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_cryptdecode/](https://rclone.org/commands/rclone_cryptdecode/)
# rclone cryptdecode

Cryptdecode returns unencrypted file names.

## Synopsis

Returns unencrypted file names when provided with a list of encrypted file
names. List limit is 10 items.

If you supply the `--reverse` flag, it will return encrypted file names.

use it like this

```console
rclone cryptdecode encryptedremote: encryptedfilename1 encryptedfilename2
rclone cryptdecode --reverse encryptedremote: filename1 filename2
```

Another way to accomplish this is by using the `rclone backend encode` (or `decode`)
command. See the documentation on the [crypt](/crypt/) overlay for more info.

```
rclone cryptdecode encryptedremote: encryptedfilename [flags]
```

## Options

```
  -h, --help      help for cryptdecode
      --reverse   Reverse cryptdecode, encrypts filenames
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone](/commands/rclone/)	 - Show help for rclone commands, flags and backends.


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_cryptdecode.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_cryptdecode.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_cryptdecode.md`
