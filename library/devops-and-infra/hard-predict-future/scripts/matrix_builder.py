"""
matrix_builder.py

Standalone matrix builder that populates the 6×3 STEEEP×Temporal grid.
Pure arithmetic. No AI calls. No web search.

Usage: python src/matrix_builder.py scored_signals.json
Output: matrix.json to stdout + writes file
"""

from __future__ import annotations
import os
import sys
# Ensure scripts directory is on path so signal_scorer can be imported from any CWD
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import json
from pathlib import Path
from typing import Dict, List

from signal_scorer import (
    Signal,
    ScoredSignal,
    Matrix,
    MatrixCell,
    STEEEP_CATEGORIES,
    TEMPORAL_LAYERS,
    build_steeep_matrix,
    score_signal,
)


def build_matrix(scored_signals: List[ScoredSignal]) -> Matrix:
    """
    Build the 6×3 STEEEP×Temporal matrix from scored signals.

    Direct wrapper around signal_scorer.build_steeep_matrix providing a
    clean entry point for the orchestrator without extra imports.

    Args:
        scored_signals: List of signals scored by signal_scorer.score_signal()

    Returns:
        Populated Matrix with 18 cells, hottest_cell, net_direction, blind_zones
    """
    return build_steeep_matrix(scored_signals)


def get_matrix_summary(matrix: Matrix) -> str:
    """
    Generate a human-readable ASCII table of the matrix.

    Args:
        matrix: Populated STEEEP matrix

    Returns:
        Formatted ASCII table string
    """
    col_width = 12
    header = f"{'':14}" + " | ".join(
        f"{t[:col_width]:{col_width}}" for t in TEMPORAL_LAYERS
    )
    sep = "-" * len(header)
    rows = [header, sep]

    for steeep in STEEEP_CATEGORIES:
        row_cells = []
        for temporal in TEMPORAL_LAYERS:
            key = f"{steeep}/{temporal}"
            cell = matrix.cells.get(key)
            val = f"{cell.score:6.2f}({cell.signal_count:2d})" if cell else "  0.00( 0)"
            row_cells.append(f"{val:{col_width}}")
        rows.append(f"{steeep[:14]:14}" + " | ".join(row_cells))

    rows += [
        sep,
        f"Hot zone : {matrix.hottest_cell}",
        f"Net      : {matrix.net_direction}",
        f"Blind    : {len(matrix.blind_zones)} zone(s)",
    ]
    return "\n".join(rows)


def get_dominant_zone(matrix: Matrix) -> Dict[str, object]:
    """
    Return metadata about the dominant (hottest) STEEEP×Temporal zone.

    Returns:
        Dict with hottest_cell, score, signal_count, blind_zones_count,
        and coverage_pct (% of 18 cells that have at least 1 signal)
    """
    key = matrix.hottest_cell
    cell = matrix.cells.get(key)
    covered = sum(1 for c in matrix.cells.values() if c.signal_count > 0)

    return {
        "hottest_cell":      key,
        "score":             cell.score if cell else 0.0,
        "signal_count":      cell.signal_count if cell else 0,
        "blind_zones_count": len(matrix.blind_zones),
        "coverage_pct":      int((covered / 18) * 100),
    }


# ─── CLI ENTRY POINT ─────────────────────────────────────────────────────────

def _matrix_to_dict(matrix: Matrix) -> dict:
    return {
        "matrix": {
            steeep: {
                temporal: round(matrix.cells[f"{steeep}/{temporal}"].score, 4)
                for temporal in TEMPORAL_LAYERS
            }
            for steeep in STEEEP_CATEGORIES
        },
        "hottest_cell": matrix.hottest_cell,
        "coldest_cell": min(matrix.cells, key=lambda k: matrix.cells[k].score),
        "blind_zones": matrix.blind_zones,
        "signal_counts": matrix.signal_counts,
        "net_direction": matrix.net_direction,
    }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: matrix_builder.py scored_signals.json"}, indent=2))
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(json.dumps({"error": f"File not found: {input_path}"}, indent=2))
        sys.exit(1)

    with open(input_path) as f:
        data = json.load(f)

    raw_scored = data.get("scored_signals", data) if isinstance(data, dict) else data

    # Reconstruct ScoredSignal objects from JSON
    scored_signals = []
    for item in raw_scored:
        s = Signal(
            content=item.get("content", ""),
            source=item.get("source", ""),
            date=item.get("date"),
            steeep_category=item.get("steeep_category"),
            temporal_layer=item.get("temporal_layer"),
            signal_type=item.get("signal_type"),
        )
        scored = score_signal(s)
        # Override with pre-computed values from JSON
        scored.steeep_category = item.get("steeep_category", scored.steeep_category)
        scored.temporal_layer = item.get("temporal_layer", scored.temporal_layer)
        scored.signal_type = item.get("signal_type", scored.signal_type)
        scored.final_score = item.get("final_score", scored.final_score)
        scored_signals.append(scored)

    matrix = build_steeep_matrix(scored_signals)
    result = _matrix_to_dict(matrix)

    out_path = Path(sys.argv[1]).parent / "matrix.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))
    sys.exit(0)


if __name__ == "__main__":
    main()
