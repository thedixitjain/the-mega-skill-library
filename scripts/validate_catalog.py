#!/usr/bin/env python3
"""Fail CI if CATALOG.tsv references a path that doesn't exist on disk.

Plain tab-split, not the csv module: this file is raw TSV (no field
quoting/escaping), and descriptions routinely contain literal quote
characters that trip up csv's default quoting rules and silently merge
physical lines together.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "CATALOG.tsv"


def main() -> int:
    missing = []
    total = 0
    with CATALOG.open(encoding="utf-8") as f:
        header = f.readline().rstrip("\n").split("\t")
        path_col = header.index("path")
        for line_num, line in enumerate(f, start=2):
            fields = line.rstrip("\n").split("\t")
            if len(fields) <= path_col:
                missing.append((line_num, "<malformed row: too few columns>"))
                continue
            total += 1
            rel_path = fields[path_col]
            if not rel_path or not (ROOT / rel_path).is_file():
                missing.append((line_num, rel_path))

    print(f"Checked {total} catalog rows.")
    if missing:
        print(f"FAIL: {len(missing)} row(s) point at a missing file:")
        for ln, rel_path in missing[:50]:
            print(f"  line {ln}: {rel_path}")
        if len(missing) > 50:
            print(f"  ... and {len(missing) - 50} more")
        return 1

    print("OK: every catalog row resolves to a real file.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
