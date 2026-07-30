#!/usr/bin/env python3
"""
hard-screening-startup/scripts/verdict_calc.py
Reads company_profile.json, computes weighted score, determines verdict.
Writes verdict_output.json.
"""

import json
import sys
import os

# Dimension weights (sum = 1.0)
WEIGHTS = {
    "team":           0.25,
    "market":         0.20,
    "product":        0.15,
    "traction":       0.15,
    "business_model": 0.10,
    "competition":    0.08,
    "financials":     0.05,
    "risk_profile":   0.02,
}

# Investor lens filters
SEQUOIA_KEY_DIMS  = ["market", "team", "product"]
YC_KEY_DIMS       = ["team", "traction"]
TIGER_KEY_DIMS    = ["traction", "business_model", "financials"]
RISK_KEY_DIMS     = ["risk_profile", "competition"]


def compute_weighted_score(scores: dict) -> float:
    total = 0.0
    for dim, weight in WEIGHTS.items():
        score = scores.get(dim, {}).get("score", 0)
        total += score * weight
    return round(total, 2)


def determine_verdict(weighted_score: float, scores: dict) -> dict:
    dimension_scores = {dim: scores.get(dim, {}).get("score", 0) for dim in WEIGHTS}
    min_score = min(dimension_scores.values())
    disqualifying_dims = [d for d, s in dimension_scores.items() if s <= 2]
    weak_dims = [d for d, s in dimension_scores.items() if s <= 3]

    if disqualifying_dims:
        verdict = "DECLINE"
        reason = f"Disqualifying score(s) on: {', '.join(disqualifying_dims)}"
    elif weighted_score >= 7.5 and min_score >= 4:
        verdict = "PASS"
        reason = "Strong across all dimensions"
    elif weighted_score >= 6.0 and min_score >= 3:
        verdict = "CONDITIONAL PASS"
        reason = f"Needs improvement on: {', '.join(weak_dims) if weak_dims else 'minor gaps'}"
    else:
        verdict = "DECLINE"
        reason = f"Weighted score {weighted_score} below threshold or weak dimensions: {', '.join(weak_dims)}"

    return {"verdict": verdict, "reason": reason, "disqualifying_dims": disqualifying_dims, "weak_dims": weak_dims}


def investor_lens_pass(scores: dict, key_dims: list, threshold: float = 6.5) -> str:
    avg = sum(scores.get(d, {}).get("score", 0) for d in key_dims) / len(key_dims)
    return "PASS" if avg >= threshold else ("WATCH" if avg >= 5.0 else "PASS")


def risk_lens(scores: dict) -> str:
    risk_score = scores.get("risk_profile", {}).get("score", 5)
    comp_score  = scores.get("competition", {}).get("score", 5)
    avg = (risk_score + comp_score) / 2
    if avg >= 7:   return "MANAGEABLE"
    if avg >= 5:   return "ELEVATED"
    return "CRITICAL"


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "..", "output")
    os.makedirs(output_dir, exist_ok=True)

    profile_path = os.path.join(output_dir, "company_profile.json")
    output_path  = os.path.join(output_dir, "verdict_output.json")

    if not os.path.exists(profile_path):
        print(f"ERROR: company_profile.json not found at {profile_path}", file=sys.stderr)
        sys.exit(1)

    with open(profile_path, "r", encoding="utf-8") as f:
        profile = json.load(f)

    scores = profile.get("scores", {})
    weighted_score = compute_weighted_score(scores)
    verdict_data   = determine_verdict(weighted_score, scores)

    # Investor lenses
    lenses = {
        "sequoia":     investor_lens_pass(scores, SEQUOIA_KEY_DIMS),
        "yc":          investor_lens_pass(scores, YC_KEY_DIMS),
        "tiger_global": investor_lens_pass(scores, TIGER_KEY_DIMS),
        "risk_mgmt":   risk_lens(scores),
    }

    # Dimension bar chart data
    bars = {}
    for dim in WEIGHTS:
        s = scores.get(dim, {}).get("score", 0)
        bars[dim] = "█" * s + "░" * (10 - s)

    output = {
        "company":        profile.get("company", "Unknown"),
        "sector":         profile.get("sector", "Unknown"),
        "stage":          profile.get("stage", "Unknown"),
        "weighted_score": weighted_score,
        "verdict":        verdict_data["verdict"],
        "verdict_reason": verdict_data["reason"],
        "weak_dims":      verdict_data["weak_dims"],
        "disqualifying":  verdict_data["disqualifying_dims"],
        "dimension_scores": {
            dim: {
                "score":    scores.get(dim, {}).get("score", 0),
                "bar":      bars[dim],
                "weight":   WEIGHTS[dim],
                "rationale": scores.get(dim, {}).get("rationale", ""),
            }
            for dim in WEIGHTS
        },
        "investor_lenses": lenses,
        "investment_thesis": profile.get("investment_thesis", ""),
        "why_now":           profile.get("why_now", ""),
        "key_risks":         profile.get("key_risks", []),
        "dd_priorities":     profile.get("dd_priorities", []),
        "comparables":       profile.get("comparables", []),
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"verdict_calc.py: weighted_score={weighted_score}, verdict={verdict_data['verdict']}")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
