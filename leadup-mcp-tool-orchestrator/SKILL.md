---
name: leadup-mcp-tool-orchestrator
description: Choose and sequence MCP servers, connectors, and tools safely for a LeadUp task. Discovers what tools are actually available this session, prefers read-only first, coordinates GitHub/browser/docs/database tools, and explains the risk before any write or exec action. Use when the user says "use MCP", "check available tools", "use connectors", "use GitHub MCP", "use browser MCP", "use docs MCP", or "tool orchestration".
---

# LeadUp MCP Tool Orchestrator

## Purpose

Pick the right tools for a task and run them in a safe order: discover what's
available, prefer read-only, escalate to write/exec only with stated risk and
approval. Tool inventories change between sessions — discover, never assume.

## When to use

Trigger phrases: "use MCP", "check available tools", "what tools do you have",
"use connectors", "use GitHub MCP", "use browser MCP", "use docs MCP",
"tool orchestration", "which tool should we use for this".

For actually driving a browser test flow → use
`leadup-browser-playwright-tester` (this skill picks/sequences tools; that one
runs the test).

## Inputs needed

- The task to accomplish.
- Any constraint (read-only only, no external publishing, dev vs prod target).

## Step-by-step workflow

Follow `references/mcp-tool-policy.md`.

1. **Restate the task** in one line.
2. **Discover** the tools/MCP servers/connectors actually available this
   session. Do not plan around tools that may not exist.
3. **Classify** relevant tools (docs/read, repo-read, repo-write, browser,
   database, deploy, memory).
4. **Pick the lowest-privilege tool** that achieves the step. Read-only first.
5. **Before any write/exec/external-publish tool**: state what it does, what it
   touches, whether it is reversible — get approval.
6. **Execute** read-only steps; pause at the approval gate for write/exec.
7. **Verify** with a read-only check and report what was done + next step.

## Required output format

1. **Task** (one line).
2. **Available relevant tools** (by class; note if a needed one is missing).
3. **Plan** — ordered steps, each tagged `[read-only]` or `[needs approval]`.
4. **Risk note** for every write/exec step.
5. **Result** after read-only steps + explicit approval gate before the rest.

## Safety rules

See `references/security-rules.md` and `mcp-tool-policy.md`. Most relevant:
- Never send `.env` contents, secrets, or private client data to any tool/
  connector.
- No deploy/push/remote-SSH via tools without explicit approval.
- Prefer read-only; least privilege; state reversibility before acting.

## Common mistakes

- Hard-coding a specific MCP tool name that isn't available this session.
- Jumping to a write/exec tool when a read tool answers the question.
- Using a browser tool to do something a docs/fetch tool does cheaper.
- Skipping the risk statement before a state-changing action.
- Sending repo secrets/config to an external connector.

## Troubleshooting

- **Under-triggers**: user said "just use the tools" — re-invoke; suggest
  trigger phrases.
- **Over-triggers** when they want a browser test executed → route to
  `leadup-browser-playwright-tester`.
- **Missing tool/MCP**: name the capability gap explicitly and give a manual
  fallback (e.g. local command, paste-in data).
- **No internet/browser**: restrict to local/read tools; defer anything
  needing network and say so.
- **Missing project files**: tool selection still works; note what context is
  unavailable.
- **Build/test failure** triggered via a tool: report raw error, do not retry
  a write tool blindly; downgrade to read-only diagnosis.

## Test prompts

### Should trigger (5)
1. "Check available tools and pick the right one to read this repo's PRs."
2. "Use MCP to fetch the Coolify docs safely."
3. "Tool orchestration: which connector for the Postgres read?"
4. "Use the GitHub MCP read-only to list open issues."
5. "What tools do you have for browsing, and which is safest here?"

### Should NOT trigger (3)
1. "Run the Playwright login test." (→ browser-playwright-tester)
2. "Research the Razorpay API." (→ api-research-builder)
3. "Update STATUS.md." (→ status-updater)

### Functional test cases (2)
1. For "list open PRs", the plan uses a read-only repo tool and tags it
   `[read-only]`, with no write step.
2. For "create a branch and push", the plan stops at an approval gate with a
   risk note before any write tool.

## Success criteria

- Plan based on tools actually discovered this session.
- Read-only steps first; every write/exec step gated + risk-noted.
- No secrets/client data sent externally.
- Missing capabilities named with a fallback.
