Prompt type: New project planning · Target: Claude Code / RuFlo

```
Plan a new LeadUp project: "[project / idea]".

Source: [PDF | notes | client requirement | one-line idea].

Context: LeadUp Technologies — multi-tenant SaaS / website / Flutter app /
hosting tool for [client/segment]. Flow: build → test in Docker → GitHub
(leadupofficial) → Coolify on leadup-server → [subdomain].leadup.in.

Deliver (PLAN ONLY — no feature code yet):
- Project summary (what, for whom, the one core value flow)
- Stack recommendation (table: layer | choice | why | alternative)
- Database plan + multi-tenant strategy (shared schema + tenant_id vs
  schema-per-tenant) + key indexes
- MVP roadmap: milestones 0–3 with a definition of done each
- Deployment plan: Docker shape, Coolify service, subdomain, env key
  NAMES (placeholders), rollback note
- Project memory files: PROJECT.md, CLAUDE.md, STATUS.md, DEPLOY.md,
  SECURITY.md, README.md, .env.example (__SET_ME__ placeholders only)

Constraints:
- Ask ≤3 scoping questions only if genuinely blocking; otherwise infer.
- Premium international UI assumed.
- Never expose secrets; no repo creation / push / deploy without approval.
- End with the single next recommended task + an approval gate.
```

Toggles: [add cost/timeline] · [Flutter instead of web] · [scope to MVP only]
