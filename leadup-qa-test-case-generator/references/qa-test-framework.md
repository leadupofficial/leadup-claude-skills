# QA test framework — LeadUp

How LeadUp writes QA plans that catch the real bugs without 200
unrunnable test cases.

## 1. Critical user flows first

Per role, list 5–10 flows the product must not break:

For a service-SaaS:

- **Customer**: book, reschedule, cancel, pay, receive reminder.
- **Staff**: log in, view today, mark done, take payment, refund.
- **Org owner**: invite staff, change plan, export GST invoice, view
  KPI dashboard.
- **Super admin (LeadUp)**: create org, suspend org, view audit log.

Each flow ships with a manual test before any automation.

## 2. Manual test case shape

```
Flow: [name]
Pre-conditions: [user logged in as X, sample data Y]
Steps:
  1. [Action]
  2. [Action]
  3. [Action]
Expected: [observable outcome]
Pass / Fail / Blocked: __
Tester: ___  Date: ___  Build: ___
```

Keep steps in plain language. Avoid CSS selectors at this stage.

## 3. Edge cases (always 3–5 per flow)

Standard edge taxonomy:

- **Empty input** (blank field, no items).
- **Invalid input** (wrong format, out-of-range, special chars).
- **Slow network / offline** (loading states, retries).
- **Concurrent action** (two users edit same record).
- **Permission denied** (role lacks permission).
- **Locked state** (cancelled booking, paid invoice, archived).
- **Boundary values** (0, 1, max, max+1).
- **Time-related** (DST, timezone change, end-of-day).
- **Language / unicode** (Hindi, Tamil, emoji).

Pick the 3–5 that matter most for that flow.

## 4. Responsive + accessibility

Per primary screen:

- Mobile 360 (one-handed thumb reach for primary actions).
- Tablet 768.
- Desktop 1280+.

Quick a11y checks:

- Tab order matches reading order.
- Visible focus ring on interactive elements.
- Contrast on buttons + body text.
- Labels on every form input.
- Errors announced to screen readers.

For LeadUp clients on India SMB: mobile-first by default.

## 5. Admin tests

For each admin action:

| Check | Rule |
|---|---|
| Role gate | only allowed roles can do it |
| Confirmation | destructive actions require confirm |
| Audit log entry | event captured with actor + diff |
| PII reveal | full reveal triggers audit |
| Export | gated by permission, password-protected if PII heavy |

Add a tenant-isolation test for every list: org A cannot see org B.

## 6. Payments + GST tests (India)

- Razorpay **test mode** only. Use test keys (placeholders).
- Successful charge → invoice created → GSTIN on invoice → payment
  state synced.
- Failed payment → user sees clear next step, no double-charge.
- Refund → invoice updated → payment row updated → notification sent.
- Webhook handling: idempotent on retry; signature verified.
- GST invoice export: HSN/SAC present, format matches GSTR-1.

For international: Stripe test mode, currency + tax handling.

## 7. Deploy tests

- Migrations run forward on a copy of prod schema (no destructive).
- Env vars present (no `__SET_ME__` left).
- Docker build succeeds in CI.
- Health check endpoint returns 200.
- Rollback plan tested at least once.

Defer the actual READY/NOT READY verdict to `leadup-deploy-checker`.

## 8. Playwright spec outline

Don't ship 50 specs on day 1. Start with a smoke pack:

```
e2e/
  smoke/
    auth.spec.ts          // login / logout / wrong password
    bookings.spec.ts      // create / list / detail / cancel
    payments.spec.ts      // Razorpay test charge
    admin.spec.ts         // tenant isolation + audit log
    public.spec.ts        // home / pricing / contact / 404
```

Each spec has `describe` blocks per flow + `test` per case. Use
`leadup-browser-playwright-tester` to run.

## 9. Acceptance criteria (for the release)

One testable bullet per deliverable. Examples:

- [ ] A logged-in customer can complete a booking on mobile in ≤ 60s.
- [ ] Razorpay test charge writes a `payments` row with `status =
      captured`.
- [ ] Org owner can export a GST invoice for a paid booking.
- [ ] Staff cannot reveal customer phone in plaintext.
- [ ] Tenant A cannot read or write tenant B's bookings.

Subjective bullets ("looks good") are banned.

## 10. Honesty rules

- No tests against endpoints / fields that don't exist.
- No real PII in fixtures.
- No live payment keys.
- Mobile checks included.
- Audit log + tenant isolation tested.
- Refusal tests for AI / regulated features.
- Hand execution to `leadup-browser-playwright-tester`.
- Hand release gating to `leadup-release-manager` and
  `leadup-deploy-checker`.
