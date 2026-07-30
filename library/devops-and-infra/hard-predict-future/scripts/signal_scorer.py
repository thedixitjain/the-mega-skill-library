"""
signal_scorer.py

Scores signals collected by Claude's web search.
Pure arithmetic. No AI calls. No web search.

Formula: score = recency_weight × reliability_weight × type_weight × evidence_weight
Regional multipliers applied via regional_context.py.

Usage as CLI: python src/signal_scorer.py signals.json
Output: scored_signals.json to stdout + writes file
"""

from __future__ import annotations
import re
import sys
import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, date
from pathlib import Path
from typing import Dict, List, Optional


# ─── DATA STRUCTURES ──────────────────────────────────────────────────────────

STEEEP_CATEGORIES = [
    "Social", "Technological", "Economic",
    "Environmental", "Ethical", "Political",
]
TEMPORAL_LAYERS = ["Operational", "Strategic", "Civilizational"]
SIGNAL_TYPES = ["SUPPORTING", "OPPOSING", "NEUTRAL", "WILDCARD"]

# ─── ALIAS NORMALIZATION ───────────────────────────────────────────────────────
# Maps common Claude hallucination variants → canonical values
# Prevents silent KeyErrors when LLM outputs "Tech" instead of "Technological"

_STEEEP_ALIASES: Dict[str, str] = {
    "tech": "Technological", "technology": "Technological", "technological": "Technological",
    "econ": "Economic", "economy": "Economic", "economic": "Economic", "financial": "Economic",
    "env": "Environmental", "environment": "Environmental", "environmental": "Environmental",
    "eth": "Ethical", "ethic": "Ethical", "ethical": "Ethical", "legal": "Ethical",
    "pol": "Political", "politics": "Political", "political": "Political", "governance": "Political",
    "soc": "Social", "society": "Social", "social": "Social", "demographic": "Social",
}

_TEMPORAL_ALIASES: Dict[str, str] = {
    "operational": "Operational", "op": "Operational", "short": "Operational",
    "short-term": "Operational", "short term": "Operational", "near-term": "Operational",
    "strategic": "Strategic", "strat": "Strategic", "medium": "Strategic",
    "medium-term": "Strategic", "medium term": "Strategic",
    "civilizational": "Civilizational", "civilisational": "Civilizational",
    "civ": "Civilizational", "long": "Civilizational",
    "long-term": "Civilizational", "long term": "Civilizational",
}

_SIGNAL_TYPE_ALIASES: Dict[str, str] = {
    "supporting": "SUPPORTING", "support": "SUPPORTING", "positive": "SUPPORTING",
    "bullish": "SUPPORTING", "favorable": "SUPPORTING", "favourable": "SUPPORTING",
    "opposing": "OPPOSING", "oppose": "OPPOSING", "negative": "OPPOSING",
    "bearish": "OPPOSING", "against": "OPPOSING", "headwind": "OPPOSING",
    "wildcard": "WILDCARD", "wild": "WILDCARD", "black swan": "WILDCARD",
    "disruptive": "WILDCARD", "wild card": "WILDCARD",
    "neutral": "NEUTRAL", "mixed": "NEUTRAL", "ambiguous": "NEUTRAL",
}


def _normalize_steeep(value: str) -> Optional[str]:
    """Normalize a STEEEP category string to its canonical form. Returns None if unrecognizable."""
    if not value:
        return None
    v = value.strip()
    if v in STEEEP_CATEGORIES:
        return v
    return _STEEEP_ALIASES.get(v.lower())


def _normalize_temporal(value: str) -> Optional[str]:
    """Normalize a temporal layer string to its canonical form. Returns None if unrecognizable."""
    if not value:
        return None
    v = value.strip()
    if v in TEMPORAL_LAYERS:
        return v
    return _TEMPORAL_ALIASES.get(v.lower())


