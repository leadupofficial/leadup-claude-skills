---
name: leadup-landing-page-cro-planner
description: Audit a LeadUp landing page and produce a prioritized CRO plan covering above-the-fold fixes, CTA, trust signals, lead form, pricing and offer clarity, mobile experience, and A/B test ideas with a clean conversion checklist. Use when the user says "increase conversion", "landing page audit", "improve landing page", "cro", "lead generation page", "cta improve", or "fix our landing page".
---

# LeadUp Landing Page CRO Planner

## Purpose

Audit a landing page (client website, SaaS LP, lead-gen page, app store
listing) and return a prioritized CRO plan the LeadUp team can ship in
days, not months. Covers above-the-fold, CTA, trust, lead form, pricing
and offer, mobile experience, A/B test ideas, and a tick-able conversion
checklist.

## When to use

Use when the user wants a page converted better. Do **not** trigger for a
full SEO audit (use `leadup-seo-strategist`), an ads plan (use
`leadup-digital-ads-planner`), a fresh blog post (use
`leadup-blog-content-writer`), or premium visual UI redesign (use
`leadup-premium-ui-upgrader`).

Trigger phrases: "increase conversion", "landing page audit", "improve
landing page", "cro", "lead generation page", "cta improve", "fix our
landing page", "conversion audit", "boost conversion".

## Inputs needed

- Landing page URL (or local repo path).
- Goal: leads, bookings, signups, purchase, demo.
- Traffic source: paid Meta, Google Ads, SEO, social, mixed.
- Audience and market (India / international, language).
- Existing conversion rate (if known) + tracking source.
- Past tests / known issues / brand constraints.
- Tools available: GA4, Hotjar / Microsoft Clarity, Lighthouse, Search
  Console.

Ask at most 2 clarifying questions if goal or traffic source is unclear.

## Required resources

- **The page itself**: HTML, screenshots desktop + mobile, scroll
  recordings if available.
- **Analytics**: GA4 conversion paths, bounce, time on page, scroll
  depth.
- **Heatmaps / recordings**: Hotjar, Microsoft Clarity, FullStory.
- **Performance**: PageSpeed Insights, Lighthouse, Web Vitals report.
- **Form analytics**: GA4 form interactions, abandonment by field.
- **Competitor pages**: 3–5 competitor LPs for the same intent.
- Final polish for any rewritten copy: `leadup-human-content-editor`.

If specific numbers are not available (CR, drop-off %), label as
**estimated band** or **requires verification**.

## Internet research workflow

1. Open the LP on desktop and mobile; take screenshots above-fold and
   at each scroll snap.
2. Time-test the path: arrive → first CTA click → form → confirm; count
   clicks, fields, frictions.
3. Run Lighthouse on mobile + desktop; record LCP, INP, CLS.
4. Look at 3 competitor LPs for the same intent: above-fold, social
   proof, form length, pricing transparency.
5. If Hotjar / Clarity available: identify drop-off zones, rage clicks,
   form-field abandonment.
6. Note assumptions and which numbers are **verified** (from analytics)
   vs **estimated**.

If a browser MCP is available, hand off to
`leadup-mcp-tool-orchestrator`.

## Step-by-step workflow

1. **Restate goal** in one line.
2. **Above-the-fold audit**: headline clarity (audience + outcome), sub,
   primary CTA visibility, hero visual relevance, page-speed LCP.
3. **CTA audit**: text (verb + outcome), placement (repeat 2–4 times),
   contrast, scroll-aware sticky, mobile thumb reach.
4. **Trust signals audit**: real reviews, logos, certifications,
   testimonials with names + photos, press, awards, security badges
   (where they help, not as decoration).
