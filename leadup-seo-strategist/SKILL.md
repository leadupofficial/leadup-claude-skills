---
name: leadup-seo-strategist
description: Audit a LeadUp client website or SaaS site and produce a clear SEO action plan covering technical SEO, on-page fixes, meta titles and descriptions, internal linking, schema, content gaps, and a 30/60/90 day roadmap for Indian and international audiences. Use when the user says "seo audit", "improve seo", "technical seo", "meta title", "search ranking", "seo roadmap", or "on page seo".
---

# LeadUp SEO Strategist

## Purpose

Audit a website and return a prioritized SEO action plan that a small LeadUp
team can actually ship in 30 / 60 / 90 days. Covers technical SEO, on-page
fixes, meta titles and descriptions, internal linking, schema, and content
gaps. Tuned for Indian small businesses, multi-tenant SaaS, and
international client sites under `*.leadup.in`.

## When to use

Use when the user wants a site audited or an SEO plan written, not when they
want a single blog draft (use `leadup-blog-content-writer`), a keyword list
(use `leadup-keyword-competitor-researcher`), or a CRO plan
(use `leadup-landing-page-cro-planner`).

Trigger phrases: "seo audit", "improve seo", "technical seo", "meta title",
"search ranking", "seo roadmap", "on page seo", "seo plan", "audit my
website seo".

## Inputs needed

- Site URL or local repo path.
- Audience and market (India / international / both, languages).
- Primary goal: leads, bookings, signups, ecommerce sales, content traffic.
- Top 3 competitor URLs if known.
- Current keywords/pages the site already ranks for (if known).
- Access to Google Search Console / GA4 / PageSpeed Insights (yes / no).
- Stack (Next.js, WordPress, custom) so fixes can be made in the right
  place.

Ask at most 2 clarifying questions if goal or market is unclear.

## Required resources

Prefer in this order:

- **Official docs**: Google Search Central, Schema.org, web.dev,
  developers.google.com/search.
- **Live signals**: Google Search Console (queries, coverage, Core Web
  Vitals), GA4 (landing pages), PageSpeed Insights / Lighthouse, Bing
  Webmaster Tools if available.
- **Crawl**: the live site (HTML, robots.txt, sitemap.xml,
  `<head>` tags, structured data via `view-source:` or fetch).
- **Competitor sites**: their public HTML, meta tags, and content
  structure (no scraping behind logins; no copying content).
- **Keyword tools** if available: Google Keyword Planner, Search Console
  query report, Ahrefs / Semrush (only if the user has access).

If a metric is not directly observable (volume, CPC, ranking position),
label it **estimated** or **requires verification** in the output.

## Internet research workflow

1. Confirm the URL is reachable; note redirects (http → https, www → root).
2. Pull `/robots.txt` and `/sitemap.xml`; note disallows, sitemap count,
   last-modified.
3. Fetch the home page and 3–5 key pages; record `<title>`,
   `<meta description>`, `<h1>`, canonical, hreflang, OG tags, JSON-LD.
4. Run PageSpeed Insights / Lighthouse on mobile + desktop for those pages
   if the tool is available; record Core Web Vitals scores.
5. Open Search Console (if the user has access): top queries, coverage
   errors, mobile usability, Core Web Vitals report.
6. Skim 3 competitor pages for the same intent: note their title pattern,
   word count band, headings, schema, internal links.
7. Note assumptions and what was not checkable in this session.

If a browser or search MCP is available, hand off to
`leadup-mcp-tool-orchestrator` for the fetch/crawl step.

## Step-by-step workflow

1. **Restate goal** in one line (e.g. "more leads from `salon-booking`
   searches in tier-2 Indian cities").
2. **Crawl basics** as above; build a per-page snapshot.
3. **Score technical SEO**: HTTPS, redirects, robots.txt, sitemap, canonical,
   hreflang (if multi-language), Core Web Vitals, mobile usability, broken
   links, duplicate content, JS rendering, indexable vs noindex.
4. **Score on-page**: title length and intent match, meta description CTR,
   H1 presence and uniqueness, heading hierarchy, image alts, content depth
   vs intent, internal link density.
5. **Suggest meta**: rewrite titles and descriptions for the 5–10 highest-
   value pages with target keyword + benefit + 50–60 / 150–160 char limits.
6. **Internal linking**: map 5–10 "hub → spoke" links the site is missing,
   using anchor text that matches the target page's main keyword.
7. **Schema**: recommend JSON-LD blocks per page type (LocalBusiness,
   Service, FAQ, Article, Product, BreadcrumbList) and link to Schema.org.
8. **Content gaps**: list 5–10 topics the site is missing vs competitors and
   the user's services; mark each with intent (informational, commercial,
   transactional).
9. **30/60/90 roadmap**: order fixes by impact and effort. 30 days =
   crawl/index/title-meta basics. 60 days = schema, internal links, top
   on-page rewrites. 90 days = content gap pieces, backlink outreach,
   measurement.
10. **Hand-off**: copy and titles go to `leadup-human-content-editor` for
    final polish; keyword/competitor lists go to
    `leadup-keyword-competitor-researcher` for deeper expansion.

