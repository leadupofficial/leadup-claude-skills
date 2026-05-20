# Changelog — LeadUp Claude Skills Pack

All notable changes to this pack are documented here.
Format based on Keep a Changelog; this pack uses date-based releases.

## [Unreleased]

### Added
- New skill **`leadup-skill-router`** (37th skill) — master router
  that takes any user request (rough idea, client message, task)
  and decides: intent category, which of 11 workflow packs applies,
  the ordered skill sequence (capped at 5–7), the model per step
  (DeepSeek for low risk, Claude Sonnet/Opus for high risk),
  research + tooling needs, the approval gate, and which memory
  files (`STATUS.md`, `DEPLOY.md`, `PROJECT.md`, `AGENTS.md`,
  `CHANGELOG.md`) must be updated. Outputs a 12-section report plus
  a ready-to-paste **super-prompt** for Claude Code / RuFlo /
  opencode. Reads `SKILL_REGISTRY.md` for the catalogue. Ships with
  5 references (`skill-routing-table.md`, `workflow-pack-map.md`,
  `model-routing-rules.md`, `safety-routing-rules.md`,
  `router-examples.md`) and 3 asset templates (`router-output`,
  `super-prompt-output`, `workflow-sequence`).
- New root-level **`SKILL_REGISTRY.md`** — single source of truth
  for every skill: name, category, risk level, use case, triggers,
  related skills. Lists 37 shipped skills and 2 planned skills
  (`leadup-multi-tenant-architect`, `leadup-backup-rollback-planner`)
  with their substitution rules.
- README updated: new "Router" section at the top of the skills
  catalogue.
- New skill **`leadup-public-api-finder`** (36th skill) — discovers,
  compares, and recommends free / public / third-party APIs for LeadUp
  projects using `public-apis/public-apis` (discovery only), official
  documentation (source of truth), provider pricing pages, GitHub
  examples, RapidAPI, ApyHub, and Postman public collections. Scores
  each candidate 1–5 on eight axes (fit, docs, pricing, reliability,
  auth, CORS, integration, commercial use), flags sub-3 axes as risks,
  and outputs a 15-section report with a best + backup pick, env
  placeholders, backend-vs-frontend placement decision, rate-limit and
  pricing notes, an implementation plan, a 3–5 fixture test plan, and a
  final `use now / prototype only / avoid` decision. Routes payments
  to `leadup-security-review`, WhatsApp to
  `leadup-whatsapp-automation-planner`, AI to
  `leadup-ai-feature-planner`, and PII to `leadup-pii-risk-reviewer`.
  Ships with 5 references (`public-api-discovery-framework.md`,
  `api-verification-checklist.md`, `api-scoring-framework.md`,
  `leadup-api-use-cases.md`, `public-apis-repo-notes.md`) and 4 asset
  templates (api-comparison, api-integration-plan, env-placeholders,
  api-test-plan). README renumbered: Development Pack now 11 skills.