def _normalize_signal_type(value: str) -> Optional[str]:
    """Normalize a signal type string to its canonical form. Returns None if unrecognizable."""
    if not value:
        return None
    v = value.strip().upper()
    if v in SIGNAL_TYPES:
        return v
    return _SIGNAL_TYPE_ALIASES.get(value.strip().lower())


@dataclass
class Signal:
    """Raw signal as provided by Claude's web_search output."""
    content: str
    source: str
    date: Optional[str] = None
    # Optional pre-classifications (Claude may provide these)
    steeep_category: Optional[str] = None
    temporal_layer: Optional[str] = None
    signal_type: Optional[str] = None


@dataclass
class ScoredSignal:
    """Signal after deterministic scoring."""
    content: str
    source: str
    date: Optional[str]
    steeep_category: str
    temporal_layer: str
    signal_type: str
    recency_weight: float      # 0.4–1.0
    reliability_weight: float  # 0.4–1.0
    type_weight: float         # 0.6–1.3
    evidence_weight: float     # 0.7–1.2
    base_score: float          # recency × reliability × type × evidence (capped at 1.0)
    final_score: float         # base_score × regional multiplier (if applied)
    india_adjusted: bool = False
    regional_adjusted: bool = False
    momentum_flag: Optional[str] = None


@dataclass
class MatrixCell:
    steeep: str
    temporal: str
    score: float        # sum of final_scores of signals in this cell
    signal_count: int


@dataclass
class Matrix:
    cells: Dict[str, MatrixCell]         # key = "STEEEP/Temporal"
    hottest_cell: str                    # key of highest-score cell
    net_direction: str                   # SUPPORTING / OPPOSING / NEUTRAL
    blind_zones: List[str]              # cell keys with zero signals
    signal_counts: Dict[str, int]        # SUPPORTING/OPPOSING/NEUTRAL/WILDCARD/total


# ─── RECENCY WEIGHTS ─────────────────────────────────────────────────────────
#  < 3 months  = 1.0
#  3–12 months = 0.8
#  1–3 years   = 0.6
#  > 3 years   = 0.4
#  unknown     = 0.5

def _recency_weight(date_str: Optional[str]) -> float:
    """Derive recency weight from a date string. Returns 0.5 on unknown."""
    if not date_str:
        return 0.5

    now = datetime.now()
    signal_date: Optional[datetime] = None

    _FORMATS = [
        "%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y",
        "%B %d, %Y", "%b %d, %Y", "%B %Y", "%b %Y",
        "%m/%d/%Y", "%d %B %Y",
    ]
    for fmt in _FORMATS:
        try:
            signal_date = datetime.strptime(date_str.strip(), fmt)
            break
        except ValueError:
            continue

    if signal_date is None:
        # Try extracting a 4-digit year
        m = re.search(r"\b(20\d{2}|19\d{2})\b", date_str)
        if m:
            signal_date = datetime(int(m.group(1)), 7, 1)  # mid-year estimate
        else:
            return 0.5

    months_old = max(0.0, (now - signal_date).days / 30.44)
    if months_old < 3:
        return 1.0
    elif months_old < 12:
        return 0.8
    elif months_old < 36:
        return 0.6
    else:
        return 0.4


# ─── RELIABILITY WEIGHTS ─────────────────────────────────────────────────────
#  government/official = 1.0
#  established news    = 0.9
#  industry report     = 0.85
#  analyst commentary  = 0.7
#  blog/opinion        = 0.5
#  unknown             = 0.4

