# Diplomat-ai org configuration

This repository is **not a product**. It holds the organization-level
configuration for [`github.com/Diplomat-ai`](https://github.com/Diplomat-ai):
the public profile page, org-wide fallback files (security policy,
contributing guide, code of conduct, support, funding), and shared
issue / PR templates.

## Looking for the products?

| | What it does |
|---|---|
| [**diplomat-agent**](https://github.com/Diplomat-ai/diplomat-agent) | Static AST scan. Maps every AI-agent tool call with side effects. Pre-deploy. |
| [**diplomat-gate**](https://github.com/Diplomat-ai/diplomat-gate) | Deterministic runtime enforcement. CONTINUE / REVIEW / STOP in <1 ms. |
| [**diplomat.run**](https://diplomat.run) | Hosted Decision Control Plane. Audit, dashboards, compliance export. |

The org landing page rendered from `profile/README.md` lives at
[github.com/Diplomat-ai](https://github.com/Diplomat-ai).

## What's in this repo

```
.
├── profile/
│   ├── README.md                  → renders as the org landing page
│   └── images/                    → reproducible SVG assets + generators
├── .github/
│   ├── ISSUE_TEMPLATE/            → org-wide issue forms
│   └── PULL_REQUEST_TEMPLATE.md   → org-wide PR checklist
├── SECURITY.md                    → org-wide vulnerability reporting policy
├── CONTRIBUTING.md                → org-wide contribution rules
├── CODE_OF_CONDUCT.md             → Contributor Covenant 2.1
├── SUPPORT.md                     → where to ask what
└── FUNDING.yml                    → Sponsor button target
```

## What gets inherited (and what doesn't)

GitHub propagates a specific subset of files from this repo to every
other repository in `Diplomat-ai/` that does not define its own copy:

**Inherited** : `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`,
`SUPPORT.md`, `FUNDING.yml`, `.github/ISSUE_TEMPLATE/`,
`.github/PULL_REQUEST_TEMPLATE.md`.

**NOT inherited** (must live in each repo): `dependabot.yml`, anything
under `.github/workflows/`, CodeQL configs, branch protection rules.
Reusable workflows must be referenced explicitly with
`uses: Diplomat-ai/.github/.github/workflows/<name>.yml@main`.

Per-repo overrides take precedence — `diplomat-gate/SECURITY.md` and
`diplomat-agent/SECURITY.md` continue to apply where they exist.

## Regenerating the visuals

The two SVGs on the org landing page are derived artifacts, generated
from Python stdlib scripts. Edit the `.py`, re-run, commit both:

```bash
python profile/images/generate_triptych.py
python profile/images/generate_benchmark.py
```

See [`profile/images/README.md`](./profile/images/README.md) for the
design tokens (palette aligned with `diplomat-gate` and `diplomat-agent`).

## Reporting an issue with org-wide files

- **Bug or typo in this repo** → [open an issue](https://github.com/Diplomat-ai/.github/issues).
- **Security vulnerability** → see [`SECURITY.md`](./SECURITY.md).
  Do not open a public issue.
- **Question about a product** → open an issue or discussion in the
  product's own repo, not here.

## License

Apache 2.0 for the contents of this repository.
