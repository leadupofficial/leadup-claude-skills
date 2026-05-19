# STATUS.md / TODO.md / CHANGELOG.md Templates

Used by `leadup-status-updater`. STATUS.md is the single source of truth for
"what next". Keep it short, current, and honest (list real bugs/blockers).

## STATUS.md template

```markdown
# STATUS — <project>

_Last updated: <YYYY-MM-DD> by <session/agent>_

## Now (current state)
One-paragraph plain summary of where the project actually is.

## Done
- [x] <thing> (<date>)

## In progress
- [ ] <thing> — <who/what's needed>

## Bugs
- [ ] <bug> — severity — repro — suspected cause

## Blocked
- [ ] <thing> — blocked by <reason / needs user / needs key / needs decision>

## Next recommended task
1. <single most valuable next step, concrete>
2. <then>

## Deploy state
- Local: <works? command>
- GitHub: <branch, pushed?>
- Server/Coolify: <deployed? subdomain? version/tag>
```

## TODO.md template

```markdown
# TODO — <project>
## P0 (blockers / breakage)
## P1 (this milestone)
## P2 (nice to have)
## Someday / ideas
```

## CHANGELOG.md template (Keep a Changelog style)

```markdown
# Changelog
## [Unreleased]
### Added
### Changed
### Fixed
### Security

## [x.y.z] - YYYY-MM-DD
```

## Update rules
- Update after every task, not just at the end.
- Never delete history from CHANGELOG; move items, don't erase.
- "Next recommended task" must always be filled (the user always asks "what next").
- Record bugs/blockers even if unsolved — visibility over tidiness.
- Never put secrets, tokens, or real env values in these files.
