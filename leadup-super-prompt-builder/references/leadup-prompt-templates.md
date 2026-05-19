# LeadUp Prompt Templates (12 types)

Used by `leadup-super-prompt-builder`. Fill the placeholders, keep the LeadUp
constraints, output as ONE copy-paste block. `[...]` = fill in.

## Shared LeadUp constraint block (paste into any prompt)

```
Context: LeadUp Technologies — build → test in Docker → GitHub (leadupofficial)
→ Coolify on leadup-server → *.leadup.in. Stack: [Next.js/Node-TS/Postgres/
Flutter/Bagisto]. Constraints: research + plan before code; recommend an
approach and wait for my go; test locally before claiming done; DO NOT push
or deploy without my approval; never read/print real .env values or keys
(use __SET_ME__ placeholders); UI must be premium international standard;
update STATUS.md (done/in progress/bugs/blocked/next task).
```

## 1. Claude Code coding prompt
```
Act as a senior engineer on [project]. Source: [repo/spec/idea].
Task: [feature/fix], in small reviewable steps.
<shared LeadUp constraint block>
Deliver: a short plan first, then implement, then how you tested in Docker.
Done when: [acceptance criteria]. Stop and ask before any push/deploy.
```

## 2. RuFlo project intelligence prompt
```
Act as a research + planning agent for [project]. Traverse prior art,
patterns, and dependencies. Goal: [research/plan X].
<shared LeadUp constraint block>
Deliver: findings, options with trade-offs, and a recommended plan. No build
until I approve the plan.
```

## 3. New project planning prompt
```
Plan a new LeadUp project: [idea]. Source: [PDF/notes].
<shared LeadUp constraint block>
Deliver: stack recommendation + DB plan (multi-tenant decision) + MVP
roadmap + deploy plan + the project memory files. No feature code yet.
```

## 4. Existing repo analysis prompt
```
Analyse the existing repo at [path]. 
<shared LeadUp constraint block>
Deliver: detected stack, exact run/test commands, current state, bugs,
missing files, and the single next recommended task. Read-only.
```

## 5. API research prompt
```
Research integrating [API, e.g. Razorpay] into [project].
<shared LeadUp constraint block>
Deliver: official docs, auth method, rate limits, current pricing (with
date), webhooks (signature + idempotency), env key NAMES as placeholders,
risks, fallback, go/no-go + integration steps. No keys.
```

## 6. GitHub repo research prompt
```
Find open-source repos for [need] compatible with [stack].
<shared LeadUp constraint block>
Deliver: 2–4 candidates with license, stars, last commit, and a
copy / adapt / inspiration-only verdict + recommendation.
```

## 7. Browser/Playwright testing prompt
```
Run [app] locally and test it in the browser.
<shared LeadUp constraint block>
Deliver: results per flow (home/login/admin CRUD), console/network errors,
responsive 375/768/1280, and updated Playwright specs (env-var creds only).
```

## 8. Deployment prompt
```
Check deploy readiness for [project] → [subdomain].leadup.in on Coolify.
<shared LeadUp constraint block>
Deliver: READY/NOT READY verdict, blocking items + fix commands, rollback
plan. Do NOT deploy or push — stop at the approval gate.
```

## 9. Security review prompt
```
Security-review [project] (secrets, auth, multi-tenant, payments, deploy).
<shared LeadUp constraint block>
Deliver: findings by severity with fixes; report any secret REDACTED with
rotation steps. Read-only; do not disable controls.
```

## 10. Premium UI prompt
```
Upgrade [screen/app] UI to premium international SaaS standard.
<shared LeadUp constraint block>
Deliver: per-screen before→after, empty/loading/error/success states,
responsive + a11y preserved, all functionality intact. No push.
```

## 11. Content calendar prompt
```
Build a [timeframe] content calendar for [brand], goal [followers/leads].
<shared LeadUp constraint block (drop Docker/deploy parts)>
Deliver: dated calendar (date|platform|pillar|format|hook|caption|CTA),
hooks bank, reel ideas, posting times (flag as heuristic), repurposing.
```

## 12. Client document prompt
```
Write a [proposal/report/handoff/API-access email] for [client/project].
<shared LeadUp constraint block (drop Docker/deploy parts)>
Deliver: PDF-ready Markdown, structured per type, no invented prices/terms
(mark assumptions), no credentials. Draft only — not sent.
```
