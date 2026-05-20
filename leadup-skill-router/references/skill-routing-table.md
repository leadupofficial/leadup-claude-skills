# Skill routing table — LeadUp

How requests map to LeadUp skills. Read top-down: cue → primary skill →
cross-pack skills to append.

## 1. Cue → primary skill (1-to-1 mapping)

| Cue (in user request) | Primary skill |
|---|---|
| "audit our SEO" / "improve search ranking" | `leadup-seo-strategist` |
| "find keywords" / "competitor research" | `leadup-keyword-competitor-researcher` |
| "write blog" / "service page draft" | `leadup-blog-content-writer` |
| "social media plan" / "Instagram strategy" | `leadup-smm-growth-planner` |
| "content calendar" | `leadup-content-calendar-builder` |
| "Google Ads" / "Meta Ads" / "ad plan" | `leadup-digital-ads-planner` |
| "increase conversion" / "landing page audit" | `leadup-landing-page-cro-planner` |
| "growth research" / "what should we do for growth" | `leadup-growth-research-agent` |
| "free image" / "icon" / "Lottie" / "GIF" | `leadup-free-creative-assets-finder` |
| "make this human" / "remove em dash" / "polish copy" | `leadup-human-content-editor` |
| "proposal" / "quote" / "AMC" / "project scope" | `leadup-sales-proposal-builder` |
| "client message" / "WhatsApp thread" / "convert to scope" | `leadup-client-requirement-analyzer` |
| "pricing tiers" / "Basic/Standard/Premium" | `leadup-pricing-package-planner` |
| "lead funnel" / "increase leads" | `leadup-lead-funnel-builder` |
| "client document" / "report" / "dev handoff doc" | `leadup-client-document-generator` |
| "saas mvp" / "paid mvp" | `leadup-saas-mvp-planner` |
| "feature roadmap" / "next feature" | `leadup-feature-option-planner` |
| "AI feature" / "AI chatbot" / "make app intelligent" | `leadup-ai-feature-planner` |
| "admin panel" / "dashboard" / "super admin" | `leadup-admin-panel-planner` |
| "premium UI" / "world-class SaaS look" | `leadup-premium-ui-upgrader` |
| "test cases" / "QA plan" / "Playwright tests" | `leadup-qa-test-case-generator` |
| "run app" / "Playwright run" / "E2E test" | `leadup-browser-playwright-tester` |
| "release notes" / "go live" | `leadup-release-manager` |
| "deploy ready" / "Coolify deploy" / "READY/NOT READY" | `leadup-deploy-checker` |
| "WhatsApp automation" / "reminders" / "BSP" | `leadup-whatsapp-automation-planner` |
| "n8n workflow" / "automation graph" | `leadup-n8n-workflow-builder` |
| "find API" / "free API" / "compare APIs" / "public-apis" | `leadup-public-api-finder` |
| "research the API" / "auth limits pricing webhooks" | `leadup-api-research-builder` |
| "open-source repo for X" / "vet this GitHub repo" | `leadup-github-repo-researcher` |
| "MCP tool" / "which tools available" / "browser tools" | `leadup-mcp-tool-orchestrator` |
| "security review" / "check secrets" / "payment security" | `leadup-security-review` |
| "PII review" / "DPDP" / "GDPR" / "privacy risk" | `leadup-pii-risk-reviewer` |
| "analyze repo" / "where did we leave off" | `leadup-existing-repo-analyzer` |
| "start new project" / "kickoff" | `leadup-project-kickoff` |
| "make super prompt" / "convert idea to prompt" | `leadup-super-prompt-builder` |
| "update STATUS.md" / "what next" / "TODO" | `leadup-status-updater` |

## 2. Default cross-pack add-ons (auto-append rules)

When the primary pick is set, append these skills automatically:

| If primary is… | Append at the end |
|---|---|
| Anything producing **public-facing copy** | `leadup-human-content-editor` |
| Anything touching **PII** / regulated industry | `leadup-pii-risk-reviewer` |
| Anything touching **payments / auth / secrets** | `leadup-security-review` |
| Anything that **builds new code** | `leadup-qa-test-case-generator` + `leadup-deploy-checker` + `leadup-release-manager` |
| Anything that **uses external tools / APIs** | `leadup-mcp-tool-orchestrator` (early) + `leadup-api-research-builder` (mid) |
| Anything in a **new project** | start with `leadup-super-prompt-builder` + `leadup-project-kickoff` |
| Anything in an **existing project** | start with `leadup-existing-repo-analyzer` + `leadup-status-updater` |

## 3. Multi-intent requests

For multi-intent (very common in LeadUp):

- **Marketing + content**: `leadup-growth-research-agent` →
  `leadup-seo-strategist` → `leadup-keyword-competitor-researcher` →
  `leadup-blog-content-writer` → `leadup-human-content-editor`.
- **Sales + content**: `leadup-client-requirement-analyzer` →
  `leadup-sales-proposal-builder` → `leadup-human-content-editor`.
- **SaaS + payments + WhatsApp**: `leadup-saas-mvp-planner` →
  `leadup-public-api-finder` → `leadup-api-research-builder` →
  `leadup-whatsapp-automation-planner` →
  `leadup-pii-risk-reviewer` → `leadup-security-review`.
- **Existing app + new feature + deploy**:
  `leadup-existing-repo-analyzer` → `leadup-feature-option-planner` →
  `leadup-qa-test-case-generator` →
  `leadup-browser-playwright-tester` → `leadup-deploy-checker` →
  `leadup-release-manager`.

## 4. Vague requests — first response template

When the request is one line and vague (e.g. "fix it", "grow our
business"):

> "Got it. I'll route this. Two quick questions:
> 1. [Most useful clarifier]
> 2. [Second clarifier]
> If I don't hear back, I'll assume [safe default] and pick the
> safest pack with planning only."

Then proceed with safe defaults if no answer.

## 5. When the request mentions a non-LeadUp tool

If the user names a tool LeadUp doesn't own (Figma, Razorpay,
Cloudflare, Notion, etc.):

- Route the *task* through LeadUp skills.
- Route the *tool research* through `leadup-mcp-tool-orchestrator`
  (discovery) and `leadup-api-research-builder` (deeper API work).

Never let the router try to do the tool's own work.

## 6. Direct skill call

If the user names a LeadUp skill explicitly ("use
`leadup-seo-strategist`"), do **not** trigger the router. Let that
skill run. The router is for ambiguous / multi-skill / multi-pack
requests.
