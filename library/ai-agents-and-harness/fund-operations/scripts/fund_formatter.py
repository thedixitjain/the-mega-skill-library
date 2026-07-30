#!/usr/bin/env python3
"""
fund-operations/scripts/fund_formatter.py
Reads fund_output.json and prints the formatted fund performance report.
"""

import json
import sys
import os


def fmt_usd(val) -> str:
    if val is None:
        return "N/A"
    v = float(val)
    if abs(v) >= 1_000_000_000:
        return f"${v/1_000_000_000:.2f}B"
    if abs(v) >= 1_000_000:
        return f"${v/1_000_000:.1f}M"
    if abs(v) >= 1_000:
        return f"${v/1_000:.0f}K"
    return f"${v:.0f}"


def moic_label(moic: float) -> str:
    if moic >= 5:   return "🔥"
    if moic >= 3:   return "⭐"
    if moic >= 1.5: return "✅"
    if moic >= 1:   return "─"
    return "🔴"


def main():
    script_dir  = os.path.dirname(os.path.abspath(__file__))
    output_dir  = os.path.join(script_dir, "..", "output")
    output_path = os.path.join(output_dir, "fund_output.json")

    if not os.path.exists(output_path):
        print("ERROR: fund_output.json not found. Run fund_kpi_calc.py first.", file=sys.stderr)
        sys.exit(1)

    with open(output_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    sep   = "━" * 54
    kpis  = data.get("kpis", {})
    carry = data.get("carry", {})

    lines = [
        "",
        sep,
        f"FUND REPORT  ·  {data.get('fund_name', 'Fund')}  ·  Vintage {data.get('vintage_year')}  ·  Age {data.get('fund_age_years')} yrs",
        sep,
        "",
        "FUND SNAPSHOT",
        f"  Committed Capital:    {fmt_usd(data.get('committed_capital'))}",
        f"  Total Invested:       {fmt_usd(data.get('total_invested'))}",
        f"  Unrealized FMV:       {fmt_usd(data.get('total_fmv'))}",
        f"  Total Realized:       {fmt_usd(data.get('total_realized'))}",
        f"  Total Value:          {fmt_usd(data.get('total_value'))}",
        f"  Investments:          {data.get('num_investments')} ({data.get('num_active')} active, {data.get('num_exited')} exited)",
        "",
        sep,
        "FUND KPIs",
        sep,
        f"  TVPI (Total Value Multiple)   {kpis.get('tvpi', 0):.2f}×",
        f"  DPI  (Distributions/Paid-In)  {kpis.get('dpi', 0):.2f}×",
        f"  RVPI (Residual Value)         {kpis.get('rvpi', 0):.2f}×",
        f"  IRR  (Annualized Return)      {kpis.get('irr_pct', 0):.1f}%",
        "",
        f"  J-Curve Position: {data.get('j_curve', '')}",
        "",
        sep,
        "FUND ECONOMICS",
        sep,
        f"  Management Fees (to date):    {fmt_usd(data.get('management_fee_total'))}",
        f"  Total Invested (net of fees): {fmt_usd(data.get('total_invested'))}",
        f"  Preferred Return to LPs:      {fmt_usd(carry.get('preferred_return'))}",
        f"  Profits Above Hurdle:         {fmt_usd(carry.get('profits_above_hurdle'))}",
        f"  Carry Earned (GP):            {fmt_usd(carry.get('carry_earned'))}  ({int(carry.get('carry_pct', 0.20)*100)}%)",
        f"  LP Total Proceeds:            {fmt_usd(carry.get('lp_total_proceeds'))}",
        "",
        sep,
        "PORTFOLIO COMPANIES (ranked by MOIC)",
        sep,
        f"  {'Company':<20}  {'Invested':>10}  {'FMV':>10}  {'Realized':>10}  {'MOIC':>7}  {'Status':<8}",
        f"  {'─'*20}  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*7}  {'─'*8}",
    ]

    for c in data.get("company_metrics", []):
        icon   = moic_label(c.get("moic", 0))
        status = c.get("status", "").capitalize()
        lines.append(
            f"  {c['company']:<20}  {fmt_usd(c['invested']):>10}  {fmt_usd(c['current_fmv']):>10}"
            f"  {fmt_usd(c['realized']):>10}  {c['moic']:>5.2f}×  {icon} {status}"
        )

    lines += [
        "",
        sep,
        "Audit files: fund_inputs.json · fund_output.json",
        sep,
        "",
    ]

    print("\n".join(lines))


if __name__ == "__main__":
    main()
