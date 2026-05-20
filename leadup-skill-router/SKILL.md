---
name: leadup-skill-router
description: Master router for the LeadUp Claude Skills Pack. Takes any user request, rough idea, client message, project task, website need, SaaS idea, marketing requirement, API question, SEO/SMM task, deployment task, security task, or content task; classifies intent, picks one of 11 workflow packs, picks an ordered skill sequence, picks the right model (DeepSeek for low risk, Claude Sonnet/Opus for high risk), flags research and tooling needs, sets the approval gate, and outputs a ready-to-paste super-prompt for Claude Code, RuFlo, or opencode. Use when the user says "which skill should I use", "use router", "route this task", "analyze my request", "what workflow needed", "choose best skill", "understand this task", "convert this into workflow", "which LeadUp skill", "auto select skill", "master router", "skill router", "workflow router", "decide skill pack", or "rough idea to workflow".
---

# LeadUp Skill Router

## Purpose

Take any inbound request (user task, client message, sales-call notes,
WhatsApp thread, half-finished spec) and decide:

1. The **intent category** (development / growth / sales / SaaS / QA /
   automation / security / creative / research / content / new project).
2. The **workflow pack** (one of 11).
3. The **ordered skill sequence** to ship the work.
4. The **model** to run it on (DeepSeek for low risk, Claude
   Sonnet/Opus for high risk).
5. Whether **internet / browser / MCP / project files** are needed.
6. The **risk level** and whether **approval** is required.
7. Which **memory files** (`STATUS.md`, `DEPLOY.md`, `PROJECT.md`,
   `AGENTS.md`) the next session must update.
8. A **copy-paste super-prompt** the user can hand to Claude Code,
   RuFlo, or opencode.

This skill is an **orchestrator**, not a worker. It does not do the
underlying SEO audit, code change, or proposal itself.

## When to use

Use when the user is unsure which skill applies, or when the request
spans multiple skills.

Trigger phrases: "which skill should I use", "use router", "route this
task", "analyze my request", "what workflow needed", "choose best
skill", "understand this task", "convert this into workflow", "which
LeadUp skill", "auto select skill", "master router", "skill router",
"workflow router", "decide skill pack", "rough idea to workflow".

