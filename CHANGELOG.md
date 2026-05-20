# Changelog — LeadUp Claude Skills Pack

All notable changes to this pack are documented here.
Format based on Keep a Changelog; this pack uses date-based releases.

## [Unreleased]

### Added
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