_GOV_TOKENS = {
    "gov", "government", "official", "ministry", "department", "parliament",
    "rbi", "sebi", "niti", "census", "statistics", "treasury", "federal",
    "reserve", "white house", "state dept", "un ", "united nations",
    "world bank", "imf", "oecd", "pib", "mospi", "isro", "nasa", "ec ",
    "european commission", "bundesbank",
}
_NEWS_TOKENS = {
    "reuters", "bloomberg", "bbc", "cnn", "nytimes", "wsj",
    "ft.com", "financial times", "the hindu", "hindustan times",
    "times of india", "economic times", "livemint", "mint",
    "the guardian", "associated press", "ap news", "afp",
    "ndtv", "cnbc", "business standard", "moneycontrol", "axios",
    "politico", "the economist", "nature", "science", "lancet",
}
_INDUSTRY_TOKENS = {
    "mckinsey", "deloitte", "pwc", "kpmg", "ey ", "ernst & young",
    "gartner", "forrester", "idc", "nasscom", "ficci", "cii",
    "report", "research", "study", "survey", "whitepaper",
    "industry", "sector", "market research", "bain", "bcg",
    "nber", "brookings", "rand corporation",
}
_ANALYST_TOKENS = {
    "analyst", "expert", "professor", "dr.", "phd", "ceo",
    "founder", "partner", "director", "chief", "head of",
    "commentary", "analysis", "perspective", "opinion",
}
_BLOG_TOKENS = {
    "blog", "substack", "medium.com", "wordpress", "personal",
    "twitter", "linkedin", "reddit", "quora",
}


def _reliability_weight(source: str) -> float:
    """Classify source type and return reliability weight."""
    if not source:
        return 0.4
    s = source.lower()

    for tok in _GOV_TOKENS:
        if tok in s:
            return 1.0
    for tok in _NEWS_TOKENS:
        if tok in s:
            return 0.9
    for tok in _INDUSTRY_TOKENS:
        if tok in s:
            return 0.85
    for tok in _ANALYST_TOKENS:
        if tok in s:
            return 0.7
    for tok in _BLOG_TOKENS:
        if tok in s:
            return 0.5
    return 0.4


# ─── TYPE WEIGHTS ─────────────────────────────────────────────────────────────
#  SUPPORTING = 1.0
#  OPPOSING   = 1.0  (opposing evidence is equally important)
#  NEUTRAL    = 0.6
#  WILDCARD   = 1.3  (high impact even if uncertain)

_TYPE_WEIGHTS = {
    "SUPPORTING": 1.0,
    "OPPOSING":   1.0,
    "NEUTRAL":    0.6,
    "WILDCARD":   1.3,
}


def _type_weight(signal_type: str) -> float:
    return _TYPE_WEIGHTS.get(signal_type.upper(), 0.6)


# ─── EVIDENCE TYPE WEIGHTS ────────────────────────────────────────────────────
#  DATA/STATISTIC = 1.2
#  EVENT/INCIDENT = 1.0
#  ANALYSIS/OPINION = 0.7

_EVIDENCE_WEIGHTS = {
    "DATA":      1.2,
    "STATISTIC": 1.2,
    "EVENT":     1.0,
    "INCIDENT":  1.0,
    "ANALYSIS":  0.7,
    "OPINION":   0.7,
}


def _evidence_weight(evidence_type: Optional[str]) -> float:
    if not evidence_type:
        return 0.7  # default to ANALYSIS
    return _EVIDENCE_WEIGHTS.get(evidence_type.upper(), 0.7)


# ─── STEEEP CLASSIFICATION ────────────────────────────────────────────────────

_STEEEP_KW: Dict[str, List[str]] = {
    "Social": [
        "social", "population", "demographic", "culture", "community",
        "education", "health", "welfare", "inequality", "migration",
        "labor", "workforce", "employment", "poverty", "middle class",
        "consumer", "lifestyle", "urban", "rural", "youth", "elderly",
        "voter", "citizen", "gender", "caste",
    ],
    "Technological": [
        "technology", "tech", "digital", "ai ", "artificial intelligence",
        "software", "hardware", "internet", "mobile", "data", "cloud",
        "automation", "robot", "innovation", "platform", "semiconductor",
        "upi", "fintech", "ev ", "electric vehicle", "renewable", "5g",
        "saas", "b2b saas", "startup", "unicorn", "ipo",
    ],
    "Economic": [
        "economic", "economy", "gdp", "growth", "market", "trade",
        "investment", "finance", "fiscal", "monetary", "inflation",
        "currency", "export", "import", "revenue", "profit", "loss",
        "sector", "industry", "b2b", "valuation", "funding",
    ],
    "Environmental": [
        "environment", "climate", "carbon", "emission", "pollution",
        "energy", "solar", "wind", "fossil", "renewable", "green",
        "sustainable", "water", "land", "biodiversity", "weather",
        "temperature", "flood", "drought", "disaster", "ev battery",
    ],
    "Ethical": [
        "ethical", "ethics", "moral", "legal", "law", "regulation",
        "compliance", "governance", "corruption", "transparency",
        "accountability", "rights", "privacy", "security", "trust",
        "fair", "justice", "equality", "discrimination", "censor",
    ],
    "Political": [
        "political", "politics", "policy", "government", "election",
        "parliament", "minister", "president", "vote", "party",
        "legislation", "tax", "subsidy", "regulation", "geopolit",
        "diplomatic", "treaty", "alliance", "sanction", "tariff",
        "pli", "fdi", "trade war",
    ],
}


