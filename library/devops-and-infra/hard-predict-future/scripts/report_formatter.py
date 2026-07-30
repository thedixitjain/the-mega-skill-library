"""
report_formatter.py

Enforces the crisp Foresight Engine output template.
No narrative generation — only slots Claude-written content into structure.
Pure formatting logic. No AI calls. No web search.

CRISP FORMAT RULES (strictly enforced):
  - Executive header:  max 1 line per field
  - Signal pulse:      visual bar format only
  - Each scenario:     max 5 lines total
  - IF / BUT / NEEDS:  max 1 line each
  - PROOF line:        must contain a number or date (warns if missing)
  - The One Thing:     max 5 lines total
  - No paragraph prose anywhere

Usage: python src/report_formatter.py report_data.json
Output: formatted plain text to stdout + writes report_output.json
"""

from __future__ import annotations
import os
import re
import sys
# Ensure scripts directory is on path so sibling modules can be imported from any CWD
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from signal_scorer import Matrix
from probability_calc import Analogue, ProbabilityResult
from input_validator import ValidationResult


# ─── DATA STRUCTURES ──────────────────────────────────────────────────────────

@dataclass
class Scenario:
    """Scenario content written by Claude, formatted by this module."""
    name: str
    description: str        # max 1 line (20-word soft cap enforced)
    proof: str              # must contain a number or date
    if_condition: str       # max 1 line — PROBABLE/PLAUSIBLE/POSSIBLE only
    but_condition: str      # max 1 line — PROBABLE/PLAUSIBLE/POSSIBLE only
    needs_condition: Optional[str] = None   # PREFERABLE only
    leverage: Optional[str] = None          # PREFERABLE only


@dataclass
class Report:
    """Final output in both human-readable text and JSON-serialisable dict."""
    text: str
    data: dict


# ─── HELPERS ──────────────────────────────────────────────────────────────────

_BAR_LEN = 20  # Total characters in a visual bar


def _bar(count: int, max_count: int) -> str:
    """
    Generate a 20-char visual bar: ████████░░░░░░░░░░░░

    Args:
        count:     Value to represent
        max_count: Value at which bar is 100% full (never < 1)
    """
    if max_count < 1:
        max_count = 1
    filled = min(_BAR_LEN, round((count / max_count) * _BAR_LEN))
    return "\u2588" * filled + "\u2591" * (_BAR_LEN - filled)


def _truncate(text: str, max_words: int) -> str:
    """Trim text to max_words words, appending '…' if cut."""
    words = text.split()
    return text if len(words) <= max_words else " ".join(words[:max_words]) + "…"


def _has_number_or_date(text: str) -> bool:
    """
    Return True if text contains a digit or a recognisable date token.
    PROOF lines must satisfy this check.
    """
    if re.search(r"\d", text):
        return True
    months = (
        "january|february|march|april|may|june|july|august|"
        "september|october|november|december|"
        "jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec"
    )
    return bool(re.search(rf"\b({months})\b", text.lower()))


_DIV = "\u2501" * 31   # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# ─── MAIN FORMATTER ───────────────────────────────────────────────────────────

