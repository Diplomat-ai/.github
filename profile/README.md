<!-- Destination: Diplomat-ai/.github  →  profile/README.md -->

<p align="center">
  <img src="https://raw.githubusercontent.com/Diplomat-ai/diplomat-agent/main/docs/assets/readme-vision-v3.svg" alt="Diplomat: assess, control, prove" width="900">
</p>

# Your AI agents act on their own. Your rules have to keep up.

Diplomat turns your company's rules into automatic controls that block or approve every sensitive action your AI agents take, in under a millisecond, with verifiable proof.

An assistant suggests. An agent executes. A rule written in a prompt is a request; only a rule applied to the action is a barrier.

## Assess · Control · Prove

One chain, three steps. Each step delivers value on its own, you decide how far to go.

| Step | Question | Product | License | Status |
|---|---|---|---|---|
| **Assess** | What can our agents actually do? | [diplomat-agent](https://github.com/Diplomat-ai/diplomat-agent) | Apache-2.0 | [![PyPI](https://img.shields.io/pypi/v/diplomat-agent)](https://pypi.org/project/diplomat-agent/) |
| **Control** | Do our rules apply before agents act? | [diplomat-gate](https://github.com/Diplomat-ai/diplomat-gate) | BSL 1.1 (source-available) | [![PyPI](https://img.shields.io/pypi/v/diplomat-gate)](https://pypi.org/project/diplomat-gate/) |
| **Prove** | Can we show who authorized what? | [diplomat.run](https://diplomat.run) | Commercial (hosted) | early access |

- **diplomat-agent** is a static AST scanner for Python agents. It lists every tool call with a side effect (payment, email, database write, delete, subprocess, upload, agent invocation) and checks whether a guard surrounds it. It outputs a `toolcalls.yaml` Behavioral BOM, SARIF 2.1.0, CSAF 2.0, JSON and Markdown.
- **diplomat-gate** is a deterministic runtime layer. It intercepts a tool call and returns `CONTINUE`, `REVIEW` or `STOP` in about 20 µs (one policy) to about 500 µs (five policies). No LLM call, no network. Each decision produces a SHA-256 hash-chained receipt, and `REVIEW` decisions go to a local review queue.
- **diplomat.run** is the hosted layer: cross-tenant audit, dashboard, managed approval routing, and an export mapped to EU AI Act Article 12.

## Why

We scanned 16 open-source agent codebases (7,552 tool calls). **71% of the analyzable tool calls had no guard** in the code. Method and raw results: [REALITY_CHECK_RESULTS.md](https://github.com/Diplomat-ai/diplomat-agent/blob/main/docs/REALITY_CHECK_RESULTS.md).

## A note on licenses

- `diplomat-agent` is open source under Apache-2.0.
- `diplomat-gate` is **source-available under the Business Source License 1.1**, not open source in the OSI sense. You can read it, run it in production inside your own organization, and modify it. You cannot offer it to third parties as a competing hosted or managed service. Each version converts to Apache-2.0 on its Change Date. Versions published before the license change stay under Apache-2.0. Details: [LICENSE](https://github.com/Diplomat-ai/diplomat-gate/blob/main/LICENSE) and [LICENSING.md](https://github.com/Diplomat-ai/diplomat-gate/blob/main/LICENSING.md).

## What we are not

Diplomat is intentionally narrow. It is defense in depth, not a silver bullet.

- `diplomat-gate` is **syntactic, not semantic**. It enforces the rules you write on the parameters of a tool call. It does not classify intent and does not detect prompt injection.
- The audit chain detects accidental corruption. It is not tamper-evidence against a privileged local attacker, who can rebuild a valid chain.
- Rate limits are accurate within a single process.
- `diplomat-agent` is intra-procedural plus decorators within the same package, and Python only today. It does no runtime detection.
- Diplomat complements your cybersecurity tools. They watch for threats; Diplomat enforces your decisions.

## Standards

Findings and decisions are mapped to the OWASP Agentic Top 10, and the audit output is built to support work against the EU AI Act (Article 12), NIST AI RMF and DORA. This is documentation support, not a legal qualification of your systems: validate it with your legal counsel or DPO.

## Get started

```bash
pip install diplomat-agent
diplomat-agent scan ./your-agent
```

Questions, a 30-minute assessment of your agents, or a licensing question: [diplomat.run](https://diplomat.run) · Diplomat Services SASU, Cagnes-sur-Mer, France.
