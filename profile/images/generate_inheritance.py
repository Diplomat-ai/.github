"""
Generate: org-inheritance.svg

Visual: how files in this repo (.github) propagate (or do not) to other
repositories under the Diplomat-ai organization. Replaces a dense prose
section in the root README.

Reproducible — committed alongside the SVG. Stdlib only.
Regenerate: python profile/images/generate_inheritance.py
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

# ---------------------------------------------------------------------------
# Design tokens (aligned with profile/images/generate_triptych.py and
# diplomat-gate/docs/images/)
# ---------------------------------------------------------------------------

BG = "#FFFFFF"
TEXT_PRIMARY = "#0F172A"
TEXT_MUTED = "#64748B"
TEXT_SUBTLE = "#94A3B8"
BORDER_SOFT = "#E2E8F0"

INDIGO_FILL = "#4F46E5"
INDIGO_STROKE = "#312E81"
INDIGO_LIGHT = "#E0E7FF"

GREEN_FILL = "#10B981"
GREEN_STROKE = "#047857"
GREEN_LIGHT = "#D1FAE5"

RED_FILL = "#EF4444"
RED_STROKE = "#991B1B"
RED_LIGHT = "#FEE2E2"

FONT_FAMILY = (
    "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', "
    "Roboto, 'Helvetica Neue', Arial, sans-serif"
)
FONT_MONO = (
    "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, "
    "'Liberation Mono', monospace"
)

# Files that propagate org-wide
INHERITED = [
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SUPPORT.md",
    "FUNDING.yml",
    ".github/ISSUE_TEMPLATE/",
    ".github/PULL_REQUEST_TEMPLATE.md",
]

# Files that do NOT propagate (must live in each repo)
NOT_INHERITED = [
    "dependabot.yml",
    ".github/workflows/",
    "CodeQL configs",
    "branch protection",
]

# Target repos
TARGET_REPOS = ["diplomat-agent", "diplomat-gate", "future repos"]


# ---------------------------------------------------------------------------
# Canvas
# ---------------------------------------------------------------------------

W, H = 1200, 620

# Three columns
SOURCE_X = 60
SOURCE_W = 360

CENTER_X = 500
CENTER_W = 200

TARGET_X = 760
TARGET_W = 380

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
        "Diplomat-ai/.github inheritance map"
    )
    ET.SubElement(root, "desc", {"id": "desc"}).text = (
        "Diagram showing how files in the .github org repo propagate to "
        "other Diplomat-ai repositories. SECURITY.md, CONTRIBUTING.md, "
        "CODE_OF_CONDUCT.md, SUPPORT.md, FUNDING.yml, ISSUE_TEMPLATE and "
        "PULL_REQUEST_TEMPLATE are inherited as fallbacks. dependabot.yml, "
        "workflows, CodeQL configs and branch protection do not propagate "
        "and must live in each repo."
    )
    ET.SubElement(
        root, "rect",
        {"x": "0", "y": "0", "width": str(W), "height": str(H), "fill": BG},
    )
    return root


def rounded_rect(parent, x, y, w, h, fill, stroke, stroke_w=1.5, r=10):
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
         color=TEXT_PRIMARY, anchor="start", family=FONT_FAMILY):
    el = ET.SubElement(
        parent, "text",
        {
            "x": str(x), "y": str(y),
            "font-family": family,
            "font-size": str(size),
            "font-weight": weight,
            "fill": color,
            "text-anchor": anchor,
        },
    )
    el.text = content


def file_chip(parent, x, y, w, h, label, *, status="inherited"):
    """Draw a code-style chip representing a file."""
    if status == "inherited":
        fill, stroke = GREEN_LIGHT, GREEN_STROKE
    elif status == "blocked":
        fill, stroke = RED_LIGHT, RED_STROKE
    else:
        fill, stroke = "#F8FAFC", BORDER_SOFT

    rounded_rect(parent, x, y, w, h, fill=fill, stroke=stroke,
                 stroke_w=1, r=6)
    text(parent, x + 14, y + h - 9, label,
         size=12, weight="500", color=TEXT_PRIMARY, family=FONT_MONO)

    # Status icon on the right
    if status == "inherited":
        # Green checkmark
        cx = x + w - 18
        cy = y + h / 2
        path = (f"M {cx - 5} {cy} L {cx - 1} {cy + 4} L {cx + 6} {cy - 4}")
        ET.SubElement(
            parent, "path",
            {
                "d": path, "fill": "none",
                "stroke": GREEN_STROKE, "stroke-width": "2",
                "stroke-linecap": "round", "stroke-linejoin": "round",
            },
        )
    elif status == "blocked":
        # Red cross
        cx = x + w - 18
        cy = y + h / 2
        for path in [
            f"M {cx - 5} {cy - 5} L {cx + 5} {cy + 5}",
            f"M {cx + 5} {cy - 5} L {cx - 5} {cy + 5}",
        ]:
            ET.SubElement(
                parent, "path",
                {
                    "d": path, "fill": "none",
                    "stroke": RED_STROKE, "stroke-width": "2",
                    "stroke-linecap": "round",
                },
            )


def arrow_path(parent, x1, y1, x2, y2, color, dashed=False):
    """Curved arrow from (x1,y1) to (x2,y2) with chevron at the end."""
    mid_x = (x1 + x2) / 2
    d = f"M {x1} {y1} C {mid_x} {y1}, {mid_x} {y2}, {x2 - 8} {y2}"
    attrs = {
        "d": d, "fill": "none",
        "stroke": color, "stroke-width": "1.8",
        "opacity": "0.85",
    }
    if dashed:
        attrs["stroke-dasharray"] = "5,4"
    ET.SubElement(parent, "path", attrs)
    # Chevron
    chev = f"M {x2 - 10} {y2 - 5} L {x2} {y2} L {x2 - 10} {y2 + 5}"
    ET.SubElement(
        parent, "path",
        {
            "d": chev, "fill": "none",
            "stroke": color, "stroke-width": "1.8",
            "stroke-linecap": "round", "stroke-linejoin": "round",
        },
    )


# ---------------------------------------------------------------------------
# Compose
# ---------------------------------------------------------------------------


def build() -> ET.Element:
    root = svg_root()

    # ---- Header band ----
    text(root, W / 2, 38, "ORG-WIDE INHERITANCE",
         size=12, weight="700", color=TEXT_MUTED, anchor="middle")
    text(root, W / 2, 64,
         "What this repo propagates to every other Diplomat-ai repository",
         size=16, weight="600", color=TEXT_PRIMARY, anchor="middle")

    # ---- Section column labels ----
    label_y = 110
    text(root, SOURCE_X, label_y, "SOURCE — Diplomat-ai/.github",
         size=11, weight="700", color=TEXT_MUTED)
    text(root, CENTER_X + CENTER_W / 2, label_y, "PROPAGATION",
         size=11, weight="700", color=TEXT_MUTED, anchor="middle")
    text(root, TARGET_X, label_y, "TARGET — every other repo",
         size=11, weight="700", color=TEXT_MUTED)

    # ---- Source files (left column) ----
    chip_h = 30
    chip_gap = 8
    src_top = 140

    for i, fname in enumerate(INHERITED):
        y = src_top + i * (chip_h + chip_gap)
        file_chip(root, SOURCE_X, y, SOURCE_W, chip_h, fname,
                  status="inherited")

    # Center hub box
    hub_y = src_top + (len(INHERITED) * (chip_h + chip_gap)) / 2 - 50
    rounded_rect(root, CENTER_X, hub_y, CENTER_W, 100,
                 fill=INDIGO_FILL, stroke=INDIGO_STROKE, stroke_w=2, r=12)
    text(root, CENTER_X + CENTER_W / 2, hub_y + 42,
         "Diplomat-ai", size=15, weight="700",
         color="#FFFFFF", anchor="middle", family=FONT_MONO)
    text(root, CENTER_X + CENTER_W / 2, hub_y + 64,
         "/.github", size=15, weight="700",
         color="#FFFFFF", anchor="middle", family=FONT_MONO)
    text(root, CENTER_X + CENTER_W / 2, hub_y + 86,
         "(this repo)", size=11, weight="400",
         color="#E0E7FF", anchor="middle")

    # Arrows from source files to hub (left side)
    hub_left_x = CENTER_X
    hub_center_y = hub_y + 50
    for i, _ in enumerate(INHERITED):
        y = src_top + i * (chip_h + chip_gap) + chip_h / 2
        arrow_path(root, SOURCE_X + SOURCE_W + 4, y,
                   hub_left_x - 4, hub_center_y, GREEN_STROKE)

    # ---- Target repos (right column) ----
    target_h = 80
    target_gap = 30
    tgt_top = src_top + (len(INHERITED) * (chip_h + chip_gap)) / 2 \
        - (len(TARGET_REPOS) * (target_h + target_gap)) / 2 + 10

    target_palettes = [
        {"fill": "#FEF3C7", "stroke": "#FCD34D", "accent": "#B45309"},
        {"fill": INDIGO_LIGHT, "stroke": "#A5B4FC", "accent": INDIGO_FILL},
        {"fill": "#F8FAFC", "stroke": BORDER_SOFT, "accent": TEXT_MUTED},
    ]

    hub_right_x = CENTER_X + CENTER_W
    for i, repo in enumerate(TARGET_REPOS):
        y = tgt_top + i * (target_h + target_gap)
        palette = target_palettes[i]
        rounded_rect(root, TARGET_X, y, TARGET_W, target_h,
                     fill=palette["fill"], stroke=palette["stroke"],
                     stroke_w=1.5, r=10)

        # Repo name (mono-ish heading)
        text(root, TARGET_X + 20, y + 30, f"Diplomat-ai/{repo}",
             size=15, weight="700", color=TEXT_PRIMARY, family=FONT_MONO)

        # Subtitle
        if repo == "future repos":
            sub = "automatic — no setup needed"
        else:
            sub = "uses local files where present, falls back here otherwise"
        text(root, TARGET_X + 20, y + 56, sub,
             size=12, weight="400", color=TEXT_MUTED)

        # Arrow from hub to this target
        arrow_path(root, hub_right_x + 4, hub_center_y,
                   TARGET_X - 4, y + target_h / 2, palette["accent"])

    # ---- NOT inherited box (bottom) ----
    not_y = 480
    rounded_rect(root, SOURCE_X, not_y, W - 2 * SOURCE_X, 100,
                 fill=RED_LIGHT, stroke=RED_STROKE, stroke_w=1, r=10)

    text(root, SOURCE_X + 20, not_y + 28,
         "NOT inherited — must live in each repo",
         size=14, weight="700", color=RED_STROKE)

    # Lay out the four blocked items horizontally
    item_x_start = SOURCE_X + 20
    item_y = not_y + 56
    item_gap = 12
    item_w = (W - 2 * SOURCE_X - 40 - 3 * item_gap) / 4
    for i, fname in enumerate(NOT_INHERITED):
        x = item_x_start + i * (item_w + item_gap)
        file_chip(root, x, item_y, item_w, 28, fname, status="blocked")

    # ---- Footer note ----
    text(root, W / 2, H - 14,
         "Per-repo files override the fallback. "
         "Reusable workflows must be referenced explicitly: "
         "uses: Diplomat-ai/.github/.github/workflows/<name>.yml@main",
         size=11, weight="400", color=TEXT_SUBTLE,
         anchor="middle", family=FONT_MONO)

    return root


def main():
    out_dir = Path(__file__).parent
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "org-inheritance.svg"

    root = build()
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"\u2713 wrote {out_path}")


if __name__ == "__main__":
    main()
