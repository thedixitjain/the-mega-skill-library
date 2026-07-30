#!/usr/bin/env python3
"""
cap-table-waterfall/scripts/waterfall_formatter.py
Reads captable_output.json + waterfall_output.json, prints final report.
"""

import json
import sys
import os


def fmt_usd(val) -> str:
    if val is None or val == 0:
        return "$0"
    v = float(val)
    if abs(v) >= 1_000_000:
        return f"${v/1_000_000:.1f}M"
    if abs(v) >= 1_000:
        return f"${v/1_000:.0f}K"
    return f"${v:.0f}"


def main():
    script_dir  = os.path.dirname(os.path.abspath(__file__))
    output_dir  = os.path.join(script_dir, "..", "output")
    ct_path     = os.path.join(output_dir, "captable_output.json")
    wf_path     = os.path.join(output_dir, "waterfall_output.json")

    if not os.path.exists(ct_path):
        print("ERROR: captable_output.json not found.", file=sys.stderr)
        sys.exit(1)

    with open(ct_path, "r", encoding="utf-8") as f:
        ct = json.load(f)

    wf = {}
    if os.path.exists(wf_path):
        with open(wf_path, "r", encoding="utf-8") as f:
            wf = json.load(f)

    sep = "━" * 54

    lines = [
        "",
        sep,
        f"CAP TABLE  ·  {ct.get('company', 'Unknown')}",
        sep,
        "",
        f"  Pre-Round Shares:   {ct.get('pre_round_shares', 0):>12,}",
        f"  Post-Round Shares:  {ct.get('post_round_shares', 0):>12,}",
        f"  Round Price/Share:  {fmt_usd(ct.get('round_price_per_share', 0)):>12}",
        f"  Post-Money Val:     {fmt_usd(ct.get('post_money_valuation', 0)):>12}",
        "",
    ]

    # Cap table
    lines += [sep, "OWNERSHIP TABLE", sep]
    lines.append(f"  {'Stakeholder':<22}  {'Shares':>10}  {'Pre %':>7}  {'Post %':>7}  {'Dilution':>8}")
    lines.append(f"  {'─'*22}  {'─'*10}  {'─'*7}  {'─'*7}  {'─'*8}")

    for h in ct.get("post_ownership", []):
        dilution = h.get("dilution", 0)
        dil_str  = f"-{dilution:.1f}%" if dilution > 0 else ("—" if dilution == 0 else f"+{abs(dilution):.1f}%")
        lines.append(
            f"  {h['name']:<22}  {h['shares']:>10,}  {h.get('pre_pct', 0):>6.1f}%  {h.get('post_pct', 0):>6.1f}%  {dil_str:>8}"
        )

    # SAFE conversions
    safe_results = ct.get("safe_conversions", [])
    if safe_results:
        lines += ["", sep, "SAFE CONVERSIONS", sep]
        for r in safe_results:
            lines += [
                f"  Investor:         {r.get('investor', '')}",
                f"  Principal:        {fmt_usd(r.get('principal', 0))}",
                f"  Valuation Cap:    {fmt_usd(r.get('valuation_cap', 0))}",
                f"  Conversion Price: {fmt_usd(r.get('conversion_price', 0))} per share ({r.get('conversion_method', '')})",
                f"  Shares Issued:    {r.get('shares_issued', 0):,}",
                "",
            ]

    # Waterfall scenarios
    scenarios = wf.get("scenarios", [])
    if scenarios:
        lines += [sep, "EXIT WATERFALL SCENARIOS", sep]
        holders = [h["name"] for h in ct.get("post_ownership", []) if h.get("shares", 0) > 0]

        # Header row
        header = f"  {'Stakeholder':<22}"
        for s in scenarios:
            header += f"  {s['label']:>12}"
        lines.append(header)
        lines.append(f"  {'─'*22}" + "  " + "  ".join(["─"*12]*len(scenarios)))

        for name in holders:
            row = f"  {name:<22}"
            for s in scenarios:
                val = s.get("proceeds", {}).get(name, 0)
                row += f"  {fmt_usd(val):>12}"
            lines.append(row)

        # Exit prices
        lines.append("")
        price_row = f"  {'Exit Price':<22}"
        for s in scenarios:
            price_row += f"  {fmt_usd(s.get('exit_price', 0)):>12}"
        lines.append(price_row)

    lines += [
        "",
        sep,
        "Audit files: captable_inputs.json · captable_output.json · waterfall_output.json",
        sep,
        "",
    ]

    print("\n".join(lines))


if __name__ == "__main__":
    main()
