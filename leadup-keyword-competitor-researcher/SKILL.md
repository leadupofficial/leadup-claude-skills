---
name: leadup-keyword-competitor-researcher
description: Research seed keywords, build keyword clusters with intent and priority, and analyze 3–5 competitors to surface content gaps and a keyword map for a LeadUp website, SaaS landing, or client project. Labels every volume, CPC, and difficulty number as verified, estimated, or requires verification. Use when the user says "keyword finder", "competitor analysis", "find keywords", "seo keywords", "research competitors", "keyword plan", or "what keywords should we target".
---

# LeadUp Keyword + Competitor Researcher

## Purpose

Given a business, product, or page, return a structured keyword map and a
short competitor analysis the LeadUp team can use to plan SEO content,
service pages, and landing pages. The output is grouped by topic, scored
by intent and priority, and honest about which numbers are verified vs
estimated.

## When to use

Use when the user wants keyword research or competitor analysis. Do **not**
trigger when the user wants the full SEO audit (use `leadup-seo-strategist`),
a written blog (use `leadup-blog-content-writer`), or a paid-ads keyword
plan only (use `leadup-digital-ads-planner`).

Trigger phrases: "keyword finder", "competitor analysis", "find keywords",
"seo keywords", "research competitors", "keyword plan", "what keywords
should we target", "build a keyword map".

## Inputs needed

- Business / product description in 1–2 lines.
- Audience and market (India tier-1/2/3, international, languages).
- 3–5 competitors (URLs if known; else infer from search).
- Existing pages to map keywords to (URLs or page list).
- Access to data sources: Google Search Console, Google Keyword Planner,
  Ahrefs / Semrush, Ubersuggest, AnswerThePublic, Reddit, YouTube
  (mark which are available).
- Constraint: max keywords (default 30–50 for a small business, 100–200
  for a SaaS).

Ask at most 2 clarifying questions if the business or market is unclear.

## Required resources

- **Official / authoritative**: Google Keyword Planner, Google Search
  Console (Performance + queries), Google Trends.
- **Free**: AnswerThePublic, AlsoAsked, Google "People also ask",
  autocomplete suggestions, Reddit threads, YouTube auto-suggest.
- **Paid (if user has access)**: Ahrefs, Semrush, Moz, Ubersuggest.
- **Competitor sites**: their HTML (titles, H1s, URL structure), their
  blog index, their sitemap.xml.
- **LeadUp memory**: prior project keyword lists if relevant.

If exact volume, CPC, or difficulty is not available in a tool, **estimate
with a banded label** (low/med/high) and mark the row **estimated**.

## Internet research workflow

1. Extract seed terms from the business description (services, audiences,
   problems, locations).
2. Expand seeds via: Google autocomplete, "People also ask", related
   searches, and AnswerThePublic; record each suggestion.
3. Pull competitor URLs from a search for the top 3 seed terms; record the
   top-ranking 3–5 organic results per seed.
4. For each competitor: scan sitemap.xml or `/blog/` index, list URLs by
   topic; record their title pattern, H1, and any obvious topic clusters.
5. If Search Console / Keyword Planner / Ahrefs is available, pull
   volumes, difficulty, and CPC; record source per row.
6. Cluster keywords by intent (informational, commercial, transactional,
   navigational) and by topic.
7. Identify content gaps: topics competitors rank for that the user does
   not yet have a page for.
8. Note assumptions and any term where intent was ambiguous.

If a browser or SEO MCP is available, hand off the fetch step to
`leadup-mcp-tool-orchestrator`.

## Step-by-step workflow

1. **Restate the brief** (business, audience, market, max keywords).
2. **Build the seed list** from the business description.
3. **Expand seeds** using free sources, then paid if available.
4. **Cluster** by topic and intent.
5. **Score** each keyword for priority (high/med/low) using:
   - intent fit to business goal,
   - estimated volume band (low/med/high),
   - difficulty band (low/med/high),
   - effort to rank (page already exists vs needs new page).
6. **Map** each keyword to a page (existing URL or "new").
7. **Competitor pass**: for the top 5–10 keywords, list 3 competitor URLs
   and one-line "why they rank" + content gap.
8. **Output** the keyword map (Markdown table or CSV) + the competitor
   summary + assumptions block.

Full framework: `references/keyword-research-framework.md` and
`references/competitor-analysis-framework.md`.
CSV shape: `assets/keyword-map.template.csv`.

## Required output format

One Markdown report with these sections, in this order:

1. **Brief** — business, audience, market, max keywords.
2. **Seed keywords** — 8–15 seeds the rest of the map expands from.
3. **Keyword map** — table with columns: `keyword`, `cluster`, `intent`
   (info/comm/trans/nav), `page type`, `target page`, `priority`
   (high/med/low), `volume band`, `difficulty band`, `data source`,
   `confidence` (verified / estimated / requires verification).
   Provide also a CSV-ready version using
   `assets/keyword-map.template.csv`.
