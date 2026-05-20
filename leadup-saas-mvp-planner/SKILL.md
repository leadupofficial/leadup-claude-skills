---
name: leadup-saas-mvp-planner
description: Plan a paid SaaS MVP for a LeadUp client or LeadUp's own product — target users, first paid feature, MVP modules, user roles, tenant model, admin panel scope, subscription pricing ideas, database plan, integrations, and launch roadmap. Tuned for Indian small-business SaaS plus international startups. Use when the user says "saas mvp", "build saas", "mvp plan", "paid mvp", "saas idea", or "subscription app".
---

# LeadUp SaaS MVP Planner

## Purpose

Take a SaaS idea (LeadUp's own or a client's) and produce a paid MVP plan
small enough to ship in 6–10 weeks. Defines target users, the first paid
feature, MVP modules, user roles, multi-tenant model, admin panel scope,
subscription pricing direction, database shape, key integrations, and a
launch roadmap.

## When to use

Use when the user wants a SaaS MVP designed end-to-end. Do **not**
trigger for the broader feature roadmap (use
`leadup-feature-option-planner`), AI-only feature planning (use
`leadup-ai-feature-planner`), admin-only design
(`leadup-admin-panel-planner`), or actual code kickoff
(`leadup-project-kickoff`).

Trigger phrases: "saas mvp", "build saas", "mvp plan", "paid mvp", "saas
idea", "subscription app", "plan a SaaS", "MVP scope for SaaS".

## Inputs needed

- SaaS idea in 2–3 lines.
- Target users (industry, role, country, scale).
- Monetisation guess (subscription tiers, per-seat, per-location, freemium).
- Team size + time-to-launch goal.
- Constraints (regulated industry, India-first vs global, language).
- Inspirations (3–5 SaaS to study).

Ask at most 2 clarifying questions if monetisation or audience is unclear.

## Tools/resources to use

- `references/saas-mvp-framework.md` — modules, tenant models, scoring.
- `assets/saas-mvp-roadmap.template.md` — output shape.
- `leadup-feature-option-planner` — for the broader roadmap once MVP
  is locked.
- `leadup-ai-feature-planner` — if an AI feature is part of MVP.
- `leadup-admin-panel-planner` — for the admin module.
- `leadup-pricing-package-planner` — for subscription tiers later.
- `leadup-api-research-builder` — for any third-party integration.
- `leadup-pii-risk-reviewer` / `leadup-security-review` — if regulated.
- `leadup-project-kickoff` — once MVP is approved.

## Step-by-step workflow

1. **Restate the idea** in one line + name the **one paid job** the MVP
   solves.
2. **Target users**: list 1–2 primary personas with named role, named
   job, named country/market.
3. **First paid feature** — the feature that justifies a credit card on
   day 1. Everything else exists to support it.
4. **MVP modules** — ≤ 6 modules. List each with primary role + outcome.
5. **User roles** — owner, admin, staff, customer, billing, etc. Keep
   minimum.
6. **Tenant model** — single tenant, multi-tenant by row (org_id), or
   multi-tenant by schema. State why.
7. **Admin panel scope** — list 4–8 admin modules (handed to
   `leadup-admin-panel-planner`).
8. **Subscription direction** — monthly / annual / per-seat /
   per-location / freemium; pick one. Tiers are designed later by
   `leadup-pricing-package-planner`.
9. **Database plan** — tables + key relationships + multi-tenant
   strategy + indexes flagged.
10. **Integrations** — payments (Razorpay / Stripe), email, WhatsApp BSP,
    CRM, analytics; each with a hand-off to
    `leadup-api-research-builder`.
11. **Launch roadmap** — weeks 0–N to MVP, then post-launch.
12. **Hand-offs** explicitly.

## Required output format

One Markdown plan with these sections, in this order:

1. **Brief restate** — idea, audience, monetisation direction.
2. **The paid job** — one sentence.
3. **Target users** — 1–2 personas with role + job + market.
4. **First paid feature** — what justifies a payment on day 1.
5. **MVP modules** — table: module · primary role · outcome · complexity.
6. **User roles** — list with core jobs.
7. **Tenant model** — single / row-multi / schema-multi + why.
8. **Admin panel scope** — list of modules + KPI cards.
9. **Subscription direction** — model + billing period + currency +
   GST handling.
