#!/usr/bin/env python3
"""
regional_context.py - Regional multiplier tables (self-contained).
All five regional tables are hardcoded here — no external context files needed.
Pure arithmetic. No AI calls. No web search.

Author: Santhosh Gandhi
Usage: python regional_context.py [region_string_or_query]
Output: JSON to stdout
"""

import sys
import json
from typing import Dict, List, Tuple

# ─── MULTIPLIER TABLES (6 STEEEP × 3 TEMPORAL) ───────────────────────────────
#
# > 1.0 = region has asymmetric advantage / amplified exposure in this cell
# < 1.0 = region has structural disadvantage / dampening factor
# = 1.0 = neutral — tracks global baseline
#
# Source: IFTF methodology adapted for regional structural factors

_REGIONAL_MULTIPLIERS: Dict[str, Dict[str, Dict[str, float]]] = {

    "india": {
        "Social": {
            "Operational":    1.10,   # rising aspiration, urban-rural gap
            "Strategic":      1.30,   # demographic dividend, rising middle class
            "Civilizational": 1.20,   # language/identity diversity, cultural depth
        },
        "Technological": {
            "Operational":    1.40,   # UPI/DPI advantage, mobile-first adoption
            "Strategic":      1.30,   # software talent depth, IT services scale
            "Civilizational": 0.90,   # hardware gap, semiconductor dependency
        },
        "Economic": {
            "Operational":    1.00,   # neutral — tracks global cycles
            "Strategic":      1.30,   # large domestic market, manufacturing push
            "Civilizational": 0.90,   # cost arbitrage compressing, commodity import
        },
        "Environmental": {
            "Operational":    0.90,   # policy lag, enforcement gaps
            "Strategic":      1.00,   # neutral — renewable push vs coal dependency
            "Civilizational": 1.10,   # climate vulnerability (monsoon/coastal/heat)
        },
        "Ethical": {
            "Operational":    0.90,   # regulatory unpredictability, enforcement gaps
            "Strategic":      1.00,   # neutral — digital rights framework emerging
            "Civilizational": 1.00,   # neutral — complex multi-stakeholder landscape
        },
        "Political": {
            "Operational":    0.85,   # regulatory unpredictability, state-federal friction
            "Strategic":      1.20,   # PLI/industrial policy tailwind, reform momentum
            "Civilizational": 1.15,   # US-China geopolitical positioning advantage
        },
    },

    "usa": {
        "Social": {
            "Operational":    1.00,
            "Strategic":      1.10,   # immigration-driven talent & consumer growth
            "Civilizational": 1.05,
        },
        "Technological": {
            "Operational":    1.20,   # deep VC ecosystem, fast commercialisation
            "Strategic":      1.40,   # AI/semiconductor leadership, R&D spend
            "Civilizational": 1.20,   # platform dominance, IP regime
        },
        "Economic": {
            "Operational":    1.10,   # world reserve currency, deep capital markets
            "Strategic":      1.30,   # consumer market size, M&A velocity
            "Civilizational": 1.10,
        },
        "Environmental": {
            "Operational":    0.95,   # federal policy inconsistency
            "Strategic":      1.00,
            "Civilizational": 1.05,   # climate tech investment scale
        },
        "Ethical": {
            "Operational":    1.05,
            "Strategic":      1.10,   # AI ethics leadership, regulatory capacity
            "Civilizational": 1.10,
        },
        "Political": {
            "Operational":    0.90,   # legislative gridlock, partisan volatility
            "Strategic":      0.95,
            "Civilizational": 1.00,
        },
    },

    "europe": {
        "Social": {
            "Operational":    1.00,
            "Strategic":      1.05,
            "Civilizational": 1.10,   # social safety net, aging population pressure
        },
        "Technological": {
            "Operational":    1.00,
            "Strategic":      1.10,   # deep engineering base, hardware manufacturing
            "Civilizational": 1.05,
        },
        "Economic": {
            "Operational":    0.95,   # sluggish growth, energy cost burden
            "Strategic":      0.90,   # demographic headwinds, fiscal fragmentation
            "Civilizational": 0.90,
        },
        "Environmental": {
            "Operational":    1.20,   # Green Deal implementation, carbon pricing
            "Strategic":      1.40,   # regulatory leadership (GDPR, EU AI Act)
            "Civilizational": 1.30,   # climate policy depth, biodiversity frameworks
        },
        "Ethical": {
            "Operational":    1.10,   # GDPR, Digital Markets Act enforcement
            "Strategic":      1.20,   # AI Act, strong consumer rights
            "Civilizational": 1.20,
        },
        "Political": {
            "Operational":    1.05,   # multilateral coordination capacity
            "Strategic":      1.10,
            "Civilizational": 1.10,   # rule-of-law stability, institutional depth
        },
    },

    "china": {
        "Social": {
            "Operational":    1.00,
            "Strategic":      1.10,   # state-directed social mobility programs
            "Civilizational": 1.05,
        },
        "Technological": {
            "Operational":    1.20,   # fast deployment, manufacturing integration
            "Strategic":      1.50,   # state-directed capital, talent scale
            "Civilizational": 1.30,   # deep industrial base, patent accumulation
        },
        "Economic": {
            "Operational":    1.10,   # large domestic market, export engine
            "Strategic":      1.20,
            "Civilizational": 1.10,
        },
        "Environmental": {
            "Operational":    0.90,   # enforcement gaps, coal dependency
            "Strategic":      1.00,   # EV/solar scale-up offset
            "Civilizational": 1.05,
        },
        "Ethical": {
            "Operational":    0.70,   # limited transparency, data sovereignty norms
            "Strategic":      0.75,
            "Civilizational": 0.80,
        },
        "Political": {
            "Operational":    1.10,   # fast policy execution, state coherence
            "Strategic":      1.15,
            "Civilizational": 1.00,   # long-term uncertainty on succession/legitimacy
        },
    },

    "global": {
        "Social":         {"Operational": 1.0, "Strategic": 1.0, "Civilizational": 1.0},
        "Technological":  {"Operational": 1.0, "Strategic": 1.0, "Civilizational": 1.0},
        "Economic":       {"Operational": 1.0, "Strategic": 1.0, "Civilizational": 1.0},
        "Environmental":  {"Operational": 1.0, "Strategic": 1.0, "Civilizational": 1.0},
        "Ethical":        {"Operational": 1.0, "Strategic": 1.0, "Civilizational": 1.0},
        "Political":      {"Operational": 1.0, "Strategic": 1.0, "Civilizational": 1.0},
    },
}