def _classify_steeep(content: str, provided: Optional[str]) -> str:
    """
    Classify signal into STEEEP category.
    Uses provided value if valid (with alias normalization), else infers from content keywords.
    """
    if provided:
        normalized = _normalize_steeep(provided)
        if normalized:
            return normalized
    cl = content.lower()
    scores = {cat: 0 for cat in STEEEP_CATEGORIES}
    for cat, kws in _STEEEP_KW.items():
        for kw in kws:
            if kw in cl:
                scores[cat] += 1
    best = max(scores, key=scores.get)  # type: ignore[arg-type]
    return best if scores[best] > 0 else "Economic"


# ─── TEMPORAL CLASSIFICATION ──────────────────────────────────────────────────

_TEMPORAL_KW: Dict[str, List[str]] = {
    "Operational": [
        "this year", "next year", "quarter", "monthly", "weekly",
        "current", "now", "today", "immediate", "short term",
        "2024", "2025", "2026", "recent", "latest", "this quarter",
    ],
    "Strategic": [
        "5 year", "10 year", "decade", "medium term", "strategic",
        "by 2030", "by 2032", "by 2033", "by 2034", "by 2035",
        "plan", "roadmap", "trajectory", "trend", "projection",
        "forecast", "five year", "ten year",
    ],
    "Civilizational": [
        "generation", "long term", "structural", "fundamental",
        "systemic", "paradigm", "century", "civiliz", "transform",
        "irreversible", "tipping point", "disruption", "revolution",
        "post-", "forever",
    ],
}


def _classify_temporal(content: str, provided: Optional[str]) -> str:
    """
    Classify signal into temporal layer.
    Uses provided value if valid (with alias normalization), else infers from content keywords.
    """
    if provided:
        normalized = _normalize_temporal(provided)
        if normalized:
            return normalized
    cl = content.lower()
    scores = {layer: 0 for layer in TEMPORAL_LAYERS}
    for layer, kws in _TEMPORAL_KW.items():
        for kw in kws:
            if kw in cl:
                scores[layer] += 1
    best = max(scores, key=scores.get)  # type: ignore[arg-type]
    return best if scores[best] > 0 else "Strategic"


# ─── SIGNAL TYPE CLASSIFICATION ───────────────────────────────────────────────

_WILDCARD_KW = [
    "unexpected", "surprise", "shock", "crisis", "collapse",
    "breakthrough", "disruption", "black swan", "unprecedented",
    "sudden", "dramatic", "catastrophic", "revolutionary",
    "overnight", "flash crash", "pandemic", "war",
]
_OPPOSING_KW = [
    "decline", "fall", "drop", "decrease", "reduce", "loss",
    "challenge", "obstacle", "barrier", "risk", "threat", "concern",
    "fail", "failure", "problem", "issue", "against", "oppose",
    "unlikely", "difficult", "struggle", "weaken", "slowdown",
    "headwind", "obstacle", "hurdle", "uncertain",
]
_SUPPORTING_KW = [
    "growth", "rise", "increase", "improve", "advance", "progress",
    "success", "achieve", "enable", "support", "boost", "accelerate",
    "likely", "possible", "momentum", "strength", "advantage",
    "opportunity", "invest", "fund", "launch", "expand", "surge",
    "tailwind", "favorable", "positive",
]


