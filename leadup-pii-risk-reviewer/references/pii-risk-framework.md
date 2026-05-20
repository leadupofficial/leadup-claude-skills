# PII risk framework — LeadUp

Practical PII review tuned for India SMB SaaS and global products.
Honest about what's covered vs gap. No fake compliance claims.

## 1. Categories (use consistently)

| Category | Examples |
|---|---|
| Identifier | name, username, employee id |
| Contact | phone, email, address |
| Financial | card last4, UPI VPA, bank IFSC, invoice amount, GSTIN |
| Health | medical history, prescriptions, allergies |
| Government ID | Aadhaar, PAN, passport, voter id, driver licence |
| Biometric | fingerprint, face vector, voice print |
| Demographic | DOB, gender, marital status |
| Behavioral | bookings, purchase history, click logs |
| Child data | anyone < 18 |
| Location | precise GPS, IP-derived city |

A field can have multiple categories.

## 2. Risk scoring

| Risk | Trigger |
|---|---|
| Low | de-identifiable, low harm if leaked |
| Medium | could be misused (phone, email) |
| High | financial, health, government ID, child |
| Critical | biometric, raw card data, Aadhaar mass storage |

Default LeadUp rule: anything **High** or **Critical** gets column-
level encryption + audit on reveal.

## 3. Default masking patterns

| Field | Default mask |
|---|---|
| Name | first letter + last initial |
| Phone | `+91 XXXX-XX-XX99` |
| Email | `a***@b.com` |
| Address | last 2 chars only |
| Aadhaar | `XXXX-XXXX-NNNN` |
| PAN | `XXXXX_NNNN` |
| Card | last 4 only — never store full PAN |
| GSTIN | full visible (it's a business ID); still gated by role |
| Health notes | section gated; not in row list |
| DOB | year only in views |
| Location | city level by default |

Full reveal must be role-gated AND audited.

## 4. Encryption

- **In transit**: HTTPS / TLS 1.2+ everywhere.
- **At rest**:
  - Full-disk encryption from the host (Coolify / cloud provider).
  - Column-level encryption for High/Critical fields (Aadhaar,
    health notes, biometric, raw KYC).
- **Key management**: env var or vault; rotation cadence stated (e.g.
  every 12 months or on incident).
- **Backups**: encrypted; access audited.

## 5. Retention

Defaults LeadUp suggests (verify per industry / market):

| Category | Default window | Why |
|---|---|---|
| Marketing leads | 24 months from last contact | sales cycle |
| Customer + booking | active + 7 years | India tax / GST |
| Payments / invoices | 7 years | tax/audit |
| Health notes | as per local regulation | longer in many regions |
| Marketing logs (CRM events) | 24 months | active use |
| Webhook + automation logs | 90 days (redacted) | debugging |
| AI request logs (redacted) | 30 days | quality + cost |
| Children's data | minimum needed; delete on request | strict |

A scheduled deletion job (cron / n8n) removes data past the window.

## 6. Data Subject Requests (DSR)

For each user request (export, correction, delete):

- Identify user (auth proof).
- Scope: which datasets touched.
- Export format: JSON / CSV; encrypted ZIP delivered to verified email.
- Delete: hard delete from primary store; mark in dedupe / log tables
  as "deleted user" but keep audit hashes.
- SLA: 30 days target for India / global, 1 month for EU GDPR.

Each DSR logged in audit table (who, when, what, by which staff).

## 7. Consent flow

Where consent is collected:

- Form / booking page checkbox with plain language.
- In-product consent page on first login.
- Re-consent on policy change.

Stored:
- Phone / email of consenter.
- Timestamp.
- Verbatim consent text shown.
- Policy version id.
- Source URL / event.

Withdrawal:
- Easy: STOP keyword on WhatsApp, unsubscribe link in email, toggle
  in app settings.
- Honored within 24h max.

## 8. Sub-processor list

Track each external service that touches PII:

| Sub-processor | Purpose | PII categories | DPA status | Region |
|---|---|---|---|---|
| Razorpay | payments | financial, contact | signed | India |
| Gupshup / AiSensy / Wati | WhatsApp | contact, behavioral | check | India |
| Anthropic | AI | depends (redact!) | signed | global |
| OpenAI | AI | depends (redact!) | check | global |
| Postmark / Resend / SES | email | contact | check | global |
| Sentry | error logs | sometimes contact | scrub before send | global |
| GA4 / PostHog | analytics | behavioral, IP | check | global |
| S3 / R2 / Bunny | files | varies | check | varies |

If a sub-processor lacks a DPA / training-opt-out (for AI), flag and
pause until resolved.

## 9. India DPDP + IT Rules (active scope when in force)

- Lawful basis: consent / contract / legal obligation / public
  interest. Most LeadUp use cases = consent / contract.
- Notice + purpose limitation: only collect what you need.
- Withdrawal of consent easy.
- Sensitive personal data (health, finance, biometric) — explicit
  consent.
- Data fiduciary obligations: grievance officer, transparent retention,
  cross-border transfer notes.

## 10. GDPR (for EU users)

- Lawful basis named (consent / contract / legitimate interest).
- DSR within 1 month.
- Records of processing.
- Cookie consent with reject = easy.
- Cross-border transfer mechanism (SCCs / adequacy).
- Breach notification: 72h to authority.

## 11. Privacy policy notes (for `leadup-human-content-editor`)

A short list the team can hand off:

- Who we are + contact.
- What we collect + why (per category).
- Sub-processors named (link to list).
- Retention windows (plain language).
- User rights (DSR + how to ask).
- Consent withdrawal.
- Updates / version log.

## 12. Developer checklist

Concrete code-level items:

- [ ] All PII columns documented in the schema with category.
- [ ] Column-level encryption for High / Critical fields.
- [ ] No PII in URLs or query params.
- [ ] No PII in error logs (Sentry scrubbing on).
- [ ] No PII in third-party analytics events.
- [ ] Masking applied in default admin views.
- [ ] Reveal endpoints audited (event written).
- [ ] DSR endpoints (`export`, `delete`) implemented and tested.
- [ ] Consent records stored with policy version id.
- [ ] AI calls redact PII before send (or use a no-train provider with
      DPA, and minimal data).
- [ ] Cron job: retention deletion runs and reports.
- [ ] Backups encrypted; access audited.

## 13. Honesty rules

- Name what's covered vs what's gap.
- No invented compliance claims.
- No real secrets / PII in the output.
- Sub-processor DPA status named per row.
- Encryption layer named (not "we encrypt everything").
- Final consent / privacy copy through
  `leadup-human-content-editor`.
- Uncertain compliance items routed to a privacy professional.
