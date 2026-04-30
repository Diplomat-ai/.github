<!--
Thanks for the PR. Quick checklist before requesting review.
Strip the comments before submitting.
-->

## What this changes

<!-- One sentence on the user-visible behavior change. -->

## Why

<!-- Link the issue if there is one: "Closes #123". -->
<!-- If there isn't, explain the problem in 2-3 lines. -->

## Type of change

- [ ] Bug fix (no public API change)
- [ ] New feature (new pattern, policy, adapter, or output format)
- [ ] Breaking change (public API, CLI flag rename, removal)
- [ ] Documentation only
- [ ] Internal refactor (no behavior change)

## Checklist

- [ ] Tests added or updated for the change
- [ ] `pytest` passes locally
- [ ] `ruff check .` and `ruff format --check .` pass
- [ ] `CHANGELOG.md` updated under `## [Unreleased]` if user-visible
- [ ] No new mandatory dependency added (or it's in an optional extra)
- [ ] Public API additions have type hints and docstrings
- [ ] Commits are GPG-signed

## For diplomat-gate releases only

- [ ] `python scripts/validate_release.py` passes (11-step gate)

## For new diplomat-agent patterns

- [ ] Fixture added in `tests/fixtures/`
- [ ] Assertion in `tests/test_scanner.py`
- [ ] False-positive coverage in `tests/test_false_positives.py`

## Notes for reviewers

<!-- Anything tricky, intentionally out of scope, or worth a second look. -->
