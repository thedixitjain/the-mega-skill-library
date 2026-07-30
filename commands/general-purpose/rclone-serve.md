---
name: rclone-serve
description: "Serve a remote over a protocol."
category: general-purpose
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/rclone-cli/references/commands/rclone_serve.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/rclone-cli/references/commands/rclone_serve.md
---


> **Official documentation:** [https://rclone.org/commands/rclone_serve/](https://rclone.org/commands/rclone_serve/)
# rclone serve

Serve a remote over a protocol.

## Synopsis

Serve a remote over a given protocol. Requires the use of a
subcommand to specify the protocol, e.g.

```console
rclone serve http remote:
```

When the "--metadata" flag is enabled, the following metadata fields will be provided as headers:
- "content-disposition"
- "cache-control"
- "content-language"
- "content-encoding"
Note: The availability of these fields depends on whether the remote supports metadata.

Each subcommand has its own options which you can see in their help.


```
rclone serve <protocol> [opts] <remote> [flags]
```

## Options

```
  -h, --help   help for serve
```

See the [global flags page](/flags/) for global options not listed here.

## See Also

<!-- markdownlint-capture -->
<!-- markdownlint-disable ul-style line-length -->

* [rclone](/commands/rclone/)	 - Show help for rclone commands, flags and backends.
* [rclone serve dlna](/commands/rclone_serve_dlna/)	 - Serve remote:path over DLNA
* [rclone serve docker](/commands/rclone_serve_docker/)	 - Serve any remote on docker's volume plugin API.
* [rclone serve ftp](/commands/rclone_serve_ftp/)	 - Serve remote:path over FTP.
* [rclone serve http](/commands/rclone_serve_http/)	 - Serve the remote over HTTP.
* [rclone serve nfs](/commands/rclone_serve_nfs/)	 - Serve the remote as an NFS mount
* [rclone serve restic](/commands/rclone_serve_restic/)	 - Serve the remote for restic's REST API.
* [rclone serve s3](/commands/rclone_serve_s3/)	 - Serve remote:path over s3.
* [rclone serve sftp](/commands/rclone_serve_sftp/)	 - Serve the remote over SFTP.
* [rclone serve webdav](/commands/rclone_serve_webdav/)	 - Serve remote:path over WebDAV.


<!-- markdownlint-restore -->

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/rclone-cli/references/commands/rclone_serve.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/rclone-cli/references/commands/rclone_serve.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/rclone-cli/references/commands/rclone_serve.md`
