#!/usr/bin/env python3
"""
input_validator.py - Binary gate for query validation.
Pure deterministic logic. No AI, no web calls.
Author: Santhosh Gandhi

Usage: python src/input_validator.py "query string"
Output: JSON to stdout
"""

from __future__ import annotations
import re
import sys
import json
from dataclasses import dataclass, asdict
from typing import Callable, List, Optional


@dataclass
class ValidationResult:
    valid: bool
    rule_failed: Optional[str]
    failure_reason: Optional[str]
    scope_note: Optional[str]
    proceed: bool


# --- KNOWN FICTIONAL / NON-EXISTENT SETS ---

_FICTIONAL_CHARACTERS = {
    "harry potter", "sherlock holmes", "batman", "superman",
    "iron man", "spider-man", "spiderman", "gandalf", "frodo",
    "darth vader", "voldemort", "hermione", "dumbledore", "tony stark",
    "captain america", "thanos", "hermione granger",
}

_NON_EARTH_BODIES = {
    "mars", "moon", "jupiter", "saturn", "neptune", "uranus",
    "pluto", "venus", "mercury", "galaxy", "universe", "multiverse",
    "planet x", "nibiru",
}

_POLITICAL_TITLES = {
    "president", "prime minister", "pm", "king", "queen", "emperor",
    "chancellor", "premier", "secretary general", "governor", "dictator",
}

_GEOLOGICAL_PATTERNS = [
    r"\b(million|billion)\s+years?\b",
    r"\b[1-9]\d{4,}\s*(ad|ce|bc|bce)?\b",
    r"\bpost.?human\b",
    r"\bheat.?death\b",
    r"\bend\s+of\s+(all\s+)?life\b",
]

_VAGUE_CATCHALL_PATTERNS = [
    r"^what\s+will\s+happen\s*\??$",
    r"^what\s+happens\s+next\s*\??$",
    r"^what\s+is\s+the\s+future\s*\??$",
    r"^predict\s+the\s+future\s*\??$",
    r"^what\s+comes\s+next\s*\??$",
    r"^tell\s+me\s+the\s+future\s*\??$",
]

_PRIVATE_INDIVIDUAL_PATTERNS = [
    r"\bmy\s+(friend|neighbor|neighbour|colleague|classmate|boss|wife|husband|partner|sibling|brother|sister)\b",
    r"\bthis\s+(guy|person|girl|woman|man)\b",
    r"\bsomeone\s+i\s+know\b",
    r"\ba\s+person\s+i\s+know\b",
]

_PUBLIC_DOMAIN_KEYWORDS = {
    "india", "china", "us", "usa", "uk", "europe", "global", "world",
    "sector", "industry", "market", "technology", "tech", "ai",
    "ev", "electric", "saas", "fintech", "healthcare", "energy",
    "policy", "government", "economy", "startup", "company",
    "bitcoin", "crypto", "stock", "real estate", "climate", "war",
    "election", "will", "could", "might", "would", "become", "happen",
}


# --- RULE IMPLEMENTATIONS ---

def _rule1_entity_reality(query: str) -> Optional[ValidationResult]:
    q = query.lower()
    for char in _FICTIONAL_CHARACTERS:
        if char in q:
            return ValidationResult(
                valid=False,
                rule_failed="RULE_1",
                failure_reason=f"'{char.title()}' is a fictional character, not a real-world entity.",
                scope_note="Rephrase with a real named person, company, sector, technology, policy, or country.",
                proceed=False,
            )
    for pattern in _PRIVATE_INDIVIDUAL_PATTERNS:
        if re.search(pattern, q):
            return ValidationResult(
                valid=False,
                rule_failed="RULE_1",
                failure_reason="Query references an unnamed private individual with no public presence.",
                scope_note="Rephrase with a named public figure, company, sector, or policy.",
                proceed=False,
            )
    return None


def _rule2_system_existence(query: str) -> Optional[ValidationResult]:
    q = query.lower()
    for body in _NON_EARTH_BODIES:
        for title in _POLITICAL_TITLES:
            if (re.search(rf"\b{re.escape(title)}\s+of\s+(the\s+)?{re.escape(body)}\b", q)
                    or re.search(rf"\b{re.escape(body)}\b.*\b{re.escape(title)}\b", q)
                    or re.search(rf"\b{re.escape(title)}\b.{{0,30}}\b{re.escape(body)}\b", q)):
                return ValidationResult(
                    valid=False,
                    rule_failed="RULE_2",
                    failure_reason=f"{body.title()} has no political system or human governance structure.",
                    scope_note="Rephrase with a real-world political office or system.",
                    proceed=False,
                )
    if re.search(r"\b(king|queen|president|ruler)\s+of\s+(the\s+)?internet\b", q):
        return ValidationResult(
            valid=False,
            rule_failed="RULE_2",
            failure_reason="The Internet has no political governance structure.",
            scope_note="Rephrase with a real-world institution or jurisdiction.",
            proceed=False,
        )
    return None


