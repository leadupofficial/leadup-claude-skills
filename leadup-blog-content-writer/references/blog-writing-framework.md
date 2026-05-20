# Blog writing framework — LeadUp

How LeadUp writes blogs and service pages that rank, read like a human
wrote them, and convert.

## Step 1 — Brief

Before drafting, lock these in one short block:

- **Goal**: rank for X / generate Y leads / explain Z to existing users.
- **Target keyword** + 2–4 secondary keywords.
- **Search intent**: informational / commercial / transactional / nav.
- **Audience**: who, where, what stage of buying.
- **Tone**: simple business (default), premium/corporate, casual, or
  technical.
- **Word target**: 600–1000 (service), 800–1500 (blog), 2000+ (pillar).
- **Must-include**: facts, numbers, product names, CTAs.
- **Must-avoid**: hype words, competitor claims, regulated claims without
  source.
- **Internal pages to link to** (URL list from the user's site).

## Step 2 — SERP scan

Pull the top 3–5 ranking pages for the target keyword. Record:

- H1 + the full H2 list.
- Word count band.
- Schema used (Article / FAQ / Product / HowTo).
- FAQ topics covered.
- Common gaps (what no one covers, but the user could).

This tells you the **table-stakes** shape and the **differentiator** angle.

## Step 3 — Title and meta

Write 5 title options, each with a different angle:

1. **How-to** ("How to reduce salon no-shows in 30 days")
2. **List** ("7 ways to reduce no-shows")
3. **Mistake** ("Why most clinics still get 20% no-shows")
4. **Comparison** ("WhatsApp reminders vs SMS for clinics")
5. **Case / outcome** ("How one Coimbatore clinic cut no-shows by 30%")

Title rules: ≤ 60 chars, target keyword early, benefit/payoff visible.

Meta description: 150–160 chars, target keyword + benefit + soft CTA.

## Step 4 — Outline

Default outline shape for a 1000–1500 word blog:

```
H1 — [matches intent, includes target keyword]

Hook (2–4 lines) — name the problem, name who feels it, promise the answer.

H2 — [the answer in 30 seconds]
  short paragraph + 3–5 bullets

H2 — [the deeper how]
  H3s as needed, with one example each

H2 — [common mistakes / pitfalls]
  list + one-line fix each

H2 — [tools / next steps]
  with internal links to the user's pages

FAQ (3–6 questions, from PAA)

Closing CTA (one clear action)
```

Adjust for service pages: trade the "deeper how" for **pricing / process /
deliverables / proof / FAQ / CTA**.

## Step 5 — Draft (human writing rules)

Apply the LeadUp human writing rules:

- One idea per sentence.
- Mix sentence lengths — short, medium, occasional long. Avoid four
  same-shape sentences in a row.
- Active voice. Concrete nouns. Plain words.
- Contractions OK unless the brand is formal.
- **No em dashes** (unless the user asks). Replace with comma, period,
  or "and".
- No banned AI hype words (full list in `leadup-human-content-editor`
  references).
- Use specific examples that match the audience (Indian tier-2 city,
  global SaaS user, etc.).
- Where a stat would help but you don't have one, write `[verify: source]`
  instead of inventing.

## Step 6 — FAQ

Pull 3–6 questions from Google PAA + autocomplete + Reddit/Quora for the
target keyword. Answer each in 40–80 words. Mark FAQ section with
`<h2>` and Q&As with `<h3>` or `<strong>` so `FAQPage` schema is easy to
add later.

## Step 7 — Internal links

3–7 internal links per post, with:

- **Anchor** matching the target page's main keyword (varied, not
  stuffed).
- **Target URL** from the user's actual site.
- **Reason** (one line) for why the link belongs there.

No more than 2 links to the same target URL per post.

## Step 8 — Self-check before delivering

- [ ] Zero em dashes (unless asked).
- [ ] Zero banned hype words.
- [ ] Title and meta within length limits.
- [ ] Outline matches the SERP scan + adds one differentiator.
- [ ] Every stat / citation either sourced or flagged `[verify: source]`.
- [ ] FAQ derived from real PAA, not invented.
- [ ] Internal links present with reasoning.
- [ ] Tone matches LeadUp simple-business voice; if not, route to
      `leadup-human-content-editor`.

## When a topic is regulated

For medical, financial, legal, real estate, or other regulated niches:

- Flag every outcome claim with `[verify: source]`.
- Avoid guarantee language ("guaranteed results").
- Add a "consult a professional" line where applicable.
- Tell the user this draft needs subject-matter review before publishing.
