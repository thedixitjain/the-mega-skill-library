#!/usr/bin/env python3
"""
decision_guidance.py - Compute strategic decision guidance.
Pure logic and arithmetic. No AI. No web calls.
Author: Santhosh Gandhi

Usage: python src/decision_guidance.py probabilities.json matrix.json scored_signals.json
Output: guidance.json to stdout + writes file
"""

from __future__ import annotations
import sys
import json
from pathlib import Path
from typing import Optional


def compute_recommended_stance(probable_pct: float, plausible_pct: float) -> str:
    """
    RECOMMENDED STANCE logic (deterministic).

    If probable_pct > 50: directional alignment
    Elif plausible_pct > 35: hedge between probable and plausible
    Else: maintain optionality
    """
    if probable_pct > 50:
        return "Align with probable scenario trajectory"
    elif plausible_pct > 35:
        return "Hedge between probable and plausible scenarios"
    else:
        return "Maintain optionality — signals too mixed for directional commitment"


def compute_low_regret_move(hottest_cell: str, net_direction: str) -> str:
    """
    LOW-REGRET MOVE logic.

    Find the action that appears beneficial across at least 2 of 3 probability-
    weighted scenarios. Based on the hottest matrix cell and net direction.
    """
    steeep_actions = {
        "Technological": "Invest in technology capability building and digital infrastructure",
        "Economic": "Diversify revenue streams and strengthen unit economics",
        "Political": "Build regulatory relationships and policy engagement capacity",
        "Social": "Strengthen community stakeholder relationships and workforce adaptation",
        "Environmental": "Integrate sustainability metrics into core operations",
        "Ethical": "Establish governance frameworks and compliance infrastructure",
    }

    steeep = hottest_cell.split("/")[0] if "/" in hottest_cell else "Technological"
    base_action = steeep_actions.get(steeep, steeep_actions["Technological"])

    if net_direction == "SUPPORTING":
        return f"{base_action} — signals favor accelerated commitment"
    elif net_direction == "OPPOSING":
        return f"{base_action} — while preserving exit optionality given opposing signals"
    else:
        return f"{base_action} — with staged commitments pending signal clarification"


def compute_risk_trigger(scored_signals: list) -> str:
    """
    RISK TRIGGER logic.

    Find the OPPOSING signal with highest final_score.
    That signal's content = the risk trigger to watch.
    """
    opposing_signals = [
        s for s in scored_signals
        if s.get("signal_type", "").upper() == "OPPOSING"
    ]

    if not opposing_signals:
        # Fallback: find the WILDCARD with highest score
        wildcards = [s for s in scored_signals if s.get("signal_type", "").upper() == "WILDCARD"]
        if wildcards:
            top = max(wildcards, key=lambda s: s.get("final_score", 0))
            content = top.get("content", "")
            return content[:120] + "..." if len(content) > 120 else content
        return "No significant opposing signals detected — monitor for emerging headwinds"

    top_opposing = max(opposing_signals, key=lambda s: s.get("final_score", 0))
    content = top_opposing.get("content", "")
    return content[:120] + "..." if len(content) > 120 else content


def compute_confidence_tier(confidence_score: int, signals_count: int,
                             probable_pct: float) -> str:
    """
    Confidence tier classification.

    HIGH = confidence_score > 70 AND probable_pct > 50
    MEDIUM = confidence_score 40-70 OR probable_pct 35-50
    LOW = confidence_score < 40 OR signals < 10
    """
    if confidence_score < 40 or signals_count < 10:
        return "LOW"
    if confidence_score > 70 and probable_pct > 50:
        return "HIGH"
    return "MEDIUM"


def compute_guidance(probabilities: dict, matrix: dict, scored_signals: list,
                     confidence_score: int = 50) -> dict:
    """
    Compute all three guidance outputs deterministically.

    Args:
        probabilities: Dict with probable_pct, plausible_pct, possible_pct
        matrix: Dict with hottest_cell, net_direction
        scored_signals: List of scored signal dicts
        confidence_score: Integer 0-100 from confidence_calc

    Returns:
        guidance dict with recommended_stance, low_regret_move, risk_trigger,
        dominant_matrix_zone, confidence_in_guidance
    """
    probable_pct = float(probabilities.get("probable_pct", 33.3))
    plausible_pct = float(probabilities.get("plausible_pct", 33.3))

    hottest_cell = matrix.get("hottest_cell", "Technological/Strategic")
    net_direction = matrix.get("net_direction", "NEUTRAL")

    stance = compute_recommended_stance(probable_pct, plausible_pct)
    move = compute_low_regret_move(hottest_cell, net_direction)
    trigger = compute_risk_trigger(scored_signals)

    signals_count = len(scored_signals)
    confidence_tier = compute_confidence_tier(confidence_score, signals_count, probable_pct)

    return {
        "recommended_stance": stance,
        "low_regret_move": move,
        "risk_trigger": trigger,
        "dominant_matrix_zone": hottest_cell,
        "confidence_in_guidance": confidence_tier,
    }


def main():
    if len(sys.argv) < 4:
        print(json.dumps({
            "error": "Usage: decision_guidance.py probabilities.json matrix.json scored_signals.json"
        }, indent=2))
        sys.exit(1)

    prob_path = Path(sys.argv[1])
    matrix_path = Path(sys.argv[2])
    signals_path = Path(sys.argv[3])

    for p in [prob_path, matrix_path, signals_path]:
        if not p.exists():
            print(json.dumps({"error": f"File not found: {p}"}, indent=2))
            sys.exit(1)

    with open(prob_path) as f:
        probabilities = json.load(f)
    with open(matrix_path) as f:
        matrix = json.load(f)
    with open(signals_path) as f:
        signals_data = json.load(f)

    scored_signals = (
        signals_data.get("scored_signals", signals_data)
        if isinstance(signals_data, dict)
        else signals_data
    )

    # Read confidence from probabilities if available
    confidence_score = int(probabilities.get("confidence", 50))

    result = compute_guidance(probabilities, matrix, scored_signals, confidence_score)

    out_path = Path(sys.argv[1]).parent / "guidance.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))
    sys.exit(0)


if __name__ == "__main__":
    main()
