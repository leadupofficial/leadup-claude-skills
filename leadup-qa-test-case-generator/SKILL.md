---
name: leadup-qa-test-case-generator
description: Generate manual and automated test cases for a LeadUp website, SaaS, admin panel, API, mobile app, or deployment — including critical user flows, edge cases, Playwright test ideas, mobile/responsive checks, admin panel tests, payment/deploy tests, and clear acceptance criteria. Use when the user says "test cases", "QA plan", "manual testing", "Playwright tests", "test this app", or "create test cases".
---

# LeadUp QA Test Case Generator

## Purpose

Take a feature, screen, repo, or release scope and produce a structured
QA plan that covers the critical user flows, edge cases, responsive
behavior, admin paths, payments / deploy paths, and the acceptance
criteria the team can sign against.

## When to use

Use when the user wants test cases or a QA plan. Do **not** trigger for
running the app (use `leadup-browser-playwright-tester`), security
audits (use `leadup-security-review`), or deployment readiness checks
(use `leadup-deploy-checker`).

Trigger phrases: "test cases", "QA plan", "manual testing", "Playwright
tests", "test this app", "create test cases", "test plan", "regression
suite".

## Inputs needed

- Feature / repo / release scope.
- Stack (Next.js, Flutter, Django, etc.).
- User roles involved.
- Critical user flows the team can name (booking, payment, signup, …).
- Existing tests and what coverage they have.
- Regulated category? (payments, PII, medical, kids)
- Environments available (local Docker, staging, prod).

Ask at most 2 clarifying questions if scope is unclear.

## Tools/resources to use

- `references/qa-test-framework.md` — flow shape, edge-case taxonomy.
- `assets/qa-test-cases.template.md` — output shape.
- `leadup-browser-playwright-tester` — to actually run UI tests.
- `leadup-deploy-checker` — to gate release.
- `leadup-security-review` — for security-sensitive flows.
- `leadup-pii-risk-reviewer` — for PII flows.
- `leadup-release-manager` — for the release sign-off pass.

## Step-by-step workflow

1. **Restate scope** (feature / release / repo).
2. **List critical user flows** (5–10) per role, end-to-end.
3. **For each flow**, write:
   - Manual happy-path test (steps + expected).
   - 3–5 edge cases (empty, invalid, slow network, locked state, …).
   - Responsive checks (mobile 360, tablet 768, desktop 1280+).
   - Accessibility quick check (focus, contrast, labels).
4. **Admin tests**: critical actions (CRUD, role gates, exports,
   audit logging, impersonate).
5. **Payment / deploy tests** if relevant: Razorpay test flow, refund,
   webhook handling, GST invoice, env switch, migration safety.
6. **Playwright spec outline**: file names + describe blocks (without
   writing the code unless asked).
7. **Acceptance criteria**: 1 testable line per deliverable.
8. **Hand off** to `leadup-browser-playwright-tester` for execution.

## Required output format

One Markdown plan with these sections, in this order:

1. **Brief restate** — scope, stack, environments.
2. **Critical user flows** — per role, numbered.
3. **Manual test cases** — table per flow: step · expected · pass/fail.
4. **Edge cases** — per flow: list of 3–5 with what to check.
5. **Responsive / accessibility** — checks per screen.
6. **Admin tests** — table: action · role · expected · audit log entry.
7. **Payment / deploy tests** — if relevant.
8. **Playwright spec outline** — file list with `describe` blocks.
9. **Acceptance criteria** — 1 line per deliverable.
10. **Hand-offs** — to other LeadUp skills.

## Safety rules

- Do **not** invent endpoints, fields, or flows that don't exist —
  flag with "verify" if unsure.
- Do **not** propose tests that require real production data or real
  customer PII. Use test fixtures.
- For payments: test in **test mode** only; use Razorpay test keys
  (placeholders, not real).
- For PII flows: test masking, audit log entries, export permissions.
- For regulated categories: cover refusal cases and disclaimer text.
- Default to mobile-first (LeadUp clients are mostly on mobile).
- For India: include UPI, GST invoice, regional language checks where
  applicable.
- Defer execution to `leadup-browser-playwright-tester`.
- Defer release gating to `leadup-release-manager`.

## Common mistakes

- 200 test cases with no priority — team skips them.
- Only happy-path tests, no edge cases.
- Tests written against URLs that don't exist yet.
- Skipping mobile / responsive.
- No audit log checks on admin tests.
- Payment tests on live keys.
- Treating QA as the dev's problem alone — no acceptance criteria for
  the client / PM.

## Troubleshooting

- **No staging env**: write Docker-only test plan; note what needs
  prod-like to validate.
- **Mobile-heavy app**: write 60% mobile / 30% desktop / 10% tablet
  cases; cover one-handed thumb reach.
- **AI feature involved**: include golden / edge / jailbreak cases per
  `leadup-ai-feature-planner` test plan.
- **Regulated category**: include refusal tests, disclaimer text
  checks, PII masking tests, audit log entries.
- **Old repo with no tests**: deliver "v1 QA plan" = top 5 flows
  manual + 1 Playwright smoke; phase 2 expands.
- **Multi-tenant**: include tenant isolation tests (org A cannot see
  org B's data).

## Test prompts

### Should trigger (5)
1. "Generate test cases for our salon booking flow."
2. "QA plan for the admin panel of our clinic SaaS."
3. "Manual + Playwright tests for our payment integration."
4. "Test cases for the WhatsApp reminder feature."
5. "Create a test plan for the next release."

### Should NOT trigger (3)
1. "Run Playwright on the app now." (→ `leadup-browser-playwright-tester`)
2. "Is the deploy ready or not?" (→ `leadup-deploy-checker`)
3. "Audit security of this auth flow." (→ `leadup-security-review`)

### Functional test cases (2)
1. Given "salon booking SaaS, Next.js, multi-tenant, Razorpay
   payments", return a QA plan with 5–10 critical flows per role, edge
   cases for each, mobile checks, admin tests with audit log
   verification, Razorpay test-mode flows, GST invoice export check,
   and Playwright spec outline.
2. Given a regulated category (clinic SaaS with patient PII), return
   a plan that includes PII masking tests, audit log entries on
   reveal, tenant isolation tests, refusal tests on disallowed
   actions, and a hand-off to `leadup-pii-risk-reviewer` and
   `leadup-security-review`.

## Success criteria

- All 10 sections present in order.
- 5–10 critical flows per role.
- Each flow has happy path + 3–5 edge cases.
- Mobile / responsive included.
- Admin tests include audit log verification.
- Payments tested in test mode only.
- Playwright spec outline names files + describe blocks.
- Acceptance criteria are 1 testable line each.
- No real PII or live keys anywhere in the plan.
