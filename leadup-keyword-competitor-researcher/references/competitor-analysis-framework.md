# Competitor analysis framework — LeadUp

Short, honest competitor research for SEO and growth planning. No invented
traffic, no scraped copy.

## Who counts as a competitor?

Three kinds, name them separately:

1. **Direct competitors** — same product, same audience (e.g. another
   salon-booking SaaS in India).
2. **Search competitors** — different product, but ranks for your target
   keywords (e.g. a salon-booking *blog* outranks salon SaaS pages).
3. **Adjacent competitors** — different audience but the same buyer might
   compare with you (e.g. a generic CRM that does salon scheduling).

Pick 3–5 total across these buckets, not 20.

## What to look at for each competitor

Public signals only (no logins, no scraping behind auth, no copying copy):

- **Domain** + **about page** — what they actually do, in their words.
- **Homepage** — hero, value proposition, top CTA, top trust signals.
- **Service / pricing page** — packaging, price points (in their currency).
- **Sitemap** (`/sitemap.xml`) or `/blog/` index — total pages, topic
  coverage, recency of updates.
- **Top 5 ranking pages** for the user's 5 target keywords — URL, title
  pattern, H1, word count band, schema present.
- **Backlinks / authority** — only if a paid tool is available; otherwise
  write **requires verification**.
- **Social signals** — Instagram / LinkedIn presence, follower band, last
  post date.
- **Ads** — running Meta Ads or Google Ads? (Check Meta Ad Library,
  Google Ads Transparency).

## How to record findings

For each competitor, one short profile:

```
Competitor: [domain]
Bucket: [direct / search / adjacent]
What they do: [one line]
Target audience: [one line]
Top traffic guess: [band — small / medium / large; mark "estimated"
                   unless tool number]
Ranks for: [3–5 of the user's target keywords]
Content structure: [pillar+spoke / lots of thin posts / pure landing pages]
One strength: [one line]
One gap to attack: [one line — content topic, page type, or angle]
Ads running: [yes / no / unknown; platforms]
```

## Spotting content gaps

For each cluster the user wants to rank for:

1. List the top 5 ranking competitor URLs.
2. Note the **shared headings** across them — these are the table-stakes
   sections any new page must include.
3. Note **angles missing from all of them** — these are differentiation
   opportunities (e.g. an Indian price comparison, a regional language
   version, a calculator).
4. Mark which gaps the user can credibly fill given their actual product /
   audience.

## What NOT to do

- Do **not** quote competitor copy verbatim. Reference structure and angle
  only.
- Do **not** invent traffic numbers. Bands with "estimated" label only.
- Do **not** scrape content behind logins or paywalls.
- Do **not** call a much larger player "easy to beat" — be honest about
  effort and authority.
- Do **not** pad the competitor list to look thorough. 3–5 is enough.

## India / international notes

- For Indian local-service businesses, competitors are usually within the
  same city; do not benchmark a tier-2 salon against a national chain
  without saying so.
- For SaaS, separate **Indian competitors** from **global competitors**;
  pricing, language, and trust signals differ.
- Note **language coverage**: do competitors have Hindi / regional pages?
  If yes, that's a gap or a moat depending on the user's market.

## Output (for the keyword researcher)

The competitor analysis section in the final report should contain:

- 3–5 competitor profiles (one block each, format above).
- A **content gaps** sub-section listing 5–10 specific topics the user can
  attack, with intent and proposed page type.
- An **assumptions** note: which numbers are verified vs estimated.

Hand-off: feed the gap list to `leadup-seo-strategist` (for roadmap),
`leadup-blog-content-writer` (for drafts), or
`leadup-landing-page-cro-planner` (for landing pages).
