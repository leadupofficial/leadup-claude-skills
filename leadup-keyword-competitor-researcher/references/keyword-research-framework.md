# Keyword research framework — LeadUp

A small, repeatable framework for keyword research. Built for LeadUp client
sites and SaaS products. No invented numbers.

## 1. Seed the list (8–15 seeds)

Start from the business itself, not from a tool. Write seeds for:

- **Services** the business offers (e.g. "salon booking software").
- **Audiences** (e.g. "for small salon owners", "for dental clinics").
- **Problems** the product solves (e.g. "reduce no-shows",
  "send appointment reminders").
- **Locations** (e.g. "Coimbatore", "tier-2 India", "Dubai").
- **Comparisons** (e.g. "Calendly vs Zoho Bookings").

## 2. Expand (free sources first)

For each seed, expand using:

- **Google autocomplete**: type the seed, capture all suggestions.
- **"People also ask"** boxes on the SERP.
- **Related searches** at the bottom of the SERP.
- **AnswerThePublic / AlsoAsked** for question variants.
- **YouTube autocomplete** for video-intent terms.
- **Reddit / Quora** for natural-language queries.

Only after free sources, add paid:

- **Google Keyword Planner** (volume, competition for ads — use as a
  band hint, not absolute SEO truth).
- **Ahrefs / Semrush** (volume, KD, parent topic) if the user has access.

## 3. Classify by intent

Every keyword falls into one of four buckets:

| Intent | Example | Page type |
|---|---|---|
| Informational | "how to reduce no-shows" | blog, guide |
| Commercial | "best salon booking software" | comparison, listicle |
| Transactional | "salon booking software pricing" | service / pricing page |
| Navigational | "leadup booking demo" | brand page, docs |

If a keyword is ambiguous, write the **likely** intent and flag it.

## 4. Cluster by topic

Group related keywords into 6–10 clusters. Each cluster gets:

- A **pillar topic** (one broad page).
- 5–10 **spoke keywords** (each becomes a sub-page or section).
- A recommended **page type** for the pillar (service / blog / landing /
  comparison).

Avoid one giant cluster of 50 keywords; the team cannot ship one giant
page.

## 5. Score priority (high / med / low)

For each keyword, score on:

| Factor | High | Medium | Low |
|---|---|---|---|
| Intent fit to business goal | direct buyer | adjacent | tangential |
| Volume band | est. 1k+ /mo | est. 200–1k /mo | est. <200 /mo |
| Difficulty band | low / med | med | high |
| Existing page coverage | already ranks page 2–3 | thin page | no page |

Priority = high if at least two factors are high and intent fit is direct.

Always label volume and difficulty as **bands**, not exact numbers, unless
the number came from a tool (then cite the tool).

## 6. Map keywords to pages

Each keyword gets a **target page**:

- An **existing URL** if the page can rank for the keyword with on-page
  edits.
- **NEW** if a new page is needed — write the proposed URL and page type.

No keyword should be unmapped.

## 7. Content gaps

Find topics where:

- Competitors rank for the keyword on page 1.
- The user has no page at all.
- The intent matches the user's business.

These become the priority "new page" targets for the next 60–90 days.

## 8. Data confidence

Every row in the final map carries a confidence label:

- **Verified** — number came from a tool the user has access to (cite the
  tool, e.g. "GSC", "GKP", "Ahrefs").
- **Estimated** — banded based on signals (autocomplete depth, SERP
  competition, common sense).
- **Requires verification** — not estimable without access; mark for the
  next pass once the tool is connected.

## 9. India-specific notes

- Include both English and transliterated forms of common Hindi/regional
  terms ("salon" vs "saloon"; "kirana" vs "grocery").
- Anchor by **city / locality** for service businesses; do not assume
  national reach.
- Be careful with regulated industries (health, finance, real estate,
  alcohol, gambling) — flag keywords that need legal review.

## 10. Output

Always deliver:

- A **Markdown table** of the keyword map for in-doc reading.
- A **CSV** at `assets/keyword-map.template.csv` for spreadsheet use.
- A **clusters** section grouping rows for content planning.
- An **assumptions** block listing sources and what is verified vs
  estimated vs requires verification.

Never deliver a raw list of 300 keywords with no clusters, no intent, and
no priority — that is a wish list, not a plan.
