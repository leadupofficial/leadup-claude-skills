---
name: leadup-digital-ads-planner
description: Plan a paid digital ads campaign across Google Ads, Meta (Facebook + Instagram), YouTube, and LinkedIn for a LeadUp client or SaaS, with objective, platform pick, audiences, campaign/ad set/ad structure, budget split, ad copy variants, creative ideas, landing page requirements, tracking checklist, and platform policy risk notes. Use when the user says "ads plan", "digital ads", "google ads", "meta ads", "facebook ads", "instagram ads", "campaign plan", or "ad budget".
---

# LeadUp Digital Ads Planner

## Purpose

Take a business goal and produce a complete paid-ads plan a small LeadUp
team can launch: which platform(s), what audiences, what campaign
structure, what budget split, what ad copy and creative, what landing
page is required, what tracking must be in place, and what policy /
account risks to watch.

## When to use

Use when the user wants a paid-ads plan, not a social media organic
calendar (use `leadup-smm-growth-planner`), not an SEO audit (use
`leadup-seo-strategist`), and not the actual ads account setup (which is
manual work in the platform).

Trigger phrases: "ads plan", "digital ads", "google ads", "meta ads",
"facebook ads", "instagram ads", "campaign plan", "ad budget", "ppc plan",
"performance ads", "youtube ads", "linkedin ads".

## Inputs needed

- Business / product, audience, market (country, city, language).
- Goal: leads, bookings, signups, ecommerce sales, app installs, brand.
- Budget per month (currency and amount).
- Existing assets: landing page, tracking, pixel, GA4, conversion API.
- Past campaign data (if any): platform, ROAS, CPL, CPA, CTR.
- Constraints: regulated industry, brand restrictions, banned competitors.

Ask at most 2 clarifying questions if goal, budget, or market is unclear.

## Required resources

- **Official docs**: Google Ads Help, Meta Business Help Center, LinkedIn
  Ads Help, YouTube Ads, Microsoft Advertising, Apple Search Ads.
- **Native tools**: Google Ads, Meta Ads Manager, LinkedIn Campaign
  Manager, GA4, Google Tag Manager.
- **Audience research**: Meta Ad Library, Google Ads Transparency, Reddit
  / niche communities, the user's CRM/list.
- **Compliance**: Google Ads policies, Meta advertising standards,
  industry-specific rules (health, finance, real estate, gambling).
- Keyword inputs from `leadup-keyword-competitor-researcher`.
- Landing page from `leadup-landing-page-cro-planner`.
- Tracking integration via `leadup-api-research-builder`.

If exact CPC, CPM, or CPL data is not available, label as **estimated
band** based on market and category.

## Internet research workflow

1. Confirm objective + measurable conversion event (lead form, booking,
   signup, purchase).
2. Confirm market and audience size band (small / medium / large) for the
   chosen platforms.
3. Check 5–10 active ads from 3 competitors in **Meta Ad Library** and
   **Google Ads Transparency**; record format, hook, CTA, landing page
   pattern.
4. Check Google Keyword Planner for keyword volume + CPC bands (if
   running Search).
5. Verify any regulated category against platform policies before
   committing creative direction.
6. Note assumptions and which numbers are **verified** vs **estimated**.

If a browser or ads-platform MCP is available, hand off to
`leadup-mcp-tool-orchestrator`.

## Step-by-step workflow

1. **Restate brief** (business, goal, budget, market, conversion event).
2. **Pick platform(s)** using the audience × intent × budget rule:
   - **Search-intent buyers** → Google Search Ads first.
   - **Visual discovery / interest-based** → Meta + Instagram.
   - **B2B / role-targeted** → LinkedIn.
   - **Video / awareness** → YouTube + Shorts.
   - **Hyper-local services** → Google Local + Meta lookalikes.
3. **Audience design**: define core, lookalike, and remarketing segments
   per platform.
4. **Campaign / ad set / ad structure**: build out the hierarchy with
   3–6 campaigns at most; one objective per campaign.
5. **Budget split**: % per platform, % per campaign, daily vs lifetime,
   bid strategy.
6. **Ad copy**: 3 variants per ad set (hook + body + CTA), within each
   platform's character limits.
7. **Creative ideas**: 3–6 specific concepts (UGC, founder, before/after,
   demo, testimonial).
8. **Landing page requirement**: spec what the LP must include; if it
   doesn't exist or won't convert, route to
   `leadup-landing-page-cro-planner`.
9. **Tracking checklist**: pixel, conversion API, GA4 events, UTM
   structure, offline conversion upload (if relevant).
10. **Policy + risk notes**: regulated claims, restricted categories,
    account-disable risks, brand-safety.
11. **Test plan**: what to test first (audience vs creative vs offer),
    minimum data needed before deciding, kill criteria.

Full framework: `references/digital-ads-framework.md`.
Plan shape: `assets/ad-plan.template.md`.

## Required output format

One Markdown plan with these sections, in this order:

1. **Brief** — business, goal, market, budget, conversion event.
2. **Platform recommendation** — table: platform · why · share of budget.
3. **Audiences** — per platform, list of segments (core, lookalike,
   remarketing) with one-line targeting rules.