Do **not** trigger when the user names a skill directly ("use
`leadup-seo-strategist`") or when the request maps cleanly to one
skill the user already knows (let that skill run).

## Inputs needed

- The request, in whatever shape the user has it (paragraph, bullets,
  WhatsApp thread, voice-note transcript, link).
- Project context if known (Hostendor / LeadUp site / Jewellery SaaS /
  Salon SaaS / INET CRM / Trivasia / Security suite / other).
- Audience and market hint (India / global / both) if relevant.
- Constraints (deadline, budget, regulated category, do-not-deploy).
- Whether the user wants planning only or planning + execution.

Ask at most 2 clarifying questions, only if the intent is genuinely
ambiguous (e.g. "fix it" with no target).

## Intent classification workflow

Classify the request into one of 11 categories. Use the dominant verb
+ object pair:

| Category | Cues |
|---|---|
| New project | "start", "kick off", "build new", "from scratch" |
| Development | "fix", "refactor", "add feature", "implement", "debug" |
| Growth marketing | "SEO", "rank", "ads", "social", "keywords", "CRO" |
| Human content | "rewrite", "make this human", "polish copy", "proposal text" |
| Sales & client | "proposal", "quote", "client message", "pricing", "scope" |
| SaaS / product | "MVP", "feature roadmap", "AI feature", "admin panel" |
| QA / release | "test", "Playwright", "release notes", "go live" |
| Automation | "WhatsApp", "n8n", "workflow", "automate" |
| Security & compliance | "secrets", "PII", "auth", "payment", "DPDP", "GDPR" |
| Creative assets | "free image", "icon", "Lottie", "GIF", "3D", "video" |
| API / resource research | "find API", "public-apis", "RapidAPI", "compare APIs", "GitHub repos for X" |

If the request spans two categories (very common: e.g. "SEO + blog +
human polish"), pick the **primary** category for the pack and add the
other category's skills into the **sequence**.

Full cue list: `references/skill-routing-table.md`.

## Skill pack routing table

11 packs, each with a default skill order. Pick the pack, then trim or
extend the sequence to fit the request.

| # | Pack | Default skills (in order) |
|---|---|---|
| 1 | Development Pack | `leadup-existing-repo-analyzer` → `leadup-status-updater` → (work) → `leadup-qa-test-case-generator` → `leadup-browser-playwright-tester` → `leadup-deploy-checker` → `leadup-release-manager` |
| 2 | New Project Pack | `leadup-super-prompt-builder` → `leadup-project-kickoff` → `leadup-saas-mvp-planner` → `leadup-feature-option-planner` → `leadup-admin-panel-planner` → (`leadup-ai-feature-planner` if needed) → `leadup-deploy-checker` → `leadup-security-review` |
| 3 | Growth Marketing Pack | `leadup-growth-research-agent` → `leadup-seo-strategist` → `leadup-keyword-competitor-researcher` → `leadup-blog-content-writer` → `leadup-smm-growth-planner` → `leadup-digital-ads-planner` → `leadup-landing-page-cro-planner` → `leadup-human-content-editor` |
| 4 | Human Content Pack | `leadup-human-content-editor` (default); add `leadup-blog-content-writer` / `leadup-client-document-generator` / `leadup-content-calendar-builder` when the source is a draft from one of those flows |
| 5 | Sales and Client Pack | `leadup-client-requirement-analyzer` → `leadup-pricing-package-planner` → `leadup-sales-proposal-builder` → `leadup-lead-funnel-builder` → `leadup-client-document-generator` → `leadup-human-content-editor` |
| 6 | SaaS / Product Pack | `leadup-saas-mvp-planner` → `leadup-feature-option-planner` → `leadup-ai-feature-planner` → `leadup-admin-panel-planner` → `leadup-security-review` (`leadup-multi-tenant-architect` is *planned*; use `leadup-saas-mvp-planner` tenant section until shipped) |
| 7 | QA / Release Pack | `leadup-qa-test-case-generator` → `leadup-browser-playwright-tester` → `leadup-deploy-checker` → `leadup-release-manager` (`leadup-backup-rollback-planner` is *planned*; use `leadup-release-manager` rollback section until shipped) |
| 8 | Automation Pack | `leadup-mcp-tool-orchestrator` → `leadup-public-api-finder` → `leadup-api-research-builder` → `leadup-whatsapp-automation-planner` → `leadup-n8n-workflow-builder` |
| 9 | Security and Compliance Pack | `leadup-security-review` → `leadup-pii-risk-reviewer` → `leadup-deploy-checker` → `leadup-release-manager` |
| 10 | Creative Assets Pack | `leadup-free-creative-assets-finder` → `leadup-premium-ui-upgrader` (UI use) OR `leadup-smm-growth-planner` / `leadup-digital-ads-planner` (marketing use) → `leadup-human-content-editor` |
| 11 | API and Resource Research Pack | `leadup-public-api-finder` → `leadup-api-research-builder` → `leadup-github-repo-researcher` → `leadup-growth-research-agent` → `leadup-mcp-tool-orchestrator` |

Full mapping with cross-pack hand-offs: `references/workflow-pack-map.md`.

## Skill sequence planner

1. **Restate** the request in one line.
2. **Pick** the primary pack.
3. **Trim** the default sequence to the steps that actually apply.
4. **Append** cross-pack skills when needed:
   - Anything public-facing → end with `leadup-human-content-editor`.
   - Anything touching production / DB / payments → end with
     `leadup-security-review` + `leadup-deploy-checker` +
     `leadup-release-manager`.
   - Anything new → start with
     `leadup-super-prompt-builder` and/or
     `leadup-project-kickoff` / `leadup-existing-repo-analyzer`.
   - Anything that needs external research → insert
     `leadup-mcp-tool-orchestrator` early.
   - Anything touching PII / regulated → insert
     `leadup-pii-risk-reviewer` before code.
5. **Cap** the sequence at 5–7 skills; longer chains lose focus.
6. **Mark** which skills are **planning only** vs **execution** so the
   approval gate is clear.

Sequence shape: `assets/workflow-sequence.template.md`.

## Model routing rules

- **LOW RISK → DeepSeek**: docs, prompts, content, SEO planning,
  keyword ideas, status update, simple analysis, social calendar,
  blog draft, proposal draft, PII inventory write-up.
- **MEDIUM RISK → DeepSeek first, Claude Sonnet review if needed**:
  UI changes, Docker fixes, API planning, admin-panel changes, normal
  feature code, n8n workflow design, ads plan, CRO audit.
- **HIGH RISK → Claude Sonnet or Opus only**: payments, webhooks,
  authentication, PII handling code, production deploy, DB migration,
  server recovery, large dirty-repo cleanup, architecture decisions,
  multi-tenant boundary work, security review write-ups.

Tie-breakers and example mapping: `references/model-routing-rules.md`.

## Step-by-step workflow

1. **Restate** the request in one line; note project + audience +
   constraints.
2. **Classify** intent into one of 11 categories (Intent classification
   workflow).
3. **Pick** the workflow pack (Skill pack routing table).
4. **Plan** the ordered skill sequence (Skill sequence planner).
5. **Choose** the model per step (Model routing rules).
6. **List** files / resources the next session must read
   (`STATUS.md`, `DEPLOY.md`, `PROJECT.md`, `AGENTS.md`, repo paths,
   client docs).
7. **Decide** research + tools needed (browser / MCP / search /
   Playwright / Docker).
8. **Set** the approval gate (planning OK without approval; commit,
   push, deploy, migrate, refund, send to client → approval required).
9. **Name** memory updates owed at the end (which `STATUS.md` etc.).
10. **Output** the router report **and** a copy-paste super-prompt.

## Required output format

One Markdown report with these sections, in this order. The
super-prompt is a separate fenced code block at the end.

1. **Request understanding** — one paragraph restating the user's
   request in plain English.
2. **Intent category** — single line: one of the 11 categories.
3. **Workflow pack selected** — pack number and name.
4. **Skill sequence** — ordered list of 1–7 LeadUp skills, each with a
   one-line job ("`leadup-seo-strategist` — audit + 30/60/90 plan").
5. **Recommended model / tool** — model per skill step (DeepSeek /
   Claude Sonnet / Claude Opus) with a one-line reason.
6. **Risk level** — Low / Medium / High with one-line reason.
7. **Files / resources to read** — `STATUS.md`, `DEPLOY.md`,
   `PROJECT.md`, `AGENTS.md`, specific repo paths, public links.
8. **Research / tools needed** — browser, MCP server, Search Console,
   Lighthouse, Razorpay docs, public-apis, etc.; each marked
   **available** or **requires verification**.
9. **Approval needed?** — yes/no per step; reason in one line. Default
   approval-required for commit / push / deploy / migration / refund /
   external send.
10. **Memory updates owed** — list of files the next session must
    update at the end (`STATUS.md`, `DEPLOY.md`, `PROJECT.md`,
    `AGENTS.md`, `CHANGELOG.md`).
11. **Execution plan** — short numbered list the user will hand to the
    next agent.
12. **Super-prompt (copy-paste)** — a single fenced code block
    containing the full prompt for Claude Code / RuFlo / opencode,
    pre-loaded with project context, the skill sequence, the safety
    + approval rules, and the expected output format. Built on the
    `assets/super-prompt-output.template.md` shape.

Templates: `assets/router-output.template.md`,
`assets/super-prompt-output.template.md`,
`assets/workflow-sequence.template.md`.

## Safety rules

- **Never commit / push / deploy / migrate / refund / send to client**
  without explicit user approval. The router only **plans**; the
  worker step asks for approval at its own gate.
- **Never read or print real `.env` values, API keys, tokens, secrets,
  card data, Aadhaar, or other PII** in the router output. Use
  `__SET_ME__` placeholders and "redacted" markers only.
- **Never ask the user to paste secrets.** Reference env names only.
- **High-risk routes (payments, security, PII, DB migration, prod
  deploy)** → force Claude Sonnet/Opus + add `leadup-security-review`
  / `leadup-pii-risk-reviewer` to the sequence + insert an approval
  gate before code.
- **Browser / Playwright / MCP usage** → route through
  `leadup-mcp-tool-orchestrator` (discover read-only first, escalate
  with approval).
- **Public-facing copy** → always end with `leadup-human-content-editor`
  before publishing.
- **Regulated industries** (clinic / finance / kids / real estate /
  alcohol / gambling) → require `leadup-pii-risk-reviewer` +
  legal/compliance flag in the report.
- **Planned-but-not-yet-built skills**
  (`leadup-multi-tenant-architect`, `leadup-backup-rollback-planner`)
  → substitute the closest shipped skill and mark the gap in the
  report.

Full rule set: `references/safety-routing-rules.md`.

## Common mistakes

- Treating the router as a worker — doing the SEO audit / writing the
  code itself.
- Producing a 12-skill chain — users can't run that. Cap at 5–7.
- Forgetting `leadup-human-content-editor` on public-facing copy.
- Skipping `leadup-security-review` / `leadup-pii-risk-reviewer` on
  PII / payments / regulated work.
- Picking Claude Opus for low-risk content tasks (cost without need).
- Picking DeepSeek for payment / auth / DB migration work (risk).
- No approval gate on commit / push / deploy / migrate steps.
- Output without a copy-paste super-prompt at the end.
- Ignoring memory updates (`STATUS.md` etc.).

## Troubleshooting

- **Ambiguous request**: ask up to 2 clarifying questions; if still
  unclear, pick the safest pack and flag the assumption.
- **Multi-intent request**: pick primary pack; append cross-pack skills
  to sequence; cap at 7.
- **User wants execution, not planning**: still produce the router
  report **and** the super-prompt; tell the user the next agent must
  ask for approval at sensitive steps.
- **High-risk + tight deadline**: do not downgrade the model. Time
  pressure is not a reason to use DeepSeek on auth/payment code.
- **No project context**: write the report with placeholders; ask the
  user to fill before kicking off the worker.
- **Skill referenced is "planned"**: substitute the closest existing
  skill and call out the gap in the "Skill sequence" section.
- **Request references a non-LeadUp tool**: still route through the
  closest LeadUp skill (`leadup-mcp-tool-orchestrator` for tool
  discovery, `leadup-api-research-builder` for vendor API, etc.).

## Test prompts

### Should trigger (5)
1. "Which LeadUp skill should I use for this client message?"
2. "Route this task: 'Create SEO plan and blog content for Hostendor'."
3. "Auto select skill — we need to add WhatsApp reminders to our salon SaaS."
4. "Master router: client wants a free maps API for a Flutter app."
5. "Convert this rough idea into a workflow — 'make our landing page convert better'."

### Should NOT trigger (3)
1. "Use `leadup-seo-strategist` to audit our site." (direct skill call → run that skill)
2. "Write the actual blog post now." (→ `leadup-blog-content-writer`)
3. "Just polish this copy." (→ `leadup-human-content-editor`)

### Functional test cases (2)
1. Given "Create SEO plan and blog content for Hostendor" with no
   regulated category and no PII, return a Growth Marketing Pack
   route with 4–5 skills (`leadup-growth-research-agent` →
   `leadup-seo-strategist` → `leadup-keyword-competitor-researcher`
   → `leadup-blog-content-writer` → `leadup-human-content-editor`),
   DeepSeek for planning/content + optional Claude Sonnet review, no
   approval needed for planning, approval needed before any website
   code changes, memory updates to `STATUS.md`, and a copy-paste
   super-prompt.
2. Given "Add Razorpay refund flow to our jewellery SaaS prod", return
   a High-risk route with Claude Sonnet/Opus only, mandatory
   `leadup-security-review` + `leadup-pii-risk-reviewer` early,
   approval gates before commit / push / deploy / refund test, full
   QA + release pack at the tail (`leadup-qa-test-case-generator` →
   `leadup-deploy-checker` → `leadup-release-manager`), and memory
   updates to `STATUS.md` + `DEPLOY.md`.

## Success criteria

- All 12 output sections present in order.
- Skill sequence is 1–7 ordered LeadUp skills, each existing or
  flagged as **planned**.
- Model per step matches risk level (no DeepSeek on auth / payments /
  PII / migration).
- Public-facing copy ends with `leadup-human-content-editor`.
- PII / payments / regulated routes include `leadup-security-review`
  and `leadup-pii-risk-reviewer`.
- Approval gate explicit per step (planning vs commit / push / deploy
  / migrate / send).
- Memory updates named (`STATUS.md`, `DEPLOY.md`, etc.).
- Final fenced code block is a copy-paste super-prompt that loads the
  next agent with project context, sequence, safety + approval rules,
  and expected output.
- No real secrets, PII, or live keys anywhere in the output.