Full checklist: `references/seo-checklist.md`.
Filled audit shape: `assets/seo-audit.template.md`.

## Required output format

One Markdown report with these sections, in this order:

1. **Summary** — site, goal, top 3 wins, top 3 risks.
2. **Technical SEO** — table: issue · severity (high/med/low) · where ·
   fix · effort (S/M/L).
3. **On-page SEO** — per-page rewrites for the top 5–10 pages: current
   title / current meta / proposed title / proposed meta / target keyword.
4. **Internal linking** — list of 5–10 new links: from-page → to-page,
   anchor text, intent.
5. **Schema** — per page type, the JSON-LD type to add and one-line reason.
6. **Content gaps** — 5–10 topics with intent and suggested page type.
7. **30/60/90 day roadmap** — three bulleted blocks, ordered by impact.
8. **Assumptions and data confidence** — what is **verified** vs
   **estimated** vs **requires verification** (volumes, CPC, ranking
   positions).

Keep tone simple and business-ready; defer final public-facing copy edits
to `leadup-human-content-editor`.

## Safety rules

- Do **not** invent traffic numbers, keyword volumes, CPC, or ranking
  positions. Label any number as **verified** (came from a tool/source),
  **estimated** (reasoned), or **requires verification**.
- Do **not** promise rankings or timelines beyond "based on similar sites,
  expect X within Y, assuming Z". No guarantees.
- Do **not** copy competitor content. Reference their patterns, do not
  paste their text.
- Respect copyright and the site's robots.txt; do not crawl behind logins
  or paywalls.
- Do not push hat techniques (PBNs, link buying, cloaking, doorway pages).
- Keep meta titles 50–60 chars and descriptions 150–160 chars unless the
  user explicitly overrides.
- For client work, flag changes that need legal / brand approval (claims
  like "best in India", trademarks, comparative claims).
- Defer public copy to `leadup-human-content-editor`; defer integrations to
  `leadup-api-research-builder`; defer browser/search tooling to
  `leadup-mcp-tool-orchestrator`.

## Common mistakes

- Treating volume estimates as fact.
- Rewriting every title to be 60 chars exactly (template feel).
- Recommending JSON-LD for page types the site does not have.
- Suggesting 100 fixes with no priority — the team cannot ship 100.
- Ignoring mobile and Core Web Vitals.
- Forgetting India-specific signals (UPI, GST, Hindi/regional language
  pages, hreflang).
- Confusing this skill with `leadup-keyword-competitor-researcher` — that
  one expands keywords; this one audits and plans.
- Writing the rewritten meta titles in AI hype tone (em dashes, "unlock /
  empower"). Pass through `leadup-human-content-editor`.

## Troubleshooting

- **No GSC / GA4 access**: do the audit from public signals only; flag
  every metric as **requires verification** and list what to confirm once
  access is granted.
- **JS-rendered site (SPA)**: note that the visible DOM differs from the
  raw HTML; recommend SSR/ISR for the pages that need to rank.
- **Multi-tenant SaaS**: scope the audit to the marketing site, not tenant
  subdomains (unless the user asks).
- **Multi-language**: confirm hreflang strategy and language URLs before
  proposing meta rewrites.
- **Site temporarily down / blocked**: pause and ask for a cached copy, a
  preview URL, or a recent crawl export.
- **User wants a single blog post**: route to `leadup-blog-content-writer`.

## Test prompts

### Should trigger (5)
1. "Do an SEO audit of our jewellery client's site."
2. "Improve SEO for our SaaS landing page."
3. "Write a 30/60/90 day SEO roadmap for this Next.js site."
4. "Fix on-page SEO and meta titles for these 8 pages."
5. "Technical SEO audit for our salon booking site."

### Should NOT trigger (3)
1. "Write one SEO blog post on dental veneers." (→ `leadup-blog-content-writer`)
2. "Find me 100 keywords and their volumes." (→ `leadup-keyword-competitor-researcher`)
3. "Improve our landing-page conversion rate." (→ `leadup-landing-page-cro-planner`)

### Functional test cases (2)
1. Given a Next.js marketing site URL and "improve search rankings for
   dental booking in Coimbatore", return a Markdown report with all 8
   required sections, prioritized 30/60/90 actions, per-page meta rewrites
   under 60/160 char limits, and every metric explicitly labelled
   verified/estimated/requires verification.
2. Given a WordPress site with no GSC access, return the audit using only
   public signals, flag every traffic and ranking number as **requires
   verification**, and list the GSC/GA4 checks needed to upgrade those to
   **verified** in the next pass.

## Success criteria

- Report has all 8 required sections in order.
- Every metric is labelled verified / estimated / requires verification.
- Top 5–10 pages have proposed meta titles (50–60 char) and meta
  descriptions (150–160 char).
- 30/60/90 roadmap is prioritized by impact × effort, not by a flat list.
- No ranking promises, no copied competitor content, no hype tone.
- Hand-offs called out: copy → `leadup-human-content-editor`, keywords →
  `leadup-keyword-competitor-researcher`, tools → `leadup-mcp-tool-orchestrator`.
