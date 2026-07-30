#!/usr/bin/env python3
"""
market-size/scripts/market_formatter.py
Reads market_output.json and prints the formatted market sizing report.
"""

import json
import sys
import os


def fmt_usd(val) -> str:
    if not val or val == 0:
        return "N/A"
    v = float(val)
    if v >= 1_000_000_000:
        return f"${v/1_000_000_000:.1f}B"
    if v >= 1_000_000:
        return f"${v/1_000_000:.0f}M"
    return f"${v/1_000:.0f}K"


def check_icon(status: str) -> str:
    return {"PASS": "✅", "WATCH": "⚠️ ", "FAIL": "❌"}.get(status, "  ")


def main():
    script_dir  = os.path.dirname(os.path.abspath(__file__))
    output_dir  = os.path.join(script_dir, "..", "output")
    output_path = os.path.join(output_dir, "market_output.json")

    if not os.path.exists(output_path):
        print("ERROR: market_output.json not found. Run tam_calculator.py first.", file=sys.stderr)
        sys.exit(1)

    with open(output_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    sep = "━" * 54
    td  = data.get("top_down", {})
    bu  = data.get("bottom_up", {})
    con = data.get("consensus", {})

    lines = [
        "",
        sep,
        f"MARKET SIZE  ·  {data.get('company', 'Unknown')}  ·  {data.get('market', '')}  ·  {data.get('geography', '')}",
        sep,
        "",
        "MARKET SIZING — CONSENSUS",
        f"  TAM   {fmt_usd(con.get('tam_low'))} – {fmt_usd(con.get('tam_high'))}",
        f"  SAM   {fmt_usd(con.get('sam_low'))} – {fmt_usd(con.get('sam_high'))}",
        f"  SOM   {fmt_usd(con.get('som_low'))} – {fmt_usd(con.get('som_high'))}",
        "",
        "TOP-DOWN METHOD",
        f"  TAM   {fmt_usd(td.get('tam'))}  (Source: {td.get('source', 'N/A')})",
        f"  SAM   {fmt_usd(td.get('sam'))}  ({int(td.get('addressable_fraction', 0)*100) if 'addressable_fraction' in td else ''}% of TAM)",
        f"  SOM   {fmt_usd(td.get('som'))}",
        f"  CAGR  {td.get('cagr_pct', 0):.1f}%  →  TAM in 5yr: {fmt_usd(td.get('tam_5yr'))}",
        "",
        "BOTTOM-UP METHOD",
        f"  Total Potential Customers   {bu.get('total_potential_customers', 0):,}",
        f"  Addressable Customers       {bu.get('addressable_customers', 0):,}",
        f"  Obtainable Customers (3yr)  {bu.get('obtainable_customers', 0):,}",
        f"  ARPU (annual)               {fmt_usd(bu.get('arpu_annual', 0))}",
        f"  TAM   {fmt_usd(bu.get('tam'))}",
        f"  SAM   {fmt_usd(bu.get('sam'))}",
        f"  SOM   {fmt_usd(bu.get('som'))}",
        "",
        sep,
        "VC RULE CHECKS",
        sep,
    ]

    for check in data.get("vc_checks", []):
        lines.append(f"  {check_icon(check['status'])}  {check['msg']}")

    competitors = data.get("competitors", [])
    if competitors:
        lines += ["", sep, "COMPETITIVE LANDSCAPE", sep]
        for c in competitors:
            funding = fmt_usd(c.get("funding_total_usd", 0))
            arr     = fmt_usd(c.get("estimated_arr_usd", 0))
            yr      = c.get("founded_year", "")
            diff    = c.get("differentiation", "")
            lines.append(f"  {c.get('name', 'Unknown'):<22}  Founded {yr}  Funding {funding}  Est ARR {arr}")
            if diff:
                lines.append(f"  {'':22}  {diff}")

    lines += [
        "",
        sep,
        "Audit files: market_inputs.json · market_output.json",
        sep,
        "",
    ]

    print("\n".join(lines))


if __name__ == "__main__":
    main()
