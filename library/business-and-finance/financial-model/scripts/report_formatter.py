#!/usr/bin/env python3
"""
financial-model/scripts/report_formatter.py
Reads model_output.json and prints the formatted financial report.
"""

import json
import sys
import os


def fmt_usd(val) -> str:
    if val == "N/A" or val is None:
        return "N/A"
    v = float(val)
    if abs(v) >= 1_000_000:
        return f"${v/1_000_000:.1f}M"
    if abs(v) >= 1_000:
        return f"${v/1_000:.0f}K"
    return f"${v:.0f}"


def health_icon(status: str) -> str:
    return {"HEALTHY": "✅", "WATCH": "⚠️ ", "CRITICAL": "❌"}.get(status, " ")


def main():
    script_dir  = os.path.dirname(os.path.abspath(__file__))
    output_dir  = os.path.join(script_dir, "..", "output")
    output_path = os.path.join(output_dir, "model_output.json")

    if not os.path.exists(output_path):
        print("ERROR: model_output.json not found. Run financial_calc.py first.", file=sys.stderr)
        sys.exit(1)

    with open(output_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    sep = "━" * 54
    sm  = data.get("saas_metrics", {})
    rm  = data.get("revenue_multiple", {})
    dcf = data.get("dcf", {})
    h   = sm.get("health", {})
    vr  = data.get("valuation_range", {})
    bm  = data.get("benchmarks", {})

    lines = [
        "",
        sep,
        f"FINANCIAL MODEL  ·  {data.get('company', 'Unknown')}  ·  {data.get('stage', '')}",
        sep,
        "",
        f"  ARR: {fmt_usd(data.get('arr', 0))}",
        "",
        "VALUATION RANGE",
        f"  Low:   {fmt_usd(vr.get('low', 0))}",
        f"  High:  {fmt_usd(vr.get('high', 0))}",
        "",
        "  DCF Intrinsic Value:     " + fmt_usd(dcf.get("dcf_value", 0)),
        f"  Revenue Multiple (low):  {fmt_usd(rm.get('implied_value_low', 0))}  ({rm.get('multiples', {}).get('low', 0)}× ARR)",
        f"  Revenue Multiple (mid):  {fmt_usd(rm.get('implied_value_mid', 0))}  ({rm.get('multiples', {}).get('mid', 0)}× ARR)",
        f"  Revenue Multiple (high): {fmt_usd(rm.get('implied_value_high', 0))}  ({rm.get('multiples', {}).get('high', 0)}× ARR)",
        "",
        sep,
        "SAAS HEALTH METRICS",
        sep,
        f"  {health_icon(h.get('ltv_cac'))}  LTV:CAC Ratio       {sm.get('ltv_cac_ratio', 'N/A')}×   (target: > 3×)",
        f"  {health_icon(h.get('payback'))}  CAC Payback         {sm.get('cac_payback_months', 'N/A')} months  (target: < 18 months)",
        f"  {health_icon(h.get('nrr'))}  Net Revenue Retention {sm.get('nrr_pct', 'N/A')}%   (target: > 100%)",
        f"  {health_icon(h.get('burn'))}  Burn Multiple       {sm.get('burn_multiple', 'N/A')}×   (target: < 2×)",
        f"     LTV                 {fmt_usd(sm.get('ltv', 0))}",
        f"     Cust. Lifetime      {sm.get('customer_lifetime_months', 'N/A')} months",
        f"     Runway              {sm.get('runway_months', 'N/A')} months",
        f"     Rule of 40 Score    {sm.get('rule_of_40', 'N/A')}",
        f"     ARR Growth (annual) {sm.get('arr_growth_annual_pct', 'N/A')}%",
        "",
    ]

    if bm:
        lines += [sep, "STAGE BENCHMARKS", sep]
        for k, v in bm.items():
            label = k.replace("_", " ").title().ljust(24)
            lines.append(f"  {label}  {v}")
        lines.append("")

    # DCF projection table
    revs = dcf.get("revenues", [])
    fcfs = dcf.get("fcfs", [])
    if revs:
        lines += [sep, "DCF PROJECTION", sep]
        lines.append(f"  {'Year':<6} {'Revenue':>12} {'FCF':>12}")
        lines.append(f"  {'────':<6} {'────────':>12} {'───':>12}")
        for i, (r, f) in enumerate(zip(revs, fcfs), start=1):
            lines.append(f"  Yr {i:<3} {fmt_usd(r):>12} {fmt_usd(f):>12}")
        lines += [
            f"  Terminal Value: {fmt_usd(dcf.get('terminal_value', 0))}",
            "",
        ]

    lines += [
        sep,
        "Audit files: model_inputs.json · model_output.json",
        sep,
        "",
    ]

    print("\n".join(lines))


if __name__ == "__main__":
    main()