4. **Campaign structure** — campaign → ad set → ad hierarchy.
5. **Budget split** — % per campaign, daily cap, bid strategy.
6. **Ad copy** — 3 variants per ad set with character counts.
7. **Creative ideas** — 3–6 concepts with format notes.
8. **Landing page requirement** — must-haves + CTA + form fields.
9. **Tracking checklist** — pixel / CAPI / GA4 events / UTM / offline.
10. **Policy + risk notes** — what could get the ad disapproved or the
    account disabled.
11. **Test plan** — first 14 days: what to test, minimum data, kill rules.
12. **Assumptions and data confidence** — verified / estimated / requires
    verification.

Defer ad-copy stylistic polish to `leadup-human-content-editor`.

## Safety rules

- Do **not** invent CTR, CPC, CPM, or CPL numbers. Use **estimated
  bands** based on market/category; label clearly.
- Do **not** promise a specific ROAS or CPA without a stated assumption
  set (audience size, creative quality, landing page CR).
- Do **not** propose tactics that violate platform policy: cloaking,
  before/after for restricted categories without disclaimers, personal
  attribute targeting (race, religion, sexual orientation) on Meta,
  fake countdowns, fake scarcity, misleading claims.
- Do **not** use trademarked competitor names in Google Search ad copy
  without rights; for keyword bidding, follow each platform's rules.
- Regulated industries (health, finance, real estate, alcohol, gambling,
  crypto): flag every claim for compliance review; note category-specific
  ad restrictions.
- For India: do not target unsupported categories; remember KYC + Razorpay
  rules where relevant; flag IT Rules and ASCI guidelines for influencer-
  style creative.
- Defer integrations (pixel, CAPI, server-side tracking) to
  `leadup-api-research-builder`.
- Defer landing-page conversion work to `leadup-landing-page-cro-planner`.
- Defer copy polish to `leadup-human-content-editor`.

## Common mistakes

- Picking Meta when buyers are clearly searching (Search beats Discovery).
- 10 campaigns × 5 ad sets × 5 ads on a ₹30,000/month budget — too
  fragmented to learn.
- No conversion event defined → optimizing for link clicks → no leads.
- Inventing a CPL number to justify the budget.
- Forgetting the pixel or CAPI before launch.
- Ignoring landing-page conversion — high CTR + bad LP = wasted spend.
- Using "best in India" / "guaranteed" claims that get the ad disapproved.
- Setting bid to "Maximize Conversions" with no conversion data — the
  algorithm has nothing to optimize toward.

## Troubleshooting

- **Budget too small for the platform** (e.g. LinkedIn at ₹500/day): pick
  a cheaper platform or narrow scope; flag the constraint.
- **No tracking yet**: stage a 7-day pre-launch checklist (pixel, CAPI,
  GA4, UTM, GTM); do not launch until tracking validated.
- **Regulated category disapproval**: rework creative to remove banned
  claims; cite the specific policy clause.
- **Past campaigns underperformed**: ask for the export; diagnose
  (creative, audience, LP, offer) before recommending a new plan.
- **No landing page**: pause and route to
  `leadup-landing-page-cro-planner`; do not launch ads to the homepage
  for a paid campaign.
- **User wants 'just give me the ad copy'**: deliver only sections 6–8
  + the policy risk notes.

## Test prompts

### Should trigger (5)
1. "Plan a Google Ads campaign for our salon booking SaaS in India."
2. "Build a Meta Ads plan for a jewellery client, budget ₹50K/month."
3. "Set up a LinkedIn ads strategy for our B2B booking tool."
4. "Digital ads plan for a dental clinic in Coimbatore."
5. "We have ₹1L/month for ads — what should we run and how do we structure it?"

### Should NOT trigger (3)
1. "Plan 30 days of organic Instagram posts." (→ `leadup-smm-growth-planner`)
2. "Improve our landing page conversion." (→ `leadup-landing-page-cro-planner`)
3. "Research keywords for SEO." (→ `leadup-keyword-competitor-researcher`)

### Functional test cases (2)
1. Given "Indian salon booking SaaS, ₹60K/month, goal = signups", return
   a plan with Google Search + Meta split, 3 campaigns max, 3 ad
   variants per ad set, full tracking checklist, India-specific policy
   notes (ASCI, IT Rules), and bands not invented numbers for CPC/CPL.
2. Given a regulated category (a dental clinic running before/after
   visuals on Meta), return a plan that flags the platform-policy risk,
   rewords creative to comply, lists the disclaimers required, and notes
   what would get the account disabled.

## Success criteria

- Plan has all 12 required sections in order.
- Platform pick is justified by audience × intent × budget reasoning.
- Campaign hierarchy fits the stated budget (no over-fragmentation).
- Tracking checklist is concrete (pixel ID placeholder, GA4 events
  named, UTM convention defined).
- Policy and risk notes are specific to the user's category and market.
- Every metric (CTR, CPC, CPL, ROAS) is labelled **estimated band** with
  the source, or marked **requires verification**.
- Hand-offs to `leadup-landing-page-cro-planner`,
  `leadup-api-research-builder`, and `leadup-human-content-editor` are
  explicit.
