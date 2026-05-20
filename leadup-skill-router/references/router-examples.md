# Router examples — LeadUp

Worked examples showing what a router run looks like for common
LeadUp requests. These are illustrative — actual chains and models
adapt to project context, but the shape is repeatable.

## Example 1 — Growth: SEO + blog for Hostendor

**Request:** "Create SEO plan and blog content for Hostendor."

**Router result:**

- **Intent:** Growth marketing.
- **Pack:** Growth Marketing Pack.
- **Skills (5):**
  1. `leadup-growth-research-agent` — classify + cite sources.
  2. `leadup-seo-strategist` — audit + 30/60/90 plan.
  3. `leadup-keyword-competitor-researcher` — keyword map + 3
     competitors.
  4. `leadup-blog-content-writer` — 3 pillar drafts.
  5. `leadup-human-content-editor` — final polish.
- **Model per step:** DeepSeek for all five.
- **Risk:** Low.
- **Tools:** web search, competitor sites, Search Console (if
  available); flagged **requires verification**.
- **Approval:** not needed for planning + drafts. Needed before
  any website code change or publishing.
- **Memory:** `STATUS.md` (growth track), `CHANGELOG.md` if a content
  release ships.

## Example 2 — Sales: messy WhatsApp thread from a clinic owner

**Request:** "Here's a WhatsApp thread from a salon owner — what do
they actually want?"

**Router result:**

- **Intent:** Sales & client.
- **Pack:** Sales and Client Pack.
- **Skills (4):**
  1. `leadup-client-requirement-analyzer` — extract goal +
     must-haves + missing questions.
  2. `leadup-pricing-package-planner` — if budget is ambiguous.
  3. `leadup-sales-proposal-builder` — generate the proposal.
  4. `leadup-human-content-editor` — polish before sending.
- **Model:** DeepSeek for all four.
- **Risk:** Low.
- **Approval:** required before sending the proposal to the client.
- **Memory:** none until project starts (then New Project Pack).

## Example 3 — High-risk: Razorpay refund flow on jewellery SaaS

**Request:** "Add Razorpay refund flow to our jewellery SaaS prod."

**Router result:**

- **Intent:** Development + Security.
- **Pack:** Development Pack with mandatory Security & Compliance
  tail.
- **Skills (6):**
  1. `leadup-existing-repo-analyzer` — recover state.
  2. `leadup-api-research-builder` — refund API + webhook signature.
  3. `leadup-security-review` — payment & secret handling.
  4. `leadup-pii-risk-reviewer` — customer + invoice PII.
  5. `leadup-qa-test-case-generator` — refund test cases + tenant
     isolation.
  6. `leadup-deploy-checker` → `leadup-release-manager` →
     `leadup-status-updater` (close out).
- **Model:** Claude Sonnet (Opus only if context is huge). DeepSeek
  blocked for this chain.
- **Risk:** High.
- **Tools:** browser/Playwright for Razorpay test mode; MCP discovery
  if available.
- **Approval:** required before commit, push, deploy, and refund
  testing.
- **Memory:** `STATUS.md`, `DEPLOY.md` (env + migration if any),
  `CHANGELOG.md`, `SECURITY.md` if a sensitive change.

## Example 4 — New SaaS kickoff: salon booking in tier-2 India

**Request:** "Start a new salon-booking SaaS for tier-2 Indian cities,
team of 2, launch in 8 weeks."

**Router result:**

- **Intent:** New project.
- **Pack:** New Project Pack.
- **Skills (6):**
  1. `leadup-super-prompt-builder` — sharpen brief.
  2. `leadup-project-kickoff` — bootstrap CLAUDE / STATUS / DEPLOY /
     SECURITY / `.env.example`.
  3. `leadup-saas-mvp-planner` — MVP modules + tenant model.
  4. `leadup-admin-panel-planner` — back office.
  5. `leadup-pii-risk-reviewer` — customer data plan.
  6. `leadup-deploy-checker` + `leadup-security-review` at first
     ship.
- **Model:** DeepSeek for planning; Claude Sonnet for the tenant
  model + DB plan + initial admin code.
- **Risk:** Medium overall; High when touching payments / PII /
  multi-tenant boundary.
- **Tools:** MCP discovery; browser optional.
- **Approval:** required before first push, first deploy, payment
  KYC, BSP onboarding.
- **Memory:** `STATUS.md`, `PROJECT.md`, `DEPLOY.md`, `AGENTS.md`,
  `CHANGELOG.md`.

## Example 5 — API discovery: maps for Flutter web app

**Request:** "Master router: client wants a free maps API for a
Flutter app."

**Router result:**

- **Intent:** API / resource research.
- **Pack:** API and Resource Research Pack.
- **Skills (4):**
  1. `leadup-public-api-finder` — discover + score candidates.
  2. `leadup-api-research-builder` — deeper API + SDK depth.
  3. `leadup-github-repo-researcher` — Flutter map widgets (only if
     OSS reuse is on the table).
  4. `leadup-mcp-tool-orchestrator` — if browser MCP available for
     verification.
- **Model:** DeepSeek for all four.
- **Risk:** Low.
- **Approval:** not needed for planning. Needed when wiring keys into
  the app (use backend proxy for secret keys).
- **Memory:** `PROJECT.md` (vendor choice), `STATUS.md`.

## Example 6 — Automation: WhatsApp reminders for dental clinic

**Request:** "Plan WhatsApp appointment reminders for a dental clinic."

**Router result:**

- **Intent:** Automation + Privacy.
- **Pack:** Automation Pack with PII tail.
- **Skills (5):**
  1. `leadup-public-api-finder` — pick BSP / Cloud API option.
  2. `leadup-api-research-builder` — BSP API depth.
  3. `leadup-whatsapp-automation-planner` — opt-in + templates +
     flow.
  4. `leadup-n8n-workflow-builder` — automation graph.
  5. `leadup-pii-risk-reviewer` — patient data scope.
- **Model:** DeepSeek for planning; Claude Sonnet for the
  PII-touching code.
- **Risk:** Medium → High (regulated clinic + PII).
- **Tools:** browser for BSP onboarding flow if MCP available.
- **Approval:** required before sending any real WhatsApp message,
  before storing patient data, before BSP go-live.
- **Memory:** `STATUS.md`, `DEPLOY.md` (env), `SECURITY.md`.

## Example 7 — Vague: "fix our landing page"

**Request:** "Master router: make our landing page convert better."

**Router result:**

- **Clarify (max 2):** "Is this a planning pass or do you want code
  changes too?" / "Which page URL?"
- **If planning only:**
  - Pack: Growth Marketing Pack.
  - Skills: `leadup-landing-page-cro-planner` →
    `leadup-keyword-competitor-researcher` (only if SEO is part) →
    `leadup-human-content-editor`.
  - Model: DeepSeek.
  - Risk: Low.
- **If code changes:**
  - Pack: Development Pack with Growth Marketing tail.
  - Skills: `leadup-existing-repo-analyzer` →
    `leadup-landing-page-cro-planner` → (code work) →
    `leadup-qa-test-case-generator` → `leadup-deploy-checker` →
    `leadup-release-manager` → `leadup-human-content-editor` (any
    copy change) → `leadup-status-updater`.
  - Model: DeepSeek for content; Claude Sonnet for code; approval
    before push + deploy.

## Common shape across examples

- One **primary pack**.
- 3–7 ordered **skills**.
- A model per step.
- A risk verdict.
- Explicit **approval gates** at the dangerous steps.
- Named **memory updates** at the end.
- A copy-paste **super-prompt** as the last block of the report
  (built from `assets/super-prompt-output.template.md`).
