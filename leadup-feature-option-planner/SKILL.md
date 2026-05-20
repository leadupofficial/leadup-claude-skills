---
name: leadup-feature-option-planner
description: Plan the feature roadmap for a LeadUp SaaS or client product. Splits ideas into must-have, premium, and AI-powered features, defines user roles, sorts MVP vs Phase 2 vs Phase 3, scores monetization impact and complexity, and recommends the next feature to build. Use when the user says "feature planning", "feature ideas", "premium features", "what features to add", "saas features", "future roadmap", or "more intelligent options".
---

# LeadUp Feature Option Planner

## Purpose

Given a product (LeadUp SaaS, client SaaS, or a client website with app
behaviour), produce a clear feature roadmap: must-haves vs premium vs
AI-powered, user roles, MVP vs Phase 2 vs Phase 3, monetization impact,
complexity score, and a single recommended next feature. Built so a small
team can decide what to build next without analysis paralysis.

## When to use

Use when the user wants product / feature decisions made. Do **not**
trigger when the user wants the actual implementation (use
`leadup-project-kickoff` or `leadup-existing-repo-analyzer`), or a UI
upgrade (use `leadup-premium-ui-upgrader`).

Trigger phrases: "feature planning", "feature ideas", "premium features",
"what features to add", "saas features", "future roadmap", "more
intelligent options", "phase 2 features", "next feature to build",
"product roadmap".

## Inputs needed

- Product description in 2–3 lines (what it does, for whom).
- Current state: live / beta / prototype / idea.
- Current top 3 user complaints or feature requests (if any).
- Audience and market (India SMB, global SaaS, internal tool).
- Monetization model (subscription tiers, one-time, free + paid,
  marketplace).
- Constraints: team size, time-to-ship, budget, regulated industry.
- Inspiration list: 3–5 competitor / adjacent products to study.

Ask at most 2 clarifying questions if monetization or audience is unclear.

## Required resources

- **The product itself**: live URL or repo path.
- **User signals**: support tickets, sales objections, churn reasons,
  in-product analytics.
- **Competitors**: their feature pages, changelogs, pricing tiers.
- **Public roadmaps**: many SaaS publish theirs; learn from gaps.
- **Industry standards** for the category (e.g. booking SaaS = calendar,
  payments, reminders, CRM lite).
- **AI feature inspiration**: relevant LLM / vision / voice use cases for
  the category — but only where they create real user value, not "AI
  sticker on top of nothing".

If competitor data is not directly observable, label **estimated** and
move on.

## Internet research workflow

1. Confirm the product's core job (one sentence).
2. List the table-stakes features for the category (what every similar
   product must have).
3. Pull 3–5 competitors' feature pages and pricing tiers; map each feature
   to a tier (free / paid / enterprise).
4. Pull 3–5 user-side signals (support transcripts, reviews, complaints).
5. Brainstorm AI-powered options that solve a real user job (e.g.
   "summarize last 10 bookings" beats "AI dashboard").
6. Note assumptions and ambiguous monetization fits.

If a browser / search MCP is available, hand off to
`leadup-mcp-tool-orchestrator`.

## Step-by-step workflow

1. **Restate brief** (product, audience, monetization, constraints).
2. **Define user roles**: list each role (owner, admin, staff, customer,
   accountant, partner) and the core jobs of each.
3. **Brainstorm features** (30–60 ideas across all roles).
4. **Sort** into three buckets:
   - **Must-have**: table-stakes for the category; without it the product
     looks broken.
   - **Premium**: monetizable upgrades that justify a paid tier.
   - **AI-powered**: features that need an LLM / vision / voice / RAG
     component and add real user value.
5. **Score each feature** on:
   - **Monetization impact** (low / med / high).
   - **Complexity** (S / M / L / XL).
   - **Differentiation** (low / med / high).
   - **User pain solved** (named role + named job).
6. **Phase**: MVP / Phase 2 / Phase 3 / "later or never".
7. **Recommend ONE next feature** with reasoning.
8. **Output** the roadmap and decisions.

Full framework: `references/feature-planning-framework.md`.
Roadmap shape: `assets/feature-roadmap.template.md`.

## Required output format

One Markdown plan with these sections, in this order:

1. **Brief** — product, audience, monetization, constraints.
2. **User roles** — list with core jobs per role.
3. **Feature buckets** — three tables (must-have / premium / AI-powered),
   each with: feature · user role · job solved · monetization impact ·
   complexity · differentiation.
