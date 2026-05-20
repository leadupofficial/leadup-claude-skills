# LeadUp Claude Skills Pack

A pack of 22 Claude skills built around the real LeadUp Technologies
workflow: attach a source → analyze & research → plan → build → test in
Docker → push → deploy to Coolify/`leadup-server` → update project memory.
Split into a **Core Pack** (14 skills for the build-and-ship loop) and a
**Growth Pack** (8 skills for SEO, content, social, ads, CRO, features,
and growth research).

Each skill is a **fully self-contained** folder: a `SKILL.md` plus its own
`references/` subfolder bundling only the reference files it links. A single
skill folder can be dropped into `~/.claude/skills/` and works with no extra
files. The repo-root `references/` folder is the **master/source** of that
shared knowledge (workflow, security rules, checklists, templates); per-skill
copies are kept in sync from it via `scripts/sync_references.py`.

## What this pack is for

LeadUp runs many client websites, multi-tenant SaaS apps, Flutter apps, and
hosting tools in parallel, deployed under `*.leadup.in`. These skills encode
the repeatable parts of that work so any Claude session starts already knowing
the workflow, the safety rules, and the expected output format.

## Skills

### Core Pack (build-and-ship loop)

| # | Skill | Use it to… |
|---|---|---|
| 1 | `leadup-project-kickoff` | Bootstrap a new project (PROJECT/CLAUDE/STATUS/DEPLOY/SECURITY/README/.env.example, stack, DB plan, MVP, deploy plan) |
| 2 | `leadup-existing-repo-analyzer` | Recover an existing repo's state, stack, bugs, next task |
| 3 | `leadup-api-research-builder` | Research an API (docs, auth, limits, pricing, webhooks) before integrating |
| 4 | `leadup-github-repo-researcher` | Vet open-source repos (license, activity, copy/adapt/inspiration) |
| 5 | `leadup-mcp-tool-orchestrator` | Pick & sequence MCP/tools safely, read-only first |
| 6 | `leadup-browser-playwright-tester` | Run & E2E-test the app, write Playwright specs |
| 7 | `leadup-deploy-checker` | Produce a READY/NOT READY deploy verdict (never deploys) |
| 8 | `leadup-security-review` | Review secrets, auth, multi-tenant, payments, deploy risks |
| 9 | `leadup-premium-ui-upgrader` | Raise UI to premium international-SaaS standard |
| 10 | `leadup-status-updater` | Keep STATUS.md/TODO.md/CHANGELOG.md current |
| 11 | `leadup-content-calendar-builder` | Build a social content calendar & strategy |
| 12 | `leadup-client-document-generator` | Generate proposals, reports, dev/handoff docs, API emails |
| 13 | `leadup-super-prompt-builder` | Turn a rough idea/instruction into a copy-paste-ready structured prompt for Claude Code, opencode, RuFlo, or ChatGPT |
| 14 | `leadup-human-content-editor` | Rewrite AI-generated or AI-looking copy into natural, human, business-ready content for websites, SaaS, app UI, proposals, and social posts |

### Growth Pack (SEO, content, ads, social, CRO, features, research)

| # | Skill | Use it to… |
|---|---|---|
| 15 | `leadup-seo-strategist` | Audit a site and ship a 30/60/90 day SEO plan (technical + on-page + schema + content gaps) |
| 16 | `leadup-keyword-competitor-researcher` | Build a clustered keyword map + 3–5 competitor analysis with honest data labels |
| 17 | `leadup-blog-content-writer` | Draft SEO-aware blog or service-page content in LeadUp's human, em-dash-free voice |
| 18 | `leadup-smm-growth-planner` | Plan a 30-day social media growth strategy with pillars, reels, hooks, schedule, and KPIs |
| 19 | `leadup-digital-ads-planner` | Plan paid campaigns (Google, Meta, LinkedIn, YouTube) with structure, budget, copy, creative, tracking, and policy notes |
| 20 | `leadup-landing-page-cro-planner` | Audit a landing page and produce prioritized CRO fixes, A/B tests, and a conversion checklist |
| 21 | `leadup-feature-option-planner` | Plan must-have, premium, and AI-powered features with MVP / Phase 2 / Phase 3 phasing and one recommended next feature |
| 22 | `leadup-growth-research-agent` | Orchestrator: classify a growth request, pick the right LeadUp skill, run cross-cutting research, and recommend the next action |

## How it helps LeadUp work

- **No re-explaining the workflow** — every skill already follows the LeadUp
  loop and approval gates.
- **Consistent, resumable output** — STATUS/CLAUDE/DEPLOY memory keeps any
  session able to continue.
- **Safety by default** — no secret printing, no auto-push, no auto-deploy.

## Install in Claude.ai

1. In Claude.ai, open **Settings → Capabilities/Skills** (Skills feature).
2. Upload each skill folder (the folder containing `SKILL.md`), or upload a
   zip produced by `scripts/package_all_skills.sh` (run only after review).
3. Claude reads the `description` to decide when to trigger each skill.

## Use in Claude Code

- **Per-project:** copy the skill folders into `.claude/skills/` in a repo.
- **Global:** copy them into `~/.claude/skills/`.
- Then just talk normally — say a trigger phrase ("analyze this repo",
  "prepare deploy") and the matching skill activates.

See `INSTALL.md` for exact steps.

## Test trigger phrases

Each `SKILL.md` has a **Test prompts** section: 5 prompts that should trigger
it, 3 that should not, and 2 functional cases. `TESTING.md` explains how to
run the structure validator and how to manually test triggering/over-triggering.

## Update skills

1. Edit the relevant `SKILL.md` and/or the **master** repo-root `references/`.
2. `python3 scripts/sync_references.py` — propagate master → per-skill copies.
3. Bump `CHANGELOG.md`.
4. `python3 scripts/check_all_skills.py` — must pass.
5. Re-upload to Claude.ai / re-copy the skill folder to `~/.claude/skills/`.

Keep the 10 required section headings byte-stable; the validator greps them.

## How skills work with MCP / connectors

Skills do **not** hard-code MCP tool names (inventories change per session).
`leadup-mcp-tool-orchestrator` and `references/mcp-tool-policy.md` define the
pattern: discover available tools, prefer read-only, escalate to write/exec
only with a stated risk and explicit approval. No `.env`/secret/client data is
ever sent to an external tool.

## Security warnings

- Skills never read or print real `.env` values or API keys.
- `.env.example` files use `__SET_ME__` placeholders only.
- No skill pushes to GitHub, deploys, or runs remote SSH without explicit
  approval — they stop at a checklist/approval gate.
- `scripts/package_all_skills.sh` exists but is **not** run automatically;
  packaging/zipping/committing happens only on the user's approval.

## About LeadUp

Built and maintained by **LeadUp Technologies** — a web agency + SaaS shop
that builds client websites, multi-tenant SaaS products, Flutter apps, and
hosting tools, tested in Docker and deployed under `*.leadup.in`.

- 🌐 Website: **https://leadup.in**
- 🧑‍💻 GitHub: **https://github.com/leadupofficial**
- 📦 This pack: **https://github.com/leadupofficial/leadup-claude-skills**

These skills encode LeadUp's real working loop so any Claude session starts
already knowing the workflow, safety rules, and expected output format.

License: MIT (see `LICENSE`). © LeadUp Technologies — https://leadup.in
