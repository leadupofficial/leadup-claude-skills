# Release checklist — LeadUp

Pre-release gate + rollback + client communication. Bias toward
No-Go when in doubt.

## 1. Pre-release gate (must all be true)

- [ ] Test status: manual sign-off + automated CI green (or noted gaps).
- [ ] Migration forward tested on a copy of the target schema.
- [ ] Migration **rollback** path documented (script, SQL, or "no
      destructive change → safe to roll forward only").
- [ ] Env var diff captured; new vars added to target environment.
- [ ] Secrets stay out of the repo (use placeholders, vaults, or
      Coolify env).
- [ ] Health check endpoint returns 200 in staging.
- [ ] Multi-tenant isolation regression checked (if applicable).
- [ ] PII / payment changes reviewed by `leadup-pii-risk-reviewer` /
      `leadup-security-review`.
- [ ] Public copy passed through `leadup-human-content-editor`.
- [ ] `STATUS.md` ready to update post-release.

If any box is unchecked, default to **No-Go**.

## 2. Migration safety

Preferred order:

1. **Additive only** (new columns / tables / indexes) → safe.
2. **Backfill** new columns in a separate step.
3. **Switch reads** to the new column.
4. **Cleanup** (drop old column / index) in a later release.

Destructive in a single release (drop column / table / NOT NULL on
populated rows) is **No-Go** unless there's a confirmed maintenance
window + tested rollback.

## 3. Env vars

For every env var in the diff, record:

- Added / Changed / Removed.
- Required in prod? (yes / no)
- Secret? (yes — use vault / `__SET_ME__` placeholder)
- Where to set (Coolify env tab, `.env`, server env).
- Service that needs to restart.

## 4. Test status

Three categories:

| Type | Status |
|---|---|
| Manual happy-paths | pass / fail / partial |
| Manual edge cases | pass / fail / partial |
| Automated (Playwright / unit) | pass / fail / partial |
| Tenant isolation | pass / fail / partial (if applicable) |
| Payment test mode | pass / fail / partial (if applicable) |
| PII masking + audit log | pass / fail / partial (if applicable) |

Use only **pass / fail / partial / unknown**. Do not invent percentages.

## 5. Risk register

Each risk:

```
Risk: [one line]
Severity: low / med / high
Likelihood: low / med / high
Mitigation: [one line]
Owner: [name]
```

If any risk is high × high without a mitigation, default to **No-Go**.

## 6. Rollback plan

Required for every release:

- **App rollback**: `git revert` / `coolify rollback` / redeploy
  previous image tag.
- **DB rollback**: forward script, backwards script (if available),
  or "additive only, no rollback needed".
- **Cache / queue**: how to clear / drain.
- **Webhook keys / third-party secrets**: how to rotate if needed.
- **Time to roll back**: estimated minutes.
- **Decision authority**: who calls rollback.

Print this in the release pack so the on-call has it at hand.

## 7. Client communication

Three audiences, three templates:

### Internal (team)

Short, factual, in Slack or shared channel:

> Releasing v0.5 today at [time IST]. Includes: [features]. Migration:
> [yes/no]. Downtime window: [N min / none]. On-call: [name].

### Paying clients

Plain-language, India-friendly:

```
Hi [Client name],

Heads up — we're shipping an update tomorrow [Day, date, IST time].
What's new:
- [Plain bullet]
- [Plain bullet]

You don't need to do anything. If anything looks off, reply here or
WhatsApp us.

— LeadUp Technologies
```

### Public changelog

A short entry on the changelog page or in-product notification:

```
### v0.5.0 — [Date]

- [Plain headline]
- [Plain headline]
- Bug fixes and small improvements.
```

Pass all three through `leadup-human-content-editor` before sending /
publishing.

## 8. Post-release (within 24 hours)

- [ ] Smoke test in prod (with `leadup-browser-playwright-tester` if
      available).
- [ ] Monitor error rate, latency, and payment success for 24h.
- [ ] `STATUS.md` updated (`leadup-status-updater`).
- [ ] Retrospective bullet: what worked, what didn't.
- [ ] Tickets / TODO updated.

## 9. Go / No-Go rules

**Default Go** when all pre-release boxes check.

**Default No-Go** if any of:
- Rollback untested / undocumented.
- Test status partial/unknown on critical flows.
- Sensitive PII / payment change unreviewed.
- Env vars missing in target.
- Destructive migration with no maintenance window.
- Release time within 4 hours of a major Indian holiday peak unless
  business-critical.

State the top reason for the recommendation in one line.
