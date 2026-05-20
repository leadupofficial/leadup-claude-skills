# SEO checklist — LeadUp SEO strategist

A practical, ship-able SEO checklist for LeadUp client sites and SaaS
products. Tuned for small teams who need to prioritize what actually moves
search rankings in India and internationally.

## Technical SEO

### Crawl + index
- [ ] HTTPS everywhere (no mixed content).
- [ ] One canonical host (www vs root, http vs https) with 301 redirects.
- [ ] `robots.txt` present, allows crawl of public pages, disallows admin.
- [ ] `sitemap.xml` present, listed in `robots.txt`, submitted in Search
      Console, last-modified dates accurate.
- [ ] No accidental `noindex` on important pages.
- [ ] No infinite parameter URLs in the index.
- [ ] Canonical tags self-reference on canonical pages and point cross-host
      correctly on duplicates.

### Rendering
- [ ] Important content visible in raw HTML (or SSR/ISR if Next.js).
- [ ] Critical links present in HTML, not only after JS.
- [ ] No important content hidden behind tabs/accordions that require JS to
      load.

### Speed and Core Web Vitals
- [ ] LCP < 2.5s on mobile for the top 5 templates.
- [ ] INP < 200ms.
- [ ] CLS < 0.1.
- [ ] Images served as WebP/AVIF with width/height set.
- [ ] Critical CSS inlined; non-critical CSS deferred.
- [ ] Fonts: `font-display: swap`; preload only the variant the page uses.
- [ ] Third-party scripts audited and lazy-loaded where possible.

### Mobile
- [ ] Mobile usability shows no errors in Search Console.
- [ ] Tap targets ≥ 48px; no horizontal scroll.
- [ ] Viewport meta tag present and correct.

### International / India
- [ ] If multi-language: `hreflang` clusters complete and self-referencing.
- [ ] Currency, prices, and units shown in the visitor's expected format.
- [ ] India: GSTIN footer if invoicing; UPI mention where relevant.

## On-page SEO

### Titles + meta
- [ ] One `<title>` per page, 50–60 chars, keyword + benefit.
- [ ] One `<meta name="description">`, 150–160 chars, CTR-focused, includes
      target keyword.
- [ ] One `<h1>` per page, matches search intent.
- [ ] Heading hierarchy: H1 → H2 → H3, no skipped levels.
- [ ] Title and H1 are similar but not identical.

### Content
- [ ] Content depth matches top-3 ranking pages for the target query (not
      necessarily longer — same intent depth).
- [ ] FAQ section for informational and commercial pages.
- [ ] No thin / duplicate / near-duplicate pages.
- [ ] Updated date visible where relevant (blogs, prices, schedules).

### Images
- [ ] Descriptive file names (not `IMG_1234.jpg`).
- [ ] `alt` text for every meaningful image; empty alt for decorative ones.
- [ ] Captions used where they help users.

### Links
- [ ] Internal links from high-authority pages (home, services) to the
      pages you want to rank.
- [ ] Anchor text matches the target page's main keyword (varied, not
      stuffed).
- [ ] No orphan pages (no pages with zero internal links pointing to them).
- [ ] Broken links: 0 (both internal and outbound).

## Schema (JSON-LD)

Recommend by page type:

| Page type | Suggested JSON-LD |
|---|---|
| Home (local business) | `LocalBusiness`, `Organization` |
| Service page | `Service`, `Organization`, `Breadcrumb` |
| Product page | `Product`, `Offer`, `AggregateRating` (only if real) |
| Article / blog | `Article`, `BreadcrumbList`, optional `FAQPage` |
| FAQ section | `FAQPage` (only when Q&A is visible to user) |
| Reviews | `Review` (only with real, attributable reviews) |
| Pricing | `Service` + `Offer` |
| Contact | `LocalBusiness` with full NAP |

Rule: only add schema for content that is actually on the page. Do not add
`AggregateRating` unless the rating is real and verifiable.

## Content gaps

For each target topic, decide page type:
- **Informational** (how/what/why) → blog or guide.
- **Commercial** (best X for Y, X vs Y) → comparison or list page.
- **Transactional** (buy, book, hire, near me) → service or product page.
- **Navigational** (brand + feature) → product or docs page.

Build "hub → spoke" structures: one pillar page + 5–10 related posts that
link back to the pillar.

## Local SEO (India + global)

- [ ] Google Business Profile claimed, NAP consistent across the web.
- [ ] City + service in title and H1 of local landing pages.
- [ ] Embed of the location map on contact page (lazy-loaded).
- [ ] Local schema with full address, opening hours, phone.
- [ ] Reviews collected through a real flow; do not buy or fake reviews.

## Measurement

- [ ] Search Console verified and connected to GA4.
- [ ] GA4 conversion events defined (lead form, booking, signup, purchase).
- [ ] Weekly check: top queries, top landing pages, coverage errors, Core
      Web Vitals report.
- [ ] Monthly check: ranking movement, click-through rate by query, new
      content performance.

## 30/60/90 day shape (default LeadUp ordering)

**0–30 days — fix crawl, index, and titles**
- Robots, sitemap, canonical, redirects, noindex audit.
- Title + meta rewrites for top 5–10 pages.
- Fix critical Core Web Vitals issues.
- GSC + GA4 setup if missing.

**30–60 days — structure and internal links**
- Schema for each existing page type.
- Internal linking from home/services to ranking targets.
- Image alts, heading hierarchy clean-up.
- Local pages if relevant.

**60–90 days — content and authority**
- Ship 3–5 content-gap pieces (pillar + spokes).
- Backlink outreach to relevant niche sites and directories.
- Measure: which queries moved, which pages need iteration.

## Safety / accuracy rules

- Never invent volumes, CTR, CPC, or ranking positions.
- Label every metric verified / estimated / requires verification.
- No black-hat: PBNs, link buying, cloaking, doorway pages, AI-stuffed thin
  content.
- Defer public copy polish to `leadup-human-content-editor`.
- Defer keyword expansion and competitor depth to
  `leadup-keyword-competitor-researcher`.
