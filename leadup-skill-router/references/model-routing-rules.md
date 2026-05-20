# Model routing rules — LeadUp

How LeadUp picks the model for each step. Bias toward DeepSeek for low
risk (cheap, fast, plenty good for content + planning), Claude Sonnet
for medium-risk code, Claude Opus for the highest-risk work
(architecture, payments, auth, PII, complex repo cleanup).

## 1. Risk levels

| Risk | Typical work | Model |
|---|---|---|
| Low | docs, prompts, content, SEO planning, keyword ideas, status updates, simple analysis, calendars, blog drafts, proposal drafts, PII inventories (write-up only) | **DeepSeek** |
| Medium | UI changes, Docker fixes, API integration plans, admin-panel changes, normal feature code, n8n workflows, ads plans, CRO audits | **DeepSeek first, Claude Sonnet review if needed** |
| High | payments, webhooks, auth, PII-handling code, production deploy, DB migration, server recovery, large dirty-repo cleanup, architecture decisions, multi-tenant boundary work, security review write-ups for client | **Claude Sonnet (default) or Claude Opus** |

## 2. Heuristics (in order)

Apply top-down. Stop at the first match.

1. Touches **secrets / payments / auth / PII / DB migration** → High
   → Claude Sonnet or Opus.
2. **Production server / Coolify / `leadup-server` ops** → High →
   Claude Sonnet/Opus.
3. **New architecture decision** (multi-tenant model, queue choice,
   vendor lock-in) → High → Claude Sonnet/Opus.
4. **Dirty repo / large refactor / cross-cutting cleanup** → High →
   Claude Sonnet (Opus if context > 200k tokens).
5. **AI feature design / cost ledger / fallback** → Medium →
   Claude Sonnet for the design pass; DeepSeek for the doc write-up.
6. **API integration code / webhook handler** → Medium → DeepSeek
   first, Claude Sonnet review.
7. **Plain feature code / UI screen / admin form** → Medium →
   DeepSeek.
8. **SEO plan / keyword map / blog draft / proposal draft / calendar
   / status update** → Low → DeepSeek.
9. **Polishing public copy** → Low → DeepSeek (using
   `leadup-human-content-editor`).

## 3. Step-by-step in a chain

In a multi-skill chain, the model can change per step:

| Step | Model |
|---|---|
| `leadup-growth-research-agent` | DeepSeek |
| `leadup-seo-strategist` | DeepSeek |
| `leadup-keyword-competitor-researcher` | DeepSeek |
| `leadup-blog-content-writer` | DeepSeek |
| `leadup-smm-growth-planner` | DeepSeek |
| `leadup-content-calendar-builder` | DeepSeek |
| `leadup-digital-ads-planner` | DeepSeek (+ Sonnet review if budget is large) |
| `leadup-landing-page-cro-planner` | DeepSeek |
| `leadup-human-content-editor` | DeepSeek |
| `leadup-sales-proposal-builder` | DeepSeek |
| `leadup-pricing-package-planner` | DeepSeek |
| `leadup-lead-funnel-builder` | DeepSeek |
| `leadup-client-requirement-analyzer` | DeepSeek |
| `leadup-client-document-generator` | DeepSeek |
| `leadup-saas-mvp-planner` | DeepSeek (Sonnet for the tenant/architecture sub-section) |
| `leadup-feature-option-planner` | DeepSeek |
| `leadup-ai-feature-planner` | Claude Sonnet (cost ledger + fallback design) |
| `leadup-admin-panel-planner` | DeepSeek |
| `leadup-premium-ui-upgrader` | DeepSeek (Sonnet if the change is large) |
| `leadup-qa-test-case-generator` | DeepSeek |
| `leadup-browser-playwright-tester` | Claude Sonnet (real execution + flakiness debugging) |
| `leadup-deploy-checker` | Claude Sonnet |
| `leadup-release-manager` | Claude Sonnet |
| `leadup-security-review` | Claude Sonnet (Opus for complex audits) |
| `leadup-pii-risk-reviewer` | Claude Sonnet |
| `leadup-whatsapp-automation-planner` | DeepSeek (Sonnet if payments / regulated) |
| `leadup-n8n-workflow-builder` | DeepSeek (Sonnet for sensitive flows) |
| `leadup-api-research-builder` | DeepSeek (Sonnet for payment / auth APIs) |
| `leadup-public-api-finder` | DeepSeek |
| `leadup-github-repo-researcher` | DeepSeek |
| `leadup-mcp-tool-orchestrator` | DeepSeek (Sonnet when escalating to write/exec tools) |
| `leadup-free-creative-assets-finder` | DeepSeek |
| `leadup-super-prompt-builder` | DeepSeek |
| `leadup-status-updater` | DeepSeek |
| `leadup-project-kickoff` | Claude Sonnet (architecture + DB plan) |
| `leadup-existing-repo-analyzer` | Claude Sonnet |

## 4. Tie-breakers

- **Time pressure** is not a reason to downgrade. Auth / payment work
  stays on Sonnet / Opus even on a deadline.
- **Budget pressure** is not a reason to upgrade to Opus for low-risk
  content. DeepSeek is fine.
- **Large context** (long client transcripts, big repo) pushes toward
  Claude Opus (1M context) — but only if the request actually needs
  it.

## 5. Output line in the router report

For each step, write one line:

> `leadup-seo-strategist` — DeepSeek (low-risk planning) — no approval
> needed.

If the model is Sonnet / Opus, name the trigger:

> `leadup-security-review` — Claude Sonnet (touches payments + auth)
> — approval required before commit.
