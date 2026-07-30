#!/usr/bin/env python3
"""
market-size/scripts/tam_calculator.py
Reads market_inputs.json, computes TAM/SAM/SOM using top-down and bottom-up.
Writes market_output.json.
"""

import json
import sys
import os


VENTURE_TAM_THRESHOLD = 1_000_000_000   # $1B
GOOD_CAGR_THRESHOLD   = 0.15            # 15%


def top_down_sizing(td: dict, arpu: float) -> dict:
    total_market = td.get("total_market_size_usd", 0)
    addr_frac    = td.get("addressable_fraction", 0.20)
    obt_frac     = td.get("obtainable_fraction", 0.05)
    cagr         = td.get("cagr_pct", 0) / 100.0

    tam = total_market
    sam = total_market * addr_frac
    som = sam * obt_frac

    # 5-year projections
    tam_5yr = tam * ((1 + cagr) ** 5)
    sam_5yr = sam * ((1 + cagr) ** 5)

    return {
        "method": "top-down",
        "tam": round(tam, 0),
        "sam": round(sam, 0),
        "som": round(som, 0),
        "tam_5yr": round(tam_5yr, 0),
        "sam_5yr": round(sam_5yr, 0),
        "cagr_pct": td.get("cagr_pct", 0),
        "source": td.get("source", "industry report"),
    }


def bottom_up_sizing(bu: dict) -> dict:
    total_customers    = bu.get("total_potential_customers", 0)
    addr_customers     = bu.get("addressable_customers", 0)
    obt_customers      = bu.get("obtainable_customers", 0)
    arpu               = bu.get("arpu_annual", 0)

    if addr_customers == 0 and total_customers > 0:
        addr_customers = int(total_customers * 0.20)
    if obt_customers == 0 and addr_customers > 0:
        obt_customers = int(addr_customers * 0.05)

    tam = total_customers * arpu
    sam = addr_customers * arpu
    som = obt_customers * arpu

    return {
        "method": "bottom-up",
        "tam": round(tam, 0),
        "sam": round(sam, 0),
        "som": round(som, 0),
        "total_potential_customers": total_customers,
        "addressable_customers":     addr_customers,
        "obtainable_customers":      obt_customers,
        "arpu_annual":               arpu,
    }


def consensus(td_result: dict, bu_result: dict) -> dict:
    td_tam = td_result.get("tam", 0)
    bu_tam = bu_result.get("tam", 0)
    td_sam = td_result.get("sam", 0)
    bu_sam = bu_result.get("sam", 0)
    td_som = td_result.get("som", 0)
    bu_som = bu_result.get("som", 0)

    valid_tams = [v for v in [td_tam, bu_tam] if v > 0]
    valid_sams = [v for v in [td_sam, bu_sam] if v > 0]
    valid_soms = [v for v in [td_som, bu_som] if v > 0]

    return {
        "tam_low":  round(min(valid_tams), 0) if valid_tams else 0,
        "tam_high": round(max(valid_tams), 0) if valid_tams else 0,
        "sam_low":  round(min(valid_sams), 0) if valid_sams else 0,
        "sam_high": round(max(valid_sams), 0) if valid_sams else 0,
        "som_low":  round(min(valid_soms), 0) if valid_soms else 0,
        "som_high": round(max(valid_soms), 0) if valid_soms else 0,
    }


def vc_rule_check(tam: float, cagr: float) -> list:
    flags = []
    if tam >= VENTURE_TAM_THRESHOLD:
        flags.append({"status": "PASS", "msg": f"TAM ${tam/1e9:.1f}B > $1B — venture-scale opportunity"})
    elif tam >= 500_000_000:
        flags.append({"status": "WATCH", "msg": f"TAM ${tam/1e9:.1f}B ($500M–$1B) — tight for top-tier VC"})
    else:
        flags.append({"status": "FAIL", "msg": f"TAM ${tam/1e6:.0f}M < $500M — likely too small for institutional VC"})

    if cagr >= GOOD_CAGR_THRESHOLD:
        flags.append({"status": "PASS", "msg": f"CAGR {cagr:.0%} — strong market tailwind"})
    elif cagr >= 0.05:
        flags.append({"status": "WATCH", "msg": f"CAGR {cagr:.0%} — moderate growth"})
    else:
        flags.append({"status": "FAIL", "msg": f"CAGR {cagr:.0%} — slow or flat market, headwind risk"})

    return flags


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "..", "output")
    os.makedirs(output_dir, exist_ok=True)

    inputs_path = os.path.join(output_dir, "market_inputs.json")
    output_path = os.path.join(output_dir, "market_output.json")

    if not os.path.exists(inputs_path):
        print(f"ERROR: market_inputs.json not found at {inputs_path}", file=sys.stderr)
        sys.exit(1)

    with open(inputs_path, "r", encoding="utf-8") as f:
        inputs = json.load(f)

    arpu = inputs.get("price_per_customer_annual", 0)
    td   = inputs.get("top_down", {})
    bu   = inputs.get("bottom_up", {})

    if bu.get("arpu_annual", 0) == 0 and arpu > 0:
        bu["arpu_annual"] = arpu

    td_result  = top_down_sizing(td, arpu)
    bu_result  = bottom_up_sizing(bu)
    cons       = consensus(td_result, bu_result)
    cagr       = td.get("cagr_pct", 0) / 100.0
    flags      = vc_rule_check(cons["tam_high"], cagr)

    output = {
        "company":     inputs.get("company", "Unknown"),
        "market":      inputs.get("market_category", "Unknown"),
        "geography":   inputs.get("geography", "Global"),
        "top_down":    td_result,
        "bottom_up":   bu_result,
        "consensus":   cons,
        "vc_checks":   flags,
        "competitors": inputs.get("competitors", []),
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    tam = cons.get("tam_high", 0)
    print(f"tam_calculator.py: TAM=${tam/1e9:.1f}B, CAGR={cagr:.0%}")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
