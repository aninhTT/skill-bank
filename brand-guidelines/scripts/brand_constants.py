#!/usr/bin/env python3
"""Thumbtack brand constants as structured JSON + font registration helpers.

Run standalone:  python brand_constants.py          → prints full JSON
Import:          from brand_constants import BRAND  → dict
Fonts:           from brand_constants import register_thumbtack_fonts
                 → registers Thumbtack Rise with reportlab (returns True/False)
"""

import json
import os
import sys

BRAND = {
    "colors": {
        "primary": {
            "tt_blue":   {"hex": "#009FD9", "rgb": [0, 159, 217],   "cmyk": [77, 25, 0, 0]},
            "black":     {"hex": "#2F3033", "rgb": [47, 58, 51],    "cmyk": [63, 62, 59, 88]},
            "black_300": {"hex": "#676D73", "rgb": [103, 109, 115], "cmyk": [23, 16, 13, 46]},
            "gray":      {"hex": "#D3D4D5", "rgb": [211, 212, 213], "cmyk": None},
            "gray_300":  {"hex": "#E9ECED", "rgb": [233, 236, 237], "cmyk": None},
            "gray_200":  {"hex": "#FAFAFA", "rgb": [250, 250, 250], "cmyk": None},
            "white":     {"hex": "#FFFFFF", "rgb": [255, 255, 255], "cmyk": [0, 0, 0, 0]},
        },
        "secondary": {
            "purple": {"hex": "#8D56EB", "rgb": [141, 86, 235],  "cmyk": [37, 58, 0, 8],  "usage": "Educational, announcements"},
            "indigo": {"hex": "#5968E2", "rgb": [89, 104, 226],  "cmyk": [54, 48, 0, 11], "usage": "Educational, announcements"},
            "green":  {"hex": "#2DB783", "rgb": [45, 183, 131],  "cmyk": [54, 0, 20, 28], "usage": "Educational, announcements"},
            "yellow": {"hex": "#FEBE14", "rgb": [254, 190, 20],  "cmyk": [0, 25, 92, 0],  "usage": "Educational, announcements"},
            "red":    {"hex": "#FF5A5F", "rgb": [255, 90, 95],   "cmyk": [0, 65, 63, 0],  "usage": "Warnings/errors only"},
        },
        "blue_tints": ["#3EB6E3", "#99DAF0", "#D1ECF7"],
        "indigo_tints": ["#808BE8", "#9CA4EF", "#BDC3F3", "#DFE1FA"],
        "yellow_tints": ["#FFDD80", "#FFEBB3"],
    },
    "typography": {
        "external": {
            "family": "Thumbtack Rise",
            "weights": ["Light", "Regular", "Medium", "Bold", "Heavy"],
            "usage": {
                "headlines": ["Bold", "Heavy"],
                "subheads": ["Medium", "Bold"],
                "body": ["Light", "Regular"],
                "captions": ["Light"],
            },
        },
        "internal": {
            "family": "Montserrat",
            "note": "Used for Google apps (Slides, Docs, Sheets) and internal presentations",
        },
    },
    "slide_dimensions": {
        "width_inches": 10.0,
        "height_inches": 5.6,
        "width_emu": 9144000,
        "height_emu": 5080000,
        "aspect_ratio": "widescreen",
    },
    "slide_typography": {
        "title": {"font": "Montserrat", "weight": "Medium", "size_pt": 57, "color": "#2F3033"},
        "section_eyebrow": {"font": "Montserrat", "weight": "ExtraBold", "size_pt": 9, "color": "#009FD9", "transform": "ALL CAPS"},
        "section_statement": {"font": "Montserrat", "weight": "Medium", "size_pt": 40, "color": "#2F3033"},
        "content_title": {"font": "Montserrat", "weight": "Medium", "size_pt": 23, "color": "#2F3033"},
        "body": {"font": "Montserrat", "weight": "Medium", "size_pt": 11, "color": "#2F3033"},
        "metadata_tag": {"font": "Montserrat", "weight": "SemiBold", "size_pt": 12, "color": "#2F3033"},
        "footer": {"font": "Montserrat", "weight": "SemiBold", "size_pt": 7, "color": "#79D2F2"},
        "card_title": {"font": "Montserrat", "weight": "SemiBold", "size_pt": 21, "color": "#2F3033"},
        "card_body": {"font": "Montserrat", "weight": "Medium", "size_pt": 11, "color": "#2F3033"},
        "numbered_item": {"font": "Montserrat", "weight": "SemiBold", "size_pt": 17, "color": "#2F3033"},
    },
    "logo": {
        "variants": ["Full logo (Tack + Wordmark)", "The Tack (standalone)"],
        "layouts": ["Horizontal", "Vertical/Stacked"],
        "color_modes": ["Two-color (blue Tack + black Wordmark)", "All-black", "All-white"],
        "clear_space": "x-height of Wordmark 'u'",
    },
    "voice": {
        "attributes": ["Relatable", "Grounded", "Natural"],
        "tones": ["Celebratory", "Instructive", "Playful", "Reassuring", "Encouraging", "Supportive", "Helpful"],
    },
    "brand_values": ["Convenience", "Reliability", "Achievement"],
}


