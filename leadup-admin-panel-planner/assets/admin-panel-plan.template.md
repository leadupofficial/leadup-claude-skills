# Admin panel plan — [Product]

> Date: [YYYY-MM-DD]
> Tenant model: [single / multi-tenant by row / by schema]
> Stack: [Next.js + Tailwind + shadcn / Flutter / other]

## 1. Brief restate

[Product purpose + tenant model + role list.]

## 2. Top-level navigation (per role)

### Super admin (LeadUp)
Dashboard / Organizations / Billing / Audit / Settings

### Org owner
Dashboard / [Bookings] / [Customers] / Staff / Payments / Reports / Settings

### Org admin
Dashboard / [Bookings] / [Customers] / Staff / Payments / Reports

### Staff
Today / [Bookings] / [Customers]

### Accountant
Reports / Invoices

## 3. Modules

### Module: Bookings

- Purpose: [staff manage day-to-day bookings]
- Columns visible (≤ 7): id, date+time, customer, service, staff, status, amount
- Filters: date range, status, staff, service, text search
- Sort default: date desc
- Bulk actions: change status, export, delete (confirm)
- Row actions: view, edit, mark done, refund, send reminder

### Module: Customers

- Columns visible: id, name (masked), phone (masked), email (masked), last booking, total spent, tags
- Filters: tag, last_booking range, text search
- Sort default: last_booking desc
- Bulk actions: export (audited), tag, message via WhatsApp template
- Row actions: view (full reveal audited), edit, archive

### Module: Payments

[…]

### Module: Staff

[…]

### Module: Reports

[…]

### Module: Settings

[…]

## 4. Roles + permissions matrix

| Action | Super | Owner | Admin | Staff | Accountant |
|---|---|---|---|---|---|
| Cross-org view | ✅ | ❌ | ❌ | ❌ | ❌ |
| Manage org settings | ✅ | ✅ | partial | ❌ | ❌ |
| Manage staff | ✅ | ✅ | ✅ | ❌ | ❌ |
| Bookings CRUD | ✅ | ✅ | ✅ | ✅ (own + assigned) | read |
| Customer PII reveal | ✅ (audited) | ✅ (audited) | ✅ (audited) | masked | masked |
| Payments CRUD | ✅ | ✅ | ✅ | restricted | read + export |
| Invoices export | ✅ | ✅ | ✅ | ❌ | ✅ |
| Audit log read | ✅ | ✅ | ✅ | ❌ | ❌ |
| Impersonate | ✅ (audited) | ❌ | ❌ | ❌ | ❌ |

## 5. Dashboard KPI cards

### Owner dashboard (4–6 cards)

| Card | Source query | Refresh |
|---|---|---|
| Today's bookings | `bookings WHERE date = today` | live |
| This week revenue | `payments WHERE week = current AND status = paid` | 5m |
| No-show rate (7d) | `bookings WHERE status = no_show / total` | hourly |
| Top service (30d) | `bookings GROUP BY service ORDER BY count DESC` | daily |
| Active customers (30d) | `customers WHERE last_booking ≥ 30d` | daily |
| Pending invoices | `invoices WHERE status = pending` | live |

### Staff dashboard

[…]

### Accountant dashboard

[…]

## 6. Reports

| Report | Date range | Filters | Export | Notes |
|---|---|---|---|---|
| Daily summary | today / range | staff, service | CSV / PDF | one-pager |
| Weekly revenue | week / range | service | CSV / PDF | for owner |
| GST monthly statement | month | n/a | CSV (GSTR-1) | India |
| Customer list | all / range | tag, source | CSV | audited |
| Service performance | range | service, staff | CSV | trend chart |

## 7. Empty / loading / error states

- Empty (Customers): "No customers yet. Add your first customer to start
  sending reminders." [+ Add customer]
- Loading (Bookings): skeleton rows.
- Error: "We could not load this list. Check your internet and try
  again. If this keeps happening, contact support."
- No-permission: "You don't have access to this section. Ask your org
  admin to grant the 'Reports' permission."

## 8. Audit log events (minimum)

- Login / logout
- Role change
- PII reveal (field, record id, by whom)
- Payment / refund
- Export of any list
- Impersonate session start/end
- Settings change
- Destructive actions (delete)
- API key creation / rotation

## 9. PII + sensitive flags

| Field | Default | Reveal | Audit |
|---|---|---|---|
| name | masked first letter | role-gated | yes |
| phone | `+91 XXXX-XX-XX99` | role-gated | yes |
| email | `a***@b.com` | role-gated | yes |
| address | last 2 chars only | role-gated | yes |
| Aadhaar / PAN | XXXX-XXXX-NNNN | super only | yes |
| payment card | last 4 only | never full | n/a |
| medical notes | section gated | role-gated | yes |

Route the full inventory to `leadup-pii-risk-reviewer`.

## 10. Hand-offs

- PII / sensitive scope review → `leadup-pii-risk-reviewer`.
- Visual / premium UI → `leadup-premium-ui-upgrader`.
- Public-facing copy polish → `leadup-human-content-editor`.
- New feature scope → `leadup-feature-option-planner`.
- AI feature in admin → `leadup-ai-feature-planner`.
- QA test cases → `leadup-qa-test-case-generator`.
