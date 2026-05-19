---
name: leadup-super-prompt-builder
description: Turn a rough plain-language idea, short instruction, broken English, or vague task into a strong, copy-paste-ready structured prompt for Claude Code, opencode, RuFlo, ChatGPT, or another AI coding/research agent — using LeadUp's workflow, stack, and safety rules. Use when the user says "make super prompt", "convert to prompt", "improve my prompt", "prompt this properly", "make master prompt", "turn this idea into prompt", "write prompt for Claude Code", "write prompt for RuFlo", or "make this instruction better".
---

# LeadUp Super Prompt Builder

## Purpose

Convert a rough idea, one-liner, broken-English instruction, client
requirement, or a vague "do recommended" into a complete, structured,
copy-paste-ready prompt for the right AI agent (Claude Code, opencode, RuFlo,
ChatGPT, or similar) — already loaded with LeadUp context, the build→test→
deploy loop, and the safety rules.

## When to use

Use when the user wants a *prompt produced*, not the task itself done.

Trigger phrases: "make super prompt", "convert to prompt", "improve my
prompt", "prompt this properly", "make master prompt", "turn this idea into
prompt", "write prompt for Claude Code", "write prompt for RuFlo", "write
prompt for opencode", "make this instruction better", "rewrite this as a
proper prompt".

If the user actually wants the work done (build it, analyse it, research it),
route to the matching skill instead: `leadup-project-kickoff`,
`leadup-existing-repo-analyzer`, `leadup-api-research-builder`,
`leadup-deploy-checker`, etc. This skill only produces the prompt.

## Inputs needed

- The rough input (idea / instruction / requirement / "do recommended").
- Target agent: Claude Code, opencode, RuFlo, ChatGPT, or other (infer if
  not given — default Claude Code for build/fix, RuFlo for research/plan).
- Prompt type — one of the 12 below (infer from the input if not stated).
- Project + stack if known; any hard constraint (deadline, must-use stack).

Ask at most 3 clarifying questions, and only if the intent is genuinely
ambiguous (the user dislikes excessive questioning — infer sensibly).

## Step-by-step workflow

1. **Restate the real intent** in one line; confirm only if blocking.
2. **Pick the prompt type** (1–12) and **target agent**; infer if unstated.
3. **Pick the framework** from `references/prompt-frameworks.md` (core
   skeleton + agent variant).
4. **Fill the template** from `references/leadup-prompt-templates.md` or the
   matching file in `assets/`, injecting LeadUp context: stack, Docker →
   GitHub `leadupofficial` → Coolify → `*.leadup.in`, STATUS.md loop.
5. **Inject the LeadUp constraint block**: research+plan before code, test in
   Docker, no push/deploy without approval, no secrets / `__SET_ME__` only,
   premium international UI, update STATUS.md, definition of done.
6. **Output one copy-paste block** — just the prompt, no mixed commentary.
7. **Offer 2–3 one-line toggles** (shorter / stricter / add research / add
   tests) after the block.

## Required output format

- One line above the block: `Prompt type: <type> · Target: <agent>`.
- The prompt itself inside a single fenced code block, self-contained and
  ready to paste — no explanation interleaved.
- Optional 2–3 quick toggle suggestions *below* the block.
- Keep it simple and copy-paste friendly; no preamble inside the block.

## Prompt frameworks

Core skeleton (always): **Role → Context → Source → Task → Constraints →
Definition of done → Output expectation**. Agent variants: Claude Code/
opencode (agentic, approval gates, small steps), RuFlo (research/plan/
memory, plan before build), ChatGPT/generic (more explicit pasted context).
Full detail and the quality checklist are in
`references/prompt-frameworks.md`.

Supported prompt types (each maps to a template):
1. Claude Code coding prompt
2. RuFlo project intelligence prompt
3. New project planning prompt
4. Existing repo analysis prompt
5. API research prompt
6. GitHub repo research prompt
7. Browser/Playwright testing prompt
8. Deployment prompt
9. Security review prompt
10. Premium UI prompt
11. Content calendar prompt
12. Client document prompt

Reusable templates: `references/leadup-prompt-templates.md`. Concrete
fill-in assets: `assets/claude-code-prompt.template.md`,
`assets/ruflo-prompt.template.md`, `assets/api-research-prompt.template.md`,
`assets/new-project-prompt.template.md`.

## Safety rules

See `references/security-rules.md`. Most relevant here:
- Never bake real secrets, API keys, tokens, or `.env` values into a
  generated prompt — use names / `__SET_ME__` placeholders only.
- Every generated prompt must instruct the target agent: do not push/deploy
  without approval, and never print secrets or real `.env` values.
- Do not invent client commitments, prices, or facts inside a prompt — mark
  unknowns as `[fill in]`.

## Common mistakes

- Output not copy-paste-ready (commentary mixed inside the code block).
- Doing the actual task instead of producing the prompt.
- Generic prompt missing LeadUp stack/deploy/STATUS context.
- Dropping the safety / approval / no-secrets clause.
- Wrong prompt type or wrong target agent (e.g. RuFlo build prompt that
  should have been a research/plan prompt).
- Asking too many clarifying questions instead of inferring.

## Troubleshooting

- **Under-triggers**: user said "make this instruction better" and it didn't
  fire — re-invoke; suggest the trigger phrases.
- **Over-triggers**: user wanted the task *done*, not a prompt → route to the
  matching `leadup-*` skill (kickoff / analyzer / api-research / deploy / …).
- **Missing tool/MCP**: not applicable — this is pure text generation.
- **No internet/browser**: fine — no external calls needed.
- **Missing project files / thin input**: still deliverable; use `[fill in]`
  placeholders and state the assumptions made.
- **Build/test failure**: n/a here, but the generated prompt should tell the
  agent to capture failures, not disable checks, and log them in STATUS.md.

## Test prompts

### Should trigger (5)
1. "Make a super prompt: build a salon booking SaaS in Next.js."
2. "Convert this rough idea into a Claude Code prompt — add Razorpay to the jewellery app."
3. "Write a prompt for RuFlo to research and plan the hosting panel."
4. "Improve my prompt: 'fix login and make ui nice'."
5. "Turn this client requirement into a developer prompt."

### Should NOT trigger (3)
1. "Actually build the salon SaaS now." (→ leadup-project-kickoff — do the work)
2. "Analyze this repo's current state." (→ leadup-existing-repo-analyzer)
3. "Update STATUS.md after this task." (→ leadup-status-updater)

### Functional test cases (2)
1. Given broken English "make app for gold rate alert ui premium", output a
   single copy-paste block: a Claude Code prompt with role/context/task,
   LeadUp stack, and the premium-UI + no-secrets + test-in-Docker +
   ask-before-deploy + update-STATUS constraints.
2. Given "prompt for RuFlo to research GitHub repos for Flutter chat UI",
   output a RuFlo project-intelligence prompt of type "GitHub repo research"
   with license/stars/recency criteria and the LeadUp stack-fit constraint.

## Success criteria

- One copy-paste block containing a complete, structured prompt.
- Correct prompt type and target agent (inferred sensibly if unstated).
- LeadUp context + safety/approval/no-secrets clauses present; premium-UI
  clause included where UI is involved.
- ≤3 clarifying questions; no secrets anywhere.
- The skill produced a prompt — it did **not** perform the underlying task.