def _classify_signal_type(content: str, provided: Optional[str]) -> str:
    """
    Classify signal as SUPPORTING / OPPOSING / NEUTRAL / WILDCARD.
    Uses provided value if valid (with alias normalization), else infers from content keywords.
    """
    if provided:
        normalized = _normalize_signal_type(provided)
        if normalized:
            return normalized

    cl = content.lower()

    for kw in _WILDCARD_KW:
        if kw in cl:
            return "WILDCARD"

    opp = sum(1 for kw in _OPPOSING_KW if kw in cl)
    sup = sum(1 for kw in _SUPPORTING_KW if kw in cl)

    if sup > opp * 1.5:
        return "SUPPORTING"
    if opp > sup * 1.5:
        return "OPPOSING"
    return "NEUTRAL"


# ─── MAIN SCORING FUNCTION ───────────────────────────────────────────────────

def score_signal(signal: Signal, india_relevant: bool = False,
                 region: Optional[str] = None) -> ScoredSignal:
    """
    Score a single signal deterministically.

    Formula: score = recency_weight × reliability_weight × type_weight × evidence_weight
    Cap at 1.0, then apply regional multiplier if applicable.

    Args:
        signal:         Raw signal from Claude's web_search output
        india_relevant: If True, applies India context multipliers (legacy)
        region:         Region string for regional_context routing

    Returns:
        ScoredSignal with all weights and final_score populated
    """
    steeep   = _classify_steeep(signal.content, signal.steeep_category)
    temporal = _classify_temporal(signal.content, signal.temporal_layer)
    sig_type = _classify_signal_type(signal.content, signal.signal_type)
    ev_type  = getattr(signal, "evidence_type", None)

    r_wt  = _recency_weight(signal.date)
    re_wt = _reliability_weight(signal.source)
    t_wt  = _type_weight(sig_type)
    e_wt  = _evidence_weight(ev_type)

    base = min(1.0, r_wt * re_wt * t_wt * e_wt)  # cap at 1.0

    scored = ScoredSignal(
        content=signal.content,
        source=signal.source,
        date=signal.date,
        steeep_category=steeep,
        temporal_layer=temporal,
        signal_type=sig_type,
        recency_weight=r_wt,
        reliability_weight=re_wt,
        type_weight=t_wt,
        evidence_weight=e_wt,
        base_score=base,
        final_score=base,
        india_adjusted=False,
        regional_adjusted=False,
    )

    # Apply regional multipliers
    effective_region = region or ("india" if india_relevant else None)
    if effective_region:
        try:
            import sys as _sys
            import os as _os
            _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
            from regional_context import get_multipliers
            multipliers = get_multipliers(effective_region)
            mult = multipliers.get(steeep, {}).get(temporal, 1.0)
            scored.final_score = min(1.0, base * mult)
            scored.regional_adjusted = True
            if effective_region == "india":
                scored.india_adjusted = True
        except (ImportError, Exception):
            pass

    return scored


# ─── MATRIX BUILDER ──────────────────────────────────────────────────────────