# ---------------------------------------------------------------------------
# Font file paths (relative to this script → resolved at runtime)
# ---------------------------------------------------------------------------
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_FONT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "..", "assets", "fonts"))

FONT_FILES = {
    "ThumbtackRise-Light":   os.path.join(_FONT_DIR, "ThumbtackRise-Light.ttf"),
    "ThumbtackRise-Regular": os.path.join(_FONT_DIR, "ThumbtackRise-Regular.ttf"),
    "ThumbtackRise-Medium":  os.path.join(_FONT_DIR, "ThumbtackRise-Medium.ttf"),
    "ThumbtackRise-Bold":    os.path.join(_FONT_DIR, "ThumbtackRise-Bold.ttf"),
    "ThumbtackRise-Heavy":   os.path.join(_FONT_DIR, "ThumbtackRise-Heavy.ttf"),
    "ThumbtackRise-Italic":  os.path.join(_FONT_DIR, "ThumbtackRise-Italic.ttf"),
}

# Mapping from brand weight names → reportlab registered font names
FONT_WEIGHT_MAP = {
    "Light":   "ThumbtackRise-Light",
    "Regular": "ThumbtackRise-Regular",
    "Medium":  "ThumbtackRise-Medium",
    "Bold":    "ThumbtackRise-Bold",
    "Heavy":   "ThumbtackRise-Heavy",
    "Italic":  "ThumbtackRise-Italic",
}

# Fallback mapping (Helvetica) when Thumbtack Rise is not available
FONT_FALLBACK_MAP = {
    "Light":   "Helvetica",
    "Regular": "Helvetica",
    "Medium":  "Helvetica",
    "Bold":    "Helvetica-Bold",
    "Heavy":   "Helvetica-Bold",
    "Italic":  "Helvetica-Oblique",
}


def fonts_available() -> bool:
    """Check whether all Thumbtack Rise font files exist on disk."""
    return all(os.path.isfile(p) for p in FONT_FILES.values())


def register_thumbtack_fonts() -> bool:
    """Register Thumbtack Rise fonts with reportlab's pdfmetrics.

    Returns True if registration succeeded, False if fonts are missing
    and the caller should fall back to Helvetica.

    Usage:
        from brand_constants import register_thumbtack_fonts, get_font
        registered = register_thumbtack_fonts()
        font_name = get_font("Bold")  # → "ThumbtackRise-Bold" or "Helvetica-Bold"
    """
    if not fonts_available():
        return False

    try:
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont

        for name, path in FONT_FILES.items():
            try:
                pdfmetrics.registerFont(TTFont(name, path))
            except Exception:
                return False
        return True
    except ImportError:
        return False


def get_font(weight: str = "Regular", *, _registered: list = []) -> str:
    """Return the correct font name for a given brand weight.

    Auto-registers fonts on first call. Falls back to Helvetica if
    Thumbtack Rise is unavailable.

    Args:
        weight: One of Light, Regular, Medium, Bold, Heavy, Italic

    Returns:
        Reportlab font name string (e.g. "ThumbtackRise-Bold" or "Helvetica-Bold")
    """
    if not _registered:
        _registered.append(register_thumbtack_fonts())

    if _registered[0]:
        return FONT_WEIGHT_MAP.get(weight, "ThumbtackRise-Regular")
    else:
        return FONT_FALLBACK_MAP.get(weight, "Helvetica")


if __name__ == "__main__":
    json.dump(BRAND, sys.stdout, indent=2)
    print()
    print(f"\nFont directory: {_FONT_DIR}")
    print(f"Fonts available: {fonts_available()}")
    if fonts_available():
        for name, path in FONT_FILES.items():
            print(f"  ✓ {name}: {path}")
    else:
        missing = [n for n, p in FONT_FILES.items() if not os.path.isfile(p)]
        print(f"  Missing: {missing}")