- **Sales + SaaS + QA + Automation + Privacy expansion** (12 new skills,
  24th–35th) — adds the rest of LeadUp's working loop beyond build + grow.
  All follow the same 10-required-headings structure, ship their own
  `references/` + `assets/`, and route public copy through
  `leadup-human-content-editor` and sensitive scopes through
  `leadup-pii-risk-reviewer` / `leadup-security-review`:
  - **`leadup-sales-proposal-builder`** — client-ready proposals, scopes,
    quotes, retainers, AMC plans, follow-up messages. References:
    `proposal-framework.md`. Assets: `proposal.template.md`.
  - **`leadup-client-requirement-analyzer`** — convert messy client
    input into structured requirements + missing questions + next reply.
    References: `client-requirement-framework.md`. Assets:
    `client-requirements.template.md`.
  - **`leadup-pricing-package-planner`** — Basic / Standard / Premium
    tiers with honest exclusions, margin notes, GST handling.
    References: `pricing-package-framework.md`. Assets:
    `pricing-packages.template.md`.
  - **`leadup-lead-funnel-builder`** — end-to-end funnel design: traffic,
    LP, capture (form or WhatsApp), qualify, follow-up, automation,
    tracking. References: `lead-funnel-framework.md`. Assets:
    `lead-funnel.template.md`.
  - **`leadup-saas-mvp-planner`** — paid SaaS MVP plan with first paid
    feature, ≤ 6 modules, tenant model, integrations, weekly launch
    roadmap. References: `saas-mvp-framework.md`. Assets:
    `saas-mvp-roadmap.template.md`.
  - **`leadup-ai-feature-planner`** — one AI feature end-to-end with
    model + fallback, prompt design, cost ledger, privacy flow,
    non-AI fallback, logging redaction, golden + jailbreak test plan,
    gated rollout. References: `ai-feature-framework.md`. Assets:
    `ai-feature-plan.template.md`.
  - **`leadup-admin-panel-planner`** — navigation, modules, tables,
    filters, role + permission matrix, KPI cards with named queries,
    reports, empty/loading/error/no-permission states, audit log
    events, PII masking. References: `admin-panel-framework.md`.
    Assets: `admin-panel-plan.template.md`.
  - **`leadup-qa-test-case-generator`** — critical user flows, manual
    test cases, edge cases, mobile + a11y, admin + tenant isolation,
    Razorpay test-mode, Playwright spec outline, acceptance criteria.
    References: `qa-test-framework.md`. Assets:
    `qa-test-cases.template.md`.
  - **`leadup-release-manager`** — release summary, modules touched,
    migration safety + rollback, env diff, test status, risk register,
    client comms (internal / paying / public), Go/No-Go. References:
    `release-checklist.md`. Assets: `release-notes.template.md`.
  - **`leadup-whatsapp-automation-planner`** — Meta-policy-safe WhatsApp
    plan: category (Utility / Marketing / Auth / Service), opt-in
    handling, templates with typed placeholders, CRM fields, workflow
    steps, failure handling, India IT Rules + DPDP + ASCI notes.
    References: `whatsapp-automation-framework.md`. Assets:
    `whatsapp-automation.template.md`.
  - **`leadup-n8n-workflow-builder`** — n8n workflow with trigger,
    atomic nodes, credentials as placeholders, signature-verified
    webhooks, idempotency, retries + dead-letter, manual approval for
    sensitive actions, text workflow diagram. References:
    `n8n-workflow-framework.md`. Assets: `n8n-workflow.template.md`.
  - **`leadup-pii-risk-reviewer`** — PII inventory, data flow, risk
    scoring, masking + encryption + retention + DSR + consent +
    privacy-policy notes + developer checklist; aligned with India
    DPDP, IT Rules, GDPR. References: `pii-risk-framework.md`.
    Assets: `pii-risk-review.template.md`.
- README reorganised into eight packs: Development, Growth Marketing,
  Human Content, Sales and Client, SaaS / Product, QA / Release,
  Automation, Privacy / Compliance.
- New skill **`leadup-free-creative-assets-finder`** (23rd skill) — finds
  free or safe-to-use creative assets (photos, stock images, vectors,
  illustrations, icons, animated icons, Lottie, GIFs, stickers, 3D
  models, 3D icons, video clips, emojis, avatars, plus SFX/music when
  asked) for LeadUp websites, SaaS, admin panels, Flutter apps, social,
  ads, blogs, proposals, and client projects. Verifies licenses for
  commercial use, attribution, modification, redistribution, trademark
  use, model/property releases, and API/TOS terms before recommending.
  Outputs an 11-section asset plan (requirement summary, source
  categories, search keywords, scored candidate table, license notes,
  recommended format, implementation + performance notes, best pick,
  backups, risk register). Marks any unclear case "Needs license
  verification". Ships with 6 references
  (`free-asset-source-list.md`, `license-checklist.md`,
  `asset-format-guide.md`, `performance-optimization-guide.md`,
  `leadup-asset-use-cases.md`, `search-keyword-framework.md`) and 5
  asset templates (search brief, comparison table, license check,
  website asset plan, social asset plan).
- **Growth Skills Pack** (8 new skills, 15th–22nd) — turns the pack from a
  build-and-ship loop into a build + grow loop. Each skill follows the
  same 10-required-headings structure, ships with its own
  `references/` + `assets/`, and never invents metrics:
  - **`leadup-seo-strategist`** — technical + on-page audit, meta
    rewrites, schema, internal linking, content gaps, 30/60/90 roadmap.
    References: `seo-checklist.md`. Assets: `seo-audit.template.md`.
  - **`leadup-keyword-competitor-researcher`** — seed keywords,
    clusters, intent, priority, competitor pages, content gaps; volume /
    CPC / difficulty labelled verified / estimated / requires
    verification. References: `keyword-research-framework.md`,
    `competitor-analysis-framework.md`. Assets:
    `keyword-map.template.csv`.
  - **`leadup-blog-content-writer`** — SEO blog and service-page drafts
    with brief, outline, titles, meta, FAQ, internal links, and a
    human-style draft (no em dashes, no banned hype words). References:
    `blog-writing-framework.md`. Assets: `blog-brief.template.md`.
  - **`leadup-smm-growth-planner`** — 30-day social plan with pillars,
    reels ideas, hooks, captions, posting schedule, engagement plan,
    KPIs (in bands, never invented). References: `smm-framework.md`.
    Assets: `content-calendar.template.md`.
  - **`leadup-digital-ads-planner`** — paid plan covering Google, Meta,
    LinkedIn, YouTube with structure, budget split, copy variants,
    creative ideas, LP requirements, tracking checklist, and platform-
    policy risk notes. References: `digital-ads-framework.md`. Assets:
    `ad-plan.template.md`.
  - **`leadup-landing-page-cro-planner`** — above-the-fold, CTA, trust,
    form, offer, mobile, performance, A/B test plan, and a 25+ item
    conversion checklist. References: `cro-framework.md`. Assets:
    `cro-audit.template.md`.
  - **`leadup-feature-option-planner`** — must-have / premium / AI
    feature buckets, user roles, MVP / Phase 2 / Phase 3 phasing, and
    exactly one recommended next feature. References:
    `feature-planning-framework.md`. Assets:
    `feature-roadmap.template.md`.
  - **`leadup-growth-research-agent`** — orchestrator: classifies a
    growth request, picks the right Growth Pack skill, runs the
    cross-cutting research (cited sources + access dates), and
    recommends one next action. References:
    `growth-research-source-list.md`. Assets:
    `growth-research-report.template.md`.
