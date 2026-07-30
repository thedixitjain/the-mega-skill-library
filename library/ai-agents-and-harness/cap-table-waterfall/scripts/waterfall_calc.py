#!/usr/bin/env python3
"""
cap-table-waterfall/scripts/waterfall_calc.py
Reads captable_output.json and runs exit waterfall for each scenario.
Writes waterfall_output.json.
"""

import json
import sys
import os


def run_waterfall(
    exit_price: float,
    post_ownership: list,
    new_round: dict,
    new_money: float,
) -> dict:
    """
    4-step waterfall:
    1. Return of capital to preferred investors (at 1× or stated multiple)
    2. Liquidation preference multiple (if > 1×)
    3. Participation (if participating preferred)
    4. Remainder to common (pro-rata)
    """
    preference_multiple = new_round.get("preference_multiple", 1.0)
    participating       = new_round.get("preference", "non-participating") == "participating"
    post_total          = sum(h["shares"] for h in post_ownership)

    if exit_price <= 0 or post_total == 0:
        return {"error": "Invalid exit price or share count", "proceeds": {}}

    remaining    = float(exit_price)
    proceeds     = {h["name"]: 0.0 for h in post_ownership}
    step_log     = []

    # Identify preferred + common shareholders
    preferred_holders = [h for h in post_ownership if h["type"] in ("preferred", "converted-safe")]
    common_holders    = [h for h in post_ownership if h["type"] == "common"]
    option_holders    = [h for h in post_ownership if h["type"] == "options"]

    # Step 1: Return of capital to preferred (1× of invested)
    pref_return = min(remaining, new_money * preference_multiple)
    step_log.append({"step": 1, "label": f"Preferred return ({preference_multiple}×)", "amount": round(pref_return, 0)})

    if preferred_holders and pref_return > 0:
        total_pref_shares = sum(h["shares"] for h in preferred_holders)
        for h in preferred_holders:
            share = (h["shares"] / total_pref_shares) * pref_return if total_pref_shares > 0 else 0
            proceeds[h["name"]] += share
        remaining -= pref_return

    # Step 2: Remaining split
    if remaining <= 0:
        step_log.append({"step": 2, "label": "No remainder for common", "amount": 0})
    else:
        if participating:
            # Participating: preferred gets pro-rata share of remainder too
            step_log.append({"step": 2, "label": f"Participating preferred — split remainder pro-rata", "amount": round(remaining, 0)})
            for h in post_ownership:
                if h["shares"] > 0 and h["type"] != "options":
                    share = (h["shares"] / post_total) * remaining
                    proceeds[h["name"]] += share
        else:
            # Non-participating: preferred either keeps liquidation pref or converts to common
            # Determine if preferred gets more from conversion
            pref_common_value = sum(
                (h["shares"] / post_total) * exit_price for h in preferred_holders
            )
            if pref_common_value > new_money * preference_multiple:
                # Better to convert — reset and split everything pro-rata
                proceeds = {h["name"]: 0.0 for h in post_ownership}
                remaining = exit_price
                step_log.append({"step": 2, "label": "Preferred converts to common (higher value)", "amount": round(remaining, 0)})
                for h in post_ownership:
                    if h["shares"] > 0 and h["type"] != "options":
                        proceeds[h["name"]] = (h["shares"] / post_total) * remaining
            else:
                # Keep liquidation preference, give remainder to common
                step_log.append({"step": 2, "label": "Remainder to common shareholders", "amount": round(remaining, 0)})
                common_total = sum(h["shares"] for h in common_holders)
                for h in common_holders:
                    if common_total > 0:
                        proceeds[h["name"]] += (h["shares"] / common_total) * remaining

    # Compute return multiples for preferred investors
    return_multiples = {}
    for h in preferred_holders:
        cost_basis = new_money * (h["shares"] / sum(ph["shares"] for ph in preferred_holders)) \
                     if preferred_holders else 0
        if cost_basis > 0:
            return_multiples[h["name"]] = round(proceeds[h["name"]] / cost_basis, 2)

    return {
        "exit_price":       exit_price,
        "proceeds":         {k: round(v, 0) for k, v in proceeds.items()},
        "return_multiples": return_multiples,
        "waterfall_steps":  step_log,
        "participating":    participating,
    }


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "..", "output")
    os.makedirs(output_dir, exist_ok=True)

    captable_path = os.path.join(output_dir, "captable_output.json")
    output_path   = os.path.join(output_dir, "waterfall_output.json")

    if not os.path.exists(captable_path):
        print(f"ERROR: captable_output.json not found. Run captable_calc.py first.", file=sys.stderr)
        sys.exit(1)

    with open(captable_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    new_round     = data.get("new_round", {})
    new_money     = new_round.get("new_money", 0)
    post_ownership = data.get("post_ownership", [])
    scenarios      = data.get("exit_scenarios", [])

    scenario_results = []
    for scenario in scenarios:
        result = run_waterfall(
            exit_price=scenario.get("exit_price", 0),
            post_ownership=post_ownership,
            new_round=new_round,
            new_money=new_money,
        )
        result["label"] = scenario.get("label", "Scenario")
        scenario_results.append(result)

    output = {
        "company":   data.get("company", "Unknown"),
        "scenarios": scenario_results,
        "post_ownership": post_ownership,
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"waterfall_calc.py: {len(scenario_results)} scenario(s) computed")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
