# Notes on `public-apis/public-apis` and other sources

How LeadUp uses each discovery source. Strengths, weaknesses, and the
rules for trusting their data.

## `public-apis/public-apis` (GitHub)

URL: `https://github.com/public-apis/public-apis`.

**What it is:** a community-curated Markdown index of public APIs,
grouped by category, with one-line columns for Auth, HTTPS, CORS, and
a link.

**Strengths:**
- Wide breadth across categories.
- Easy to scan during discovery.
- Free, no signup, no rate limit.

**Weaknesses (must remember):**
- Entries can be **stale**. Auth, CORS, and HTTPS columns may not
  reflect current behavior.
- Pricing is **not** captured.
- Commercial-use status is **not** captured.
- "CORS = yes" sometimes means "yes for some endpoints" only.
- "Auth = No" sometimes means "no for the demo; key required for
  real usage".
- Active maintenance varies across category sections.

**LeadUp rule:** use only as a **discovery starting point**. Never
quote auth, HTTPS, CORS, or pricing from this directory in the final
recommendation. Always re-read the **official docs**.

**Citation in the report:** `public-apis/public-apis` (accessed
YYYY-MM-DD).

## Official API documentation (each provider)

**What it is:** the provider's own docs.

**Strengths:** the source of truth for auth, limits, pricing,
commercial terms, CORS, SDK, webhooks.

**Weaknesses:** marketing pages can blur into docs; pricing pages can
hide caps; old docs can linger.

**LeadUp rule:** every claim in the final recommendation is anchored
to an **official docs URL + access date**.

## Provider pricing pages

**What it is:** the `/<provider>/pricing` page.

**Strengths:** authoritative on tiers, free tier, currency, GST
language.

**Weaknesses:** "Contact sales" tiers hide the real price;
discounts / promo banners can mislead.

**LeadUp rule:** copy the free-tier numbers verbatim with the access
date. If a tier is "contact sales", label it **requires
verification** and link the page.

## RapidAPI

URL: `https://rapidapi.com/`.

**Strengths:** unified billing, request volume + latency stats, user
reviews, common interface for many providers.

**Weaknesses:**
- Extra middleman: latency + potential downtime on top of the
  provider's own.
- Pricing can differ from the provider's direct pricing.
- Some providers have caveats about commercial use through RapidAPI.

**LeadUp rule:** useful for discovery and prototyping; for production,
confirm whether direct integration is cheaper / safer.

## ApyHub

URL: `https://apyhub.com/`.

**Strengths:** utility APIs (PDF, image, validation, conversion) with
a single key and decent free tiers.

**Weaknesses:** newer; verify reliability / SLA before mission-critical
use.

**LeadUp rule:** good for non-critical utility needs; verify
maintenance history before committing.

## Postman public collections

URL: `https://www.postman.com/explore`.

**Strengths:** ready-to-run requests; great for first integration
spike.

**Weaknesses:** collections vary in quality and freshness.

**LeadUp rule:** use for quickstart; do not assume the collection's
auth or env vars match the current docs.

## GitHub (SDKs and examples)

**Strengths:** real code examples, recent commits, issues that show
real-world failure modes.

**Weaknesses:** unofficial libraries may be abandoned or insecure.

**LeadUp rule:** prefer **official** SDKs. If using a community SDK,
check stars, last commit, open security issues. Cite the repo URL.

## API status / incident pages

**Examples:** `status.openai.com`, `status.stripe.com`,
`status.razorpay.com`.

**Strengths:** incident history, SLA signals.

**Weaknesses:** missing or hidden for smaller providers.

**LeadUp rule:** for any production candidate, link the status page in
the report. If there is no status page, downgrade the Reliability
score and flag a risk.

## Aggregator search results (Google)

**Strengths:** surfaces providers not in any directory.

**Weaknesses:** SEO spam; "best X API in 2026" listicles can be
sponsored.

**LeadUp rule:** treat as a lead, not a verdict. Always click through
to the provider's own docs.

## What never goes into the final recommendation

- "The public-apis repo says…" as a pricing or auth claim.
- "An old blog post says…" as a feature claim.
- "Looks free" without a pricing-page URL.
- "Has CORS" without testing or a docs quote.

## How to cite in the LeadUp report

For each candidate:

```
Provider: <name>
Discovered via: public-apis/public-apis (accessed YYYY-MM-DD)
Official docs: <URL> (accessed YYYY-MM-DD)
Pricing page: <URL> (accessed YYYY-MM-DD)
Status page: <URL or "none">
SDK / GitHub: <URL or "REST only">
```

This is the minimum citation block for production-bound recommendations.
