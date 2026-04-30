# Security policy — Diplomat-ai

This is the **organization-wide security policy** for all Diplomat-ai
repositories. Individual repos may override it with their own
`SECURITY.md` when their threat model differs (see [`diplomat-gate/SECURITY.md`](https://github.com/Diplomat-ai/diplomat-gate/blob/main/SECURITY.md)
and [`diplomat-agent/SECURITY.md`](https://github.com/Diplomat-ai/diplomat-agent/blob/main/SECURITY.md)).

## Reporting a vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Email the maintainer at **security@diplomat.run** (or
**josselin@diplomat.run** as fallback) with:

- A description of the vulnerability
- Steps to reproduce
- The repository and version(s) affected
- Your disclosure timeline expectations

You will receive an acknowledgment within **72 hours**.
A mitigation or clarification within **7 days for critical issues**,
**30 days otherwise**.

## Scope

In scope across all Diplomat-ai repositories:

- **Policy bypass** — a policy marked STOP allows the action through
- **Audit log tampering** — modifying the SQLite database without
  detection by `diplomat-gate audit verify`
- **Incorrect verdict** — a valid STOP wrongly returned as CONTINUE,
  or vice versa
- **Information disclosure** in audit or review storage beyond the
  documented redaction list
- **Scanner false negatives on critical patterns** — payments,
  destructive commands, agent invocations not detected by
  `diplomat-agent`
- **CI gate bypass** — a way to make `--fail-on-unchecked` exit 0 on
  an unguarded codebase

## Out of scope (known and documented limits)

We are explicit about what we don't claim to defend against. These are
**by design** and documented in each project's README.

- **Semantic attacks on `diplomat-gate`** — an agent sends to a domain
  that doesn't match any blocklist pattern. Design allowlists with
  least privilege.
- **Local attacker with write access to the audit DB** — `rebuild-chain`
  can recreate a valid chain for legitimate recovery. If your threat
  model includes a privileged local attacker, ship records to a
  write-once external store.
- **Multi-process rate-limit accuracy** — current rate-limit and
  velocity policies are single-process accurate. Wrap with an external
  lock or distributed store for multi-process workloads.
- **Prompt injection detection** — `diplomat-gate` evaluates tool
  calls, not prompts. Combine with LLM-based guardrails for
  prompt-level threats.
- **Vulnerabilities in scanned codebases** — `diplomat-agent` reports,
  it does not patch. Findings about *third-party* code in a scan are
  not vulnerabilities in `diplomat-agent`.

## Responsible disclosure

We commit to:

- Acknowledging your report within 72 hours
- Providing a timeline for the fix
- Crediting you in the release notes unless you prefer anonymity
- Publishing a GitHub Security Advisory once a patch is available

We ask you to:

- Not exploit the issue beyond confirming it exists
- Not disclose publicly until a fix is released, or 90 days,
  whichever comes first
- Test only on systems you own
