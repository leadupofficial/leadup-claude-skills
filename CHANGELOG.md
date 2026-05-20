# Changelog — LeadUp Claude Skills Pack

All notable changes to this pack are documented here.
Format based on Keep a Changelog; this pack uses date-based releases.

## [Unreleased]

### Added
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
