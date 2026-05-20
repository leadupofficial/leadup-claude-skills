# Release pack — [Product] v[X.Y.Z]

> Target: [Coolify / leadup-server / Vercel / other]
> Date / time (IST): [YYYY-MM-DD HH:MM]
> Branch: [release/vX.Y.Z]  ·  Build: [git sha]
> Release manager: [name]  ·  On-call: [name]

## 1. Release summary

[One short paragraph: what this release is for and who it affects.]

## 2. What changed

### Features
- [Feature in plain English]
- [Feature]

### Improvements
- [Improvement]
- [Improvement]

### Fixes
- [Bug fix]
- [Bug fix]

### Internal
- [Refactor / infra / dev-only]

## 3. Modules / files touched

- `apps/web` — [areas]
- `apps/admin` — [areas]
- `packages/db` — migrations + schema
- `infra/` — Docker / Coolify config

## 4. Migrations

| # | Change | Forward script | Rollback strategy |
|---|---|---|---|
| 1 | [add column `bookings.staff_id`] | `db/migrations/2026XXXX_add_staff_id.sql` | nullable + new index; no rollback needed |
| 2 | [backfill staff_id] | one-off job | safe to re-run |

Destructive changes: [none / list].

## 5. Env vars

| Var | Action | Required | Secret | Where to set |
|---|---|---|---|---|
| `WHATSAPP_BSP_TOKEN` | added | yes | yes | Coolify env |
| `WHATSAPP_TEMPLATE_ID` | added | yes | no | Coolify env |
| `OLD_VAR` | removed | n/a | n/a | n/a |

Restart needed: [services list]

## 6. Test status

| Type | Status | Notes |
|---|---|---|
| Manual happy-paths | pass | covered top 5 flows |
| Manual edge cases | partial | 1 known, see risks |
| Playwright smoke | pass | CI green |
| Tenant isolation | pass | regression spec |
| Razorpay test mode | pass | test charge + webhook |
| PII masking + audit log | pass | reviewed by `leadup-pii-risk-reviewer` |

## 7. Known risks

| # | Risk | Severity | Likelihood | Mitigation | Owner |
|---|---|---|---|---|---|
| 1 | [WhatsApp BSP template approval lag] | med | med | fallback to email; toggle flag | [name] |
| 2 | [Razorpay webhook signature change] | low | low | retry + alert; rollback plan in §8 | [name] |

If any high × high without mitigation → No-Go.

## 8. Rollback plan

App rollback:
```
# 1. In Coolify, redeploy previous image tag:
#    [tag: vX.Y.(Z-1)]
# OR revert latest deploy via Coolify UI.

# 2. If self-deployed:
git revert <commit-sha>
docker compose -f docker-compose.prod.yml up -d --build
```

DB rollback:
- Additive migration only → no DB rollback needed.
- If a backfill ran: keep new columns; revert app only.

Cache / queue:
- Flush queue: [command]
- Bust CDN if relevant.

Time to roll back: ~[N] minutes.
Decision authority: [name + WhatsApp number].

## 9. Client communication

### Internal (Slack / team channel)

> Releasing **vX.Y.Z** at [HH:MM IST]. Includes: [headlines]. Migration:
> [yes/no, additive]. Downtime: [none / N min]. On-call: [name].

### Paying clients (email + WhatsApp)

```
Hi [Client name],

Heads up — we're shipping an update on [Day, date, IST time].
What's new:
- [Plain bullet]
- [Plain bullet]

You don't need to do anything. If anything looks off, reply here or
WhatsApp us.

— LeadUp Technologies
```

### Public changelog

```
### vX.Y.Z — [Date]

- [Plain headline]
- [Plain headline]
- Bug fixes and small improvements.
```

Pass all three through `leadup-human-content-editor` before publishing.

## 10. Go / No-Go recommendation

> **[GO / NO-GO]** — top reason: [one line].

Conditions to flip to GO (if currently NO-GO):
- [ ] [Outstanding item]
- [ ] [Outstanding item]

## 11. Hand-offs

- Deploy verdict → `leadup-deploy-checker`.
- QA pass needed? → `leadup-qa-test-case-generator`.
- Security-sensitive scope → `leadup-security-review`.
- PII surface change → `leadup-pii-risk-reviewer`.
- Public copy polish → `leadup-human-content-editor`.
- Post-release memory update → `leadup-status-updater`.
