#!/usr/bin/env python3
"""
fund-operations/scripts/fund_kpi_calc.py
Reads fund_inputs.json, computes TVPI/DPI/RVPI/IRR/MOIC and carried interest.
Writes fund_output.json.
"""

import json
import sys
import os
import math
from datetime import datetime


def xirr(cash_flows: list, dates: list, guess: float = 0.10) -> float:
    """
    Compute IRR using Newton-Raphson method.
    cash_flows: list of floats (negative = outflow, positive = inflow)
    dates: list of datetime objects
    Returns annualized IRR as decimal.
    """
    if not cash_flows or len(cash_flows) != len(dates):
        return 0.0

    # Normalize dates to year fractions from first date
    t0 = dates[0]
    t  = [(d - t0).days / 365.25 for d in dates]

    def npv(rate):
        return sum(cf / (1 + rate) ** ti for cf, ti in zip(cash_flows, t))

    def dnpv(rate):
        return sum(-ti * cf / (1 + rate) ** (ti + 1) for cf, ti in zip(cash_flows, t))

    rate = guess
    for _ in range(100):
        n = npv(rate)
        d = dnpv(rate)
        if abs(d) < 1e-10:
            break
        rate -= n / d
        if rate <= -1:
            rate = -0.999
        if abs(n) < 0.01:
            break

    return round(rate, 4)


def simple_irr_approx(total_invested: float, total_value: float, years: float) -> float:
    """Simplified IRR approximation when cash flow dates not available."""
    if total_invested <= 0 or years <= 0:
        return 0.0
    moic = total_value / total_invested
    irr = moic ** (1 / years) - 1
    return round(irr, 4)


def compute_carry(
    total_realized: float,
    total_invested: float,
    hurdle_rate: float,
    carry_pct: float,
    fund_age_years: float,
) -> dict:
    """European waterfall carried interest calculation."""
    if total_invested <= 0:
        return {"carry_earned": 0, "lp_preferred_return": 0, "total_lp_proceeds": 0}

    preferred_return     = total_invested * ((1 + hurdle_rate) ** fund_age_years - 1)
    lp_hurdle_total      = total_invested + preferred_return
    total_profits        = max(0, total_realized - total_invested)
    profits_above_hurdle = max(0, total_realized - lp_hurdle_total)

    if profits_above_hurdle <= 0:
        carry_earned = 0
        lp_total     = total_realized
    else:
        carry_earned = profits_above_hurdle * carry_pct
        lp_total     = total_realized - carry_earned

    return {
        "total_invested":        total_invested,
        "preferred_return":      round(preferred_return, 0),
        "lp_hurdle_total":       round(lp_hurdle_total, 0),
        "total_profits":         round(total_profits, 0),
        "profits_above_hurdle":  round(profits_above_hurdle, 0),
        "carry_earned":          round(carry_earned, 0),
        "lp_total_proceeds":     round(lp_total, 0),
        "carry_pct":             carry_pct,
        "hurdle_rate":           hurdle_rate,
    }


