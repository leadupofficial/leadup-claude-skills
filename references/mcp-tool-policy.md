# MCP / Connector / Tool Policy

Used by `leadup-mcp-tool-orchestrator` and any skill that reaches for external
tools. Tool inventories change between sessions — **discover, don't assume**.

## Principles

1. **Discover first.** List what tools/MCP servers/connectors are actually
   available this session before planning around them. Do not hard-code
   specific tool names that may not exist.
2. **Read-only first.** Prefer fetch/list/get/search/snapshot tools before any
   create/update/delete/write/exec tool.
3. **Least privilege.** Use the narrowest tool that does the job. Don't reach
   for a browser/exec tool when a docs/read tool suffices.
4. **State intent + risk.** Before a write/exec/external-publish tool, say what
   it will do, what it touches, and whether it is reversible. Get approval.
5. **No exfiltration.** Never send `.env` contents, secrets, or private client
   data to an external tool/connector.

## Tool class → default posture

| Class | Examples (if present) | Default |
|---|---|---|
| Docs / fetch / search | web fetch, docs search, repo read | Use freely (read-only) |
| Repo read | get file contents, list PRs/issues | Use freely (read-only) |
| Repo write | create branch/PR, push files | Plan only; approval required |
| Browser | navigate/snapshot vs click/type/submit | Snapshot freely; interactions need a goal + approval for state changes |
| Database | read queries vs writes/migrations | Reads ok on dev; writes/migrations need approval, never on prod blindly |
| Deploy / infra | server, deploy triggers | Never auto-run; output a plan |
| Memory / notes | store/search project memory | Use, but never store secrets |

## Selection routine

1. Restate the task in one line.
2. List relevant available tools (by class).
3. Pick the lowest-privilege tool that achieves it.
4. If only a write/exec tool fits → produce the plan, request approval, stop.
5. After acting, report what was done and the next read-only verification step.

## When a needed tool is missing

Say so explicitly, name the capability gap, and offer a manual fallback
(e.g. "no browser MCP available — here are the manual steps / a Playwright
script you can run locally").
