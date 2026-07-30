#!/usr/bin/env python3
"""
deal-sourcing-signals/scripts/sourcing_formatter.py
Reads signal_output.json and prints the formatted sourcing brief report.
"""

import json
import sys
import os


def bar(score: float, width: int = 10) -> str:
    filled = int(round(score / 10))
    filled = max(0, min(width, filled))
    return "█" * filled + "░" * (width - filled)


def readiness_label(status: str) -> str:
    labels = {
        "MOVE FAST": "🚀 MOVE FAST",
        "ENGAGE":    "⚡ ENGAGE",
        "MONITOR":   "👁  MONITOR",
    }
    return labels.get(status, status)


def sentiment_icon(s: str) -> str:
    return {"POSITIVE": "▲", "NEGATIVE": "▼", "NEUTRAL": "─"}.get(s, "─")


def main():
    script_dir  = os.path.dirname(os.path.abspath(__file__))
    output_dir  = os.path.join(script_dir, "..", "output")
    output_path = os.path.join(output_dir, "signal_output.json")

    if not os.path.exists(output_path):
        print("ERROR: signal_output.json not found. Run signal_scorer.py first.", file=sys.stderr)
        sys.exit(1)

    with open(output_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    sep = "━" * 54

    lines = [
        "",
        sep,
        f"DEAL SIGNALS  ·  {data.get('company', 'Unknown')}  ·  {data.get('scan_date', '')}",
        sep,
        "",
        f"  Total Signals:   {data.get('total_signals', 0)}",
        f"  Positive:        {data.get('positive_signals', 0)}",
        f"  Negative:        {data.get('negative_signals', 0)}",
        "",
        "SIGNAL SCORES BY TYPE",
    ]

    scores = data.get("signal_scores", {})
    counts = data.get("signal_counts", {})
    types  = ["HIRING", "FUNDING", "PRODUCT", "TEAM", "MARKET", "TECH"]

    for t in types:
        score = scores.get(t, 0)
        count = counts.get(t, 0)
        b     = bar(score)
        lines.append(f"  {t:<10}  {score:>5.1f}/100  [{b}]  ({count} signal{'s' if count != 1 else ''})")

    overall   = data.get("overall_score", 0)
    readiness = readiness_label(data.get("investment_readiness", "MONITOR"))

    lines += [
        "",
        f"  OVERALL SCORE   {overall:.1f}/100",
        "",
        sep,
        f"  INVESTMENT READINESS:  {readiness}",
        sep,
        "",
        "TOP SIGNALS DETECTED",
    ]

    # Show top 3 strongest signals
    all_signals = []
    for t in types:
        for s in data.get("signals_by_type", {}).get(t, []):
            all_signals.append(s)

    top_signals = sorted(all_signals, key=lambda x: x.get("strength", 0), reverse=True)[:6]

    for s in top_signals:
        icon = sentiment_icon(s.get("sentiment", "NEUTRAL"))
        lines.append(f"  {icon} [{s.get('type', '')}] {s.get('description', '')}")
        if s.get("source"):
            lines.append(f"      Source: {s.get('source')}  ·  {s.get('date', '')}")

    lines += [
        "",
        sep,
        "Audit files: raw_signals.json · signal_output.json",
        sep,
        "",
    ]

    print("\n".join(lines))


if __name__ == "__main__":
    main()
