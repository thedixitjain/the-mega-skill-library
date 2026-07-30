#!/usr/bin/env python3
"""
cap-table-waterfall/scripts/captable_calc.py
Reads captable_inputs.json, computes SAFE conversions and post-round ownership.
Writes captable_output.json.
"""

import json
import sys
import os


def safe_conversion(safe: dict, pre_round_shares: int, pre_money_valuation: float) -> dict:
    """Compute SAFE conversion shares at the new priced round."""
    principal      = safe.get("principal", 0)
    cap            = safe.get("valuation_cap", 0)
    discount       = safe.get("discount_rate", 0.20)
    safe_type      = safe.get("type", "post-money-safe")

    if pre_round_shares <= 0 or pre_money_valuation <= 0:
        return {"error": "Invalid pre-round shares or valuation", "shares": 0}

    round_price    = pre_money_valuation / pre_round_shares
    discount_price = round_price * (1 - discount)

    if cap > 0:
        cap_price          = cap / pre_round_shares
        conversion_price   = min(cap_price, discount_price)
        conversion_method  = "cap" if cap_price <= discount_price else "discount"
    else:
        conversion_price  = discount_price
        conversion_method = "discount"

    shares = int(principal / conversion_price) if conversion_price > 0 else 0

    return {
        "investor":          safe.get("investor", "SAFE Investor"),
        "principal":         principal,
        "valuation_cap":     cap,
        "discount_rate":     discount,
        "round_price":       round(round_price, 6),
        "conversion_price":  round(conversion_price, 6),
        "conversion_method": conversion_method,
        "shares_issued":     shares,
        "effective_pct":     0,  # filled after total shares known
    }


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "..", "output")
    os.makedirs(output_dir, exist_ok=True)

    inputs_path = os.path.join(output_dir, "captable_inputs.json")
    output_path = os.path.join(output_dir, "captable_output.json")

    if not os.path.exists(inputs_path):
        print(f"ERROR: captable_inputs.json not found at {inputs_path}", file=sys.stderr)
        sys.exit(1)

    with open(inputs_path, "r", encoding="utf-8") as f:
        inputs = json.load(f)

    stakeholders = inputs.get("stakeholders", [])
    safes        = inputs.get("safes", [])
    new_round    = inputs.get("new_round", {})

    pre_money    = new_round.get("pre_money_valuation", 0)
    new_money    = new_round.get("new_money", 0)
    pool_pct     = new_round.get("new_option_pool_pct", 0.10)

    # Pre-round total shares
    pre_shares = sum(s.get("shares", 0) for s in stakeholders)
    if pre_shares == 0:
        print("ERROR: No shares found in stakeholders.", file=sys.stderr)
        sys.exit(1)

    # Pre-round ownership
    pre_ownership = [
        {
            "name":    s["name"],
            "shares":  s["shares"],
            "type":    s.get("type", "common"),
            "pct":     round(s["shares"] / pre_shares * 100, 2),
        }
        for s in stakeholders
    ]

    # SAFE conversions
    safe_results = [safe_conversion(safe, pre_shares, pre_money) for safe in safes]
    safe_shares  = sum(r["shares_issued"] for r in safe_results)

    # New investor shares
    round_price     = pre_money / pre_shares if pre_shares > 0 else 0
    new_inv_shares  = int(new_money / round_price) if round_price > 0 else 0

    # Post-round option pool increase
    post_total_est  = pre_shares + safe_shares + new_inv_shares
    pool_new_shares = int(post_total_est * pool_pct)

    # Post-round total
    post_total = pre_shares + safe_shares + new_inv_shares + pool_new_shares

    # Post-round ownership table
    post_ownership = []
    for s in pre_ownership:
        post_ownership.append({
            "name":     s["name"],
            "shares":   s["shares"],
            "type":     s["type"],
            "pre_pct":  s["pct"],
            "post_pct": round(s["shares"] / post_total * 100, 2),
            "dilution":  round(s["pct"] - s["shares"] / post_total * 100, 2),
        })

    for r in safe_results:
        post_ownership.append({
            "name":     r["investor"],
            "shares":   r["shares_issued"],
            "type":     "converted-safe",
            "pre_pct":  0,
            "post_pct": round(r["shares_issued"] / post_total * 100, 2),
            "dilution":  0,
        })

    post_ownership.append({
        "name":     "New Investor (Round)",
        "shares":   new_inv_shares,
        "type":     "preferred",
        "pre_pct":  0,
        "post_pct": round(new_inv_shares / post_total * 100, 2),
        "dilution":  0,
    })

    post_ownership.append({
        "name":     "New Option Pool",
        "shares":   pool_new_shares,
        "type":     "options",
        "pre_pct":  0,
        "post_pct": round(pool_new_shares / post_total * 100, 2),
        "dilution":  0,
    })

    output = {
        "company":          inputs.get("company", "Unknown"),
        "pre_round_shares": pre_shares,
        "post_round_shares": post_total,
        "round_price_per_share": round(round_price, 6),
        "post_money_valuation": pre_money + new_money,
        "safe_conversions": safe_results,
        "pre_ownership":    pre_ownership,
        "post_ownership":   post_ownership,
        "new_round":        new_round,
        "exit_scenarios":   inputs.get("exit_scenarios", []),
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"captable_calc.py: pre={pre_shares:,} shares, post={post_total:,} shares, round_price=${round_price:.4f}")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
