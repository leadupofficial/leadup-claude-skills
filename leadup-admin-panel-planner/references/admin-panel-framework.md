# Admin panel framework — LeadUp

How LeadUp designs admin panels that owners actually use and staff don't
hate.

## 1. Navigation rules

- 5–9 top-level items max per role.
- Group by role; show only what the user can access.
- Use plain nouns ("Bookings", "Customers", "Payments"), not jargon
  ("Records", "Modules").
- Mobile collapses to a drawer; primary actions stay reachable with one
  thumb.

Default for a service-SaaS owner:

```
Dashboard / Bookings / Customers / Staff / Payments / Reports / Settings
```

Staff sees a trimmed version (Bookings / Customers / Payments).

## 2. Per-module spec

For every module:

| Item | Default rule |
|---|---|
| Columns visible | ≤ 7; overflow into a row drawer |
| Filters | 3–5 most useful (date, status, owner, search) |
| Sort default | most recent first |
| Bulk actions | export, status change, delete (with confirm) |
| Row actions | view, edit, status change, delete |
| Search | scoped to the module, fuzzy where possible |
| Empty state | clear next action |
| Loading | skeleton, not spinner-on-blank |

Every column / filter / action must name the role(s) it's for.

## 3. Roles + permissions matrix

Default LeadUp matrix for multi-tenant SaaS:

| Action | Super admin | Org owner | Org admin | Staff | Accountant |
|---|---|---|---|---|---|
| Cross-org view | ✅ | ❌ | ❌ | ❌ | ❌ |
| Manage org settings | ✅ | ✅ | partial | ❌ | ❌ |
| Manage staff | ✅ | ✅ | ✅ | ❌ | ❌ |
| Bookings CRUD | ✅ | ✅ | ✅ | ✅ (own + assigned) | read |
| Customer PII reveal | ✅ (audited) | ✅ (audited) | ✅ (audited) | masked | masked |
| Payments CRUD | ✅ | ✅ | ✅ | restricted | read + export |
| Invoices export | ✅ | ✅ | ✅ | ❌ | ✅ |
| Audit log read | ✅ | ✅ | ✅ | ❌ | ❌ |
| Impersonate org user | ✅ (audited) | ❌ | ❌ | ❌ | ❌ |

Tighten further for regulated categories.

## 4. Dashboard KPI cards

4–6 cards per role. Each card has:

- Title (plain noun + verb).
- Number with band/comparison.
- Data source (table + query).
- Refresh cadence (live / 5m / hourly / daily).
- Drill-down link to the right module.

Default cards for a service-SaaS owner:

| Card | Value | Source |
|---|---|---|
| Today's bookings | count | bookings WHERE date = today |
| This week revenue (paid) | ₹ sum | payments WHERE week = current |
| No-show rate (7d) | % | bookings WHERE status = no_show / total |
| Top service (30d) | name | bookings GROUP BY service |
| Active customers (30d) | count | customers WHERE last_booking ≥ 30d |
| Pending invoices | count | invoices WHERE status = pending |

## 5. Reports

3–6 reports max. Each has:

- Title
- Date range (default + custom)
- Filters (status, service, staff, location)
- Export formats (CSV, PDF, Excel)
- Compliance bit (GST invoice for India)

Common reports for India SMB:

- Daily summary.
- Weekly revenue.
- GST-ready monthly statement.
- Customer list export.
- Service performance.

## 6. Empty / loading / error states

- **Empty**: one sentence + one primary action.
  > "No customers yet. Add your first customer to start sending
  > reminders." [+ Add customer]
- **Loading**: skeleton rows matching the table shape.
- **Error**: plain language + what to do next.
  > "We could not load this list. Check your internet and try again.
  > If this keeps happening, contact support."
- **No-permission**: clear text + who to ask.
  > "You don't have access to this section. Ask your org admin to
  > grant the 'Reports' permission."

Banned: "Oops!", "Something went wrong" with no next action.

## 7. Audit log (minimum events)

- Login / logout.
- Role change.
- PII reveal (which field, by whom, for which record).
- Payment / refund actions.
- Export of any list.
- Impersonate session start/end.
- Settings change.
- Destructive actions (delete).
- API key creation / rotation.

Each event records: `actor`, `org_id`, `action`, `target_type`,
`target_id`, `before/after diff` (for sensitive), `timestamp`, `ip`.

## 8. PII handling defaults

- Mask phone (`+91 XXXX-XX-XX99`), email (`a***@b.com`), Aadhaar
  (`XXXX-XXXX-1234`) by default.
- Full reveal requires a role + audit log event.
- No raw PII in URLs or logs.
- Exports of PII gated by permission + audit + (optional) password
  protection.

Route to `leadup-pii-risk-reviewer` for the per-product PII inventory.

## 9. India + global considerations

- India: GST invoice format, HSN/SAC, GSTIN field on `orgs`, GSTR
  export.
- India: language toggle (English + regional) where customers see UI.
- Global: timezone per org user, currency per org, GDPR support
  requests (export / delete / consent log).

## 10. Stack-specific tips

- **Next.js + Tailwind + shadcn**: standard LeadUp stack; use Server
  Components for tables + drawers for row detail.
- **Flutter (mobile admin)**: cards over tables; pull-to-refresh; small
  number of primary actions per screen.
- **Plain HTML / Django / Rails admin**: lean on the framework's
  built-in admin; customise tables and filters.

## 11. Honesty rules

- Cite data source per KPI / report.
- No raw PII in default views.
- Audit every sensitive action.
- Empty / error states never blame the user.
- Defer visual polish to `leadup-premium-ui-upgrader`.
- Defer public copy polish to `leadup-human-content-editor`.
- Route PII / sensitive scopes to `leadup-pii-risk-reviewer`.