10. **Database plan** — tables, relationships, multi-tenant strategy,
    flagged indexes, PII flagged.
11. **Integrations** — payments / email / WhatsApp / CRM / analytics.
12. **Launch roadmap** — week-by-week to MVP, then post-launch.
13. **Assumptions and data confidence** — verified / estimated /
    requires verification.
14. **Hand-offs** — to specific LeadUp skills.

## Safety rules

- Do **not** invent market size, ARR projections, customer counts.
- Do **not** propose features that require licences the user doesn't
  have (fintech, healthcare, alcohol, gambling).
- Do **not** ignore PII / payments scope — route to
  `leadup-pii-risk-reviewer` and `leadup-security-review`.
- For India: payment KYC, GST invoicing, IT Rules, DPDP scope when in
  force.
- For global: SOC 2 path for enterprise B2B, GDPR for EU.
- Keep the MVP small enough that the team can ship it. ≤ 6 modules.
- For AI features, route to `leadup-ai-feature-planner` for cost +
  fallback design.
- Defer pricing-tier design to `leadup-pricing-package-planner`.
- Defer admin design to `leadup-admin-panel-planner`.
- Defer integration depth to `leadup-api-research-builder`.

## Common mistakes

- MVP with 15 modules — the team ships nothing.
- "AI everywhere" with no clear user job.
- Multi-tenant decision deferred → costly migration later.
- Building admin first (clients pay for product, not admin).
- Picking Stripe in India because it's familiar — Razorpay / Cashfree
  often fit better.
- Underestimating WhatsApp BSP onboarding (3–7 days of approvals).
- Ignoring the "first paid feature" question.
- Promising launch in 2 weeks when the team can deliver in 6.

## Troubleshooting

- **Idea is too broad**: scope down to one persona + one paid job; the
  rest goes to Phase 2.
- **Idea is too narrow / unprofitable**: surface the assumption ("how
  many users would pay $/month") and ask the user.
- **Highly regulated**: route to compliance first; design with caps on
  what the MVP can do without licences.
- **AI feature is the main draw**: route to `leadup-ai-feature-planner`
  and bring back the spec; ensure infra cost < tier price.
- **Multi-language at MVP**: only if the primary market needs it; else
  defer to Phase 2.
- **User wants 2-week MVP**: trim to one paid feature + the absolute
  minimum supporting modules; flag what's deferred.

## Test prompts

### Should trigger (5)
1. "Plan an MVP for a salon booking SaaS in India."
2. "Build a SaaS MVP for a clinic appointment platform."
3. "MVP plan for a B2B booking tool, India + Middle East."
4. "Paid MVP for a hostel-management SaaS."
5. "Subscription app plan for a tutoring centre."

### Should NOT trigger (3)
1. "Plan all the features for our SaaS." (→ `leadup-feature-option-planner`)
2. "Design just the admin panel." (→ `leadup-admin-panel-planner`)
3. "Bootstrap the actual repo." (→ `leadup-project-kickoff`)

### Functional test cases (2)
1. Given "salon booking SaaS, India tier-2, team of 2, launch in
   8 weeks", return ≤ 6 MVP modules, 1–2 personas, a named first paid
   feature, multi-tenant-by-row decision with reasoning, an admin scope
   handed to `leadup-admin-panel-planner`, integrations (Razorpay +
   WhatsApp BSP) handed to `leadup-api-research-builder`, and a weekly
   roadmap.
2. Given a regulated category (a dental clinic SaaS storing patient
   notes), return an MVP that flags PII fields, routes to
   `leadup-pii-risk-reviewer`, recommends row-level multi-tenant with
   org_id + encryption at rest, and caps what the MVP can offer
   without sector compliance.

## Success criteria

- MVP has ≤ 6 modules.
- Exactly one named "first paid feature".
- Tenant model decided with reasoning.
- Database plan flags PII and indexes.
- Integration list is concrete with hand-offs.
- Launch roadmap is week-by-week.
- All hand-offs to other LeadUp skills are explicit.
- No invented ARR / market-size numbers.
