# Feature roadmap — [Product]

> Date: [YYYY-MM-DD]  ·  Product stage: [live / beta / prototype / idea]
> Audience: [one line]  ·  Monetization: [tier model]
> Team: [size]  ·  Budget / runway: [one line]

## 1. Brief

- **Core product job:** "Help [audience] do [job] in [time], so [outcome]."
- **Top 3 user complaints / requests:** [list]
- **Competitors studied:** [3–5 names + one-line gap each]
- **Constraints:** [team, time, regulated category, infra]

## 2. User roles

| Role | Core jobs |
|---|---|
| Owner | […] |
| Admin | […] |
| Staff | […] |
| Customer | […] |
| Accountant (optional) | […] |
| Partner (optional) | […] |

## 3. Feature buckets

### Must-have (table-stakes)

| Feature | Role | Job solved | Monetization | Complexity | Differentiation |
|---|---|---|---|---|---|
| [e.g. Calendar view of bookings] | Owner / Admin | see today's schedule | n/a (must) | M | low |
| […] | […] | […] | […] | […] | […] |

### Premium (monetizable)

| Feature | Role | Job solved | Monetization | Complexity | Differentiation |
|---|---|---|---|---|---|
| Multi-branch | Owner | manage 2+ outlets | high | L | med |
| Role-based access | Admin | restrict staff | med | M | low |
| White-label / branding | Owner | sell as their brand | high | M | med |
| Integrations (CRM, accounting) | Admin | sync data | med | M | med |
| Advanced reports | Owner | spot trends | med | M | med |

### AI-powered

| Feature | Role | Real user job | Monetization | Complexity | Infra cost |
|---|---|---|---|---|---|
| No-show prediction | Owner | flag risky bookings | med | M | low (small model) |
| WhatsApp reply assist | Staff | draft customer replies | med | M | med (LLM tokens) |
| 30-day summary | Owner | spot pattern in 10s | low | S | low |
| Pricing recommendation | Owner | off-peak discounts | high | L | med |

(Add only AI features whose monthly infra cost < tier price.)

## 4. Phased roadmap

### MVP (weeks 0–6)
- [must-have #1]
- [must-have #2]
- [must-have #3]
- [must-have #4]
- [must-have #5]

Definition of done: [one line]
Target ship date: [YYYY-MM-DD]

### Phase 2 (weeks 6–12)
- [premium #1]
- [premium #2]
- [first AI feature]

### Phase 3 (weeks 12+)
- [enterprise / advanced features]

### Later or never
- [list]

## 5. Recommended next feature

> **Next: [feature name]**
>
> **Why now:** [reasoning]
> **For whom:** [role + job]
> **Definition of done:** [one line]
> **Effort band:** [S/M/L]  ·  **Infra cost note:** [low/med/high]
> **Success looks like:** [metric + target band]
> **Deferred to make room:** [list]

## 6. Risks and dependencies

| Risk | Type | Notes |
|---|---|---|
| […] | technical | […] |
| […] | regulatory (KYC / PII / GST) | […] |
| […] | vendor lock-in (LLM / BSP) | […] |
| […] | operational (support load) | […] |

## 7. Hand-offs

- Implementation start (greenfield) → `leadup-project-kickoff`.
- Continue existing project → `leadup-existing-repo-analyzer`.
- New API / integration → `leadup-api-research-builder`.
- UI / premium upgrade → `leadup-premium-ui-upgrader`.
- Public copy → `leadup-human-content-editor`.
- Marketing this feature → `leadup-blog-content-writer` /
  `leadup-smm-growth-planner` / `leadup-digital-ads-planner`.

## 8. Assumptions and data confidence

- **Verified** (named source): [list]
- **Estimated**: [list]
- **Requires verification** (need user data / decisions): [list]
