#!/usr/bin/env python3
"""Validate text against Thumbtack brand guidelines.

Usage:
    python brand_validator.py --text "Check this copy for brand violations"
    python brand_validator.py path/to/file.md
    python brand_validator.py --text "..." --json   (machine-readable output)

Exit codes: 0 = pass, 1 = violations found, 2 = usage error
"""

import argparse
import json
import re
import sys
from pathlib import Path

# --- Violation rules -----------------------------------------------------------

RULES = [
    {
        "id": "wrong_blue_hex",
        "description": "Uses a blue hex that is not TT Blue #009FD9",
        "pattern": r"#(?:0[0-9a-fA-F]{2}(?:[89a-fA-F][0-9a-fA-F]|[0-9a-fA-F][89a-fA-F])[dD][0-9a-fA-F])",
        "exclude": ["#009FD9", "#009fd9", "#3EB6E3", "#3eb6e3", "#99DAF0", "#99daf0",
                     "#D1ECF7", "#d1ecf7", "#18A2D5", "#18a2d5", "#019ED9", "#019ed9",
                     "#79D2F2", "#79d2f2"],
        "check": "regex_with_exclude",
    },
    {
        "id": "non_brand_font",
        "description": "References a non-brand font (use Thumbtack Rise or Montserrat)",
        "pattern": r"\b(?:Arial|Helvetica|Times New Roman|Calibri|Roboto|Open Sans|Lato|Poppins|Inter|Comic Sans)\b",
        "check": "regex",
    },
    {
        "id": "rounded_corners",
        "description": "Mentions rounded corners (brand uses sharp 90-degree corners only)",
        "pattern": r"\brounded\s+corner",
        "check": "regex",
    },
    {
        "id": "drop_shadow",
        "description": "Mentions drop shadows on text (off-brand)",
        "pattern": r"\bdrop[\s-]?shadow",
        "check": "regex",
    },
    {
        "id": "quarter_circle",
        "description": "Mentions quarter circles (only full circles, half circles, or rectangles)",
        "pattern": r"\bquarter[\s-]?circle",
        "check": "regex",
    },
    {
        "id": "punny_language",
        "description": "Uses puns or overly cute wordplay (brand is Natural, not cutesy)",
        "pattern": r"\b(?:nail(?:ed|ing) it|hammer(?:ed|ing) (?:home|out)|screw(?:ed|ing) (?:up|around)|drill(?:ed|ing) down|a cut above|raising the (?:bar|roof)|tack-tic|thumbs? up for|pin-point|on point)\b",
        "check": "regex",
    },
    {
        "id": "overly_aspirational",
        "description": "Uses lofty/aspirational language (brand is Grounded, not slick)",
        "pattern": r"\b(?:revolutionary|revolutioniz(?:e|ed|ing|es)|transformative|game[\s-]?chang(?:er|ing|ed)|disruptive|disruptor|world[\s-]?class|cutting[\s-]?edge|best[\s-]?in[\s-]?class|next[\s-]?gen(?:eration)?|paradigm|synergy|leverage|unlock(?:ing)?\s+(?:your|the)\s+(?:potential|power|future))\b",
        "check": "regex",
    },
    {
        "id": "excessive_hype",
        "description": "Uses exclamation-heavy or ALL CAPS hype (brand is grounded)",
        "pattern": r"!!+",
        "check": "regex",
    },
]


def check_text(text: str) -> list[dict]:
    """Return a list of violations found in the given text."""
    violations = []
    for rule in RULES:
        if rule["check"] == "regex":
            matches = list(re.finditer(rule["pattern"], text, re.IGNORECASE))
            for m in matches:
                violations.append({
                    "rule": rule["id"],
                    "description": rule["description"],
                    "match": m.group(),
                    "position": m.start(),
                })
        elif rule["check"] == "regex_with_exclude":
            matches = list(re.finditer(rule["pattern"], text, re.IGNORECASE))
            for m in matches:
                if m.group().upper() not in [e.upper() for e in rule.get("exclude", [])]:
                    violations.append({
                        "rule": rule["id"],
                        "description": rule["description"],
                        "match": m.group(),
                        "position": m.start(),
                    })
    return violations


def main():
    parser = argparse.ArgumentParser(description="Validate text against Thumbtack brand guidelines")
    parser.add_argument("file", nargs="?", help="File to validate")
    parser.add_argument("--text", "-t", help="Text to validate directly")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    if args.text:
        text = args.text
    elif args.file:
        path = Path(args.file)
        if not path.exists():
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(2)
        text = path.read_text()
    else:
        parser.print_help()
        sys.exit(2)

    violations = check_text(text)
    result = {
        "passed": len(violations) == 0,
        "violation_count": len(violations),
        "violations": violations,
    }

    if args.json:
        json.dump(result, sys.stdout, indent=2)
        print()
    else:
        if result["passed"]:
            print("PASS — No brand violations found.")
        else:
            print(f"FAIL — {result['violation_count']} brand violation(s) found:\n")
            for v in violations:
                print(f"  [{v['rule']}] {v['description']}")
                print(f"    Match: \"{v['match']}\" at position {v['position']}\n")

    sys.exit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
