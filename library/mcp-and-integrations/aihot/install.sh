#!/usr/bin/env bash
# AI HOT Agent Skill installer.
# Downloads and validates the complete runtime package before one directory swap.

set -euo pipefail

SITE="https://aihot.virxact.com"
TARGET=""
INSTALL_DIR=""
MIGRATE_LEGACY=0
SHARED_TARGET=0
TMP_ROOT=""
TARGET_BACKUP=""
COMMITTED=0
LEGACY_PATHS=()
LEGACY_BACKUPS=()
LEGACY_COUNT=0

usage() {
  cat <<'EOF'
Usage:
  install.sh --target <claude|codex|gemini|copilot|opencode|agents> [--migrate-legacy]
  install.sh --dir <absolute-or-home-relative-path>

Targets:
  codex|gemini|copilot|opencode|agents  ~/.agents/skills/aihot
  claude                                ~/.claude/skills/aihot

Examples:
  bash install.sh --target codex
  bash install.sh --target agents --migrate-legacy
  bash install.sh --dir "$HOME/.agents/skills/aihot"

The installer never uses sudo. It downloads the complete runtime package,
validates every SHA-256, then replaces one explicit target directory.

If an older AI HOT Skill ran this script without a target, do not guess or
retry with sudo. Open https://aihot.virxact.com/aihot-skill/README.md and give
its recommended update prompt to the Agent that owns the current Skill folder.
EOF
}

fail() {
  echo "[ERR] $*" >&2
  exit 1
}

