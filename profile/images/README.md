# Images — reproducible org-level assets

All visuals in `profile/README.md` are reproducible from code.

## SVG files

- `triptych-know-decide-prove.svg` — the three pillars of the Diplomat-ai
  ecosystem (Know / Decide / Prove)

Note: `benchmark-unguarded.svg` (the former 76% chart) was removed because that figure
is superseded by the 70.9% / 71% measurement. `generate_benchmark.py` is still in this
folder but its output is no longer used by `profile/README.md`.

## Regeneration

Each SVG listed above has a generator script alongside it:

```bash
# From the repo root
python profile/images/generate_triptych.py
```

The scripts use only Python stdlib (`xml.etree.ElementTree`, `pathlib`)
— no dependencies needed. Regenerated files overwrite existing ones in
place.

## Design tokens

These match the palette used in `diplomat-gate/docs/images/` and
`diplomat-agent/docs/`:

| Role | Color |
|---|---|
| Brand indigo (gate / decide) | `#4F46E5` |
| Verdict CONTINUE / success | `#10B981` |
| Verdict REVIEW / warning | `#F59E0B` |
| Verdict STOP / risk | `#EF4444` |
| Text primary | `#0F172A` |
| Text muted | `#64748B` |
| Soft border | `#E2E8F0` |

Stripe / Linear / Plausible-style: white background, soft shadows from
borders not blurs, system sans-serif stack, no gradients, no emojis in
SVG.
