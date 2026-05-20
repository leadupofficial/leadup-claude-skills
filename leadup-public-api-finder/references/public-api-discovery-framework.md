# Public API discovery framework — LeadUp

How LeadUp finds candidate APIs without inventing facts and without
trusting any single index as truth.

## 1. Start from the requirement, not the catalogue

Write the requirement in one line first:

> "Server-side email validation for our LeadUp client lead form, India
> + global audience, commercial use, 1k checks/day, free preferred."

The single line tells you the **category** (validation), **runtime**
(server-side), **scale** (1k/day), and **constraints** (free,
commercial, India + global).

Without it, every catalogue looks useful.

## 2. Map to a category

Pick one primary category:

| Category | Examples |
|---|---|
| Validation | email, phone, address, VAT, GSTIN, BIN, IBAN |
| Payments | Razorpay, Stripe, Cashfree, PayPal |
| Messaging | WhatsApp BSPs, SMS, transactional email, push |
| Maps / Geo | Google Maps, Mapbox, OpenStreetMap, IP geo |
| Weather | OpenWeather, weatherapi.com, Open-Meteo |
| Docs / Files | PDF, OCR, conversion, signing |
| Security | URL reputation, malware, breach-check, MX/DMARC |
| AI / LLM | Anthropic, OpenAI, Google, OSS — see `leadup-ai-feature-planner` |
| Data / Reference | currency, country, postal, holiday, ISO codes |
| Search / NLP | search, summarization, embeddings |
| Travel | flight, airline, airport, hotel, fare |
| Identity / KYC | document OCR, Aadhaar (regulated), PAN |
| Local / business | Google Places, Justdial-style local |

Cross-category needs (e.g. "WhatsApp template send + delivery
reports") get **two** categories and may need two APIs.

## 3. Discovery passes (in this order)

1. **public-apis/public-apis** repo on GitHub. Skim the relevant
   category section; capture 3–8 raw candidates.
2. **Open Google search** for "best <category> API 2026 India" /
   "<requirement> open source alternative" / "official docs <name>".
3. **RapidAPI** marketplace search. Note request volume, latency,
   review counts.
4. **ApyHub** for utility APIs not listed on `public-apis`.
5. **GitHub** for SDKs / clients with stars/last-commit.
6. **Postman public collections** for quick request examples.

If a browser / search MCP is unavailable, document each candidate
URL the user should open to verify.

## 4. Capture per candidate (cheap pass)

For each raw candidate, capture:

- Name + domain.
- One-line description of the feature.
- Auth method (rough).
- Source of the listing (which index / page).
- Date you discovered it.

This is **not yet** verification. It is shortlisting.

## 5. Cull obviously bad fits

Drop candidates where any of these is true at first glance:

- Clearly wrong category.
- Dead site / 404 / domain parked.
- No HTTPS on the homepage.
- "Free for personal use" only and user needs commercial.
- Pay-only when user is strictly free.
- Last visible commit / release > 36 months.

## 6. Shortlist 3–5 for verification

Final shortlist length:

- 3 candidates if the category is well-served.
- 5 candidates if the category is contested or unclear.

Never 1 (no backup) and never 8+ (no signal).

## 7. India / global heuristics

- Prefer providers with **India region** when latency matters
  (payments, WhatsApp BSP, local search).
- Prefer providers that publish **INR billing + GST invoice** for
  client work.
- For EU users: prefer providers with EU residency.
- For US-only audiences: weight US uptime + payment in USD.

## 8. Direct-from-browser vs server-side

Always ask: where will this run?

| Where | Risk |
|---|---|
| Browser-only with a public key | CORS must be open; key visible in DOM/network |
| Browser with a secret key | NEVER — needs backend proxy |
| Server-side only | safest; verify rate-limit on shared infra |
| Both | usually means a tokenised public client + protected server |

Pin this decision before scoring.

## 9. AI APIs are a special case

Route AI / LLM searches through `leadup-ai-feature-planner` for the
cost ledger, fallback model, and privacy / redaction plan. This skill
still produces the candidate table; AI feature design does not happen
here.

## 10. Handoff to verification

Pass the shortlist + the runtime decision + the constraint set to the
verification step (`references/api-verification-checklist.md`). Do
**not** stop at "found 5 free APIs" — verification decides which one
ships.