4. **Clusters** — list of topic clusters; for each, the 5–10 keywords
   inside and the recommended page type (pillar / spoke / service /
   landing / blog).
5. **Competitor analysis** — for 3–5 competitors: domain, what they rank
   for, content structure, one strength, one gap LeadUp can attack.
6. **Content gaps** — 5–10 topics the user does not yet cover that
   competitors do.
7. **Assumptions and data confidence** — sources used, what is verified
   vs estimated vs requires verification, what would unlock better data.
8. **Hand-offs** — pages to feed into `leadup-seo-strategist`,
   `leadup-blog-content-writer`, or `leadup-landing-page-cro-planner`.

Keep tone simple. Defer public copy polish to `leadup-human-content-editor`.

## Safety rules

- Never invent volumes, CPC, or difficulty. Use banded labels
  (low/med/high) and mark **estimated** if a tool number is not available.
- Never invent competitor traffic ("they get 50K visits/month") — say
  **estimated band** with reasoning.
- Do not copy competitor content; reference structure and patterns only.
- Respect robots.txt and paywalls; do not scrape gated content.
- No ranking guarantees.
- Flag any keyword that conflicts with brand voice, legal claims, or
  regulated industries (health, finance, alcohol, gambling, real estate).
- Keep India-specific keywords (city + service) honest; do not pad lists
  with cities the user does not operate in.
- Defer integrations to `leadup-api-research-builder`; defer browser /
  search tooling to `leadup-mcp-tool-orchestrator`; defer public copy
  polish to `leadup-human-content-editor`.

## Common mistakes

- Treating tool-free estimates as fact.
- Padding the list with high-volume but irrelevant keywords.
- Skipping intent classification — the map becomes a wish list.
- One huge cluster with 80 keywords instead of 6–10 focused clusters.
- Ignoring informational keywords because they "don't convert" — they feed
  the pillar pages.
- Inventing competitors that don't actually rank for the seed terms.
- Forgetting to map each keyword to a target page (existing or new).
- Producing prose instead of a table the user can paste into a sheet.

## Troubleshooting

- **No paid tools, no GSC**: deliver fully labelled **estimated** map +
  list the GSC/Keyword-Planner queries that would upgrade rows to
  **verified**.
- **Hindi / regional language market**: cluster English and vernacular
  keywords separately; note transliteration variants (e.g. "salon" vs
  "saloon").
- **Local-only business**: anchor clusters by city/locality, not
  nationally.
- **SaaS with global audience**: split clusters by region (IN/US/EU)
  because intent and competitors differ.
- **Highly regulated industry**: cap claims; flag every transactional
  keyword for legal/compliance review.
- **User wants instant answers**: deliver a smaller, sharper map (20
  keywords, fully labelled) instead of 200 unlabelled ones.

## Test prompts

### Should trigger (5)
1. "Find keywords and competitors for our dental clinic in Coimbatore."
2. "Build a keyword map for our salon booking SaaS."
3. "Research competitors for our jewellery client's website."
4. "What SEO keywords should we target for hostel-management software?"
5. "Keyword plan for a Flutter app for tutoring centres."

### Should NOT trigger (3)
1. "Do a full SEO audit of our site." (→ `leadup-seo-strategist`)
2. "Write a blog post on dental veneers." (→ `leadup-blog-content-writer`)
3. "Plan a Google Ads campaign for booking searches." (→ `leadup-digital-ads-planner`)

### Functional test cases (2)
1. Given "salon booking SaaS, target tier-2 Indian cities", with no paid
   tool access, return a 30–50 row keyword map with intent, priority,
   volume band, difficulty band, data source per row, and every numerical
   cell labelled estimated / requires verification, plus 3 competitors
   with one-line gaps.
2. Given access to Google Search Console for the user's existing site,
   return a map that explicitly marks rows pulled from GSC as
   **verified** with the GSC query name, and labels the rest as
   **estimated**; include a content-gap section listing 5+ topics
   competitors cover but the user does not.

## Success criteria

- Keyword map has all required columns and every numeric cell is labelled
  verified / estimated / requires verification.
- Keywords are clustered by topic AND classified by intent.
- Each keyword is mapped to an existing or new target page.
- Competitor analysis is honest about traffic estimates (banded, not
  invented).
- Content gaps are specific (named topics, named page types).
- CSV-ready version of the map is provided via
  `assets/keyword-map.template.csv`.
- Hand-offs to `leadup-seo-strategist`, `leadup-blog-content-writer`, or
  `leadup-landing-page-cro-planner` are explicit.
