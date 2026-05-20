# LeadUp Skill Registry

Single source of truth for every LeadUp skill. Used by
`leadup-skill-router` to decide which skill / pack / model to apply.
Skills marked **planned** are referenced by the router but not yet
shipped — substitute the closest shipped skill until they ship.

> 37 skills shipped · 2 planned

## Quick legend

- **Category**: which of the 11 workflow packs this skill primarily
  serves.
- **Risk level**: default risk band when this skill is run (Low =
  DeepSeek; Medium = DeepSeek first, Sonnet review; High = Sonnet /
  Opus only).
- **Related**: typical neighbours in a chain (not exhaustive).

## Master index (all skills)

### Router

| Skill | Category | Risk | Use case |
|---|---|---|---|
| `leadup-skill-router` | router (cross-cutting) | Low (planning only) | Master orchestrator. Picks pack + skills + model + approval gate for any request. |

Triggers: "which skill should I use", "use router", "route this
task", "analyze my request", "what workflow needed", "choose best
skill", "understand this task", "convert this into workflow", "which
LeadUp skill", "auto select skill", "master router", "skill router",
"workflow router", "decide skill pack", "rough idea to workflow".

Related: every other skill (it picks them).

### Development Pack

| Skill | Risk | Use case | Related |
|---|---|---|---|
| `leadup-project-kickoff` | Medium | Bootstrap a new project (CLAUDE / STATUS / DEPLOY / SECURITY / README / `.env.example`, stack, DB plan, MVP, deploy plan) | `leadup-saas-mvp-planner`, `leadup-deploy-checker` |
| `leadup-existing-repo-analyzer` | Medium | Recover an existing repo's state, stack, bugs, next task | `leadup-status-updater`, `leadup-feature-option-planner` |
| `leadup-api-research-builder` | Medium (High for payments/auth) | Research a third-party API before integrating: docs, auth, limits, pricing, webhooks | `leadup-public-api-finder`, `leadup-n8n-workflow-builder` |
| `leadup-public-api-finder` | Low | Discover + score + pick free / public APIs; outputs best + backup + env placeholders + decision | `leadup-api-research-builder`, `leadup-github-repo-researcher` |
| `leadup-github-repo-researcher` | Low | Vet open-source repos (license, activity, copy/adapt/inspiration) | `leadup-public-api-finder` |
| `leadup-mcp-tool-orchestrator` | Low | Pick + sequence MCP / tool servers safely; read-only first; escalate with approval | `leadup-public-api-finder`, every chain that needs external tools |
| `leadup-browser-playwright-tester` | Medium | Run & E2E-test the app; write Playwright specs | `leadup-qa-test-case-generator`, `leadup-deploy-checker` |
| `leadup-deploy-checker` | High | READY/NOT READY deploy verdict for Coolify / `leadup-server` (never deploys) | `leadup-release-manager`, `leadup-security-review` |
| `leadup-premium-ui-upgrader` | Medium | Raise UI to premium international-SaaS standard | `leadup-free-creative-assets-finder`, `leadup-human-content-editor` |
| `leadup-status-updater` | Low | Keep `STATUS.md` / `TODO.md` / `CHANGELOG.md` current after a task | every close-out chain |
| `leadup-super-prompt-builder` | Low | Convert rough idea / instruction / broken-English into copy-paste-ready prompt for Claude Code / RuFlo / opencode / ChatGPT | `leadup-skill-router`, `leadup-project-kickoff` |

Triggers (selected): "bootstrap a new project", "analyze this repo",
"research the API", "find an API", "vet this repo", "deploy ready",
"premium UI", "update STATUS.md", "make super prompt".

### Growth Marketing Pack

| Skill | Risk | Use case | Related |
|---|---|---|---|
| `leadup-growth-research-agent` | Low | Orchestrator for cross-cutting growth research; picks SEO/keywords/ads/CRO/feature angle | every other growth skill |
| `leadup-seo-strategist` | Low | SEO audit + 30/60/90 plan (technical + on-page + schema + content gaps) | `leadup-keyword-competitor-researcher`, `leadup-blog-content-writer` |
| `leadup-keyword-competitor-researcher` | Low | Clustered keyword map + 3–5 competitor analysis with honest data labels | `leadup-seo-strategist`, `leadup-blog-content-writer` |
| `leadup-blog-content-writer` | Low | SEO-aware blog / service-page drafts in human voice (no em dashes, no banned hype) | `leadup-human-content-editor` |
| `leadup-smm-growth-planner` | Low | 30-day social media plan: pillars, reels, hooks, schedule, KPIs | `leadup-content-calendar-builder`, `leadup-digital-ads-planner` |
| `leadup-content-calendar-builder` | Low | Dated content calendar with platform mix, hooks, captions, posting times | `leadup-smm-growth-planner`, `leadup-human-content-editor` |
| `leadup-digital-ads-planner` | Medium | Google / Meta / LinkedIn / YouTube plan with structure, budget, copy, creative, tracking, policy notes | `leadup-landing-page-cro-planner`, `leadup-api-research-builder` |
| `leadup-landing-page-cro-planner` | Medium | Landing-page audit + prioritized CRO fixes + A/B tests + 25+ item checklist | `leadup-digital-ads-planner`, `leadup-human-content-editor` |
| `leadup-free-creative-assets-finder` | Low | Free / safe-to-use photos, icons, Lottie, GIFs, 3D, video, avatars, emojis (and SFX/music) with verified licenses | `leadup-premium-ui-upgrader`, `leadup-smm-growth-planner` |

