---
name: bump-version
description: "Bump the project version following semantic versioning rules based on changes since last release."
category: engineering-core
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/release-manager/commands/bump-version.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/release-manager/commands/bump-version.md
---


Bump the project version following semantic versioning rules based on changes since last release.

## Steps


1. Find the current version:
2. Analyze changes since the last version:
3. Determine the version bump:
4. Update the version in all relevant files:
5. Update CHANGELOG.md with categorized changes.
6. Create a version commit: `chore: bump version to <new-version>`.
7. Create a git tag: `git tag v<new-version>`.

## Format


```
Previous Version: <X.Y.Z>
New Version: <X.Y.Z>
Bump Type: <major|minor|patch>
Changes: <feat: N, fix: N, breaking: N>
```


## Rules

- Follow semver strictly: breaking = major, feature = minor, fix = patch.
- Update ALL files that contain the version number.
- Never skip a version number.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/release-manager/commands/bump-version.md`
