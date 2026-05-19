---
name: leadup-status-updater
description: Keep a LeadUp project's memory current. Updates STATUS.md, TODO.md, and CHANGELOG.md after a task with done, in-progress, bugs, blocked, and the single next recommended task, so any future session can resume cleanly. Use when the user says "update status", "what next", "what still left", "make TODO", or "continue from STATUS.md".
---

# LeadUp Status Updater

## Purpose

Maintain the project's single source of truth. After any task, record what was
done, what's in progress, real bugs, blockers, and the one next recommended
task — and surface "what next" instantly when asked.

## When to use

Trigger phrases: "update status", "update STATUS.md", "what next", "what's
next", "what still left", "make TODO", "continue from STATUS.md", "log this
in the changelog", "where are we".

For a full cold-start analysis of an unfamiliar repo → use
`leadup-existing-repo-analyzer` (this skill maintains memory; that one
reconstructs it from scratch).

## Inputs needed

- The repo path.
- What was just done this session (or read recent changes/commits to infer).
- Existing `STATUS.md`/`TODO.md`/`CHANGELOG.md` if present.

## Step-by-step workflow

Use `references/status-template.md`. Reusable stub:
`assets/STATUS.template.md`.

1. **Read existing memory files** (don't blow away history).
2. **Determine deltas**: what got done, what's in progress, new bugs/blockers.
3. **Update STATUS.md**: Now / Done / In progress / Bugs / Blocked / Next
   recommended task / Deploy state. Keep it short and honest.
4. **Update TODO.md**: move/close items by priority (P0/P1/P2/someday).
5. **Update CHANGELOG.md**: add to Unreleased (Added/Changed/Fixed/Security);
   never erase history.
6. **Always fill "Next recommended task"** — one concrete step (the user
   always asks "what next").
7. **Report** the diff applied and state the next task plainly.

## Required output format

1. **STATUS.md** — updated content (or the applied diff).
2. **TODO.md / CHANGELOG.md** — updated sections.
3. **Next recommended task** — one concrete step, stated plainly.
4. **Open bugs/blockers** — listed even if unsolved.

## Safety rules

See `references/security-rules.md`. Most relevant here:
- Never write secrets, tokens, or real env values into these files.
- Never delete CHANGELOG history; move items, don't erase.
- Do not commit/push the updated files without approval.

## Common mistakes

- Overwriting STATUS.md and losing prior context/history.
- Leaving "Next recommended task" blank or vague.
- Hiding bugs/blockers to make status look clean (visibility > tidiness).
- Marking things "done" that were only started.
- Writing a secret or real URL-with-creds into STATUS/CHANGELOG.

## Troubleshooting

- **Under-triggers**: user asked "so where are we" — re-invoke; suggest
  trigger phrases.
- **Over-triggers** when they need a full repo audit → route to
  `leadup-existing-repo-analyzer`.
- **Missing tool/MCP**: if file write unavailable, output the exact updated
  Markdown for the user to paste.
- **No internet/browser**: irrelevant — this is local memory bookkeeping.
- **Missing project files**: create STATUS.md/TODO.md/CHANGELOG.md from the
  template and say they were created.
- **Build/test failure** in the task being logged: record it as a bug with
  the error summary — do not mark the task done.

## Test prompts

### Should trigger (5)
1. "Update STATUS.md — we finished the Razorpay webhook."
2. "What next on the salon SaaS?"
3. "What's still left in the jewellery app?"
4. "Make a TODO from where we are."
5. "Continue from STATUS.md and tell me the next task."

### Should NOT trigger (3)
1. "Analyze this unfamiliar repo from scratch." (→ existing-repo-analyzer)
2. "Is the project ready to deploy?" (→ deploy-checker)
3. "Security review of the payments code." (→ security-review)

### Functional test cases (2)
1. Given "we fixed login + found a billing bug", STATUS.md shows login under
   Done, the billing bug under Bugs, and a filled Next recommended task.
2. CHANGELOG.md gains an Unreleased entry while prior released history is
   untouched.

## Success criteria

- STATUS/TODO/CHANGELOG updated accurately, history preserved.
- "Next recommended task" always present and concrete.
- Bugs/blockers visible even when unsolved.
- No secrets written; nothing pushed without approval.
