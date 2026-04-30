"""
Generate: benchmark-unguarded.svg

Visual: the 76% benchmark — across 16 open-source agent repos scanned with
diplomat-agent, 76% of tool calls with side effects had zero deterministic
guards. This is the strongest hook of the org.

Reproducible — committed to profile/images/generate_benchmark.py for
maintainability. Stdlib only. Regenerate:
    python profile/images/generate_benchmark.py
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

# ---------------------------------------------------------------------------
# Design tokens
# ---------------------------------------------------------------------------

BG = "#FFFFFF"
TEXT_PRIMARY = "#0F172A"
TEXT_MUTED = "#64748B"
TEXT_SUBTLE = "#94A3B8"
BORDER_SOFT = "#E2E8F0"

# Risk semantics — matches gate verdict palette
RED_FILL = "#EF4444"      # unguarded — STOP-equivalent risk
RED_STROKE = "#991B1B"
RED_LIGHT = "#FEE2E2"

GREEN_FILL = "#10B981"    # guarded
GREEN_STROKE = "#047857"
GREEN_LIGHT = "#D1FAE5"

INDIGO_ACCENT = "#4F46E5"

FONT_FAMILY = (
    "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', "
    "Roboto, 'Helvetica Neue', Arial, sans-serif"
)

# Data — sourced from REALITY_CHECK_RESULTS.md (top 4 publicly-named repos)
# Other 12 repos aggregated into "12 more agent repos" for the bar chart.
REPOS = [
    {"name": "PraisonAI",  "calls": 1028, "unguarded": 911, "pct": 89},
    {"name": "CrewAI",     "calls": 348,  "unguarded": 273, "pct": 78},
    {"name": "Skyvern",    "calls": 452,  "unguarded": 345, "pct": 76},
    {"name": "Dify",       "calls": 1009, "unguarded": 759, "pct": 75},
]

# ---------------------------------------------------------------------------
# Canvas
# ---------------------------------------------------------------------------

W, H = 1200, 560

# Two-column layout: big stat on the left, repo bars on the right
STAT_X = 60
STAT_W = 460

BARS_X = 580
BARS_W = 560
BARS_TOP = 140
ROW_H = 70

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
        "76% of AI agent tool calls have zero deterministic guards"
    )
    ET.SubElement(root, "desc", {"id": "desc"}).text = (
        "Bar chart of four open-source AI agent repositories scanned with "
        "diplomat-agent: PraisonAI (89% unguarded), CrewAI (78%), "
        "Skyvern (76%), Dify (75%). Aggregate across 16 repos: 76% of tool "
        "calls with real-world side effects had no guards."
    )
    ET.SubElement(
        root, "rect",
        {"x": "0", "y": "0", "width": str(W), "height": str(H), "fill": BG},
    )
    return root


def rounded_rect(parent, x, y, w, h, fill, stroke, stroke_w=1.5, r=8):
    ET.SubElement(
        parent, "rect",
        {
            "x": str(x), "y": str(y),
            "width": str(w), "height": str(h),
            "rx": str(r), "ry": str(r),
            "fill": fill, "stroke": stroke,
            "stroke-width": str(stroke_w),
        },
    )


def text(parent, x, y, content, *, size=14, weight="400",
         color=TEXT_PRIMARY, anchor="start"):
    el = ET.SubElement(
        parent, "text",
        {
            "x": str(x), "y": str(y),
            "font-family": FONT_FAMILY,
            "font-size": str(size),
            "font-weight": weight,
            "fill": color,
            "text-anchor": anchor,
        },
    )
    el.text = content


# ---------------------------------------------------------------------------
# Compose
# ---------------------------------------------------------------------------


def build() -> ET.Element:
    root = svg_root()

    # Header band
    text(
        root, STAT_X, 60,
        "BENCHMARK · 16 OPEN-SOURCE AGENT REPOS",
        size=12, weight="700", color=TEXT_MUTED,
    )

    # ---- Left column: the headline number ----

    # Big "76%"
    text(
        root, STAT_X, 220,
        "76%",
        size=140, weight="800", color=RED_FILL,
    )

    # Subtitle
    text(
        root, STAT_X, 270,
        "of AI agent tool calls",
        size=20, weight="600", color=TEXT_PRIMARY,
    )
    text(
        root, STAT_X, 300,
        "have ZERO deterministic guards.",
        size=20, weight="600", color=TEXT_PRIMARY,
    )

    # Method line
    text(
        root, STAT_X, 350,
        "Aggregated across 16 popular open-source",
        size=13, weight="400", color=TEXT_MUTED,
    )
    text(
        root, STAT_X, 370,
        "AI agent repos. Scanned with diplomat-agent.",
        size=13, weight="400", color=TEXT_MUTED,
    )

    # CTA pill
    cta_y = 410
    rounded_rect(
        root, STAT_X, cta_y, 300, 44,
        fill="#0F172A", stroke="#0F172A", stroke_w=1, r=8,
    )
    text(
        root, STAT_X + 20, cta_y + 28,
        "$ pip install diplomat-agent",
        size=14, weight="600", color="#FFFFFF",
    )

    # Footnote under CTA
    text(
        root, STAT_X, cta_y + 70,
        "Run the same scan on your codebase in ~2 seconds.",
        size=12, weight="500", color=TEXT_MUTED,
    )

    # ---- Right column: per-repo bars ----

    # Column header
    text(
        root, BARS_X, 90,
        "% of tool calls without any deterministic guard",
        size=13, weight="600", color=TEXT_MUTED,
    )

    # Bars
    bar_label_w = 130
    bar_track_x = BARS_X + bar_label_w
    bar_track_w = BARS_W - bar_label_w - 60  # leave room for "%"
    bar_h = 22

    for i, repo in enumerate(REPOS):
        y = BARS_TOP + i * ROW_H

        # Repo name
        text(
            root, BARS_X, y + bar_h - 4,
            repo["name"],
            size=15, weight="600", color=TEXT_PRIMARY,
        )

        # Track (background)
        rounded_rect(
            root, bar_track_x, y, bar_track_w, bar_h,
            fill=BORDER_SOFT, stroke=BORDER_SOFT, stroke_w=0, r=6,
        )

        # Filled bar
        fill_w = int(bar_track_w * repo["pct"] / 100)
        rounded_rect(
            root, bar_track_x, y, fill_w, bar_h,
            fill=RED_FILL, stroke=RED_STROKE, stroke_w=1, r=6,
        )

        # Pct label
        text(
            root, bar_track_x + bar_track_w + 12, y + bar_h - 4,
            f"{repo['pct']}%",
            size=15, weight="700", color=RED_FILL,
        )

        # Sub-detail under the bar
        text(
            root, bar_track_x, y + bar_h + 16,
            f"{repo['unguarded']:,} of {repo['calls']:,} call sites unguarded",
            size=11, weight="400", color=TEXT_MUTED,
        )

    # Plus 12 more repos
    plus_y = BARS_TOP + len(REPOS) * ROW_H + 8
    text(
        root, BARS_X, plus_y,
        "+ 12 more repos in the dataset",
        size=12, weight="500", color=TEXT_SUBTLE,
    )

    # Footer note
    text(
        root, W / 2, H - 20,
        "Methodology and full per-repo breakdown: diplomat-agent/REALITY_CHECK_RESULTS.md",
        size=11, weight="400", color=TEXT_SUBTLE, anchor="middle",
    )

    return root


def main():
    out_dir = Path(__file__).parent
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "benchmark-unguarded.svg"

    root = build()
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"\u2713 wrote {out_path}")


if __name__ == "__main__":
    main()
