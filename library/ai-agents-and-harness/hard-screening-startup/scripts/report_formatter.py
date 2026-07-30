#!/usr/bin/env python3
"""
hard-screening-startup/scripts/report_formatter.py
Reads verdict_output.json and prints the final formatted terminal report.
"""

import json
import sys
import os


def bar(score: int, width: int = 10) -> str:
    score = max(0, min(10, score))
    return "█" * score + "░" * (width - score)


def verdict_color_label(verdict: str) -> str:
    labels = {
        "PASS":             "✅ PASS",
        "CONDITIONAL PASS": "⚠️  CONDITIONAL PASS",
        "DECLINE":          "❌ DECLINE",
    }
    return labels.get(verdict, verdict)


def lens_label(value: str, lens_type: str = "invest") -> str:
    if lens_type == "risk":
        labels = {"MANAGEABLE": "✅ MANAGEABLE", "ELEVATED": "⚠️  ELEVATED", "CRITICAL": "❌ CRITICAL"}
    else:
        labels = {"PASS": "✅ PASS", "WATCH": "⚠️  WATCH", "FAIL": "❌ FAIL"}
    return labels.get(value, value)


def main():
    script_dir  = os.path.dirname(os.path.abspath(__file__))
    output_dir  = os.path.join(script_dir, "..", "output")
    output_path = os.path.join(output_dir, "verdict_output.json")

    if not os.path.exists(output_path):
        print("ERROR: verdict_output.json not found. Run verdict_calc.py first.", file=sys.stderr)
        sys.exit(1)

    with open(output_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    sep = "━" * 54

    lines = [
        "",
        sep,
        f"STARTUP SCREEN  ·  {data['company']}  ·  {data['stage']}  ·  {data['sector']}",
        sep,
        "",
        "DIMENSION SCORES",
    ]

    dim_labels = {
        "team":           "Team           ",
        "market":         "Market         ",
        "product":        "Product        ",
        "traction":       "Traction       ",
        "business_model": "Business Model ",
        "competition":    "Competition    ",
        "financials":     "Financials     ",
        "risk_profile":   "Risk Profile   ",
    }

    dim_scores = data.get("dimension_scores", {})
    for dim, label in dim_labels.items():
        d = dim_scores.get(dim, {})
        score     = d.get("score", 0)
        rationale = d.get("rationale", "")
        b         = bar(score)
        lines.append(f"  {label}  {score:2}/10  [{b}]  {rationale}")

    ws = data.get("weighted_score", 0)
    lines += [
        "",
        f"  WEIGHTED SCORE   {ws:.1f}/10",
        "",
        "INVESTOR LENSES",
    ]

    lenses = data.get("investor_lenses", {})
    lines.append(f"  Sequoia         {lens_label(lenses.get('sequoia', ''))}")
    lines.append(f"  YC              {lens_label(lenses.get('yc', ''))}")
    lines.append(f"  Tiger Global    {lens_label(lenses.get('tiger_global', ''))}")
    lines.append(f"  Risk Mgmt       {lens_label(lenses.get('risk_mgmt', ''), 'risk')}")

    lines += [
        "",
        sep,
        f"VERDICT:  {verdict_color_label(data.get('verdict', ''))}",
        sep,
    ]

    weak = data.get("weak_dims", [])
    if data.get("verdict") == "CONDITIONAL PASS" and weak:
        lines.append("")
        lines.append("  Conditions to address:")
        for w in weak:
            lines.append(f"  • Strengthen {w.replace('_', ' ').title()} dimension before committing capital")

    thesis = data.get("investment_thesis", "")
    if thesis:
        lines += ["", "INVESTMENT THESIS", thesis]

    why_now = data.get("why_now", "")
    if why_now:
        lines += ["", "WHY NOW", why_now]

    risks = data.get("key_risks", [])
    if risks:
        lines += ["", "KEY RISKS"]
        for i, r in enumerate(risks, 1):
            lines.append(f"  {i}. {r}")

    dd = data.get("dd_priorities", [])
    if dd:
        lines += ["", "DD PRIORITIES"]
        for i, d in enumerate(dd, 1):
            lines.append(f"  {i}. {d}")

    comps = data.get("comparables", [])
    if comps:
        lines += ["", "COMPARABLES"]
        for c in comps:
            lines.append(f"  · {c}")

    lines += [
        "",
        sep,
        "Audit files: company_profile.json · verdict_output.json",
        sep,
        "",
    ]

    print("\n".join(lines))


if __name__ == "__main__":
    main()