def j_curve_position(tvpi: float, dpi: float, fund_age: float) -> str:
    """Estimate where the fund is on the J-curve."""
    if fund_age <= 2:
        return "EARLY — fees dragging returns, expected negative to flat TVPI"
    if fund_age <= 4 and tvpi < 1.0:
        return "VALLEY — typical J-curve trough, focus on portfolio development"
    if tvpi >= 1.0 and dpi < 0.5:
        return "CLIMBING — paper gains building, awaiting realizations"
    if dpi >= 0.5 and tvpi >= 1.5:
        return "INFLECTING — strong realizations, above-water DPI"
    if dpi >= 1.0:
        return "MATURE — capital returned, carry potential visible"
    return "DEVELOPING"


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "..", "output")
    os.makedirs(output_dir, exist_ok=True)

    inputs_path = os.path.join(output_dir, "fund_inputs.json")
    output_path = os.path.join(output_dir, "fund_output.json")

    if not os.path.exists(inputs_path):
        print(f"ERROR: fund_inputs.json not found at {inputs_path}", file=sys.stderr)
        sys.exit(1)

    with open(inputs_path, "r", encoding="utf-8") as f:
        inputs = json.load(f)

    investments      = inputs.get("investments", [])
    committed        = inputs.get("committed_capital", 0)
    mgmt_fee_pct     = inputs.get("management_fee_pct", 0.02)
    carry_pct        = inputs.get("carry_pct", 0.20)
    hurdle_rate      = inputs.get("hurdle_rate", 0.08)
    vintage_year     = inputs.get("vintage_year", 2020)
    current_year     = inputs.get("current_year", 2025)
    fund_age         = max(0.5, current_year - vintage_year)

    # Portfolio aggregates
    total_invested  = sum(i.get("invested", 0) for i in investments)
    total_fmv       = sum(i.get("current_fmv", 0) for i in investments)
    total_realized  = sum(i.get("realized", 0) for i in investments)

    # Fund KPIs
    total_value = total_fmv + total_realized
    tvpi  = round(total_value / total_invested, 2) if total_invested > 0 else 0
    dpi   = round(total_realized / total_invested, 2) if total_invested > 0 else 0
    rvpi  = round(total_fmv / total_invested, 2) if total_invested > 0 else 0

    # IRR
    cash_flows_raw = inputs.get("cash_flows", [])
    if len(cash_flows_raw) >= 2:
        try:
            cfs    = [cf["amount"] for cf in cash_flows_raw]
            dates  = [datetime.strptime(cf["date"], "%Y-%m") for cf in cash_flows_raw]
            irr    = xirr(cfs, dates)
        except Exception:
            irr = simple_irr_approx(total_invested, total_value, fund_age)
    else:
        irr = simple_irr_approx(total_invested, total_value, fund_age)

    # Management fees (investment period = first 5 years, harvest = remaining)
    invest_period_years = min(fund_age, 5)
    harvest_years       = max(0, fund_age - 5)
    mgmt_fee_total      = (committed * mgmt_fee_pct * invest_period_years) + \
                          (total_invested * mgmt_fee_pct * harvest_years)

    # Carry
    carry_data = compute_carry(total_realized, total_invested, hurdle_rate, carry_pct, fund_age)

    # Per-company metrics
    company_metrics = []
    for inv in investments:
        invested = inv.get("invested", 0)
        fmv      = inv.get("current_fmv", 0)
        realized = inv.get("realized", 0)
        total    = fmv + realized
        moic     = round(total / invested, 2) if invested > 0 else 0
        company_metrics.append({
            "company":      inv.get("company", "Unknown"),
            "invested":     invested,
            "current_fmv":  fmv,
            "realized":     realized,
            "total_value":  total,
            "moic":         moic,
            "status":       inv.get("status", "active"),
        })

    # Sort by MOIC descending
    company_metrics.sort(key=lambda x: x["moic"], reverse=True)

    j_pos = j_curve_position(tvpi, dpi, fund_age)

    output = {
        "fund_name":       inputs.get("fund_name", "Fund"),
        "vintage_year":    vintage_year,
        "fund_age_years":  round(fund_age, 1),
        "committed_capital": committed,
        "total_invested":  total_invested,
        "total_fmv":       total_fmv,
        "total_realized":  total_realized,
        "total_value":     total_value,
        "kpis": {
            "tvpi":          tvpi,
            "dpi":           dpi,
            "rvpi":          rvpi,
            "irr_pct":       round(irr * 100, 1),
            "gross_moic":    tvpi,
        },
        "management_fee_total": round(mgmt_fee_total, 0),
        "carry":           carry_data,
        "j_curve":         j_pos,
        "company_metrics": company_metrics,
        "num_investments": len(investments),
        "num_active":      sum(1 for i in investments if i.get("status") == "active"),
        "num_exited":      sum(1 for i in investments if i.get("status") == "exited"),
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"fund_kpi_calc.py: TVPI={tvpi}×, DPI={dpi}×, IRR={irr*100:.1f}%")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