- New skill **`leadup-human-content-editor`** (14th skill) — converts
  AI-generated or AI-looking text into natural, human, client-ready copy
  for LeadUp websites, SaaS, app UI, proposals, and social content. Covers
  9 rewrite modes (landing, SaaS feature, About, service, microcopy,
  proposal, social, WhatsApp/email, technical). Strips em dashes and the
  banned hype-word list (seamless, empower, unlock, robust, cutting-edge,
  …), preserves meaning, SEO keywords, and structure, and flags
  unverifiable claims. Ships with 4 references
  (`human-writing-rules.md`, `ai-style-warning-signs.md`,
  `leadup-copy-tone.md`, `rewrite-examples.md`) and 3 asset templates
  (website, SaaS, microcopy).
- New skill **`leadup-super-prompt-builder`** (13th skill) — converts a
  rough idea / instruction / broken-English task into a copy-paste-ready
  structured prompt for Claude Code, opencode, RuFlo, or ChatGPT, covering
  12 prompt types. Includes master references `prompt-frameworks.md` and
  `leadup-prompt-templates.md` (synced into the skill) and 4 prompt asset
  templates (Claude Code, RuFlo, API research, new project).
- `CONTRIBUTING.md` — contribution rules, repo/sync model, skill
  requirements, and commit conventions for the public repo.

## [0.1.0] - 2026-05-19

First public release. Published at
https://github.com/leadupofficial/leadup-claude-skills

### Changed
- Skills are now **fully self-contained**: each skill bundles its own
  `references/` subfolder with only the reference files it links. SKILL.md
  links rewritten from `../references/...` to local `references/...` so a
  single skill folder works standalone in `~/.claude/skills/`.
- Repo-root `references/` is now the explicit master/source; per-skill copies
  are synced from it (no unused references duplicated into skills).
- Renamed `leadup-project-kickoff/assets/README.md` →
  `README.template.md` to avoid any confusion with the "no README.md inside a
  skill folder" rule.
- Added `scripts/sync_references.py` to propagate master references to the
  skills that link them (supports `--check` and `--prune`).

### Added
- Initial pack of 12 skills:
  - leadup-project-kickoff
  - leadup-existing-repo-analyzer
  - leadup-api-research-builder
  - leadup-github-repo-researcher
  - leadup-mcp-tool-orchestrator
  - leadup-browser-playwright-tester
  - leadup-deploy-checker
  - leadup-security-review
  - leadup-premium-ui-upgrader
  - leadup-status-updater
  - leadup-content-calendar-builder
  - leadup-client-document-generator
- Shared `references/`: leadup-workflow, security-rules, deploy-checklist,
  api-research-template, github-research-template, mcp-tool-policy,
  playwright-test-flows, premium-ui-checklist, status-template,
  project-docs-template.
- Per-skill assets/scripts: project-kickoff doc templates, status template,
  content-calendar template, client-document templates, Playwright example
  spec, `scan_secrets.py` (read-only), `detect_stack.py` (read-only).
- Pack tooling: `check_skill_structure.py`, `validate_frontmatter.py`,
  `list_skills.py`, `check_all_skills.py`, `package_skills.sh`,
  `package_all_skills.sh`.
- Root docs: README, INSTALL, TESTING, LICENSE (MIT), .gitignore.
- "About LeadUp" section in README with company website https://leadup.in.

### Security
- All `.env.example` use `__SET_ME__` placeholders only.
- No skill pushes, deploys, or runs remote commands without approval.
- Skills never read/print real `.env` values or API keys.
- `ruvector.db`, `.env`, `__pycache__`, `dist/` git-ignored; secret scan
  clean before publish.