def _rule3_time_horizon(query: str) -> Optional[ValidationResult]:
    q = query.lower()
    for pattern in _GEOLOGICAL_PATTERNS:
        if re.search(pattern, q):
            return ValidationResult(
                valid=False,
                rule_failed="RULE_3",
                failure_reason="Query implies a geological or post-human timescale beyond the 30-year analysis window.",
                scope_note="Rephrase with a specific near/medium/long-term timeframe (e.g., by 2030, within a decade).",
                proceed=False,
            )
    for year_str in re.findall(r"\b(20[6-9]\d|2[1-9]\d{2}|[3-9]\d{3,})\b", query):
        if int(year_str) > 2056:
            return ValidationResult(
                valid=False,
                rule_failed="RULE_3",
                failure_reason=f"Year {year_str} is beyond the 30-year analysis window.",
                scope_note="Use a timeframe within 30 years for meaningful signal-based forecasting.",
                proceed=False,
            )
    return None


def _rule4_signal_availability(query: str) -> Optional[ValidationResult]:
    q = query.lower()
    private_patterns = [
        r"\bmy\s+(company|firm|startup|business)\s+(internal|private)\b",
        r"\binternal\s+(decision|policy|plan)\s+of\b",
        r"\bprivate\s+(conversation|meeting|email)\b",
    ]
    for pattern in private_patterns:
        if re.search(pattern, q):
            return ValidationResult(
                valid=False,
                rule_failed="RULE_4",
                failure_reason="Query references purely private internal decisions with no public signal trail.",
                scope_note="Rephrase to focus on publicly observable outcomes or industry trends.",
                proceed=False,
            )
    unknowable_patterns = [
        r"\bwill\s+my\s+(neighbor|neighbour|colleague|classmate)\b",
    ]
    for pattern in unknowable_patterns:
        if re.search(pattern, q):
            return ValidationResult(
                valid=False,
                rule_failed="RULE_4",
                failure_reason="Private individuals have no public signal trail for web-based analysis.",
                scope_note="Rephrase with a public figure, company, sector, or policy.",
                proceed=False,
            )
    return None


def _rule5_minimum_specificity(query: str) -> Optional[ValidationResult]:
    stripped = query.strip()
    q = stripped.lower()
    for pattern in _VAGUE_CATCHALL_PATTERNS:
        if re.match(pattern, q):
            return ValidationResult(
                valid=False,
                rule_failed="RULE_5",
                failure_reason="Query has no identifiable subject or domain.",
                scope_note="Add a specific subject: 'Will [X] happen?' where X is a named entity, sector, or trend.",
                proceed=False,
            )
    words = stripped.split()
    if len(words) < 5:
        return ValidationResult(
            valid=False,
            rule_failed="RULE_5",
            failure_reason=f"Query is too short ({len(words)} words). Insufficient context for analysis.",
            scope_note="Provide at least a subject and a specific outcome to analyze.",
            proceed=False,
        )
    has_proper_noun = bool(re.search(r"\b[A-Z][a-z]{1,}\b", stripped))
    has_domain_term = any(kw in q for kw in _PUBLIC_DOMAIN_KEYWORDS)
    if not has_proper_noun and not has_domain_term:
        return ValidationResult(
            valid=False,
            rule_failed="RULE_5",
            failure_reason="Query lacks any identifiable named entity, sector, or domain.",
            scope_note="Name a specific person, company, industry, policy, or technology to analyze.",
            proceed=False,
        )
    return None


# --- PUBLIC API ---

_RULES: List[Callable[[str], Optional[ValidationResult]]] = [
    _rule1_entity_reality,
    _rule2_system_existence,
    _rule3_time_horizon,
    _rule4_signal_availability,
    _rule5_minimum_specificity,
]


def validate(query: str) -> ValidationResult:
    if not query or not query.strip():
        return ValidationResult(
            valid=False,
            rule_failed="RULE_5",
            failure_reason="Empty query provided.",
            scope_note="Provide a specific forecasting question.",
            proceed=False,
        )
    for rule in _RULES:
        result = rule(query)
        if result is not None:
            return result
    return ValidationResult(
        valid=True,
        rule_failed=None,
        failure_reason=None,
        scope_note=None,
        proceed=True,
    )


def format_rejection(result: ValidationResult) -> str:
    rule_names = {
        "RULE_1": "Entity reality",
        "RULE_2": "System existence",
        "RULE_3": "Time horizon",
        "RULE_4": "Signal availability",
        "RULE_5": "Minimum specificity",
    }
    rule_name = rule_names.get(result.rule_failed or "", result.rule_failed or "")
    lines = [
        "INVALID QUERY",
        f"Rule failed: {result.rule_failed} - {rule_name}",
        f"Reason: {result.failure_reason}",
    ]
    if result.scope_note:
        lines.append(f"Suggestion: {result.scope_note}")
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        result = ValidationResult(
            valid=False,
            rule_failed="RULE_5",
            failure_reason="No query provided.",
            scope_note="Provide a query string as argument.",
            proceed=False,
        )
        print(json.dumps(asdict(result), indent=2))
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    result = validate(query)
    print(json.dumps(asdict(result), indent=2))

    if not result.valid:
        print()
        print(format_rejection(result))
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
