---
name: leadup-lead-funnel-builder
description: Design an end-to-end lead generation funnel for a LeadUp client or SaaS — traffic source, landing page flow, form or WhatsApp flow, CRM capture, follow-up sequence, automation, tracking, and a conversion improvement checklist. Tuned for Indian SMBs and international SaaS. Use when the user says "lead funnel", "increase leads", "lead generation", "WhatsApp funnel", "client funnel", or "sales funnel".
---

# LeadUp Lead Funnel Builder

## Purpose

Build a complete funnel that turns ad clicks or organic visitors into
qualified leads, then into customers. Covers traffic, landing page,
form / WhatsApp flow, CRM capture, follow-up sequence, marketing
automation, and tracking. India-friendly (UPI, WhatsApp, regional
language) and global-ready.

## When to use

Use when the user wants a funnel designed end-to-end. Do **not**
trigger when they want only a landing page audit (use
`leadup-landing-page-cro-planner`), an ads plan only (use
`leadup-digital-ads-planner`), or a single WhatsApp flow
(use `leadup-whatsapp-automation-planner`).

Trigger phrases: "lead funnel", "increase leads", "lead generation",
"WhatsApp funnel", "client funnel", "sales funnel", "conversion funnel",
"funnel for our business".

## Inputs needed

- Business / product, market, audience.
- Funnel goal (calls / WhatsApp chats / form leads / signups / demos /
  bookings).
- Existing assets (LP, ads, CRM, tracking, BSP account).
- Traffic source mix (Google Ads, Meta Ads, SEO, social, referrals).
- Sales process (who follows up, in how long, with what).
- Constraints (budget, regulated category, language).

Ask at most 2 clarifying questions if the goal or traffic source is
unclear.

## Tools/resources to use

- `references/lead-funnel-framework.md` — stage shape and rules.
- `assets/lead-funnel.template.md` — output shape.
- `leadup-landing-page-cro-planner` for the LP layer.
- `leadup-digital-ads-planner` for the paid traffic layer.
- `leadup-whatsapp-automation-planner` for WhatsApp flow.
- `leadup-n8n-workflow-builder` for the automation glue.
- `leadup-api-research-builder` for CRM / BSP integrations.
- `leadup-human-content-editor` for public copy polish.

## Step-by-step workflow

1. **Restate goal** in one line and pick the **funnel type** (lead form,
   WhatsApp, call, demo booking, free trial signup, ecommerce buy).
2. **Map stages**: Traffic → LP → Capture → Qualify → Follow-up → Close.
3. **Pick traffic sources** per stage and split %.
4. **Spec the LP** with above-fold, CTA, trust, form/WhatsApp choice,
   mobile rules. Hand specifics to `leadup-landing-page-cro-planner`.
5. **Design capture**:
   - **Form** path: minimum fields, validation, success state, CRM
     event.
   - **WhatsApp** path: click-to-chat, opt-in, BSP template, auto-reply.
6. **Define qualification** (who is a hot lead, who is cold, how to
   route).
7. **Build follow-up sequence**: who sends what, when, on which channel.
8. **Wire automation**: n8n / Zapier / native CRM, with credential
   placeholders.
9. **Tracking checklist**: GA4 events, pixel, CAPI, UTM convention,
   CRM stage events.
10. **Conversion-improvement checklist** for the first 30 days.
11. **Hand-offs** explicitly.

## Required output format

One Markdown plan with these sections, in this order:

1. **Brief restate** — goal, audience, funnel type.
2. **Funnel map** — stage table: stage · channel · KPI · target band.
3. **Traffic plan** — per source with share %, KPI, hand-off skill.
4. **Landing page spec** — above-fold, CTA, trust, form/WhatsApp.
5. **Capture flow** — form spec OR WhatsApp flow OR both.
6. **Qualification** — criteria, routing rules.
7. **Follow-up sequence** — touch · channel · template · timing.
8. **Automation** — tool, trigger, nodes/steps, credentials placeholder.
9. **Tracking checklist** — GA4 events, pixel, CAPI, UTM, CRM stages.
10. **Conversion improvement checklist** — first 30 days.
11. **Assumptions and data confidence** — verified / estimated /
    requires verification.
