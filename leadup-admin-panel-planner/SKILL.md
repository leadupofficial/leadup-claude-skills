---
name: leadup-admin-panel-planner
description: Plan an admin panel for a LeadUp SaaS, client website, or CRM — super admin, org admin, tenant admin, and staff views. Outputs navigation, modules, tables, filters, actions, roles and permissions, reports, dashboard KPI cards, and empty/loading/error states. Tuned for multi-tenant SaaS and India SMB tools. Use when the user says "admin panel", "dashboard plan", "super admin", "tenant admin", "CRM dashboard", or "admin modules".
---

# LeadUp Admin Panel Planner

## Purpose

Design the admin layer of a LeadUp product: who sees what, which
modules exist, what each module's table looks like (columns, filters,
sort, bulk actions), what KPI cards live on the dashboard, what roles
and permissions apply, and what the empty/loading/error states say.

## When to use

Use when the user wants the admin / dashboard layer of a product
designed. Do **not** trigger for the full SaaS MVP (use
`leadup-saas-mvp-planner`), pure UI polish (use
`leadup-premium-ui-upgrader`), or feature roadmap (use
`leadup-feature-option-planner`).

Trigger phrases: "admin panel", "dashboard plan", "super admin",
"tenant admin", "CRM dashboard", "admin modules", "back-office plan".

## Inputs needed

- Product context (what the user-facing app does).
- Tenant model (single / multi-tenant by row / by schema).
- User roles (owner, admin, staff, billing, support).
- Core entities (bookings, customers, payments, users, etc.).
- KPIs the owner needs to see at a glance.
- Stack hint (Next.js + Tailwind, Flutter, plain HTML, custom).
- Regulated data flags (PII, financial, medical).

Ask at most 2 clarifying questions if roles or tenant model are unclear.

## Tools/resources to use

- `references/admin-panel-framework.md` — navigation, table, role rules.
- `assets/admin-panel-plan.template.md` — output shape.
- `leadup-saas-mvp-planner` if MVP scope is still open.
- `leadup-premium-ui-upgrader` for visual polish.
- `leadup-pii-risk-reviewer` if PII is in scope.
- `leadup-feature-option-planner` for the broader feature ladder.

## Step-by-step workflow

1. **Restate** product + tenant model + roles in one block.
2. **Top-level navigation**: 5–9 items max; group by role.
3. **Per-module spec**:
   - Table columns (≤ 7 visible, with overflow).
   - Filters (3–5 most useful).
   - Sort defaults.
   - Bulk actions (with confirmation).
   - Row actions (view, edit, delete, …).
4. **Roles + permissions matrix**: who can see / create / edit / delete
   / export / impersonate.
5. **Dashboard KPI cards**: 4–6 cards per role; each card cites the
   data source.
6. **Reports**: 3–6 reports with date range, filters, export (CSV /
   PDF / GST invoice).
7. **States**: empty, loading, error, no-permission, low-data
   placeholders.
8. **Audit log**: minimum events to log (who did what, when).
9. **Hand-offs** explicitly.

## Required output format

One Markdown plan with these sections, in this order:

1. **Brief restate** — product, tenant model, roles.
2. **Top-level navigation** — list per role.
3. **Modules** — for each module: purpose · table columns · filters ·
   sort · bulk actions · row actions.
4. **Roles + permissions matrix** — table: role × action × allow/deny.
5. **Dashboard KPI cards** — per role, 4–6 cards each, with data
   source and refresh cadence.
6. **Reports** — 3–6 reports with filters, ranges, export formats.
7. **Empty / loading / error states** — sample copy for each.
8. **Audit log events** — minimum list.
9. **PII + sensitive flags** — fields, masking, access.
10. **Hand-offs** — to other LeadUp skills.

## Safety rules

- Do **not** show raw payment cards / bank details / Aadhaar / PAN; mask
  by default; full reveal only with role + audit.
- Do **not** allow staff to export data without explicit permission.
- Do **not** invent KPI sources. Each KPI must name its underlying
  table / query.
- For India: invoices honor GST format, HSN/SAC, registered name.
- For multi-tenant: every query scoped by `org_id`; RLS or app-level
  checks documented.
- For audit log: include who, what, when, target id, before/after on
  sensitive changes.
- For empty / error states: clear next action, never "Oops something
  went wrong".
- Route PII handling to `leadup-pii-risk-reviewer` before publishing.
- Defer public copy polish to `leadup-human-content-editor`.

## Common mistakes

- 30 nav items — staff can't find anything.
- Tables with 15 columns — unusable on a laptop.
- One mega-dashboard for all roles — owner doesn't need staff signals
  and vice versa.
- No bulk actions where they obviously help.
- Confirmations missing on destructive actions.
- No audit log — compliance and debugging both suffer.
- Raw PII visible to all roles by default.
- Empty state that says "no data" with no next step.

## Troubleshooting

- **Many roles**: collapse to 4–6 effective roles; create permission
  toggles for edge cases.
- **Single tenant tool**: drop org_id scoping, keep audit log.
- **Heavy export / GST needs (India)**: bake in invoice / GSTR export
  early; do not retrofit.
- **Regulated category**: tighten masking + audit; route to
  `leadup-pii-risk-reviewer`.
- **Limited dev time**: ship "v1 admin" = nav + 3 modules + 1 KPI
  dashboard + reports phase 2.
- **Mobile-only admin**: drop tables to card-style, focus on top 3
  actions per screen.

## Test prompts

### Should trigger (5)
1. "Plan the admin panel for our salon booking SaaS."
2. "Design super admin + tenant admin for a clinic SaaS."
3. "CRM dashboard plan for a tutoring centre."
4. "Admin modules for a hostel-management product."
5. "Back-office plan with KPI cards for a B2B booking tool."

### Should NOT trigger (3)
1. "Plan the SaaS MVP." (→ `leadup-saas-mvp-planner`)
2. "Make the admin look premium." (→ `leadup-premium-ui-upgrader`)
3. "Polish admin copy." (→ `leadup-human-content-editor`)

### Functional test cases (2)
1. Given "multi-tenant salon booking SaaS, roles = super admin, org
   owner, org admin, staff, accountant", return a plan with role-
   specific navigation, 5–6 modules each with columns/filters/actions,
   a permissions matrix, 4–6 KPI cards per role with data sources,
   GST-ready invoice export, masked phone/email by default, and audit
   log events.
2. Given a regulated category (clinic admin storing patient notes),
   return a plan with stricter masking, role-gated full-reveal, an
   audit log covering every PII access, and a hand-off to
   `leadup-pii-risk-reviewer`.

## Success criteria

- All 10 sections present in order.
- Navigation ≤ 9 items per role.
- Each module spec lists columns / filters / sort / bulk / row actions.
- Permissions matrix covers create/read/update/delete/export/impersonate
  for each role.
- KPI cards cite data source.
- Reports have date range + export format.
- PII masking + audit-log events explicit.
- Hand-offs to `leadup-pii-risk-reviewer`,
  `leadup-premium-ui-upgrader`, and `leadup-human-content-editor`
  called out.
