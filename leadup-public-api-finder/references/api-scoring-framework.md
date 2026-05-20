# API scoring framework — LeadUp

Eight axes, 1–5 each. Average for rank, but any sub-3 is a red flag
that must be called out in the recommendation.

## The 8 axes

### 1. Fit for feature

- 5: solves the exact job; no extra glue.
- 4: solves it with a small adapter.
- 3: works but needs noticeable wrapper code.
- 2: partial fit; need to combine with another API.
- 1: wrong category; bend-to-fit.

### 2. Documentation quality

- 5: clear, complete, OpenAPI, examples in our stack, changelog.
- 4: clear, examples in another stack we can port.
- 3: enough to ship, gaps require trial & error.
- 2: outdated examples, missing endpoints.
- 1: opaque, marketing-only pages.

### 3. Free tier / pricing

- 5: free tier covers expected use; paid tier predictable; INR + GST
     for India.
- 4: free tier covers pilot; paid tier acceptable.
- 3: free is small but workable; paid is unclear or USD-only.
- 2: free is trial only; paid is expensive or per-call surprise.
- 1: no free; pricing hidden.

### 4. Reliability / maintenance

- 5: active changelog, status page, low-incident history.
- 4: active, status page present.
- 3: active but no public status / SLA.
- 2: last release > 12 months.
- 1: looks abandoned (> 24 months) or repeated outages.

### 5. Auth / security

- 5: HTTPS, modern auth (OAuth2 / API key in header), key rotation,
     separate public + secret tokens.
- 4: HTTPS + API key in header.
- 3: HTTPS + API key in query string.
- 2: weak auth, but HTTPS.
- 1: HTTP or no auth where there should be one.

### 6. Frontend compatibility / CORS

- 5: CORS open for the endpoints we need OR clean public-token model.
- 4: CORS open; secret needed for write paths (we'll proxy those).
- 3: No CORS; backend proxy required — but doable.
- 2: No CORS + auth model fights with a proxy.
- 1: SDK strictly requires browser embed of a secret key.

### 7. Backend integration simplicity

- 5: official SDK in our stack + idiomatic.
- 4: official SDK in a stack we can use; small adapter.
- 3: REST only; well-documented; hand-roll client.
- 2: REST with odd shapes; pagination quirks; weak errors.
- 1: SOAP / proprietary / hard to integrate.

### 8. Commercial use safety

- 5: unambiguous commercial use; clean terms; no attribution.
- 4: commercial OK; light attribution acceptable.
- 3: commercial OK with notable conditions (attribution, brand).
- 2: ambiguous; needs legal review.
- 1: free for personal / research only.

## How to use the scores

- Compute an average to rank.
- Any axis < 3 must appear as a **risk** in the recommendation.
- Never recommend an API with score < 3 on **Auth / security**,
  **Commercial use safety**, or **Reliability** for production.
- If "Free tier" scores < 3, switch the decision to either
  `prototype only` or call out a paid plan tier explicitly.
- Tie-breakers: prefer **better docs + better SDK** over slightly
  cheaper.

## Worked example (illustrative — not a real recommendation)

| API | Fit | Docs | Price | Rel | Auth | CORS | Int | Comm | Avg | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
| Candidate A | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 4.75 | none |
| Candidate B | 4 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 4.25 | reliability 3 |
| Candidate C | 5 | 3 | 5 | 4 | 4 | 2 | 3 | 3 | 3.6 | CORS 2 |

Recommendation: A (best), B (backup). Note: B's reliability is the
risk; document fallback. C dropped: backend proxy needed for browser
use + ambiguous commercial.

## Documenting risks

For any sub-3 score, write one line per risk:

> "Reliability 3: provider has 3 incidents in the last 6 months; status
> page at status.example.com; plan: cache last good response for 30s
> and degrade gracefully."

Never hide risks behind a high average.
