# Contributing to Diplomat-ai

This is the **organization-wide contributing guide**. Each repository
may extend it with project-specific setup
([`diplomat-gate/CONTRIBUTING.md`](https://github.com/Diplomat-ai/diplomat-gate/blob/main/CONTRIBUTING.md),
[`diplomat-agent/CONTRIBUTING.md`](https://github.com/Diplomat-ai/diplomat-agent/blob/main/CONTRIBUTING.md)).
Read both.

Diplomat-ai is solo-maintained. Every issue and every PR is read by
[Josselin](https://github.com/josselinchasse).

## Before contributing

- For a **bug fix** or **good first issue** — open the issue first if
  one doesn't exist, describe the problem in 3-5 lines, then say you're
  working on it.
- For a **new policy**, **new pattern**, **new adapter**, or **new
  output format** — open a discussion issue first. Not every idea fits
  the *deterministic, no LLM, zero mandatory deps* constraint.
- For **larger changes** (new subsystem, public API break) — open a
  discussion and wait for a maintainer response before coding.

## Constraints that apply to every Diplomat-ai repo

These are **non-negotiable**. PRs that break them will be sent back.

- **Zero mandatory dependencies.** Everything new goes in optional
  extras (`[yaml]`, `[rich]`, `[openai]`, etc.). The core install path
  is always pure stdlib.
- **Deterministic behavior** in the evaluation / scan path. No
  randomness, no time-based decisions, no LLM calls.
- **Data over logic.** Patterns and policies live in `patterns.py` /
  `policies/*.py` as data, not as scattered conditional branches.
- **AST, not regex** for code analysis. `diplomat-agent` reads Python
  source through `ast`; regex patterns over source code are rejected.
- **Type hints mandatory** on public APIs. `from __future__ import
  annotations` at the top of every module.
- **Lint / format with ruff** — configuration lives in `pyproject.toml`,
  do not change it without an issue first.
- **Tests required** for new behavior. New pattern → fixture in
  `tests/fixtures/` + assertion in `tests/test_scanner.py`. New policy
  → test in `tests/test_<domain>_policies.py`. New adapter → test in
  `tests/test_adapters.py`.

## Local setup (template — see each repo for specifics)

```bash
git clone https://github.com/Diplomat-ai/<repo>.git
cd <repo>
python -m venv .venv
source .venv/bin/activate           # Windows: .venv\Scripts\activate
pip install -e ".[all]"             # or [dev] depending on the repo
pip install ruff pytest

pytest                              # all tests
ruff check . && ruff format --check .
```

For `diplomat-gate`, run the full release gate before tagging anything:

```bash
python scripts/validate_release.py  # 11-step gate
```

## PR process

- Branch from `main`.
- One logical change per PR. PRs touching 5+ unrelated files get split
  or rejected.
- Update `CHANGELOG.md` under `## [Unreleased]` for any user-visible
  change.
- Commits should be **GPG-signed**. CI matrix (Python 3.10–3.13 ×
  Linux / Windows / macOS for `diplomat-gate`) must be green before
  review.
- Squash-merge is the default. Write a meaningful squash message —
  the PR title becomes part of the changelog.

## Reporting bugs and false positives

- **Bug** — use the bug report issue template. Include version,
  Python version, OS, and a minimal reproducer.
- **False positive** (`diplomat-agent` only) — most valuable
  contribution. Use the false-positive template. Include the function
  code that was incorrectly flagged, the actual scanner output, and
  what you expected.
- **Missing detection** — same template, opposite direction. Function
  the scanner missed, what it does, where it lives.

## Security vulnerabilities

Do **not** file public issues. See the org-wide
[`SECURITY.md`](./SECURITY.md).

## License

By contributing, you agree your contributions are licensed under
**Apache 2.0**, the license of all Diplomat-ai repositories.
