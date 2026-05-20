# Ad plan — [Brand / product]

> Date: [YYYY-MM-DD]  ·  Market: [country / city]
> Monthly budget: [₹ / $] [amount]
> Conversion event: [lead form / booking / signup / purchase]

## 1. Brief

- **Business:** [one line]
- **Goal:** [leads / bookings / signups / sales / app installs / brand]
- **Audience:** [one or two lines]
- **Existing assets:** [LP URL, pixel status, CRM, past data]
- **Constraints:** [regulated category, banned competitors, brand rules]

## 2. Platform recommendation

| Platform | Why | Share of budget |
|---|---|---|
| Google Search | active intent buyers | 40% |
| Meta (FB+IG) | discovery + remarketing | 40% |
| YouTube Shorts | awareness | 10% |
| LinkedIn | only if B2B | 10% |

## 3. Audiences

Per platform:

**Google Search**
- Keywords: [list from `leadup-keyword-competitor-researcher`]
- Negative keywords: [list]

**Meta**
- Core: interests = [list], age = [range], geo = [cities]
- Lookalike: 1–3% from converters / customer list
- Remarketing: site visitors 7/30/90d, video viewers 75%, engagers

**LinkedIn** (if used)
- Targeting: company size + industry + seniority + function

## 4. Campaign structure

```
Campaign 1 — [objective, platform]
  Ad set 1 — [audience]
    Ad A / Ad B / Ad C
  Ad set 2 — [audience]
    Ad A / Ad B / Ad C
Campaign 2 — …
Campaign 3 — Remarketing
```

(Keep total ≤ 6 campaigns; ≤ 3 ad sets each for small budgets.)

## 5. Budget split

| Campaign | Daily / lifetime | Bid strategy | Share |
|---|---|---|---|
| Search — prospect | ₹X/day | Max Clicks → Max Conv after 30 conv | 30% |
| Meta — prospect | ₹X/day | Highest Volume | 25% |
| Meta — lookalike | ₹X/day | Highest Volume | 15% |
| Meta — remarket | ₹X/day | Cost Cap | 15% |
| YouTube — awareness | ₹X/day | Max Reach | 10% |
| Test bucket | ₹X/day | varies | 5% |

## 6. Ad copy (3 per ad set)

For each ad set list:

```
Ad A — Pain → Product → CTA
  Headline (≤27/30 chars): [...]
  Primary text: [...]
  CTA: [Book / Sign up / Get quote]

Ad B — Outcome → Proof → CTA
  […]

Ad C — Question → Reframe → CTA
  […]
```

## 7. Creative ideas

| # | Concept | Format | Notes |
|---|---|---|---|
| 1 | UGC founder talking head | 9:16, 20s, captions | phone-shot |
| 2 | Before / after | 9:16, 15s, disclaimer | category check |
| 3 | Demo walkthrough | 1:1, 30s | screen + voiceover |
| 4 | Local proof | 9:16, 25s | named city, named customer |
| 5 | Testimonial | 1:1, 30s | written consent |
| 6 | Founder POV | 9:16, 30s | story style |

## 8. Landing page requirement

Must-haves:
- Outcome headline above the fold (≤ 8 words).
- Sub-line stating who it's for + the key proof.
- Primary CTA visible without scroll.
- 3–5 trust signals (real reviews / logos).
- Form fields: only what's needed (name, phone, email if needed).
- Mobile-first; LCP < 2.5s.
- UTM-ready; conversion event fires on submit.

If gaps: route to `leadup-landing-page-cro-planner` before launch.

## 9. Tracking checklist

- [ ] Meta Pixel + Conversion API live.
- [ ] Google Ads tag + GA4 linked.
- [ ] GA4 events: `generate_lead` / `purchase` / `sign_up`.
- [ ] UTM convention defined and shared:
      `utm_source=[platform] utm_medium=cpc utm_campaign=[c] utm_content=[a]`.
- [ ] Phone-call tracking (Google call-only + click-to-call Meta).
- [ ] Offline conversion upload (if CRM doesn't fire automatically).
- [ ] One conversion = one event (no double-count).

Integration handed to `leadup-api-research-builder` if API work is needed
(CAPI server-side, CRM webhook, etc.).

## 10. Policy + risk notes

- Category: [healthcare / finance / real estate / cosmetic / general] —
  [restrictions that apply].
- Disclaimers required: [list].
- Trademarked competitor names: [avoid in copy; check bidding rules].
- India: ASCI / IT Rules / KYC notes.
- Account-disable risks: [list].

## 11. Test plan (first 14 days)

- Days 0–3: launch + watch delivery + fix tracking gaps.
- Days 3–7: hands off; let algorithm learn.
- Days 7–10: kill bottom-third creative; introduce 2 new hooks.
- Days 10–14: reallocate budget by campaign CPL.
- Kill rules:
  - Pause ad if CPL > 2× target after 100 clicks.
  - Pause ad set after ₹X spend with 0 conversions.
- Decision review at day 14.

## 12. Assumptions and data confidence

- **Verified** (tool / source named): [list]
- **Estimated bands** (CTR, CPC, CPL): [list, with band]
- **Requires verification**: [list — past CPL, audience size, etc.]

Hand-offs:
- LP work → `leadup-landing-page-cro-planner`.
- Tracking integration → `leadup-api-research-builder`.
- Copy polish → `leadup-human-content-editor`.
