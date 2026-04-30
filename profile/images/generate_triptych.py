"""
Generate: triptych-know-decide-prove.svg

Visual: the three pillars of the Diplomat-ai ecosystem.
- diplomat-agent (Know)  — static AST scan, pre-deploy
- diplomat-gate  (Decide) — runtime enforcement, < 1ms, zero deps
- diplomat.run   (Prove)  — hosted control plane, audit + compliance

Reproducible — committed to profile/images/generate_triptych.py for
maintainability. Stdlib only (xml.etree.ElementTree, pathlib).
Regenerate: python profile/images/generate_triptych.py
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

# ---------------------------------------------------------------------------
# Design tokens (aligned with diplomat-gate / diplomat-agent README visuals)
# ---------------------------------------------------------------------------

BG = "#FFFFFF"
TEXT_PRIMARY = "#0F172A"
TEXT_MUTED = "#64748B"
TEXT_SUBTLE = "#94A3B8"
BORDER_SOFT = "#E2E8F0"

# Brand indigo (gate)
INDIGO_FILL = "#4F46E5"
INDIGO_STROKE = "#312E81"
INDIGO_LIGHT = "#E0E7FF"

# Stage palette — desaturated, professional, distinct
STAGES = [
    {
        "name": "diplomat-agent",
        "stage": "KNOW",
        "tagline": "Static AST scan",
        "detail": "Pre-deploy. Maps every tool call with side effects.",
        "fill": "#FEF3C7",      # warm amber bg
        "stroke": "#FCD34D",
        "accent": "#B45309",
        "footer": "Open source · Apache 2.0",
    },
    {
        "name": "diplomat-gate",
        "stage": "DECIDE",
        "tagline": "Runtime enforcement",
        "detail": "CONTINUE / REVIEW / STOP in <1 ms. Zero deps.",
        "fill": INDIGO_LIGHT,
        "stroke": "#A5B4FC",
        "accent": INDIGO_FILL,
        "footer": "Open source · Apache 2.0",
    },
    {
        "name": "diplomat.run",
        "stage": "PROVE",
        "tagline": "Decision Control Plane",
        "detail": "Hash-chained audit. Compliance export. Hosted.",
        "fill": "#D1FAE5",
        "stroke": "#6EE7B7",
        "accent": "#047857",
        "footer": "Hosted · diplomat.run",
    },
]

FONT_FAMILY = (
    "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', "
    "Roboto, 'Helvetica Neue', Arial, sans-serif"
)

# ---------------------------------------------------------------------------
# Canvas geometry
# ---------------------------------------------------------------------------

W, H = 1200, 520

# Section header
HEADER_Y = 60

# Card row
CARD_Y = 130
CARD_H = 280
CARD_W = 340
GAP = 30
TOTAL_CARDS_W = 3 * CARD_W + 2 * GAP
CARD_X_START = (W - TOTAL_CARDS_W) // 2  # = 60

# Footer
FOOTER_Y = H - 30


# ---------------------------------------------------------------------------
# SVG helpers
# ---------------------------------------------------------------------------


def svg_root() -> ET.Element:
    root = ET.Element(
        "svg",
        {
            "xmlns": "http://www.w3.org/2000/svg",
            "viewBox": f"0 0 {W} {H}",
            "width": str(W),
            "height": str(H),
            "role": "img",
            "aria-labelledby": "title desc",
        },
    )
    ET.SubElement(root, "title", {"id": "title"}).text = (
        "Diplomat-ai ecosystem: Know, Decide, Prove"
    )
    ET.SubElement(root, "desc", {"id": "desc"}).text = (
        "Three products spanning the AI agent governance lifecycle: "
        "diplomat-agent maps tool calls statically (Know), diplomat-gate "
        "enforces policy at runtime (Decide), diplomat.run provides hosted "
        "audit and compliance (Prove)."
    )

    ET.SubElement(
        root,
        "rect",
        {"x": "0", "y": "0", "width": str(W), "height": str(H), "fill": BG},
    )
    return root


def rounded_rect(parent, x, y, w, h, fill, stroke, stroke_w=1.5, r=12):
    ET.SubElement(
        parent,
        "rect",
        {
            "x": str(x),
            "y": str(y),
            "width": str(w),
            "height": str(h),
            "rx": str(r),
            "ry": str(r),
            "fill": fill,
            "stroke": stroke,
            "stroke-width": str(stroke_w),
        },
    )


def text(parent, x, y, content, *, size=14, weight="400",
         color=TEXT_PRIMARY, anchor="start"):
    el = ET.SubElement(
        parent,
        "text",
        {
            "x": str(x),
            "y": str(y),
            "font-family": FONT_FAMILY,
            "font-size": str(size),
            "font-weight": weight,
            "fill": color,
            "text-anchor": anchor,
        },
    )
    el.text = content


def arrow(parent, x1, y, x2, color=TEXT_SUBTLE):
    """Horizontal arrow with chevron, between cards."""
    ET.SubElement(
        parent,
        "line",
        {
            "x1": str(x1),
            "y1": str(y),
            "x2": str(x2 - 8),
            "y2": str(y),
            "stroke": color,
            "stroke-width": "1.5",
            "stroke-linecap": "round",
        },
    )
    # chevron
    chevron = f"M {x2 - 10} {y - 5} L {x2} {y} L {x2 - 10} {y + 5}"
    ET.SubElement(
        parent,
        "path",
        {
            "d": chevron,
            "fill": "none",
            "stroke": color,
            "stroke-width": "1.5",
            "stroke-linecap": "round",
            "stroke-linejoin": "round",
        },
    )


# ---------------------------------------------------------------------------
# Compose
# ---------------------------------------------------------------------------


def build() -> ET.Element:
    root = svg_root()

    # Section header (small caps, muted)
    text(
        root, W / 2, HEADER_Y,
        "GOVERNANCE AND RUNTIME SAFETY FOR AI AGENTS",
        size=12, weight="700", color=TEXT_MUTED, anchor="middle",
    )
    text(
        root, W / 2, HEADER_Y + 28,
        "Three products. One ecosystem. Open source first.",
        size=18, weight="600", color=TEXT_PRIMARY, anchor="middle",
    )

    # Cards
    for i, stage in enumerate(STAGES):
        x = CARD_X_START + i * (CARD_W + GAP)

        # Card body
        rounded_rect(
            root, x, CARD_Y, CARD_W, CARD_H,
            fill=stage["fill"], stroke=stage["stroke"], stroke_w=1.8, r=14,
        )

        # Stage chip (small caps badge inside the card)
        chip_w = 80
        chip_x = x + 24
        chip_y = CARD_Y + 24
        rounded_rect(
            root, chip_x, chip_y, chip_w, 24,
            fill="#FFFFFF", stroke=stage["stroke"], stroke_w=1, r=12,
        )
        text(
            root, chip_x + chip_w / 2, chip_y + 16,
            stage["stage"],
            size=11, weight="700", color=stage["accent"], anchor="middle",
        )

        # Product name
        text(
            root, x + 24, CARD_Y + 88,
            stage["name"],
            size=22, weight="700", color=TEXT_PRIMARY,
        )

        # Tagline
        text(
            root, x + 24, CARD_Y + 118,
            stage["tagline"],
            size=14, weight="600", color=stage["accent"],
        )

        # Detail (one line, can wrap if needed — kept short on purpose)
        text(
            root, x + 24, CARD_Y + 158,
            stage["detail"],
            size=13, weight="400", color=TEXT_PRIMARY,
        )

        # Divider near footer
        ET.SubElement(
            root, "line",
            {
                "x1": str(x + 24), "y1": str(CARD_Y + CARD_H - 50),
                "x2": str(x + CARD_W - 24), "y2": str(CARD_Y + CARD_H - 50),
                "stroke": stage["stroke"], "stroke-width": "1", "opacity": "0.6",
            },
        )

        # Footer (license / hosted)
        text(
            root, x + 24, CARD_Y + CARD_H - 24,
            stage["footer"],
            size=12, weight="500", color=TEXT_MUTED,
        )

        # Arrow between cards
        if i < len(STAGES) - 1:
            arrow_y = CARD_Y + CARD_H / 2
            arrow(root, x + CARD_W + 4, arrow_y, x + CARD_W + GAP - 4)

    # Footnote
    text(
        root, W / 2, FOOTER_Y,
        "Know what your agent can do. Decide what it should. Prove what it did.",
        size=13, weight="500", color=TEXT_MUTED, anchor="middle",
    )

    return root


def main():
    out_dir = Path(__file__).parent
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "triptych-know-decide-prove.svg"

    root = build()
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"\u2713 wrote {out_path}")


if __name__ == "__main__":
    main()