12. **Hand-offs** — to other LeadUp skills.

## Safety rules

- Do **not** invent CR, CPL, ROAS, follower counts. Use **estimated
  bands** with reasoning, or mark **requires verification**.
- Do **not** guarantee leads, conversions, or revenue. Use targets
  with stated assumptions.
- Do **not** propose dark patterns: fake countdowns, fake stock, hidden
  fees, opt-out by inertia.
- Do **not** propose WhatsApp tactics that violate Meta policy
  (mass-cold-outreach without opt-in, template spam).
- Respect opt-in / consent rules; for India, follow IT Rules / DPDP
  scope; for EU, follow GDPR.
- Keep PII handling honest: state where leads are stored, who can see
  them, how long they're retained. Route to `leadup-pii-risk-reviewer`
  for confirmation.
- For payments-in-funnel: route to `leadup-security-review` and
  `leadup-api-research-builder`.
- Public copy goes through `leadup-human-content-editor` before
  publishing.

## Common mistakes

- Designing a funnel without a tracking layer (no GA4 / pixel / UTM).
- "Form on the LP" with no auto-reply → leads go cold in 24 hours.
- Cold WhatsApp outreach without opt-in → BSP account suspension.
- 10-step nurture sequence on a 1-call sale.
- 1-touch follow-up on a 10-call sale.
- No routing rule for hot vs cold leads → sales spends time on cold.
- Forgetting language / timezone of the audience.

## Troubleshooting

- **No CRM**: deliver a Google Sheets / Notion-based v1 with a clear
  upgrade path; route to `leadup-api-research-builder` when a CRM is
  picked.
- **No ad budget yet (organic only)**: lean into SEO + social + WhatsApp
  funnels; defer ads to a later phase.
- **High-ticket sale (₹50K+/lead)**: lean into demo-call funnel + 5–7
  touch sequence; lower volume, higher quality.
- **Local-services business** (salon, clinic, dentist): WhatsApp + Google
  Business + Maps reviews often outperform an LP form.
- **Regulated category** (clinic, finance, real estate): flag
  qualification + claims for compliance; route to
  `leadup-pii-risk-reviewer`.
- **User wants instant**: deliver the funnel map + capture flow + first
  3 follow-ups; build the rest in iteration 2.

## Test prompts

### Should trigger (5)
1. "Build a lead funnel for our salon booking SaaS."
2. "Increase leads for our jewellery client — design the full funnel."
3. "Plan a WhatsApp funnel for a dental clinic in Coimbatore."
4. "Design a demo-call funnel for our B2B booking tool."
5. "Sales funnel for a tutoring centre — ads to follow-up."

### Should NOT trigger (3)
1. "Audit just this landing page." (→ `leadup-landing-page-cro-planner`)
2. "Plan our Meta Ads campaign only." (→ `leadup-digital-ads-planner`)
3. "Build one WhatsApp reminder flow." (→ `leadup-whatsapp-automation-planner`)

### Functional test cases (2)
1. Given "Indian salon booking SaaS, ₹50K/month budget, no CRM yet",
   return a complete funnel plan with Google + Meta + WhatsApp +
   organic mix, a 2-field LP form, a 5-step follow-up over 14 days,
   automation in n8n with credential placeholders, a tracking
   checklist, and a hand-off to `leadup-whatsapp-automation-planner` and
   `leadup-n8n-workflow-builder`.
2. Given a regulated category (a dental clinic running ads to a "free
   consultation" funnel), return a plan that flags consent and claim
   requirements, routes PII to `leadup-pii-risk-reviewer`, removes
   guarantee language, and labels every metric estimated band /
   requires verification.

## Success criteria

- All 12 sections present in order.
- No invented CR / CPL / ROAS.
- Capture flow defines either form OR WhatsApp OR both with concrete
  rules (fields, opt-in, auto-reply, CRM event).
- Follow-up sequence has exact timing per touch.
- Tracking checklist is concrete (events named, UTM convention defined).
- Compliance and PII routed where relevant.
- Hand-offs to other LeadUp skills are explicit.
