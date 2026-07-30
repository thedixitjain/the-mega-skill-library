"""
confidence_calc.py

Standalone confidence calculation module.
Pure arithmetic. No AI calls. No web search.

Formula:
  Signal density score   (0-40): total_signals / 25 × 40  (capped at 40)
  Evidence balance score (0-30): |supporting - opposing| / total × 30
  Historical grounding   (0-30): best_analogue_similarity / 100 × 30
  confidence = density + balance + grounding  ->  int, capped at 100

Usage: python src/confidence_calc.py scored_signals.json matrix.json analogues.json
Output: single integer to stdout
"""

from __future__ import annotations
import os
import sys
# Ensure scripts directory is on path so signal_scorer can be imported from any CWD
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import json
from pathlib import Path

from signal_scorer import Matrix


def calculate_confidence(
    matrix: Matrix,
    signal_counts: dict,
    analogue_similarity: float,
) -> int:
    """
    Calculate overall confidence as integer 0–100.

    Components
    ----------
    Signal density (0–40):
        Measures how much raw evidence was collected.
        25 signals = full density score (40 pts).
        Formula: min(40, total_signals / 25 × 40)

    Evidence balance (0–30):
        Measures clarity of directional consensus.
        Higher when one side (supporting/opposing) clearly dominates.
        Formula: |supporting − opposing| / total × 30

    Historical grounding (0–30):
        Measures quality of historical precedent found.
        100% similarity = 30 pts.
        Formula: best_analogue_similarity / 100 × 30

    Parameters
    ----------
    matrix:
        Populated STEEEP matrix (used for signal_counts cross-check).
    signal_counts:
        Dict with keys 'total', 'SUPPORTING', 'OPPOSING'.
    analogue_similarity:
        Best historical analogue similarity score (0–100).

    Returns
    -------
    int
        Confidence score in [0, 100].
    """
    total      = signal_counts.get("total", 0)
    supporting = signal_counts.get("SUPPORTING", 0)
    opposing   = signal_counts.get("OPPOSING",   0)

    # 1. Signal density (0–40)
    density = min(40.0, (total / 25.0) * 40.0)

    # 2. Evidence balance (0–30)
    if total > 0:
        balance = (abs(supporting - opposing) / total) * 30.0
    else:
        balance = 0.0

    # 3. Historical grounding (0–30)
    grounding = (max(0.0, min(100.0, analogue_similarity)) / 100.0) * 30.0

    # 4. Blind spot penalty (0–15): deduct for uncovered STEEEP×Temporal cells
    blind_count   = len(matrix.blind_zones) if hasattr(matrix, 'blind_zones') else 0
    blind_penalty = min(15.0, blind_count * (15.0 / 18.0))

    return min(100, max(0, int(round(density + balance + grounding - blind_penalty))))


# ─── CLI ENTRY POINT ─────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 4:
        print(json.dumps({
            "error": "Usage: confidence_calc.py scored_signals.json matrix.json analogues.json"
        }, indent=2))
        sys.exit(1)

    signals_path = Path(sys.argv[1])
    matrix_path = Path(sys.argv[2])
    analogues_path = Path(sys.argv[3])

    for p in [signals_path, matrix_path, analogues_path]:
        if not p.exists():
            print(json.dumps({"error": f"File not found: {p}"}, indent=2))
            sys.exit(1)

    with open(signals_path) as f:
        signals_data = json.load(f)
    with open(matrix_path) as f:
        matrix_data = json.load(f)
    with open(analogues_path) as f:
        analogues_data = json.load(f)

    raw_scored = (
        signals_data.get("scored_signals", signals_data)
        if isinstance(signals_data, dict) else signals_data
    )
    raw_analogues = (
        analogues_data if isinstance(analogues_data, list)
        else analogues_data.get("analogues", [])
    )

    # Build signal_counts from raw scored signals
    signal_counts = {"total": 0, "SUPPORTING": 0, "OPPOSING": 0, "NEUTRAL": 0, "WILDCARD": 0}
    for s in raw_scored:
        st = s.get("signal_type", "NEUTRAL").upper()
        signal_counts["total"] += 1
        if st in signal_counts:
            signal_counts[st] += 1

    # Best analogue similarity
    best_sim = 0.0
    for a in raw_analogues:
        sim = float(a.get("similarity", a.get("similarity_score", 0)))
        if sim > best_sim:
            best_sim = sim

    # Use a minimal Matrix placeholder (only signal_counts needed)
    from signal_scorer import STEEEP_CATEGORIES, TEMPORAL_LAYERS, MatrixCell, Matrix
    cells = {
        f"{s}/{t}": MatrixCell(steeep=s, temporal=t, score=0.0, signal_count=0)
        for s in STEEEP_CATEGORIES for t in TEMPORAL_LAYERS
    }
    # Populate from matrix_data if available
    for steeep, temporal_dict in matrix_data.get("matrix", {}).items():
        for temporal, score in temporal_dict.items():
            key = f"{steeep}/{temporal}"
            if key in cells:
                cells[key].score = score

    matrix = Matrix(
        cells=cells,
        hottest_cell=matrix_data.get("hottest_cell", "Technological/Strategic"),
        net_direction=matrix_data.get("net_direction", "NEUTRAL"),
        blind_zones=matrix_data.get("blind_zones", []),
        signal_counts=signal_counts,
    )

    score = calculate_confidence(matrix, signal_counts, best_sim)

    # Output single integer as per spec
    print(score)
    sys.exit(0)


if __name__ == "__main__":
    main()