def build_steeep_matrix(scored_signals: List[ScoredSignal]) -> Matrix:
    """
    Build the 6×3 STEEEP×Temporal matrix from scored signals.
    Each cell score = sum of final_scores of signals mapped to that cell.

    Args:
        scored_signals: List of already-scored ScoredSignal objects

    Returns:
        Matrix with 18 cells, hottest_cell, net_direction, blind_zones
    """
    # Initialise all 18 cells
    cells: Dict[str, MatrixCell] = {
        f"{s}/{t}": MatrixCell(steeep=s, temporal=t, score=0.0, signal_count=0)
        for s in STEEEP_CATEGORIES
        for t in TEMPORAL_LAYERS
    }

    signal_counts: Dict[str, int] = {
        "SUPPORTING": 0, "OPPOSING": 0, "NEUTRAL": 0, "WILDCARD": 0, "total": 0,
    }

    for sig in scored_signals:
        key = f"{sig.steeep_category}/{sig.temporal_layer}"
        if key in cells:
            cells[key].score += sig.final_score
            cells[key].signal_count += 1
        stype = sig.signal_type.upper()
        if stype in signal_counts:
            signal_counts[stype] += 1
        signal_counts["total"] += 1

    # Hottest cell
    hottest_key = max(cells, key=lambda k: cells[k].score)

    # Net direction
    sup_score = sum(s.final_score for s in scored_signals if s.signal_type == "SUPPORTING")
    opp_score = sum(s.final_score for s in scored_signals if s.signal_type == "OPPOSING")

    if sup_score > opp_score * 1.2:
        net_direction = "SUPPORTING"
    elif opp_score > sup_score * 1.2:
        net_direction = "OPPOSING"
    else:
        net_direction = "NEUTRAL"

    blind_zones = [k for k, cell in cells.items() if cell.signal_count == 0]

    return Matrix(
        cells=cells,
        hottest_cell=hottest_key,
        net_direction=net_direction,
        blind_zones=blind_zones,
        signal_counts=signal_counts,
    )


# ─── CLI ENTRY POINT ─────────────────────────────────────────────────────────

def _signal_to_dict(s: ScoredSignal) -> dict:
    return {
        "content": s.content,
        "source": s.source,
        "date": s.date,
        "steeep_category": s.steeep_category,
        "temporal_layer": s.temporal_layer,
        "signal_type": s.signal_type,
        "recency_weight": round(s.recency_weight, 4),
        "reliability_weight": round(s.reliability_weight, 4),
        "type_weight": round(s.type_weight, 4),
        "evidence_weight": round(s.evidence_weight, 4),
        "base_score": round(s.base_score, 4),
        "final_score": round(s.final_score, 4),
        "regional_adjusted": s.regional_adjusted,
        "momentum_flag": s.momentum_flag,
    }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: signal_scorer.py signals.json"}, indent=2))
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(json.dumps({"error": f"File not found: {input_path}"}, indent=2))
        sys.exit(1)

    with open(input_path) as f:
        raw = json.load(f)

    raw_signals = raw if isinstance(raw, list) else raw.get("signals", [])

    # Convert raw dicts to Signal objects
    signal_objects = []
    for item in raw_signals:
        s = Signal(
            content=item.get("content", ""),
            source=item.get("source", ""),
            date=item.get("date"),
            steeep_category=item.get("steeep_category") or (
                item.get("steeep_categories", [None])[0]
                if isinstance(item.get("steeep_categories"), list) else None
            ),
            temporal_layer=item.get("temporal_layer"),
            signal_type=item.get("signal_type"),
        )
        # Attach evidence_type if present
        s.__dict__["evidence_type"] = item.get("evidence_type")
        signal_objects.append(s)

    # Detect region from first signal or content
    all_text = " ".join(
        (item.get("content", "") + " " + item.get("source", "")).lower()
        for item in raw_signals
    )
    region = None
    if any(kw in all_text for kw in ["india", "indian", "bharat", "rupee", "mumbai", "delhi"]):
        region = "india"
    elif any(kw in all_text for kw in ["china", "chinese", "beijing", "yuan"]):
        region = "china"
    elif any(kw in all_text for kw in ["europe", "european", "euro", "germany", "uk"]):
        region = "europe"
    elif any(kw in all_text for kw in ["usa", "america", "american", "silicon valley"]):
        region = "usa"

    scored = [score_signal(s, region=region) for s in signal_objects]

    result = {
        "scored_signals": [_signal_to_dict(s) for s in scored],
        "region_detected": region,
        "total_signals": len(scored),
    }

    out_path = Path(sys.argv[1]).parent / "scored_signals.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))
    sys.exit(0)


if __name__ == "__main__":
    main()