def format_report(
    query: str,
    validation: ValidationResult,
    matrix: Matrix,
    analogues: List[Analogue],
    probabilities: ProbabilityResult,
    confidence: int,
    scenarios: Dict[str, Scenario],
    one_thing: str,
    india_adjusted: bool,
    india_lens: Optional[str] = None,
) -> Report:
    """
    Assemble the final Foresight Engine report.

    Args:
        query:          Original query string
        validation:     Must be valid=True
        matrix:         Populated STEEEP matrix
        analogues:      Historical analogues (Claude-assessed)
        probabilities:  Normalised probability result
        confidence:     Confidence score 0–100
        scenarios:      Dict with keys 'probable','plausible','possible','preferable'
        one_thing:      Key insight written by Claude (max 5 lines)
        india_adjusted: Whether India multipliers were applied
        india_lens:     India-specific commentary (Claude-written, optional)

    Returns:
        Report with .text (plain text) and .data (JSON-serialisable dict)
    """
    today = datetime.now().strftime("%Y-%m-%d")
    sc    = matrix.signal_counts
    sup_n = sc.get("SUPPORTING", 0)
    opp_n = sc.get("OPPOSING",   0)
    wld_n = sc.get("WILDCARD",   0)
    tot_n = sc.get("total",      0)
    max_n = max(sup_n, opp_n, 1)

    best_analogue = (
        max(analogues, key=lambda a: a.similarity_score) if analogues else None
    )

    # Blind zones summary
    if matrix.blind_zones:
        blind_show = ", ".join(matrix.blind_zones[:3])
        if len(matrix.blind_zones) > 3:
            blind_show += f" (+{len(matrix.blind_zones) - 3} more)"
    else:
        blind_show = "None — full coverage"

    lines: List[str] = []

    # ── HEADER ──────────────────────────────────────────────────────────────
    lines += [
        _DIV,
        "FORESIGHT ENGINE",
        query,
        f"Confidence: {confidence}/100 | Signals: {tot_n} | {today}",
        _DIV,
    ]

    # ── SIGNAL PULSE ────────────────────────────────────────────────────────
    lines += [
        "SIGNAL PULSE",
        (
            f"Supporting {sup_n} {_bar(sup_n, max_n)} | "
            f"Opposing {opp_n} {_bar(opp_n, max_n)} | "
            f"Wild {wld_n}"
        ),
        f"Net: {matrix.net_direction}{' LEADS' if matrix.net_direction != 'NEUTRAL' else ''}",
        f"Hot zone: {matrix.hottest_cell}",
        f"Gap: {blind_show}",
    ]

    # ── HISTORICAL MATCH ────────────────────────────────────────────────────
    if best_analogue:
        sim_int = int(best_analogue.similarity_score)
        best_sim = best_analogue.similarity_score if best_analogue else 0
        india_equiv = "EXISTS" if (india_adjusted and best_sim >= 60) else ("PARTIAL" if india_adjusted else "ABSENT")
        lines += [
            "",
            "HISTORICAL MATCH",
            f"{best_analogue.name} ({sim_int}% similar)",
            f"Tipped by: {_truncate(best_analogue.tipping_incident, 15)}",
            f"India equivalent: {india_equiv}",
        ]

    lines.append(_DIV)

    # ── SCENARIOS ───────────────────────────────────────────────────────────
    scenario_order = [
        ("probable",   "PROBABLE",   f"[{probabilities.probable_pct}%]"),
        ("plausible",  "PLAUSIBLE",  f"[{probabilities.plausible_pct}%]"),
        ("possible",   "POSSIBLE",   f"[{probabilities.possible_pct}%]"),
        ("preferable", "PREFERABLE", ""),
    ]

    for key, label, pct in scenario_order:
        s = scenarios.get(key)
        if not s:
            continue

        lines.append("")
        header_line = f"\u25a0 {label} {pct} \u2014 {s.name}".strip()
        lines.append(header_line)
        lines.append(_truncate(s.description, 20))

        # PROOF validation
        proof = s.proof
        if not _has_number_or_date(proof):
            proof = f"[WARNING: No number/date found] {proof}"
        lines.append(f"PROOF: {proof}")

        if label == "PREFERABLE":
            if s.needs_condition:
                lines.append(f"NEEDS: {_truncate(s.needs_condition, 15)}")
            if s.leverage:
                lines.append(f"LEVERAGE: {_truncate(s.leverage, 15)}")
        else:
            if s.if_condition:
                lines.append(f"IF: {_truncate(s.if_condition, 15)}")
            if s.but_condition:
                lines.append(f"BUT: {_truncate(s.but_condition, 15)}")

    lines += ["", _DIV]

    # ── THE ONE THING ────────────────────────────────────────────────────────
    lines.append("THE ONE THING")
    one_thing_lines = one_thing.strip().split("\n")
    for ln in one_thing_lines[:5]:   # enforce max 5 lines
        lines.append(ln)
    lines.append(_DIV)

    # ── INDIA LENS (conditional) ────────────────────────────────────────────
    if india_adjusted:
        lines += ["", "[INDIA LENS]"]
        try:
            from india_context import get_top_multipliers
            top = get_top_multipliers(2)
            mult_str = ", ".join(f"{s}/{t} ({v:.2f}x)" for s, t, v in top)
            lines.append(f"Multipliers moved: {mult_str}")
        except ImportError:
            pass

        if india_lens:
            for ln in india_lens.strip().split("\n")[:2]:
                lines.append(ln)

        lines.append(_DIV)

    text_report = "\n".join(lines)

    # ── JSON DATA ────────────────────────────────────────────────────────────
    data = {
        "query":         query,
        "date":          today,
        "confidence":    confidence,
        "signal_counts": sc,
        "net_direction": matrix.net_direction,
        "hottest_cell":  matrix.hottest_cell,
        "blind_zones":   matrix.blind_zones,
        "historical_match": {
            "name":             best_analogue.name             if best_analogue else None,
            "similarity":       best_analogue.similarity_score if best_analogue else None,
            "tipping_incident": best_analogue.tipping_incident if best_analogue else None,
        },
        "probabilities": {
            "probable":  probabilities.probable_pct,
            "plausible": probabilities.plausible_pct,
            "possible":  probabilities.possible_pct,
        },
        "scenarios": {
            k: {
                "name":          s.name,
                "description":   s.description,
                "proof":         s.proof,
                "if_condition":  s.if_condition,
                "but_condition": s.but_condition,
            }
            for k, s in scenarios.items()
        },
        "one_thing":      one_thing,
        "india_adjusted": india_adjusted,
    }

    return Report(text=text_report, data=data)