Triggers (selected): "growth research", "seo audit", "keyword
finder", "write blog", "smm plan", "content calendar", "digital ads",
"increase conversion", "free image / icon / Lottie".

### Human Content Pack

| Skill | Risk | Use case | Related |
|---|---|---|---|
| `leadup-human-content-editor` | Low | Rewrite AI-generated or AI-looking copy into natural, human, business-ready content (websites, SaaS, app UI, proposals, social) | every public-facing chain ends here |
| `leadup-blog-content-writer` | Low | Cross-listed (Growth Pack) | (see above) |
| `leadup-client-document-generator` | Low | Generate proposals, reports, dev/handoff docs, API emails | `leadup-sales-proposal-builder`, `leadup-human-content-editor` |
| `leadup-content-calendar-builder` | Low | Cross-listed (Growth Pack) | (see above) |

Triggers (selected): "make this human", "remove em dash", "rewrite
for website", "make this client ready".

### Sales and Client Pack

| Skill | Risk | Use case | Related |
|---|---|---|---|
| `leadup-sales-proposal-builder` | Low | Client-ready proposal, scope, quote, retainer, AMC plan + follow-up | `leadup-pricing-package-planner`, `leadup-human-content-editor` |
| `leadup-client-requirement-analyzer` | Low | Convert messy client messages / PDFs / screenshots / voice notes into structured requirements + missing questions + next reply | `leadup-sales-proposal-builder`, `leadup-pricing-package-planner` |
| `leadup-pricing-package-planner` | Low | Basic / Standard / Premium tiers with honest exclusions, margin notes, GST handling | `leadup-sales-proposal-builder`, `leadup-human-content-editor` |
| `leadup-lead-funnel-builder` | Medium | End-to-end lead funnel — traffic, LP, capture (form or WhatsApp), qualify, follow-up, automation, tracking | `leadup-landing-page-cro-planner`, `leadup-whatsapp-automation-planner`, `leadup-n8n-workflow-builder` |
| `leadup-client-document-generator` | Low | Cross-listed (Human Content Pack) | (see above) |

Triggers (selected): "proposal", "quote", "AMC plan", "client
message", "pricing tiers", "lead funnel".

### SaaS / Product Pack

| Skill | Risk | Use case | Related |
|---|---|---|---|
| `leadup-saas-mvp-planner` | Medium (High for payments / multi-tenant boundary) | Paid SaaS MVP plan — users, first paid feature, modules, tenant model, integrations, launch roadmap | `leadup-feature-option-planner`, `leadup-admin-panel-planner`, `leadup-pii-risk-reviewer` |
| `leadup-feature-option-planner` | Medium | Must-have / premium / AI feature buckets + MVP/P2/P3 + recommended next feature | `leadup-ai-feature-planner`, `leadup-admin-panel-planner` |
| `leadup-ai-feature-planner` | Medium (High when PII passes through) | One AI feature end-to-end — model + fallback, prompt design, cost ledger, privacy flow, non-AI fallback, logging redaction, gated rollout | `leadup-api-research-builder`, `leadup-pii-risk-reviewer` |
| `leadup-admin-panel-planner` | Medium | Navigation, modules, tables, filters, roles + permission matrix, KPI cards, audit log, PII masking | `leadup-pii-risk-reviewer`, `leadup-premium-ui-upgrader` |
| `leadup-multi-tenant-architect` *(planned)* | High | Multi-tenant boundary, row vs schema, RLS, encryption per tenant, key rotation | substitute: tenant section of `leadup-saas-mvp-planner` |

Triggers (selected): "saas mvp", "feature roadmap", "AI feature",
"admin panel", "multi-tenant".

### QA / Release Pack

