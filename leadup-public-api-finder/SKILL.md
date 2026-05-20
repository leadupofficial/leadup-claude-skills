---
name: leadup-public-api-finder
description: Find, compare, and recommend free or third-party public APIs for LeadUp projects (websites, SaaS, CRM, hosting tools, Flutter apps, automation) using public API directories (public-apis/public-apis), official documentation, GitHub examples, RapidAPI, ApyHub, and Postman public collections. Always verifies the chosen API against the official docs before recommending, scores candidates on fit / docs / pricing / reliability / auth / CORS / commercial use, and outputs a candidate table, best + backup picks, env placeholders, integration notes, and an implementation + test plan. Use when the user says "find API", "free API", "public API", "API options", "best API for this feature", "API idea", "third party API", "API marketplace", "check public APIs", "use public-apis repo", or "API for my project".
---

# LeadUp Public API Finder

## Purpose

Take a feature need and return a short, honest shortlist of free or
public APIs that fit, with one clear recommended pick + one backup,
verified from official documentation. Built for LeadUp projects:
client websites, multi-tenant SaaS, Flutter apps, hosting / security
tools, CRM, automation workflows, travel, jewellery, salon, school,
and clinic products under `*.leadup.in`.

## When to use

Use when the user wants to **discover or choose** a public/third-party
API. Do **not** trigger when:
- They want the integration code itself written (route to
  `leadup-api-research-builder`, which does the deeper integration
  research with auth, webhooks, env mapping).
- They want a new SaaS feature planned (use
  `leadup-feature-option-planner` or `leadup-ai-feature-planner`).
- They want an n8n graph built (use `leadup-n8n-workflow-builder`).

Trigger phrases: "find API", "free API", "public API", "API options",
"best API for this feature", "API idea", "third party API", "API
marketplace", "check public APIs", "use public-apis repo", "API for my
project", "free APIs for SaaS", "compare APIs".

## Inputs needed

