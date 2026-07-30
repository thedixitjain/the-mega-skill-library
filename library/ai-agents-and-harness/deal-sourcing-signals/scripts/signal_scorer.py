#!/usr/bin/env python3
"""
deal-sourcing-signals/scripts/signal_scorer.py
Reads raw_signals.json, scores by signal type, computes overall deal score.
Writes signal_output.json.
"""

import json
import sys
import os
import math
from collections import defaultdict

# Canonical signal types
SIGNAL_TYPES = ["HIRING", "FUNDING", "PRODUCT", "TEAM", "MARKET", "TECH"]

# Weights by signal type (sum = 1.0)
SIGNAL_WEIGHTS = {
    "HIRING":  0.25,
    "FUNDING": 0.25,
    "PRODUCT": 0.20,
    "TEAM":    0.15,
    "MARKET":  0.10,
    "TECH":    0.05,
}

# Sentiment multipliers
SENTIMENT_MULT = {"POSITIVE": 1.0, "NEUTRAL": 0.6, "NEGATIVE": 0.0}

# Alias normalization
_TYPE_ALIASES = {
    "hiring": "HIRING", "jobs": "HIRING", "headcount": "HIRING", "recruitment": "HIRING",
    "funding": "FUNDING", "investment": "FUNDING", "raise": "FUNDING", "round": "FUNDING",
    "product": "PRODUCT", "launch": "PRODUCT", "feature": "PRODUCT", "release": "PRODUCT",
    "team": "TEAM", "leadership": "TEAM", "executive": "TEAM", "founder": "TEAM",
    "market": "MARKET", "industry": "MARKET", "sector": "MARKET", "competitive": "MARKET",
    "tech": "TECH", "technology": "TECH", "stack": "TECH", "engineering": "TECH",
}

def normalize_type(raw: str) -> str:
    """Normalize signal type to canonical form."""
    if raw in SIGNAL_TYPES:
        return raw
    return _TYPE_ALIASES.get(raw.lower(), "MARKET")


def score_signal_type(signals_in_type: list) -> float:
    """Score 0–100 for a given signal type using exponential curve."""
    if not signals_in_type:
        return 0.0

    raw = sum(
        s.get("strength", 5) * SENTIMENT_MULT.get(s.get("sentiment", "NEUTRAL"), 0.6)
        for s in signals_in_type
    )
    n    = len(signals_in_type)
    # Exponential normalization: caps at 100
    score = (1.0 - math.exp(-raw / (n * 7))) * 100
    return min(100.0, max(0.0, round(score, 1)))


def investment_readiness(overall_score: float, signal_scores: dict) -> str:
    funding_score = signal_scores.get("FUNDING", 0)
    if overall_score >= 70 or funding_score >= 60:
        return "MOVE FAST"
    if overall_score >= 45:
        return "ENGAGE"
    return "MONITOR"


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "..", "output")
    os.makedirs(output_dir, exist_ok=True)

    raw_path    = os.path.join(output_dir, "raw_signals.json")
    output_path = os.path.join(output_dir, "signal_output.json")

    if not os.path.exists(raw_path):
        print(f"ERROR: raw_signals.json not found at {raw_path}", file=sys.stderr)
        sys.exit(1)

    with open(raw_path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    signals = raw.get("signals", [])

    # Normalize types and group
    grouped = defaultdict(list)
    for s in signals:
        t = normalize_type(s.get("type", "MARKET"))
        s["type"] = t
        grouped[t].append(s)

    # Score per type
    signal_scores = {t: score_signal_type(grouped.get(t, [])) for t in SIGNAL_TYPES}

    # Weighted overall
    overall = sum(signal_scores[t] * SIGNAL_WEIGHTS[t] for t in SIGNAL_TYPES)
    overall = round(overall, 1)

    readiness = investment_readiness(overall, signal_scores)

    # Signal counts
    counts = {t: len(grouped.get(t, [])) for t in SIGNAL_TYPES}
    positive_count = sum(1 for s in signals if s.get("sentiment") == "POSITIVE")
    negative_count = sum(1 for s in signals if s.get("sentiment") == "NEGATIVE")

    output = {
        "company":           raw.get("company", "Unknown"),
        "scan_date":         raw.get("scan_date", ""),
        "total_signals":     len(signals),
        "positive_signals":  positive_count,
        "negative_signals":  negative_count,
        "signal_counts":     counts,
        "signal_scores":     signal_scores,
        "overall_score":     overall,
        "investment_readiness": readiness,
        "signals_by_type":   {t: grouped.get(t, []) for t in SIGNAL_TYPES},
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"signal_scorer.py: overall_score={overall}, readiness={readiness}")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