def format_rejection(query: str, validation: ValidationResult) -> str:
    """
    Format a clean rejection message for invalid queries.

    Args:
        query:      Original query string
        validation: Failed ValidationResult (valid=False)

    Returns:
        Formatted rejection string
    """
    lines = [
        "INVALID QUERY",
        f"Rule failed: {validation.rule_failed}",
        f"Reason: {validation.failure_reason}",
    ]
    if validation.scope_note:
        lines.append(f"Suggestion: {validation.scope_note}")
    return "\n".join(lines)


# ─── CLI ENTRY POINT ─────────────────────────────────────────────────────────

def format_from_dict(data: dict) -> str:
    """
    Format a complete report from a report_data dict.
    Used by the CLI main() and by the orchestrator.
    """
    query = data.get("query", "Unknown query")
    today = data.get("date", datetime.now().strftime("%Y-%m-%d"))
    confidence = int(data.get("confidence", 50))
    region = data.get("region")

    # Signal counts
    signals = data.get("signals", [])
    sc = data.get("signal_counts", {})
    if not sc and signals:
        sc = {"total": len(signals), "SUPPORTING": 0, "OPPOSING": 0,
              "NEUTRAL": 0, "WILDCARD": 0}
        for s in signals:
            st = s.get("signal_type", "NEUTRAL").upper()
            if st in sc:
                sc[st] += 1

    sup_n = sc.get("SUPPORTING", 0)
    opp_n = sc.get("OPPOSING", 0)
    wld_n = sc.get("WILDCARD", 0)
    tot_n = sc.get("total", len(signals))
    max_n = max(sup_n, opp_n, 1)

    net_direction = data.get("net_direction", "NEUTRAL")
    hottest_cell = data.get("hottest_cell", "Technological/Strategic")
    blind_zones = data.get("blind_zones", [])

    if blind_zones:
        blind_show = ", ".join(blind_zones[:3])
        if len(blind_zones) > 3:
            blind_show += f" (+{len(blind_zones) - 3} more)"
    else:
        blind_show = "None — full coverage"

    # Analogues
    analogues_raw = data.get("analogues", [])
    best_analogue = (
        max(analogues_raw, key=lambda a: float(a.get("similarity", a.get("similarity_score", 0))))
        if analogues_raw else None
    )

    # Probabilities
    probs = data.get("probabilities", {})
    prob_pct = probs.get("probable_pct", 33)
    pla_pct = probs.get("plausible_pct", 33)
    pos_pct = probs.get("possible_pct", 34)

    # Guidance
    guidance = data.get("guidance", {})

    # Scenarios
    scenarios = data.get("scenarios", {})

    # One thing
    the_one_thing = data.get("the_one_thing", {})

    lines: List[str] = []

    lines += [
        _DIV,
        "FORESIGHT ENGINE",
        query,
        f"Confidence: {confidence}/100 | Signals: {tot_n} | {today}",
        _DIV,
        "",
        "SIGNAL PULSE",
        (f"Supporting {sup_n} [{_bar(sup_n, max_n)}] | "
         f"Opposing {opp_n} [{_bar(opp_n, max_n)}] | "
         f"Wild {wld_n}"),
        f"Net: {net_direction}{' LEADS' if net_direction != 'NEUTRAL' else ''}",
        f"Hot zone: {hottest_cell}",
        f"Gap: {blind_show}",
    ]

    if best_analogue:
        sim = int(float(best_analogue.get("similarity", best_analogue.get("similarity_score", 0))))
        tip = best_analogue.get("tipping_incident", "")
        tip_short = _truncate(tip, 15)
        equiv = "EXISTS" if region else "NOT YET HAPPENED"
        lines += [
            "",
            "HISTORICAL MATCH",
            f"{best_analogue.get('name', 'Unknown')} ({sim}% similar)",
            f"Tipped by: {tip_short}",
            f"Equivalent now: {equiv}",
        ]

    lines.append("")
    lines.append(_DIV)

    scenario_order = [
        ("probable",   "PROBABLE",   f"[{prob_pct}%]"),
        ("plausible",  "PLAUSIBLE",  f"[{pla_pct}%]"),
        ("possible",   "POSSIBLE",   f"[{pos_pct}%]"),
        ("preferable", "PREFERABLE", ""),
    ]

    for key, label, pct in scenario_order:
        s = scenarios.get(key)
        if not s:
            continue
        name = s.get("name", key.title())
        desc = _truncate(s.get("description", ""), 25)
        proof = s.get("proof", "")
        if not _has_number_or_date(proof):
            proof = f"[WARNING: No number/date] {proof}"

        lines.append("")
        lines.append(f"\u25a0 {label} {pct} \u2014 {name}".strip())
        lines.append(desc)
        lines.append(f"PROOF: {proof}")

        if label == "PREFERABLE":
            if s.get("needs"):
                lines.append(f"NEEDS: {_truncate(s['needs'], 25)}")
            if s.get("leverage"):
                lines.append(f"LEVERAGE: {_truncate(s['leverage'], 25)}")
        else:
            if s.get("if_condition"):
                lines.append(f"IF: {_truncate(s['if_condition'], 25)}")
            if s.get("but_condition"):
                lines.append(f"BUT: {_truncate(s['but_condition'], 25)}")

    lines += ["", _DIV, ""]

    # THE ONE THING
    lines.append("THE ONE THING")
    if isinstance(the_one_thing, dict):
        reframe = the_one_thing.get("reframe", "")
        incident = the_one_thing.get("incident", "")
        watch = the_one_thing.get("watch_signal", "")
        if_yes = the_one_thing.get("if_yes", "")
        if_no = the_one_thing.get("if_no", "")
        if reframe:
            lines.append(reframe)
        if incident:
            lines.append(f"INCIDENT: {incident}")
        if watch:
            lines.append(f"WATCH: {watch}")
        if if_yes:
            lines.append(f"IF YES -> {if_yes}")
        if if_no:
            lines.append(f"IF NO -> {if_no}")
    else:
        for ln in str(the_one_thing).strip().split("\n")[:5]:
            lines.append(ln)

    lines += ["", _DIV, ""]

    # DECISION GUIDANCE
    lines.append("DECISION GUIDANCE")
    lines.append(f"Recommended stance: {guidance.get('recommended_stance', 'Assess signals before committing')}")
    lines.append(f"Low-regret move: {guidance.get('low_regret_move', 'Build capability in hot zone')}")
    lines.append(f"Risk trigger: {guidance.get('risk_trigger', 'Monitor opposing signals')}")

    # REGIONAL LENS
    if region and region != "global":
        lines += ["", f"[REGIONAL LENS — {region.upper()}]"]
        try:
            import os
            import sys as _sys
            src_dir = os.path.dirname(os.path.abspath(__file__))
            _sys.path.insert(0, src_dir)
            from regional_context import get_top_multipliers
            top = get_top_multipliers(region, 2)
            mult_str = ", ".join(f"{s}/{t} ({v:.2f}x)" for s, t, v in top)
            lines.append(f"Top multipliers: {mult_str}")
        except Exception:
            pass
        local_var = guidance.get("local_variable", "")
        if local_var:
            lines.append(f"Key local variable: {local_var}")

    lines.append(_DIV)
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: report_formatter.py report_data.json"}, indent=2))
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(json.dumps({"error": f"File not found: {input_path}"}, indent=2))
        sys.exit(1)

    with open(input_path) as f:
        data = json.load(f)

    report_text = format_from_dict(data)
    print(report_text)

    # Also save JSON version
    out_path = Path(sys.argv[1]).parent / "report_output.json"
    output_data = {
        "query": data.get("query", ""),
        "report_text": report_text,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "confidence": data.get("confidence", 50),
    }
    with open(out_path, "w") as f:
        json.dump(output_data, f, indent=2)

    sys.exit(0)


if __name__ == "__main__":
    main()
