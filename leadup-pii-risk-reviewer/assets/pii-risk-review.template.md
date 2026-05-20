# PII risk review — [Project]

> Date: [YYYY-MM-DD]  ·  Markets served: [India / EU / US / other]
> Tenant model: [single / multi-tenant by row / by schema]
> Regulated category: [yes (clinic / finance / kids) / no]
> Reviewer: [name]

## 1. Brief restate

[One line: project, scope, markets, regulated status.]

## 2. PII inventory

| Field | Category | Where (table.column / form) | Scope | Sensitivity |
|---|---|---|---|---|
| name | Identifier, Contact | `customers.name` | per org | Medium |
| phone | Contact | `customers.phone` | per org | High |
| email | Contact | `customers.email` | per org | Medium |
| address | Contact, Location | `customers.address` | per org | Medium |
| GSTIN | Financial / Identifier (business) | `orgs.gstin` | per org | Low–Medium |
| card_last4 | Financial | `payments.card_last4` | per org | Medium |
| amount | Financial | `payments.amount` | per org | Low |
| medical_notes | Health | `bookings.notes` (if applicable) | per org | High–Critical |
| dob | Demographic | `customers.dob` | per org | Medium |
| booking_history | Behavioral | `bookings.*` | per org | Low–Medium |

Add rows for every PII field actually present.

## 3. Data flow

For each High/Critical field:

```
phone:
  Entry → booking form on website + admin
  Storage → customers.phone (Postgres, encrypted at rest)
  Access → owner, admin, accountant (masked); staff (masked only)
  Logs → hashed in app logs; never raw
  Sub-processors → BSP (sends template), Razorpay (cardholder verification)
  Webhook → BSP delivery reports (phone present)
```

(Repeat for email, address, financial fields, medical, etc.)

## 4. Risk scores

| Field | Risk | Reason |
|---|---|---|
| phone | High | wide misuse; passes to BSP |
| email | Medium | account recovery |
| medical_notes | Critical | health; column-encrypt + audit |
| card_last4 | Medium | acceptable when tokenized via Razorpay |
| Aadhaar (if any) | Critical | mass storage off the table |
| dob | Medium | combined identifier |

## 5. Masking rules

| Field | Default mask | Reveal role | Audit |
|---|---|---|---|
| name | first letter + last initial | Owner/Admin (audited) | yes |
| phone | `+91 XXXX-XX-XX99` | Owner/Admin | yes |
| email | `a***@b.com` | Owner/Admin | yes |
| address | last 2 chars | Owner/Admin | yes |
| card_last4 | shown as last4 only | n/a (never full) | n/a |
| medical_notes | section gated | Doctor role | yes |
| Aadhaar | `XXXX-XXXX-NNNN` | Super only | yes |

Aligns with admin design from `leadup-admin-panel-planner`.

## 6. Encryption

- In transit: HTTPS / TLS 1.2+ everywhere (LE / Coolify managed).
- At rest:
  - Full-disk via cloud / Coolify host.
  - Column-level for `medical_notes`, raw KYC (if any).
- Key management: stored in Coolify env / vault; rotation every 12
  months or on incident.
- Backups: encrypted; access audited.

## 7. Retention

| Category | Window | Reason | Deletion job |
|---|---|---|---|
| Marketing leads | 24 months from last contact | sales cycle | nightly cron |
| Customer + bookings | active + 7 years | India tax | yearly archive |
| Payments / invoices | 7 years | tax / audit | yearly archive |
| Medical notes | per local rule | regulation | manual + audited |
| Webhook + automation logs | 90 days, redacted | debug | nightly cron |
| AI request logs | 30 days, redacted | quality | nightly cron |
| Children's data | minimum needed | strict | on request |

## 8. Export / delete (DSR)

- Verify user identity (auth + email confirmation).
- Export: JSON + CSV in encrypted ZIP to verified email.
- Delete: hard delete from primary store; keep audit hashes only.
- SLA: 30 days (India), 1 month (EU GDPR).
- Each DSR logged with actor, target, action, ts.

## 9. Consent flow

- Where: booking form + first-login consent page.
- Verbatim text:
  > "[Plain consent line, e.g. 'I agree to receive WhatsApp updates
  > about my booking and reminders, and to LeadUp using my contact
  > details to provide service. I can withdraw consent any time by
  > replying STOP or visiting Settings.']"
- Stored: `customers.consent` (text), `consent_ts`,
  `policy_version_id`, `source_url`.
- Withdrawal: STOP keyword, unsubscribe link, in-app toggle. Honored
  in 24h.

## 10. Privacy policy notes (for `leadup-human-content-editor`)

- Who we are + contact details.
- What we collect + why (per category).
- Sub-processors list (link).
- Retention windows (plain language).
- DSR (how to request export / delete / correction).
- Consent withdrawal path.
- Updates / version log.

## 11. Developer checklist

- [ ] All PII columns documented with category.
- [ ] Column-level encryption for High/Critical.
- [ ] No PII in URLs / query strings.
- [ ] Sentry scrubbing on; no PII in error logs.
- [ ] Admin views masked by default; reveal audited.
- [ ] DSR endpoints implemented + tested.
- [ ] Consent records stored with policy version id.
- [ ] AI calls redact PII or use a no-train provider with DPA.
- [ ] Retention cron runs and writes a report.
- [ ] Backups encrypted; access audited.
- [ ] Tenant isolation tested (Org A cannot see Org B PII).

## 12. Hand-offs

- Security-sensitive scopes → `leadup-security-review`.
- Admin panel implementation → `leadup-admin-panel-planner`.
- Sub-processor API depth → `leadup-api-research-builder`.
- Privacy / consent copy polish → `leadup-human-content-editor`.
- AI feature data flow → `leadup-ai-feature-planner`.
- Status update in project memory → `leadup-status-updater`.