expand_home_path() {
  case "$1" in
    "~") printf '%s\n' "$HOME" ;;
    \~/*) printf '%s/%s\n' "$HOME" "${1#\~/}" ;;
    *) printf '%s\n' "$1" ;;
  esac
}

validate_target_path() {
  case "$INSTALL_DIR" in
    ""|"/"|"$HOME")
      fail "refusing unsafe install path: ${INSTALL_DIR:-<empty>}"
      ;;
  esac
  [[ "$INSTALL_DIR" = /* ]] || fail "--dir must be absolute or start with ~/"
  [[ "$(basename "$INSTALL_DIR")" == "aihot" ]] || {
    fail "Skill directory must be named aihot: $INSTALL_DIR"
  }
  [[ ! -f "$INSTALL_DIR" ]] || fail "target is a file, not a Skill directory: $INSTALL_DIR"
  [[ ! -L "$INSTALL_DIR" ]] || fail "target is a symlink; choose its real directory explicitly: $INSTALL_DIR"
  if [[ -d "$INSTALL_DIR" && -f "$INSTALL_DIR/SKILL.md" ]]; then
    skill_frontmatter_has_line "$INSTALL_DIR/SKILL.md" "name: aihot" || {
      fail "target contains a different Skill and will not be overwritten: $INSTALL_DIR"
    }
  elif [[ -d "$INSTALL_DIR" ]] && [[ -n "$(ls -A "$INSTALL_DIR")" ]]; then
    fail "target is a non-empty directory without an AI HOT SKILL.md: $INSTALL_DIR"
  fi
}

skill_frontmatter_has_line() {
  local file="$1"
  local expected="$2"
  awk -v expected="$expected" '
    NR == 1 {
      if ($0 != "---") exit 1
      next
    }
    $0 == "---" {
      closed = 1
      exit found ? 0 : 1
    }
    $0 == expected {
      found = 1
    }
    END {
      if (!closed) exit 1
    }
  ' "$file"
}

cleanup_committed_backup() {
  local backup="$1"
  if [[ -n "$backup" && -e "$backup" ]] && ! rm -rf -- "$backup"; then
    echo "[WARN] The new Skill is active, but an old backup remains at: $backup" >&2
    echo "[WARN] After confirming the Skill works, remove that backup manually." >&2
  fi
}

hash_file() {
  if command -v shasum >/dev/null 2>&1; then
    shasum -a 256 "$1" | awk '{print $1}'
  elif command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | awk '{print $1}'
  else
    fail "neither shasum nor sha256sum is available"
  fi
}

restore_on_failure() {
  local i
  if [[ "$COMMITTED" -eq 0 ]]; then
    if [[ -n "$TARGET_BACKUP" && -e "$TARGET_BACKUP" && ! -e "$INSTALL_DIR" ]]; then
      mv "$TARGET_BACKUP" "$INSTALL_DIR" || true
    fi
    for ((i = 0; i < LEGACY_COUNT; i++)); do
      if [[ -n "${LEGACY_BACKUPS[$i]:-}" && -e "${LEGACY_BACKUPS[$i]}" && ! -e "${LEGACY_PATHS[$i]}" ]]; then
        mv "${LEGACY_BACKUPS[$i]}" "${LEGACY_PATHS[$i]}" || true
      fi
    done
  fi
  if [[ -n "$TMP_ROOT" && -d "$TMP_ROOT" ]]; then
    rm -rf "$TMP_ROOT"
  fi
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      [[ $# -ge 2 ]] || { echo "[ERR] --target requires a value" >&2; exit 2; }
      [[ -z "$TARGET" && -z "$INSTALL_DIR" ]] || {
        echo "[ERR] choose exactly one --target or --dir" >&2
        exit 2
      }
      TARGET="$2"
      shift 2
      ;;
    --dir)
      [[ $# -ge 2 ]] || { echo "[ERR] --dir requires a value" >&2; exit 2; }
      [[ -z "$TARGET" && -z "$INSTALL_DIR" ]] || {
        echo "[ERR] choose exactly one --target or --dir" >&2
        exit 2
      }
      INSTALL_DIR="$(expand_home_path "$2")"
      TARGET="custom"
      shift 2
      ;;
    --migrate-legacy)
      MIGRATE_LEGACY=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "[ERR] unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ -z "$TARGET" ]]; then
  echo "[ERR] no target selected; the installer will not guess Claude or another Agent" >&2
  usage >&2
  exit 2
fi

case "$TARGET" in
  claude)
    INSTALL_DIR="$HOME/.claude/skills/aihot"
    [[ "$MIGRATE_LEGACY" -eq 0 ]] || {
      echo "[ERR] --migrate-legacy is only for the shared ~/.agents/skills target" >&2
      exit 2
    }
    ;;
  codex|gemini|copilot|opencode|agents)
    INSTALL_DIR="$HOME/.agents/skills/aihot"
    SHARED_TARGET=1
    ;;
  custom)
    [[ "$MIGRATE_LEGACY" -eq 0 ]] || {
      echo "[ERR] --migrate-legacy cannot be combined with --dir" >&2
      exit 2
    }
    ;;
  *)
    echo "[ERR] unsupported target: $TARGET" >&2
    usage >&2
    exit 2
    ;;
esac

INSTALL_DIR="$(expand_home_path "$INSTALL_DIR")"
validate_target_path

if [[ "$SHARED_TARGET" -eq 1 ]]; then
  LEGACY_CANDIDATES=(
    "${CODEX_HOME:-$HOME/.codex}/skills/aihot"
    "$HOME/.gemini/skills/aihot"
    "$HOME/.copilot/skills/aihot"
    "$HOME/.config/opencode/skills/aihot"
  )
  for legacy in "${LEGACY_CANDIDATES[@]}"; do
    [[ "$legacy" != "$INSTALL_DIR" ]] || continue
    if [[ -e "$legacy" || -L "$legacy" ]]; then
      [[ -d "$legacy" && ! -L "$legacy" && -f "$legacy/SKILL.md" ]] || {
        fail "legacy path is not a regular Skill directory: $legacy"
      }
      skill_frontmatter_has_line "$legacy/SKILL.md" "name: aihot" || {
        fail "legacy path contains a different Skill and will not be touched: $legacy"
      }
      LEGACY_PATHS[$LEGACY_COUNT]="$legacy"
      LEGACY_COUNT=$((LEGACY_COUNT + 1))
    fi
  done

  if [[ "$LEGACY_COUNT" -gt 0 && "$MIGRATE_LEGACY" -eq 0 ]]; then
    echo "[ERR] legacy AI HOT Skill copies found; refusing to create a duplicate:" >&2
    for ((i = 0; i < LEGACY_COUNT; i++)); do
      echo "  - ${LEGACY_PATHS[$i]}" >&2
    done
    echo "Re-run with --migrate-legacy to replace them with one shared copy," >&2
    echo "or use --dir <existing-path> to update one location explicitly." >&2
    exit 3
  fi
fi

INSTALL_PARENT="$(dirname "$INSTALL_DIR")"
mkdir -p "$INSTALL_PARENT"
TMP_ROOT="$(mktemp -d "$INSTALL_PARENT/.aihot-install.XXXXXX")"
PACKAGE_DIR="$TMP_ROOT/package"
MANIFEST_FILE="$TMP_ROOT/manifest.sha256"
mkdir -p "$PACKAGE_DIR"
trap restore_on_failure EXIT

echo ""
echo "Installing AI HOT Agent Skill"
echo "  target: $TARGET"
echo "  path:   $INSTALL_DIR"
echo ""

curl -fsSL --max-time 30 "$SITE/aihot-skill/manifest.sha256" -o "$MANIFEST_FILE"
[[ -s "$MANIFEST_FILE" ]] || fail "downloaded manifest is empty"

FILE_COUNT=0
SEEN_FILES=$'\n'
while IFS= read -r line || [[ -n "$line" ]]; do
  [[ "$line" =~ ^([0-9a-f]{64})[[:space:]][[:space:]]([A-Za-z0-9._/-]+)$ ]] || {
    fail "invalid manifest line"
  }
  expected_hash="${BASH_REMATCH[1]}"
  relative_path="${BASH_REMATCH[2]}"
  [[ "$relative_path" != /* && "$relative_path" != *".."* && "$relative_path" != *"//"* ]] || {
    fail "unsafe package path: $relative_path"
  }
  case "$relative_path" in
    SKILL.md|LICENSE|agents/openai.yaml|references/api.md|references/sync.md|references/errors.md) ;;
    *) fail "unexpected non-runtime package path: $relative_path" ;;
  esac
  [[ "$SEEN_FILES" != *$'\n'"$relative_path"$'\n'* ]] || fail "duplicate manifest path: $relative_path"
  SEEN_FILES+="$relative_path"$'\n'
  FILE_COUNT=$((FILE_COUNT + 1))
  [[ "$FILE_COUNT" -le 50 ]] || fail "manifest contains too many files"

  output_path="$PACKAGE_DIR/$relative_path"
  mkdir -p "$(dirname "$output_path")"
  curl -fsSL --max-time 30 "$SITE/aihot-skill/$relative_path" -o "$output_path"
  actual_hash="$(hash_file "$output_path")"
  [[ "$actual_hash" == "$expected_hash" ]] || {
    fail "SHA-256 mismatch for $relative_path; existing installation was not changed"
  }
  chmod 0644 "$output_path"
done < "$MANIFEST_FILE"

[[ "$FILE_COUNT" -eq 6 ]] || fail "runtime package must contain exactly 6 files"

for required in \
  SKILL.md \
  LICENSE \
  agents/openai.yaml \
  references/api.md \
  references/sync.md \
  references/errors.md
do
  [[ -f "$PACKAGE_DIR/$required" ]] || fail "runtime package is missing $required"
done

skill_frontmatter_has_line "$PACKAGE_DIR/SKILL.md" "name: aihot" || {
  fail "downloaded SKILL.md failed identity validation"
}
skill_frontmatter_has_line "$PACKAGE_DIR/SKILL.md" "license: MIT. See LICENSE" || {
  fail "downloaded SKILL.md failed license validation"
}
grep -q '^interface:$' "$PACKAGE_DIR/agents/openai.yaml" || {
  fail "downloaded agents/openai.yaml failed validation"
}
[[ ! -e "$PACKAGE_DIR/README.md" ]] || fail "README.md must not enter the runtime package"

for ((i = 0; i < LEGACY_COUNT; i++)); do
  legacy="${LEGACY_PATHS[$i]}"
  backup="$(dirname "$legacy")/.aihot-migrate.$$.${i}"
  [[ ! -e "$backup" ]] || fail "temporary migration path already exists: $backup"
  mv "$legacy" "$backup"
  LEGACY_BACKUPS[$i]="$backup"
done

if [[ -e "$INSTALL_DIR" ]]; then
  TARGET_BACKUP="$INSTALL_PARENT/.aihot-previous.$$"
  [[ ! -e "$TARGET_BACKUP" ]] || fail "temporary update path already exists: $TARGET_BACKUP"
  mv "$INSTALL_DIR" "$TARGET_BACKUP"
fi

if ! mv "$PACKAGE_DIR" "$INSTALL_DIR"; then
  fail "failed to activate the validated package"
fi
COMMITTED=1

cleanup_committed_backup "$TARGET_BACKUP"
for ((i = 0; i < LEGACY_COUNT; i++)); do
  cleanup_committed_backup "${LEGACY_BACKUPS[$i]}"
done

VERSION="$(sed -n 's/^  version: "\([0-9][0-9.]*\)"$/\1/p' "$INSTALL_DIR/SKILL.md" | head -n 1)"

echo "✓ Installed${VERSION:+ v$VERSION} as one complete package."
if [[ "$LEGACY_COUNT" -gt 0 ]]; then
  echo "✓ Replaced $LEGACY_COUNT legacy copy/copies with the shared installation."
fi
echo ""
echo "Next: restart your Agent or start a new conversation, then ask:"
echo "  过去 24 小时 AI 圈最重要的 5 件事是什么？"
echo ""
echo "Success means the Agent finds exactly one aihot Skill, states the time window,"
echo "and links titles to AI HOT."