- The feature or job the API must do (e.g. "verify an email",
  "currency conversion INR↔USD", "send WhatsApp template", "detect
  malicious URLs").
- Project context (LeadUp website / Hostendor / Jewellery SaaS / Salon
  SaaS / INET CRM / Trivasia / Security suite / other).
- Audience and market (India / global), to weight UPI / GST / WhatsApp /
  language coverage.
- Where the API will run (browser-only, server-only, or both — CORS
  matters).
- Volume / rate expectations (calls per day, peak per minute).
- Cost ceiling (free only, free + paid OK, hard budget).
- Commercial use (yes — always, for LeadUp client work).
- Must-keep constraints (regulated industry, PII risk, regional data
  residency).

Ask at most 2 clarifying questions if the feature or runtime
(browser vs server) is genuinely ambiguous.

## Source/resource strategy

Use these sources, in this priority order:

1. **Official API documentation** of each candidate (the source of
   truth for auth, limits, pricing, commercial use, CORS, SDKs).
2. **public-apis/public-apis** on GitHub
   (`https://github.com/public-apis/public-apis`) — discovery only.
   It is a curated index; entries can be stale or incomplete.
3. **Provider pricing pages** for the current free-tier limits and
   commercial-use language.
4. **GitHub examples** (sample code, popular client libraries, recent
   stars/commits) — to gauge real-world use.
5. **RapidAPI** marketplace — for aggregated metadata, latency stats,
   reviews, and a single billing layer when useful.
6. **ApyHub** — for utility APIs (PDF, image, validation) when free
   alternatives are limited.
7. **Postman public collections / public workspaces** — for ready
   request examples and quickstart.
8. **SDK / package docs** (npm / pypi / pub.dev / packagist) — for
   integration ergonomics.
9. **API status pages** (e.g. `status.<provider>.com`) — for uptime /
   incident history.

Detail and notes per source: `references/public-apis-repo-notes.md`.

## API discovery workflow

1. **Restate the requirement** in one line (what the API must do, for
   whom, where it runs).
2. **Classify the API category** (validation / payments / messaging /
   maps / weather / docs / security / AI / data / search / files).
3. **Scan `public-apis/public-apis`** for that category; capture 3–8
   raw candidates (name + 1-line desc + auth + HTTPS + CORS hint).
4. **Cross-check** with RapidAPI, ApyHub, and an open Google search to
   surface providers not listed in `public-apis`.
5. **Drop obviously bad fits** (wrong category, dead links, paid-only
   when user said free).
6. **Shortlist 3–5** for verification.

Discovery framework + heuristics: `references/public-api-discovery-framework.md`.

## API verification workflow

For each shortlisted candidate, verify from the **official docs**
(not the directory) and record:

- **Auth method** (none / API key / OAuth2 / JWT / mTLS).
- **HTTPS** (must be yes).
- **CORS** (yes / no / partial / unknown — drives backend proxy need).
- **Free tier** (calls / month, daily, per minute; expiry of any
  trial).
- **Paid pricing** (next tier band; per-call vs subscription).
- **Rate limits** (per minute, per day, burst behavior).
- **Commercial use** (allowed / restricted / attribution required).
- **Terms / data residency** (where data is processed).
- **SDK availability** (official npm / pip / dart / etc.).
- **Webhook support** (events, retries, signature).
- **Privacy risk** (does it see PII / payments / health / kids?).
- **Backend proxy required?** (browser-CORS missing or API key would
  leak in the client).
- **Reliability / maintenance** (last release, status page, GitHub
  activity, incident history).
- **Region coverage** (India / EU / US / global) and language support
  if relevant.

Checklist with what to read on the docs page: `references/api-verification-checklist.md`.

## API scoring framework

Score each verified candidate 1–5 on the eight axes below. Average for
a quick rank, and call out any single sub-3 score as a red flag.

| Axis | What 5 looks like |
|---|---|
| Fit for feature | does exactly the job; no extra glue |
| Documentation quality | clear, examples, OpenAPI, changelog |
| Free tier / pricing | enough to ship and pilot; predictable paid path |
| Reliability / maintenance | active, status page, low-incident |
| Auth / security | HTTPS, modern auth, no leaked secrets |
| Frontend compatibility / CORS | safe direct browser use OR clear backend-proxy path |
| Backend integration simplicity | SDK + idiomatic for our stack |
| Commercial use safety | unambiguous license + acceptable terms |

Full rubric and tie-breakers: `references/api-scoring-framework.md`.

## Step-by-step workflow

1. **Restate** the requirement in one line; confirm runtime + market +
   commercial use.
2. **Discover** candidates per "API discovery workflow" above.
3. **Verify** each shortlisted candidate per "API verification
   workflow" against its **official docs**.
4. **Score** with the 8-axis rubric; mark sub-3 axes as risks.
5. **Pick** one best + one backup. Justify in 2–3 lines.
6. **Spec the integration**: env placeholders, backend-vs-frontend
   placement, error handling, rate-limit strategy, retry policy,
   logging without PII.
7. **Test plan**: 3–5 fixtures (happy path, auth fail, rate-limited,
   downstream 5xx, malformed payload).
8. **Output** the structured report (see Required output format).
9. **Hand off**:
   - Implementation depth → `leadup-api-research-builder`.
   - Workflow wiring → `leadup-n8n-workflow-builder`.
   - PII / payment scope → `leadup-pii-risk-reviewer` and
     `leadup-security-review`.
   - Public copy mentioning the integration → `leadup-human-content-editor`.

## Required output format

One Markdown report with these sections, in this order:

1. **Requirement summary** — feature, runtime, market, commercial.
2. **API category** — single tag (validation / payments / messaging /
   maps / weather / docs / security / AI / data / search / files /
   other).
3. **Candidate APIs (3–5)** — table with: name · auth · HTTPS · CORS ·
   free tier band · pricing band · region · maintained? · score.
4. **Best API recommendation** — one name + one-line reason.
5. **Backup API recommendation** — one name + one-line reason.
6. **Why selected** — 3–5 bullets weighting the 8 scoring axes.
7. **Official docs / resource links** — direct links to docs, pricing,
   status page, SDK page; cite access date.
8. **Required env variables** — `.env.example` placeholders only.
9. **Backend / frontend integration notes** — where it runs, why; CORS
   handling; secret handling; quick code shape.
10. **Security / privacy risks** — PII categories that touch the API;
    DPA status if known; route to `leadup-pii-risk-reviewer` /
    `leadup-security-review` flags.
11. **Rate limit / pricing notes** — bands, what triggers a paid
    upgrade, caps the team should set in code.
12. **Implementation plan** — concrete steps the dev follows.
13. **Test plan** — 3–5 fixtures with expected outcomes.
14. **Decision** — `use now` / `prototype only` / `avoid` + one line
    reason.
15. **Hand-offs** — to other LeadUp skills.

Templates: `assets/api-comparison.template.md`,
`assets/api-integration-plan.template.md`,
`assets/env-placeholders.template.md`,
`assets/api-test-plan.template.md`.

## Safety rules

- Treat `public-apis/public-apis` as a **discovery index only**.
  Entries can be stale; never quote pricing, CORS, or auth from the
  directory in the final output. Always re-read the official docs.
- Do **not** ask the user to paste live API keys, tokens, or `.env`
  values. Use `.env.example` placeholders like `__SET_ME__` /
  `{{API_KEY}}`.
- Do **not** put API keys in browser-shipped code. If the API is
  browser-friendly but the key is secret, recommend a backend proxy.
- Do **not** recommend an API for production if last release / commit
  is > 24 months old without an explicit "use with warning" note.
- Do **not** recommend an API that lacks HTTPS for production.
- Do **not** ignore commercial-use clauses. Free for personal /
  research is **not** free for LeadUp client work.
- For India / EU users with PII: confirm data residency and DPA;
  route to `leadup-pii-risk-reviewer`.
- For payment-related APIs: route to `leadup-security-review` and
  prefer Razorpay / Stripe / Cashfree per
  `leadup-saas-mvp-planner` defaults.
- For WhatsApp APIs: route to `leadup-whatsapp-automation-planner`
  (opt-in + template categories + BSP choice).
- For AI / LLM APIs: route to `leadup-ai-feature-planner` (cost
  ledger, fallback, redaction).
- Do **not** invent rate limits, prices, or CORS behavior. If unclear
  in the official docs, label **requires verification** and link the
  doc page.

## Common mistakes

- Quoting the directory's metadata as truth.
- Picking the API with the loudest landing page over the one with
  cleanest docs.
- Ignoring CORS until launch day.
- Putting a paid API key in a frontend bundle.
- Choosing "free" without reading commercial-use language.
- One mega table with 15 candidates and no recommendation.
- Forgetting backup; the best API will go down eventually.
- No rate-limit strategy → 429 storms in production.
- No test fixtures → "it worked once in Postman" is not proof.

## Troubleshooting

- **No browser / search MCP available**: deliver the report from
  known docs + `public-apis` notes; mark anything not directly
  verifiable as **requires verification** and include the exact URL
  to confirm.
- **Highly regulated category**: cap the recommendation; flag every
  PII or financial signal; route to `leadup-pii-risk-reviewer` and
  `leadup-security-review` before committing.
- **India-first audience**: prefer providers with INR billing,
  India data residency, GST invoices, and India-region latency.
- **Browser-only feature with secret key**: switch to a backend
  proxy plan in section 9; never expose secret keys in client code.
- **All free tiers are too small**: list the cheapest paid tier band
  per candidate and recommend a feature flag to gate usage.
- **Provider is unmaintained but unique**: deliver as "prototype only",
  not "use now"; plan migration path to an active alternative.
- **User wants instant pick**: deliver just sections 1, 3, 4, 5, 14;
  hold the rest for an iteration.

## Test prompts

### Should trigger (5)
1. "Find a free public API for email validation."
2. "What public API should we use for currency conversion in our jewellery SaaS?"
3. "Best API for IP lookup / threat reputation for Hostendor?"
4. "Free APIs for weather + flight info for Trivasia."
5. "Check public-apis repo and recommend a maps API for our salon SaaS."

### Should NOT trigger (3)
1. "Write the Razorpay integration code." (→ `leadup-api-research-builder`)
2. "Plan an AI feature using Claude." (→ `leadup-ai-feature-planner`)
3. "Build an n8n graph that calls this API." (→ `leadup-n8n-workflow-builder`)

### Functional test cases (2)
1. Given "email validation API for our lead form, used server-side,
   India audience, commercial LeadUp client use", return a report
   with 3–5 candidate APIs, 8-axis scores, a best + backup pick with
   docs links + access date, env placeholders, backend-vs-frontend
   note (server-side here), rate-limit and pricing bands, an
   implementation plan, a test plan with 4 fixtures, and a final
   `use now / prototype only / avoid` decision.
2. Given a browser-only feature ("currency conversion in a Flutter
   web app") with a secret API key, return a report that explicitly
   recommends a backend proxy (or a key-less public source like the
   ECB / `exchangerate.host`), forbids embedding the secret in the
   client, and provides a candidate alternative.

## Success criteria

- All 15 output sections present in order.
- Candidates verified from **official docs**, with a cited access
  date — `public-apis/public-apis` used only for discovery.
- 8-axis scores per candidate; sub-3 axes flagged.
- One best + one backup, with 3–5 bullet justification.
- Env shown as placeholders only; no real keys anywhere.
- CORS / backend-proxy decision is explicit.
- Commercial-use safety is confirmed for LeadUp client work.
- Rate-limit and pricing labelled **verified** vs **requires
  verification**, with links.
- Decision: `use now` / `prototype only` / `avoid`.
- Hand-offs to `leadup-api-research-builder`,
  `leadup-n8n-workflow-builder`, `leadup-pii-risk-reviewer`,
  `leadup-security-review`, `leadup-whatsapp-automation-planner`, and
  `leadup-ai-feature-planner` are explicit when relevant.
