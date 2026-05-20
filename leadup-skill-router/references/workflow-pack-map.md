# Workflow pack map — LeadUp

Eleven workflow packs. Each has a purpose, primary trigger cues, the
default ordered sequence, and cross-pack hand-offs. Use this when
picking the pack and the chain.

## 1. Development Pack

**Purpose:** ship code on an existing repo — fix bugs, add features,
refactor, deploy.

**Default sequence:**

```
leadup-existing-repo-analyzer
  → leadup-status-updater
  → (the actual work, scoped via leadup-feature-option-planner if new feature)
  → leadup-qa-test-case-generator
  → leadup-browser-playwright-tester
  → leadup-deploy-checker
  → leadup-release-manager
  → leadup-status-updater (close out)
```

**Cross-pack hand-offs:** Security & Compliance Pack when touching
secrets / PII / payments; Creative Assets Pack when UI needs images;
Human Content Pack when public-facing copy changes.

## 2. New Project Pack

**Purpose:** kick off a new project from idea to first deploy.

**Default sequence:**

```
leadup-super-prompt-builder (sharpen the brief)
  → leadup-project-kickoff (bootstrap CLAUDE.md / STATUS.md / DEPLOY.md / .env.example)
  → leadup-saas-mvp-planner (if SaaS)
  → leadup-feature-option-planner (full ladder)
  → leadup-admin-panel-planner (back office)
  → leadup-ai-feature-planner (only if AI in MVP)
  → leadup-deploy-checker
  → leadup-security-review
```

**Cross-pack hand-offs:** Growth Marketing Pack for launch comms; QA
& Release Pack at first ship.

## 3. Growth Marketing Pack

**Purpose:** SEO, content, social, paid, CRO, growth research.

**Default sequence:**

```
leadup-growth-research-agent (classify the request)
  → leadup-seo-strategist (if SEO)
  → leadup-keyword-competitor-researcher (if keywords / competitors)
  → leadup-blog-content-writer (if blog / service page)
  → leadup-smm-growth-planner / leadup-content-calendar-builder (if social)
  → leadup-digital-ads-planner (if paid)
  → leadup-landing-page-cro-planner (if LP conversion)
  → leadup-human-content-editor (final polish on public copy)
```

**Cross-pack hand-offs:** Creative Assets Pack for visuals; Sales &
Client Pack for retargeting LP forms; Automation Pack for n8n /
WhatsApp follow-ups.

## 4. Human Content Pack

**Purpose:** make copy sound human, not AI; works for websites, SaaS,
app UI, proposals, social, WhatsApp/email, technical docs.

**Default sequence:**

```
leadup-human-content-editor (default)
   + leadup-blog-content-writer (if originating a blog)
   + leadup-client-document-generator (if it's a doc/report)
   + leadup-content-calendar-builder (if social repurpose)
```

**Cross-pack hand-offs:** every other pack that produces public-facing
text ends here.

## 5. Sales and Client Pack

**Purpose:** client message → scope → quote → proposal → funnel.

**Default sequence:**

```
leadup-client-requirement-analyzer (raw input → scope)
  → leadup-pricing-package-planner (if pricing is the open question)
  → leadup-sales-proposal-builder (full proposal)
  → leadup-lead-funnel-builder (if growth side is in scope)
  → leadup-client-document-generator (any extra doc)
  → leadup-human-content-editor (polish before sending)
```

**Cross-pack hand-offs:** New Project Pack when the deal closes;
Growth Marketing Pack when the proposal includes ongoing
SEO/SMM/ads.

## 6. SaaS / Product Pack

**Purpose:** SaaS shape — MVP, features, AI, admin, multi-tenant
boundaries.

**Default sequence:**

```
leadup-saas-mvp-planner
  → leadup-feature-option-planner
  → leadup-ai-feature-planner (only if AI feature)
  → leadup-admin-panel-planner
  → leadup-pii-risk-reviewer (always for SaaS data)
  → leadup-security-review
```

**Planned (not yet built):** `leadup-multi-tenant-architect` —
substitute the multi-tenant section of `leadup-saas-mvp-planner` for
now.

**Cross-pack hand-offs:** Automation Pack for integrations; QA &
Release Pack at ship.

## 7. QA / Release Pack

**Purpose:** test, gate the release, ship safely, comms + rollback.

**Default sequence:**

```
leadup-qa-test-case-generator
  → leadup-browser-playwright-tester
  → leadup-deploy-checker
  → leadup-release-manager
  → leadup-status-updater (close out)
```

**Planned (not yet built):** `leadup-backup-rollback-planner` — use
the rollback section of `leadup-release-manager` until shipped.

**Cross-pack hand-offs:** Security & Compliance Pack for sensitive
releases; Human Content Pack for client comms polish.

## 8. Automation Pack

**Purpose:** WhatsApp, n8n, CRM, API, MCP automations.

**Default sequence:**

```
leadup-mcp-tool-orchestrator (what tools are available?)
  → leadup-public-api-finder (pick the right API)
  → leadup-api-research-builder (deeper API research)
  → leadup-whatsapp-automation-planner (if WhatsApp in scope)
  → leadup-n8n-workflow-builder (build the graph)
  → leadup-pii-risk-reviewer (if customer data passes through)
```

**Cross-pack hand-offs:** Security & Compliance Pack for payment /
auth nodes; Sales & Client Pack for funnel context.

## 9. Security and Compliance Pack

**Purpose:** secrets, PII, auth, payment, prod risk.

**Default sequence:**

```
leadup-security-review
  → leadup-pii-risk-reviewer
  → leadup-deploy-checker
  → leadup-release-manager
```

**Cross-pack hand-offs:** Mandatory tail for anything that ships and
touches sensitive scopes.

## 10. Creative Assets Pack

**Purpose:** free / safe-to-use assets — photos, vectors, icons,
Lottie, GIFs, 3D, video, avatars, emojis, SFX/music.

**Default sequence:**

```
leadup-free-creative-assets-finder
  → leadup-premium-ui-upgrader (if assets land in the product UI)
  OR
  → leadup-smm-growth-planner / leadup-digital-ads-planner (if marketing)
  → leadup-human-content-editor (captions / alt-text polish)
```

**Cross-pack hand-offs:** Growth Marketing Pack for campaign use;
Development Pack for in-product asset wiring.

## 11. API and Resource Research Pack

**Purpose:** find + vet APIs, open-source repos, tools, MCP servers.

**Default sequence:**

```
leadup-public-api-finder (free / public APIs)
  → leadup-api-research-builder (auth, limits, pricing, webhooks)
  → leadup-github-repo-researcher (open-source candidates)
  → leadup-growth-research-agent (if cross-cutting growth research)
  → leadup-mcp-tool-orchestrator (for tool discovery)
```

**Cross-pack hand-offs:** Automation Pack when chosen API becomes part
of an n8n / WhatsApp workflow; SaaS / Product Pack when chosen API
becomes part of an MVP.

## Pack selection rules of thumb

- Use one **primary pack** per request.
- Skill chains across packs are normal — but cap at **5–7 skills**.
- Always end public-facing work with `leadup-human-content-editor`.
- Always end shipping work with `leadup-deploy-checker` +
  `leadup-release-manager` + `leadup-status-updater`.
- Always insert `leadup-pii-risk-reviewer` + `leadup-security-review`
  when payments / PII / regulated category is in scope.
