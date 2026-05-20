# QA test cases — [Feature / release]

> Date: [YYYY-MM-DD]
> Scope: [feature / release / repo]
> Stack: [Next.js / Flutter / Django / …]
> Environments: [local Docker / staging / prod]

## 1. Brief restate

[One paragraph: what's being tested, why, by when.]

## 2. Critical user flows

### Customer
1. Sign up / log in
2. Search and book a service
3. Pay via Razorpay (test mode)
4. Receive WhatsApp + email reminder
5. Cancel / reschedule
6. Receive refund (if applicable)

### Staff
1. Log in
2. View today's schedule
3. Mark booking done / no-show
4. Take in-person payment
5. Refund

### Org owner
1. Invite staff
2. Change subscription plan
3. Export GST invoice
4. View KPI dashboard

### Super admin (LeadUp)
1. Create / suspend org
2. View audit log

## 3. Manual test cases

### Flow: Customer books and pays

Pre-conditions: customer signed up, test card / UPI available.

| # | Step | Expected | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Open booking page | Page renders < 2.5s mobile | __ |  |
| 2 | Pick service + slot | Slot reserved (15 min hold) | __ |  |
| 3 | Enter contact details | Validation inline | __ |  |
| 4 | Click "Pay now" | Razorpay test sheet opens | __ |  |
| 5 | Complete test payment | Success page + booking confirmed | __ |  |
| 6 | Receive WhatsApp template | Message arrives < 60s | __ |  |
| 7 | Receive email confirmation | Email arrives < 60s | __ |  |
| 8 | View booking in account | Status = confirmed | __ |  |

(Repeat the table for each critical flow.)

## 4. Edge cases (per flow)

### Customer booking
- Empty mandatory field → inline error, no submit.
- Invalid phone (length / +91) → error.
- Slot expires during checkout → user warned, slot re-pickable.
- Network drops mid-payment → no double-charge, status reconciled
  from webhook.
- Customer pays twice (double-click) → idempotent, one booking.
- Cancel during 15-min hold → slot released within 60s.

### Staff actions
- Mark done on past booking → ok.
- Mark done on cancelled booking → blocked + clear message.
- Refund on already-refunded payment → blocked.

(Add 3–5 edge cases per flow.)

## 5. Responsive + accessibility

| Screen | 360 (mobile) | 768 (tablet) | 1280 (desktop) | a11y notes |
|---|---|---|---|---|
| Home | LCP < 2.5s | layout intact | layout intact | focus ring, contrast |
| Booking | one-thumb usable | two-column | two-column | tab order |
| Payment | sheet usable | sheet usable | inline | label per field |
| Admin tables | card view | scrollable | full | column labels |

## 6. Admin tests

| Action | Role | Expected | Audit log entry |
|---|---|---|---|
| View customer phone (full) | Owner/Admin | full shown | yes (PII reveal) |
| View customer phone (full) | Staff | masked | n/a |
| Export customer CSV | Owner | success, gated | yes (export) |
| Export customer CSV | Staff | blocked | n/a |
| Impersonate org user | Super admin | session start/end | yes (impersonate) |
| Change org settings | Admin (partial) | only allowed fields | yes (settings change) |
| Delete a booking | Owner/Admin | confirm + soft delete | yes (destructive) |

Tenant isolation: log in as Org A; ensure no Org B records appear in
any list, search, or detail page.

## 7. Payment / deploy tests

### Razorpay (test mode, India)
- [ ] Successful payment writes `payments.status = captured`.
- [ ] Webhook signature verified on retry; idempotent.
- [ ] Refund updates invoice + payment + sends notification.
- [ ] GST invoice export: HSN/SAC present, format matches GSTR-1.
- [ ] Currency = INR; amount in paise.

### Deploy
- [ ] Migrations forward-only; tested on a copy of staging schema.
- [ ] All required env vars present (no `__SET_ME__` left).
- [ ] Docker build green in CI.
- [ ] Health check 200 on `/healthz`.
- [ ] Rollback plan tested.

(Defer the READY/NOT READY verdict to `leadup-deploy-checker`.)

## 8. Playwright spec outline

```
e2e/
  smoke/
    auth.spec.ts
      - "user can log in with valid credentials"
      - "user sees error on wrong password"
    bookings.spec.ts
      - "customer can create a booking on mobile"
      - "customer can cancel during hold window"
    payments.spec.ts
      - "razorpay test charge writes a payments row"
      - "refund updates invoice + sends notification"
    admin.spec.ts
      - "tenant A cannot read tenant B bookings"
      - "PII reveal triggers an audit log entry"
    public.spec.ts
      - "home loads under 2.5s on mobile"
      - "404 returns clear next action"
```

Hand to `leadup-browser-playwright-tester` to run.

## 9. Acceptance criteria

- [ ] A logged-in customer can complete a booking on mobile in ≤ 60s.
- [ ] Razorpay test charge writes a `payments` row with `status =
      captured`.
- [ ] Org owner can export a GST invoice for a paid booking.
- [ ] Staff cannot reveal customer phone in plaintext without a role
      change + audit entry.
- [ ] Tenant A cannot read or write tenant B's bookings.
- [ ] Health check returns 200 on `/healthz`.

## 10. Hand-offs

- Test execution → `leadup-browser-playwright-tester`.
- Deploy verdict → `leadup-deploy-checker`.
- Release sign-off → `leadup-release-manager`.
- Security-sensitive flows → `leadup-security-review`.
- PII flows → `leadup-pii-risk-reviewer`.