5. **Lead form audit**: number of fields (cut to what's necessary),
   field order, autofill, country code defaults, validation, error
   states, success state.
6. **Offer / pricing audit**: clarity of value, urgency (real not fake),
   pricing transparency, plan comparison, FAQ.
7. **Mobile audit**: tap targets, font size, sticky CTA, viewport,
   accidental zoom, form keyboard types, performance.
8. **Performance audit**: LCP/INP/CLS, image weight, third-party
   scripts, render-blocking.
9. **A/B test ideas**: 4–8 specific tests, ordered by expected lift × cost.
10. **Conversion checklist**: a 25–40 item tick-list the team can run as
    a pre-launch gate.

Full framework: `references/cro-framework.md`.
Audit shape: `assets/cro-audit.template.md`.

## Required output format

One Markdown audit with these sections, in this order:

1. **Summary** — page URL, goal, current CR (if known), top 3 wins, top
   3 risks.
2. **Above-the-fold** — current vs proposed (headline, sub, CTA, hero,
   speed).
3. **CTA** — placements, text, contrast, mobile reach.
4. **Trust signals** — what's there, what's missing, what to add.
5. **Lead form** — field-by-field critique + proposed minimal form.
6. **Offer / pricing** — clarity issues + proposed structure.
7. **Mobile** — issues and fixes with screenshots/locations.
8. **Performance** — Core Web Vitals + top 3 perf fixes.
9. **A/B test plan** — 4–8 tests with hypothesis, variant, expected lift
   band, effort.
10. **Conversion checklist** — 25–40 items, ticked or to-do.
11. **Assumptions and data confidence** — verified / estimated /
    requires verification.
12. **Hand-offs** — copy → `leadup-human-content-editor`, premium UI →
    `leadup-premium-ui-upgrader`, tracking → `leadup-api-research-builder`.

## Safety rules

- Do **not** invent the page's current conversion rate, drop-off
  percentages, or "industry average" numbers. Use bands and label.
- Do **not** propose dark patterns: fake countdowns, fake stock, hidden
  fees, pre-checked add-ons, opt-out-of-marketing buried in micro-text.
- Do **not** suggest fake reviews, fake logos, or "as seen on" badges
  without the user actually being featured there.
- Do **not** strip legal / compliance notices (GST, refund policy,
  consent checkbox, KYC requirements).
- Keep India-specific signals: GSTIN footer, UPI as a payment option,
  WhatsApp click-to-chat, local currency formatting.
- A/B test ideas must be testable with the user's stated traffic level —
  no recommending tests that need 50K visits/month if they have 2K.
- Defer integrations (tracking, server-side) to
  `leadup-api-research-builder`.
- Defer visual / premium UI redesign to `leadup-premium-ui-upgrader`.
- Defer all rewritten public copy to `leadup-human-content-editor`.

## Common mistakes

- "Improve the hero" with no specific headline/sub/CTA proposal.
- Recommending 30 changes with no priority.
- Adding more trust badges without removing dead weight.
- Cutting fields the sales team actually needs (cut what the marketing
  team can live without, not what sales needs).
- A/B testing 5 things at once — invalid result.
- Mobile audit ignored because the auditor only used desktop.
- Pricing made "clearer" by stripping legal terms (don't).
- Confusing CRO with SEO — different game.

## Troubleshooting

- **No analytics / heatmap data**: deliver the audit from manual UX
  pass + Lighthouse; flag every CR / drop-off claim as **requires
  verification**.
- **Low traffic page** (< 1K/month): skip A/B; deliver a single
  prioritized rebuild plan (the team can't get test significance).
- **Multi-step form / multi-page funnel**: audit each step; identify
  where the steepest drop-off is.
- **Highly regulated category** (finance, health): do not remove
  disclosures; flag changes that need legal review.
- **B2B SaaS LP with demo CTA**: optimize for **qualified demos**, not
  for raw form fills; recommend disqualifying fields if needed.
- **Local-services LP** (salon / clinic / dentist): WhatsApp click-to-
  chat usually outperforms a long form in India.

## Test prompts

### Should trigger (5)
1. "Audit our landing page for conversion."
2. "Improve our lead-gen page — leads dropped this month."
3. "Fix our pricing page CRO."
4. "Plan A/B tests for our demo signup LP."
5. "Why is our Meta Ads landing page converting so badly?"

### Should NOT trigger (3)
1. "Make this landing page look premium." (→ `leadup-premium-ui-upgrader`)
2. "Write a new blog on dental veneers." (→ `leadup-blog-content-writer`)
3. "Plan our Meta Ads campaign." (→ `leadup-digital-ads-planner`)

### Functional test cases (2)
1. Given a Next.js LP URL with Meta Ads traffic and a 4-field lead form,
   return an audit covering all 12 required sections, a proposed 2-field
   form, mobile-specific fixes, 4 A/B tests with expected lift bands,
   and a conversion checklist of 25+ items.
2. Given a LP with no analytics access, return the audit using only
   manual UX + Lighthouse; flag every CR/drop-off claim as **requires
   verification**, and list the GA4/Hotjar setup tasks needed to upgrade
   to **verified**.

## Success criteria

- Report has all 12 required sections in order.
- Every metric is labelled verified / estimated / requires verification.
- Proposed form fields are minimal but include what sales needs.
- A/B test plan is feasible at the user's stated traffic level.
- Conversion checklist has at least 25 items the team can tick off.
- No dark patterns proposed.
- Mobile audit present (not just desktop).
- Hand-offs to `leadup-premium-ui-upgrader`, `leadup-human-content-editor`,
  and `leadup-api-research-builder` are explicit.
