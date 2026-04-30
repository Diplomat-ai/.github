# Images — reproducible org-level assets

All visuals in `profile/README.md` are reproducible from code.

## SVG files

- `triptych-know-decide-prove.svg` — the three pillars of the Diplomat-ai
  ecosystem (Know / Decide / Prove)
- `benchmark-unguarded.svg` — the 76% benchmark across 16 open-source
  AI agent codebases

## Regeneration

Each SVG has a generator script alongside it:

```bash
# From the repo root
python profile/images/generate_triptych.py
python profile/images/generate_benchmark.py
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
