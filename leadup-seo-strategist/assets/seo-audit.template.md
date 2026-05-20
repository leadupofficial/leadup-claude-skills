# SEO audit — [Site name]

> Mode: LeadUp SEO Strategist  ·  Audit date: [YYYY-MM-DD]
> Auditor: [name]  ·  Stack: [Next.js / WordPress / custom]
> Goal in one line: [e.g. "more leads from `dental booking Coimbatore`"]

## 1. Summary

- **Site:** [https://…]
- **Audience / market:** [India tier-2, international, …]
- **Top 3 wins (next 30 days):**
  1. [Specific fix with expected impact]
  2. […]
  3. […]
- **Top 3 risks:**
  1. [Specific risk / blocker]
  2. […]
  3. […]

## 2. Technical SEO

| # | Issue | Severity | Where | Fix | Effort |
|---|---|---|---|---|---|
| 1 | [e.g. Missing `sitemap.xml`] | high | `/sitemap.xml` | [generate via next-sitemap] | S |
| 2 | […] | med | […] | […] | M |
| 3 | […] | low | […] | […] | S |

Core Web Vitals (mobile, top 5 pages):

| Page | LCP | INP | CLS | Notes |
|---|---|---|---|---|
| / | [s] | [ms] | [score] | […] |
| /services | […] | […] | […] | […] |

## 3. On-page SEO — proposed rewrites

| Page | Current title (chars) | Current meta (chars) | Proposed title (≤60) | Proposed meta (≤160) | Target keyword |
|---|---|---|---|---|---|
| / | […] | […] | […] | […] | […] |
| /services/x | […] | […] | […] | […] | […] |

Rule: keyword + benefit + 50–60 char title and 150–160 char meta.

## 4. Internal linking

5–10 new "hub → spoke" links:

| From page | To page | Anchor text | Intent |
|---|---|---|---|
| / | /services/booking | "online booking for clinics" | commercial |
| /services | /blog/no-show-reminders | "reduce no-shows" | informational |

## 5. Schema (JSON-LD)

| Page type | JSON-LD type(s) | One-line reason |
|---|---|---|
| Home | `LocalBusiness`, `Organization` | local intent + brand entity |
| Services | `Service`, `BreadcrumbList` | service catalog |
| Blog | `Article`, `BreadcrumbList` | article rich results |
| Contact | `LocalBusiness` (NAP) | local pack eligibility |

Only add schema for content actually on the page. No fake
`AggregateRating`.

## 6. Content gaps

| # | Topic | Intent | Page type | Notes |
|---|---|---|---|---|
| 1 | [e.g. "WhatsApp reminders for clinics"] | commercial | landing | links to bookings page |
| 2 | […] | informational | blog | pillar piece |
| 3 | […] | transactional | service | high-buyer intent |

## 7. 30 / 60 / 90 day roadmap

**0–30 days — fix crawl, index, titles**
- [ ] [Specific fix #1]
- [ ] [Specific fix #2]

**30–60 days — structure, schema, internal links**
- [ ] [Specific action]
- [ ] [Specific action]

**60–90 days — content gaps + authority**
- [ ] [Specific action]
- [ ] [Specific action]

## 8. Assumptions and data confidence

- [ ] **Verified** (tool source named): [list]
- [ ] **Estimated** (reasoned, no tool): [list]
- [ ] **Requires verification** (need GSC/GA4/PSI access): [list]

Hand-offs:
- Public copy → `leadup-human-content-editor`.
- Keyword/competitor depth → `leadup-keyword-competitor-researcher`.
- Browser/search tooling → `leadup-mcp-tool-orchestrator`.