| Skill | Risk | Use case | Related |
|---|---|---|---|
| `leadup-qa-test-case-generator` | Medium | Critical user flows, manual + Playwright + edge case + admin + tenant isolation + acceptance criteria | `leadup-browser-playwright-tester`, `leadup-release-manager` |
| `leadup-browser-playwright-tester` | Medium | Cross-listed (Development Pack) | (see above) |
| `leadup-release-manager` | High | Release summary, env diff, test status, risks, rollback, client comms, Go/No-Go | `leadup-deploy-checker`, `leadup-status-updater` |
| `leadup-deploy-checker` | High | Cross-listed (Development Pack) | (see above) |
| `leadup-backup-rollback-planner` *(planned)* | High | Backup strategy, restore drill, rollback runbook beyond a single release | substitute: rollback section of `leadup-release-manager` |

Triggers (selected): "test cases", "release notes", "go live",
"deploy checklist", "rollback".

### Automation Pack

| Skill | Risk | Use case | Related |
|---|---|---|---|
| `leadup-whatsapp-automation-planner` | Medium (High when regulated) | Meta-policy-safe WhatsApp: category, opt-in, templates with typed placeholders, workflow, failure handling, IT Rules / DPDP / ASCI | `leadup-n8n-workflow-builder`, `leadup-pii-risk-reviewer` |
| `leadup-n8n-workflow-builder` | Medium | n8n workflow with atomic nodes, credentials placeholders, signature-verified webhooks, idempotency, retries + dead-letter, manual approval, text diagram | `leadup-api-research-builder`, `leadup-whatsapp-automation-planner` |
| `leadup-api-research-builder` | Medium (High for payments / auth) | Cross-listed (Development Pack) | (see above) |
| `leadup-public-api-finder` | Low | Cross-listed (Development Pack) | (see above) |
| `leadup-mcp-tool-orchestrator` | Low | Cross-listed (Development Pack) | (see above) |

Triggers (selected): "WhatsApp automation", "n8n workflow", "find
API", "MCP tools".

### Security and Compliance Pack

| Skill | Risk | Use case | Related |
|---|---|---|---|
| `leadup-security-review` | High | Review secrets, auth, multi-tenant, payments, deploy risks | `leadup-pii-risk-reviewer`, `leadup-deploy-checker` |
| `leadup-pii-risk-reviewer` | High | PII inventory, data flow, risk scoring, masking + encryption + retention + DSR + consent + developer checklist (DPDP / IT Rules / GDPR) | `leadup-security-review`, `leadup-admin-panel-planner` |
| `leadup-deploy-checker` | High | Cross-listed (Development Pack) | (see above) |
| `leadup-release-manager` | High | Cross-listed (QA / Release Pack) | (see above) |

Triggers (selected): "security review", "PII review", "DPDP",
"GDPR", "payment security".

### Creative Assets Pack

| Skill | Risk | Use case | Related |
|---|---|---|---|
| `leadup-free-creative-assets-finder` | Low | Cross-listed (Growth Pack) | (see above) |
| `leadup-premium-ui-upgrader` | Medium | Cross-listed (Development Pack) | (see above) |
| `leadup-human-content-editor` | Low | Cross-listed (Human Content Pack) | (see above) |
| `leadup-smm-growth-planner` | Low | Cross-listed (Growth Pack) | (see above) |
| `leadup-digital-ads-planner` | Medium | Cross-listed (Growth Pack) | (see above) |

### API and Resource Research Pack

| Skill | Risk | Use case | Related |
|---|---|---|---|
| `leadup-public-api-finder` | Low | Cross-listed (Development Pack) | (see above) |
| `leadup-api-research-builder` | Medium (High for payments / auth) | Cross-listed (Development Pack) | (see above) |
| `leadup-github-repo-researcher` | Low | Cross-listed (Development Pack) | (see above) |
| `leadup-growth-research-agent` | Low | Cross-listed (Growth Pack) | (see above) |
| `leadup-mcp-tool-orchestrator` | Low | Cross-listed (Development Pack) | (see above) |

## Planned (referenced by router; not yet shipped)

| Planned skill | Closest substitute | Reason it's planned |
|---|---|---|
| `leadup-multi-tenant-architect` | tenant section of `leadup-saas-mvp-planner` | Will deep-dive on row-vs-schema multi-tenancy, RLS, per-tenant keys, cross-region replication. |
| `leadup-backup-rollback-planner` | rollback section of `leadup-release-manager` | Will design backup cadence, restore drills, RPO/RTO, and full disaster runbook. |

When the router selects a planned skill, it must:
1. Name the planned skill.
2. Substitute the closest shipped skill.
3. Flag the gap in the report.

## How the router uses this file

`leadup-skill-router` reads this registry to:

- Confirm a chosen skill exists.
- Pick the correct risk level (drives model choice).
- Surface related skills for cross-pack hand-offs.
- Mark planned skills with a substitution.

Update this file whenever a skill is added, renamed, or upgraded.
Keep risk levels honest — they drive the model routing rules and the
approval gates.