4. **Phased roadmap** — MVP / Phase 2 / Phase 3 / Later. Each phase: list
   of features, definition-of-done, target timeframe.
5. **Recommended next feature** — one feature with reasoning, why now,
   what to defer, what success looks like.
6. **Risks and dependencies** — technical, regulatory, infra, vendor
   lock-in.
7. **Hand-offs** — into `leadup-project-kickoff` (if greenfield),
   `leadup-existing-repo-analyzer` (if continuing), `leadup-api-
   research-builder` (if a new API/integration), `leadup-premium-ui-
   upgrader` (if UI work).
8. **Assumptions and data confidence** — verified / estimated / requires
   verification.

## Safety rules

- Do **not** propose features that need data / compliance the user
  hasn't agreed to handle (KYC, PII, medical records, payments) without
  flagging the requirement.
- Do **not** propose AI features as "AI for the sake of AI". Each AI
  feature must name the user job it solves.
- Do **not** invent monetization numbers ("this will add ₹50K MRR").
  Use bands and label as **estimated**.
- For regulated industries (health, finance, real estate, education,
  alcohol), flag features that need legal / compliance review.
- For India: respect IT Rules, DPDP Act (when finalised in scope), GST
  rules, KYC for payments, ASCI for marketing claims.
- Do **not** copy a competitor's full feature set wholesale; pick what
  fits the user's audience and tier.
- Defer implementation to `leadup-project-kickoff` /
  `leadup-existing-repo-analyzer`; defer integrations to
  `leadup-api-research-builder`; defer UI work to
  `leadup-premium-ui-upgrader`; defer copy to
  `leadup-human-content-editor`.

## Common mistakes

- A 40-feature roadmap with no priority — the team ships nothing.
- "AI everywhere" with no clear user job per AI feature.
- Putting must-haves into Phase 2 (the product is broken without them).
- Putting premium features in MVP (kills the upgrade path).
- Ignoring user roles — designing only for the admin.
- Inventing monetization numbers.
- Forgetting infra costs of AI features (LLM token cost, storage, vector
  DB) when scoring complexity.
- One-size-fits-all recommendation across very different segments.

## Troubleshooting

- **No user data yet**: lean heavier on competitor signals + category
  table-stakes; label as **estimated**.
- **Very small team**: cap MVP at 5 features; cap Phase 2 at 5.
- **Regulated industry**: every new feature must be flagged for
  compliance; some can't be built until the user is licensed.
- **B2B SaaS with enterprise prospects**: reserve enterprise features
  (SSO, audit log, role-based access, SCIM) for a separate tier.
- **D2C / consumer product**: weight AI features toward delight + speed,
  not analytics dashboards.
- **User wants "any clever ideas"**: deliver the recommended-next-feature
  block + 3 alternative options ranked.

## Test prompts

### Should trigger (5)
1. "Plan features for our salon booking SaaS — MVP vs phase 2."
2. "What premium features should we add to our dental clinic app?"
3. "Give me AI-powered features for our hostel-management software."
4. "Build a feature roadmap for our jewellery-shop POS."
5. "What's the next feature we should ship for our SaaS?"

### Should NOT trigger (3)
1. "Build the booking feature in code." (→ `leadup-project-kickoff`)
2. "Make this UI look premium." (→ `leadup-premium-ui-upgrader`)
3. "Integrate Razorpay." (→ `leadup-api-research-builder`)

### Functional test cases (2)
1. Given "salon booking SaaS, India tier-2, team of 2, subscription
   tiers Basic + Pro", return a roadmap with user roles, three feature
   buckets, phased MVP/P2/P3 plans, monetization bands per feature, and
   exactly one recommended next feature with reasoning.
2. Given a regulated category (a dental practice management product),
   return a roadmap that flags compliance-blocking features (medical
   records storage, KYC for online payments), separates "build now"
   from "needs license before building", and points to
   `leadup-api-research-builder` for the integrations involved.

## Success criteria

- Plan has all 8 required sections in order.
- Every feature has user role, monetization impact band, complexity,
  and differentiation.
- MVP is small enough to ship within the user's stated team / budget.
- AI features each name the real user job they solve.
- Exactly ONE recommended next feature with reasoning.
- Compliance and infra cost risks are flagged for regulated and
  AI-heavy features.
- Hand-offs to other LeadUp skills are explicit.
