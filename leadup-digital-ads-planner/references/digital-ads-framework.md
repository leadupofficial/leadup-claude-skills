# Digital ads framework — LeadUp

How LeadUp plans paid digital ads. Practical, budget-aware, platform-
policy-safe, India- and global-friendly.

## 1. Pick the platform by intent

| Intent | Best fit |
|---|---|
| Active search ("salon software pricing") | Google Search Ads |
| Visual discovery ("salon design ideas") | Meta + Instagram + Pinterest |
| Role-targeted B2B | LinkedIn |
| Long-form / awareness | YouTube |
| Hyper-local services | Google Local + Meta lookalikes |
| App installs | Meta + Google App Campaigns + Apple Search Ads |
| Remarketing | every platform's own pixel + Google Display |

Budget reality:
- LinkedIn realistically needs ≥ ₹1,500–3,000/day to learn.
- Meta + Google work from ₹500–1,000/day with tight targeting.
- YouTube needs ≥ ₹1,000/day for view-data to stabilize.

## 2. Campaign hierarchy (keep it simple)

For a small budget (≤ ₹1L/month):

- 2–3 campaigns max.
- 2–3 ad sets per campaign.
- 3 ads per ad set.

One objective per campaign. Don't split awareness + conversions in one
campaign.

For a larger budget (₹1L–5L/month):

- 3–6 campaigns.
- Separate campaigns for: prospecting cold, lookalike, remarketing.

## 3. Audience design

Three layers per platform:

1. **Core** — interest / keyword / role-based cold audience.
2. **Lookalike / similar** — built from your converters or customer list.
3. **Remarketing** — site visitors, video viewers, engagers, abandoners.

Rules:
- Core audiences large enough to learn (Meta: 500K–5M for most).
- Don't stack 20 interests — pick the top 3–5.
- Exclude existing customers from prospecting where it's a one-purchase
  product.
- For LinkedIn, target by company size + seniority + function; avoid
  broad "interest" targeting.

## 4. Budget split

Default split:

- 60–70% prospecting (cold + lookalike).
- 20–30% remarketing.
- 5–10% testing (new creative or new audience).

Bid strategies:
- New account / low data: **Maximize Conversions** only after the pixel
  has 30+ events. Until then, use **Maximize Clicks** to learn, then
  switch.
- For Search: start with **Manual CPC** or **Maximize Clicks** until
  conversion data is in.
- For Meta: **Highest Volume** for prospecting, **Cost Cap** if you have
  a target CPL.

## 5. Ad copy

Per ad set, 3 variants:

| Variant | Pattern |
|---|---|
| A | Pain → product → CTA |
| B | Outcome → proof → CTA |
| C | Question → reframe → CTA |

Platform character limits (approx; verify in the platform):

- Google Search: 30/30/30 headlines, 90/90 descriptions, 15 paths.
- Meta primary text: 125 chars visible, max 2200.
- Meta headline: 27–40 chars.
- LinkedIn Single Image: 150 char intro, 70 char headline.
- YouTube: 30 char headline, 35 char description, 15 char path.

CTA: one per ad, specific ("Book a 1-day trial", "WhatsApp us"). Avoid
"Learn more" unless there's a real reason.

No banned hype words. No fake urgency. No fake scarcity.

## 6. Creative ideas (3–6 concepts per plan)

Concepts that consistently outperform stock for small businesses:

- **UGC-style talking head** (founder or staff, phone-shot, 9:16).
- **Before / after** (only if category-safe; dental/cosmetic needs care).
- **Demo / product walk-through** (15–30s, captions on).
- **Testimonial** (real customer, named, consent given).
- **Founder POV** (why they built this).
- **Local proof** (named city + local customer).

Format:
- 9:16 vertical for Meta + Reels + Shorts.
- 1:1 square for feed.
- 16:9 for YouTube + LinkedIn in-feed.
- Captions baked in (most viewers watch muted).

## 7. Landing page requirement

Ads die if the landing page is bad. Spec must include:

- One clear goal (book / sign up / quote / buy).
- Above-the-fold: outcome headline + sub + CTA visible without scroll.
- 3–5 trust signals (real reviews, logos, certifications).
- Form: only the fields you actually need (name + phone for India SMBs,
  often).
- Mobile-first (most India traffic is mobile).
- Page speed: LCP < 2.5s, CLS < 0.1.
- UTM-ready, with form submissions firing the conversion event.

If the LP doesn't meet this, route to `leadup-landing-page-cro-planner`
before launching ads.

## 8. Tracking checklist (do not launch without this)

- [ ] Meta Pixel installed + Conversion API server-side.
- [ ] Google Ads tag installed + GA4 conversion linked.
- [ ] GA4 events: `generate_lead`, `purchase`, `sign_up` (per relevance).
- [ ] UTM convention defined (`utm_source / medium / campaign /
      content / term`) and shared with the team.
- [ ] Phone calls tracked (call-only conversion in Google Ads, click-to-
      call in Meta).
- [ ] Offline conversion upload set up if the CRM doesn't fire events.
- [ ] One conversion = one event (no double-counting).

## 9. Policy + risk notes (do this before creative)

Common reasons ads get disapproved or accounts disabled:

- Personal attributes ("Are you 45 and balding?") on Meta — banned.
- Before/after for cosmetic/medical without disclaimers on Meta — banned.
- Misleading guarantees ("100% guaranteed").
- Trademarked competitor names in Google Search ad copy.
- Restricted categories: alcohol, gambling, dating, financial services,
  pharma, weapons — each has special rules and country restrictions.
- Cloaking / multiple LP redirects.
- Fake urgency / countdown timers that don't match the offer.

India-specific:
- ASCI guidelines for influencer-style creative (must disclose).
- IT Rules for medical / financial / wellness content.
- KYC and Razorpay rules where payment is involved.

## 10. Test plan (first 14 days)

- Days 0–3: launch + watch delivery; fix delivery issues.
- Days 3–7: keep creative + audience constant; let the algorithm learn.
- Days 7–10: kill bottom-third creative; test 2 new hooks.
- Days 10–14: review CPL by campaign; decide budget reallocation.
- Kill rules: pause ads with > 2× target CPL after 100 link clicks; pause
  ad sets after ₹X spend with 0 conversions (set X based on the goal CPL).

## 11. Output

Every ads plan must end with:

- A tracking checklist the user can tick off.
- A policy + risk note specific to the category and market.
- An assumptions block with verified / estimated / requires verification.

Defer integration to `leadup-api-research-builder`. Defer LP work to
`leadup-landing-page-cro-planner`. Defer copy polish to
`leadup-human-content-editor`.
