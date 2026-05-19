---
name: leadup-api-research-builder
description: Research a third-party API before integrating it into a LeadUp project. Gathers official docs, SDK, auth method, rate limits, current pricing, webhooks, env variables, GitHub examples, risks, and a fallback plan, then outputs an integration recommendation. Use when the user says "integrate API", "add Razorpay", "add WhatsApp", "add Gemini", "add DeepSeek", "add OpenAI", "API research", or "check API docs".
---

# LeadUp API Research Builder

## Purpose

Produce a decision-ready integration dossier for a third-party API so LeadUp
can integrate it safely on the first try — official docs, auth, limits,
pricing, webhooks, env keys, reference code, risks, and a fallback. Plan
before code.

## When to use

Trigger phrases: "integrate API", "add Razorpay", "add WhatsApp", "add
Gemini", "add DeepSeek", "add OpenAI", "add Stripe", "API research", "check
API docs", "how do I connect <service>", "what does <service>'s API need".

For evaluating an open-source repo/library (not a hosted API) → use
`leadup-github-repo-researcher`.

## Inputs needed

- The API/service name and what LeadUp needs it to do.
- The project + stack it will be integrated into.
- Expected volume (affects pricing tier and rate-limit analysis).

## Step-by-step workflow

1. **Confirm the use case** in one line (what data/action, in which project).
2. **Find official docs** first; identify the official SDK (package,
   language, maintained, last release). Prefer official over blog posts.
3. **Fill the research template** in `references/api-research-template.md`:
   auth method, endpoints, rate limits, pricing (with the date checked),
   webhooks (signature + idempotency), env keys.
4. **Find 1–2 reference implementations** on GitHub; note license, stars,
   recency, what is safe to copy/adapt.
5. **Risks & fallback**: failure modes, vendor lock-in, data-residency (India
   relevance), and a degraded/alternate path if the API is down or over quota.
6. **Recommend**: go/no-go, the package to use, and a step-by-step integration
   outline (no code yet unless explicitly asked).

## Required output format

A research dossier following `api-research-template.md` sections 1–11, ending
with: **Recommendation** (go/no-go + package + integration steps) and the
exact `.env.example` key names to add (placeholders only).

## Safety rules

See `references/security-rules.md`. Most relevant here:
- Add only placeholder env keys (`PROVIDER_KEY=__SET_ME__`); never request,
  print, or store real keys/tokens.
- For payments/webhooks, mandate server-side signature + amount verification.
- State pricing/limits with the date checked — they change; never assert stale
  numbers as current.

## Common mistakes

- Using blog/tutorial info instead of official docs (often outdated).
- Skipping webhook signature verification (critical for Razorpay).
- Ignoring rate limits / quota until production breaks.
- Recommending a paid tier without checking expected LeadUp volume.
- Pasting a real key into `.env.example` instead of `__SET_ME__`.

## Troubleshooting

- **Under-triggers**: user said "connect <X>" — re-invoke; suggest triggers.
- **Over-triggers** when they meant an OSS library → route to
  `leadup-github-repo-researcher`.
- **Missing tool/MCP** (no web fetch/search): say so, give known-stable
  guidance, and mark docs/pricing as "verify before integration".
- **No internet**: produce the template with placeholders and a list of exact
  pages to confirm; do not guess pricing/limits.
- **Missing project files**: still deliverable — note where env keys/config
  should land once a project exists.
- **Build/test failure** during a later integration: capture error, check auth
  mode (test vs live), env key names, and webhook URL; do not disable
  signature checks to "make it pass".

## Test prompts

### Should trigger (5)
1. "Add Razorpay to the salon SaaS — research it first."
2. "Integrate WhatsApp notifications, do API research."
3. "Add Gemini to the therapy app — what does the API need?"
4. "Check the DeepSeek API docs before we wire it in."
5. "API research for adding OpenAI to the CRM."

### Should NOT trigger (3)
1. "Find a good open-source charting library." (→ github-repo-researcher)
2. "Analyze this repo's current state." (→ existing-repo-analyzer)
3. "Make the billing screen look premium." (→ premium-ui-upgrader)

### Functional test cases (2)
1. For "add Razorpay", output auth method, webhook signature requirement,
   test/live key prefixes, env key names as placeholders, and a fallback.
2. The dossier states the date pricing/limits were checked and flags them as
   "verify if stale".

## Success criteria

- Official docs + SDK identified; auth, limits, pricing, webhooks covered.
- Env keys listed as placeholders only.
- Reference repos vetted for license/recency.
- Clear go/no-go + ordered integration steps; no real secrets anywhere.