# ─── REGION DETECTION ─────────────────────────────────────────────────────────

_REGION_KEYWORDS: Dict[str, List[str]] = {
    "india": [
        "india", "indian", "bharat", "mumbai", "delhi", "bangalore",
        "bengaluru", "chennai", "hyderabad", "kolkata", "pune",
        "rupee", "inr", "isro", "nasscom", "tata", "reliance",
        "infosys", "wipro", "flipkart", "upi", "sensex", "nifty",
        "rbi", "sebi", "niti aayog", "pli", "modi", "bjp",
    ],
    "usa": [
        "usa", "u.s.", "america", "american", "dollar", "washington",
        "silicon valley", "nasdaq", "s&p", "federal reserve",
        "new york", "california", "congress", "white house", "fed ",
        "pentagon", "us senate",
    ],
    "europe": [
        "europe", "european", "eu ", "euro", "germany", "france",
        "uk ", "britain", "london", "paris", "berlin", "brussels",
        "ecb", "eurozone", "brexit", "gdpr", "eu ai act", "green deal",
        "italy", "spain", "netherlands", "sweden", "poland",
    ],
    "china": [
        "china", "chinese", "beijing", "shanghai", "yuan", "renminbi",
        "ccp", "alibaba", "tencent", "huawei", "byd", "baidu",
        "prc", "shenzhen", "xi jinping", "politburo",
    ],
}


def detect_region(text: str) -> str:
    """Detect region from query or signal text. Returns 'global' if no match."""
    text_lower = text.lower()
    for region, keywords in _REGION_KEYWORDS.items():
        if any(kw in text_lower for kw in keywords):
            return region
    return "global"


# ─── PUBLIC API ───────────────────────────────────────────────────────────────

def get_multipliers(region: str) -> Dict[str, Dict[str, float]]:
    """
    Return the full multiplier table for a region.

    Args:
        region: 'india', 'usa', 'europe', 'china', or 'global'

    Returns:
        Dict[STEEEP_category, Dict[temporal_layer, multiplier_float]]
    """
    region_key = (region or "global").lower().strip()
    return _REGIONAL_MULTIPLIERS.get(region_key, _REGIONAL_MULTIPLIERS["global"])


def get_multiplier(region: str, steeep_category: str, temporal_layer: str) -> float:
    """Return a single multiplier value. Returns 1.0 on unknown inputs."""
    return get_multipliers(region).get(steeep_category, {}).get(temporal_layer, 1.0)


def get_top_multipliers(region: str, n: int = 2) -> List[Tuple[str, str, float]]:
    """
    Return the top N most impactful multipliers (by distance from 1.0).

    Returns:
        List of (steeep, temporal, value) sorted by |value - 1.0| descending
    """
    multipliers = get_multipliers(region)
    all_mults: List[Tuple[str, str, float]] = [
        (steeep, temporal, value)
        for steeep, temporal_dict in multipliers.items()
        for temporal, value in temporal_dict.items()
    ]
    all_mults.sort(key=lambda x: abs(x[2] - 1.0), reverse=True)
    return all_mults[:n]


# ─── CLI ENTRY POINT ─────────────────────────────────────────────────────────

def main() -> None:
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else ""
    region = detect_region(query) if query else "global"

    multipliers = get_multipliers(region)
    top = get_top_multipliers(region, 3)

    result = {
        "region": region,
        "multipliers": multipliers,
        "top_movers": [
            {"steeep": s, "temporal": t, "value": v}
            for s, t, v in top
        ],
    }
    print(json.dumps(result, indent=2))
    sys.exit(0)


if __name__ == "__main__":
    main()
