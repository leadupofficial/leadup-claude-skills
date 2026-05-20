# API comparison — [Feature]

> Date: [YYYY-MM-DD]  ·  Project: [Hostendor / LeadUp site / Jewellery SaaS / Salon SaaS / INET CRM / Trivasia / Security suite]
> Runtime: [browser-only / server-only / both]
> Market: [India / global / both]  ·  Commercial use: [yes — LeadUp client work]

## 1. Requirement summary

> [One line: what the API must do, where it runs, expected volume.]

## 2. API category

[validation / payments / messaging / maps / weather / docs / security
/ AI / data / search / files / travel / identity / local / other]

## 3. Candidate APIs

| # | API | Auth | HTTPS | CORS | Free tier band | Paid pricing band | Region | Maintained? | Score (avg) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [name + provider] | [api key / oauth2 / none] | yes / no | yes / partial / no | [calls/day or /month] | [band] | IN / global | yes / requires verification | [4.50] |
| 2 | […] | […] | […] | […] | […] | […] | […] | […] | [n] |
| 3 | […] | […] | […] | […] | […] | […] | […] | […] | [n] |
| 4 | […] | […] | […] | […] | […] | […] | […] | […] | [n] |
| 5 | […] | […] | […] | […] | […] | […] | […] | […] | [n] |

### Per-candidate 8-axis score

| API | Fit | Docs | Price | Rel | Auth | CORS | Int | Comm | Avg | Sub-3 flags |
|---|---|---|---|---|---|---|---|---|---|---|
| Candidate A | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 4.75 | — |
| Candidate B | 4 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 4.25 | Reliability 3 |
| Candidate C | 5 | 3 | 5 | 4 | 4 | 2 | 3 | 3 | 3.6 | CORS 2; Integration 3 |

(Drop / replace candidates that have sub-3 on Auth, Reliability, or
Commercial use safety for production.)

## 4. Best API recommendation

> **[Candidate A]** — [one-line reason]

## 5. Backup API recommendation

> **[Candidate B]** — [one-line reason, including how it differs]

## 6. Why selected

- [Axis-weighted reason 1]
- [Axis-weighted reason 2]
- [Axis-weighted reason 3]
- [Axis-weighted reason 4]
- [Axis-weighted reason 5]

## 7. Official docs / resource links

- Official docs: [URL] (accessed YYYY-MM-DD)
- Pricing page: [URL] (accessed YYYY-MM-DD)
- Status page: [URL or "none — flagged"]
- SDK / GitHub: [URL or "REST only"]
- Discovery source: `public-apis/public-apis` (accessed YYYY-MM-DD)
- Postman collection: [URL or "n/a"]

## 8. Hand-offs

- Implementation depth → `leadup-api-research-builder`.
- Workflow wiring → `leadup-n8n-workflow-builder`.
- PII / payment scope → `leadup-pii-risk-reviewer`,
  `leadup-security-review`.
- WhatsApp specifics → `leadup-whatsapp-automation-planner`.
- AI specifics → `leadup-ai-feature-planner`.
- Public-facing copy mentioning the API → `leadup-human-content-editor`.
