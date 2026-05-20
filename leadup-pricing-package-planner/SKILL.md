---
name: leadup-pricing-package-planner
description: Design Basic / Standard / Premium pricing packages for LeadUp services — websites, SEO, SMM, hosting, AMC, SaaS subscriptions, AI automation — with one-time setup fees, monthly/yearly recurring placeholders, included features, exclusions, upsells, a recommended plan, and margin/risk notes for the Indian and international market. Use when the user says "pricing package", "create packages", "service pricing", "subscription pricing", "maintenance plan", "SEO package", or "SMM package".
---

# LeadUp Pricing Package Planner

## Purpose

Take a service (website, SEO, SMM, hosting, AMC, SaaS subscription, AI
automation) and produce three clear pricing tiers a client can compare
in 30 seconds. Built for LeadUp's mix of Indian small-business clients
and international clients, with honest exclusions and a flagged
recommended plan.

## When to use

Use when the user wants pricing **packages** designed. Do **not**
trigger for a single proposal (use `leadup-sales-proposal-builder`),
or for product feature roadmap (use `leadup-feature-option-planner`).

Trigger phrases: "pricing package", "create packages", "service pricing",
"subscription pricing", "maintenance plan", "SEO package", "SMM package",
"AMC tiers", "SaaS plan structure".

## Inputs needed

- Service category (website / SEO / SMM / AMC / SaaS / AI automation /
  hosting / other).
- Audience (Indian SMB, mid-market, international startup, large
  enterprise).
- LeadUp's actual delivery capacity (team size, hours/month).
- Real price band the team is comfortable charging (one number or a
  range; if unknown, the skill will recommend a band and ask for
  confirmation).
- Competitor pricing if shared.
- Currency and tax (INR + GST default; else USD/AED + relevant tax).

Ask at most 2 clarifying questions if category or capacity is unclear.

## Tools/resources to use

- `references/pricing-package-framework.md` — tier shape, anchor logic,
  upsell rules.
- `assets/pricing-packages.template.md` — fill-in output.
- `leadup-sales-proposal-builder` once tiers are confirmed.
- `leadup-human-content-editor` for public-facing pricing-page copy.

## Step-by-step workflow

1. **Restate the brief** in one line (category, audience, currency).
2. **Define the value ladder**: what does Basic deliver, what does
   Standard add, what does Premium add? Each tier adds at least one
   real, named upgrade.
3. **Set anchors**: Basic = entry, Standard = "Most popular" (default
   recommended), Premium = high-touch.
4. **Fill in pricing**: confirmed numbers if the user shared them;
   otherwise recommended bands with `[fill in]` and a confirm prompt.
5. **List included features per tier** (concrete, named).
6. **List exclusions across all tiers** (paid ad spend, third-party
   tool fees, photography, content).
7. **Add upsells** (one-time and recurring).
8. **Flag the recommended plan** and why.
9. **Add margin / risk notes** (internal): time per month, who delivers,
   where this could lose money.
10. **Hand off** the public-facing pricing copy to
    `leadup-human-content-editor`.

## Required output format

One Markdown document with these sections, in this order:

1. **Brief restate** — service, audience, currency.
2. **Pricing tiers (client-facing)** — three side-by-side blocks
   (Basic / Standard / Premium) in the
   `assets/pricing-packages.template.md` shape, with prices or
   `[fill in]` placeholders.
3. **What's included** per tier (named features).
4. **What's excluded** (across all tiers).
5. **Upsells** — one-time and recurring add-ons.
6. **Recommended plan** — which tier the user should highlight, why.
7. **Margin / risk notes** (internal) — capacity, breakeven, risk lines.
8. **Pricing-page copy** — short marketing block for the website,
   ready for `leadup-human-content-editor` polish.
9. **Hand-offs** — proposal builder, copy editor, security/PII review
   if payments are involved.

## Safety rules

- Do **not** invent prices. If unknown, use `[fill in]` or a
  recommended band, and tell the user to confirm.
- Do **not** invent client logos, awards, or "trusted by" claims on the
  pricing page.
- Do **not** promise leads, rankings, traffic, or revenue. Use targets,
  not guarantees.
- For India: state GST treatment, invoicing currency (INR), HSN/SAC if
  relevant, refund/cancellation policy summary.
- For international: state currency, applicable tax / TCS, payment
  channel.
- Keep exclusions explicit — paid ad spend, hosting fees, BSP fees,
  photography, content writing, translation.
- For SaaS subscriptions, define **billing period** (monthly / yearly),
  **cancellation policy**, **refund policy**, and **fair-use limits**.
- Defer public copy polish to `leadup-human-content-editor`.
- Defer payment / KYC / PII scope to `leadup-pii-risk-reviewer` and
  `leadup-security-review` if relevant.

## Common mistakes

- Three identical tiers with a higher number on Premium — no real
  value ladder.
- "Most popular" tag on Basic (kills upgrade intent).
- Premium has more features but the same delivery effort as Basic — bad
  margin.
- Inventing prices to "look right".
- No exclusions block, leading to scope creep.
- AMC plans with no SLA or response time.
- SaaS plans with no fair-use limits (one heavy user kills margin).
- Forgetting GST for India.

## Troubleshooting

- **User wants only 2 tiers**: deliver 2; do not pad.
- **User wants 5 tiers**: trim to 3 unless one is enterprise; flag
  enterprise as "Contact us".
- **Highly variable scope** (custom builds): switch from packages to
  "from ₹X — exact quote after scoping".
- **Regulated industry**: flag every payment / data feature for
  compliance review before pricing.
- **Indian SMB with very small budget**: build a tight Basic that's
  genuinely useful, even if margin is thin; flag risk internally.
- **International client**: use USD/AED, drop GST, note Stripe / wire.

## Test prompts

### Should trigger (5)
1. "Make Basic/Standard/Premium packages for our website service."
2. "Build SEO retainer pricing for Indian SMBs."
3. "Design AMC tiers for our hosting clients."
4. "Plan SaaS subscription pricing for our salon booking product."
5. "Create SMM packages for jewellery clients."

### Should NOT trigger (3)
1. "Send a proposal to this client." (→ `leadup-sales-proposal-builder`)
2. "Plan features for our SaaS." (→ `leadup-feature-option-planner`)
3. "Just polish this pricing copy." (→ `leadup-human-content-editor`)

### Functional test cases (2)
1. Given "website service for Indian SMBs, team can deliver 2 sites a
   month, no confirmed pricing", return three tiers with `[fill in]`
   prices, named features per tier, an exclusions block, GST handling
   notes, a recommended Standard tier with reasoning, and margin
   notes flagging capacity risk.
2. Given "SaaS subscription pricing for a B2B booking tool,
   subscription only, INR-only first market", return monthly + annual
   pricing per tier (with annual discount band), fair-use limits per
   tier, cancellation/refund language, GST handling, and a clear
   recommended plan flagged "Most popular".

## Success criteria

- Three tiers each with a real, named upgrade over the previous tier.
- No invented prices.
- Exclusions block present.
- Recommended plan flagged with reason.
- Internal margin / capacity notes filled.
- GST / tax / currency handled correctly per market.
- Hand-off to `leadup-human-content-editor` before publishing.
