# Feature planning framework — LeadUp

How LeadUp decides what to build next on a SaaS or client product.
Bias to shipping. Honest about cost.

## 1. The one-sentence product job

Lock the product's **core job** before anything else:

> "Help [audience] do [job] in [time/condition], so [outcome]."

Every proposed feature must reference this job. If it doesn't, it goes
to "later or never".

## 2. User roles

List every role + their core jobs. Default template for a service-SaaS:

| Role | Core jobs |
|---|---|
| Owner | see revenue, manage staff, set offers, view reports |
| Admin / manager | manage daily bookings, handle exceptions, billing |
| Staff | check schedule, mark service done, take payments |
| Customer | book, pay, reschedule, get reminders |
| Accountant | export invoices, view GST, reconcile payouts |
| Partner (optional) | share leads, view commissions |

A feature can serve multiple roles, but should name **the primary role**.

## 3. Three feature buckets

### Must-have (table-stakes)

What every competitor in this category has. Without these the product
looks broken. Examples for booking SaaS:

- Calendar view of bookings.
- Customer record.
- Reminder (email / SMS / WhatsApp).
- Pay-online or pay-in-store.
- Cancellation / refund flow.
- Daily / monthly revenue summary.

### Premium (monetizable)

Features that justify a paid tier or higher tier. Examples:

- Multi-location / multi-branch.
- Role-based access.
- Custom branding / white-label.
- Integrations (CRM, accounting, marketing).
- Advanced reports / cohort analysis.
- Marketing automation (campaigns, segments).
- SLA / priority support.

### AI-powered (each must name the user job)

AI features that actually help. Examples for booking SaaS:

| Feature | User job |
|---|---|
| Smart no-show prediction | flag risky bookings the day before |
| Auto-summary of last 30 bookings | help owner spot pattern in 10s |
| WhatsApp reply assist | draft replies to customer queries |
| Pricing recommendation | suggest off-peak discounts |
| AI image upscaler | improve before/after gallery quality |
| Voice-to-booking | take phone bookings via voice |

Each entry must have a real user job. Skip generic "AI dashboard"
ideas with no job named.

## 4. Scoring (4 axes)

For each feature in any bucket:

| Axis | Values | How to read |
|---|---|---|
| Monetization impact | low / med / high | does it unlock a tier, retain a churner, or lift ARPU? |
| Complexity | S / M / L / XL | engineering + design + infra cost |
| Differentiation | low / med / high | how rare is this in the category? |
| User pain solved | named role + named job | concrete, not "improves UX" |

For AI features, also note **infra cost** (LLM token cost, vector DB,
storage) — that often bumps complexity up.

## 5. Phasing

| Phase | Definition |
|---|---|
| MVP | must-haves only. ≤ 8 features. ships in weeks. |
| Phase 2 | premium upgrades to justify a paid tier; first AI feature. |
| Phase 3 | enterprise / advanced (SSO, audit log, SCIM, advanced AI). |
| Later or never | nice ideas that don't fit the audience or tier. |

Default tier mapping for a 2-tier SaaS:

- **Free / Basic** = MVP must-haves.
- **Pro** = Phase 2 premiums + first AI feature.
- **Enterprise (optional)** = Phase 3.

## 6. Recommended next feature (always one)

After the table, recommend ONE next feature with:

- Why this, not the others.
- Definition of done.
- Estimated effort band (S/M/L) and infra cost note.
- What success looks like (named metric + target band).
- What gets deferred to make room.

The team should be able to start tomorrow.

## 7. Risks and dependencies

For each recommended feature, list:

- **Technical risks** (third-party dependency, infra cost, scale).
- **Regulatory risks** (KYC, PII, medical, payments, IT Rules, DPDP).
- **Vendor lock-in** (e.g. OpenAI vs Anthropic for AI features).
- **Operational risks** (support load, refund handling, ops).

If any risk is blocking, pick a different next feature.

## 8. India + global considerations

- India payments: Razorpay / Cashfree / Stripe-India; KYC; UPI as a
  first-class option, not an after-thought.
- India compliance: GST invoicing, GSTIN capture, IT Rules, DPDP scope
  (when finalised), ASCI for marketing.
- WhatsApp: BSP (Gupshup, AiSensy, etc.) and template approvals add
  time and cost; factor into complexity.
- Global SaaS: SSO, multi-currency, multi-language, GDPR, SOC 2 path.

## 9. AI features — the honest cost ledger

Before committing to an AI feature, write down:

- LLM model + estimated tokens per call.
- Cost per call × estimated calls per user per month.
- Storage / vector DB cost.
- Latency budget (acceptable to user).
- Failure mode (what does the user see if the model is wrong / down?).

Drop AI features whose monthly cost > the user's price point unless they
clearly drive retention or upgrades.

## 10. Output rules

- One ranked recommendation, not a list of options.
- Bucketed tables (must-have / premium / AI) with the 4 scoring axes.
- Phased roadmap (MVP / Phase 2 / Phase 3 / Later).
- Risks + dependencies named per recommended feature.
- Assumptions block with verified / estimated / requires verification.
- Hand-offs to `leadup-project-kickoff` / `leadup-existing-repo-
  analyzer` / `leadup-api-research-builder` / `leadup-premium-ui-
  upgrader` / `leadup-human-content-editor` are explicit.
