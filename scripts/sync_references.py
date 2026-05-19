#!/usr/bin/env python3
"""Sync master references into each skill's local references/ folder.

The repo-root `references/` directory is the single master/source.
Each skill bundles ONLY the reference files its SKILL.md links
(`references/<name>.md`), so a skill folder is self-contained when
copied standalone into ~/.claude/skills/.

This script:
  - reads each skill's SKILL.md for `references/<name>.md` links
  - resolves transitive links (a master file pointing at another
    master file, e.g. project-docs-template -> status-template)
  - copies exactly those master files into <skill>/references/
  - never copies references a skill does not link (no bloat)
  - warns about stale local references not linked anymore (does not
    delete them — safe by default; pass --prune to remove)

Idempotent. Usage:
    python3 scripts/sync_references.py [--prune] [--check]

--check : report what would change, copy nothing, exit 1 if out of sync.
"""
import os
import re
import shutil
import sys

LINK = re.compile(r"references/([a-z0-9][a-z0-9-]*\.md)")
BACKTICK = re.compile(r"`([a-z0-9][a-z0-9-]*\.md)`")


def repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def find_skills(root):
    return [
        os.path.join(root, e)
        for e in sorted(os.listdir(root))
        if os.path.isdir(os.path.join(root, e))
        and os.path.isfile(os.path.join(root, e, "SKILL.md"))
    ]


def read(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        return fh.read()


def resolve_needed(skill_md_text, master_dir):
    """Direct links from SKILL.md + transitive links between master files."""
    master_files = {
        f for f in os.listdir(master_dir) if f.endswith(".md")
    }
    needed = {m for m in LINK.findall(skill_md_text) if m in master_files}
    changed = True
    while changed:
        changed = False
        for name in list(needed):
            txt = read(os.path.join(master_dir, name))
            for ref in set(LINK.findall(txt)) | set(BACKTICK.findall(txt)):
                if ref in master_files and ref not in needed:
                    needed.add(ref)
                    changed = True
    return sorted(needed)


def main(argv):
    prune = "--prune" in argv
    check = "--check" in argv
    root = repo_root()
    master_dir = os.path.join(root, "references")
    if not os.path.isdir(master_dir):
        print("error: repo-root references/ (master) not found")
        return 2

    drift = 0
    for skill in find_skills(root):
        name = os.path.basename(skill)
        needed = resolve_needed(read(os.path.join(skill, "SKILL.md")),
                                master_dir)
        local_dir = os.path.join(skill, "references")
        os.makedirs(local_dir, exist_ok=True)
        existing = {f for f in os.listdir(local_dir) if f.endswith(".md")} \
            if os.path.isdir(local_dir) else set()

        for f in needed:
            src = os.path.join(master_dir, f)
            dst = os.path.join(local_dir, f)
            if (not os.path.exists(dst)) or read(src) != read(dst):
                drift += 1
                if check:
                    print(f"[DRIFT] {name}/references/{f} differs from master")
                else:
                    shutil.copy2(src, dst)
                    print(f"[sync ] {name}/references/{f}")

        stale = existing - set(needed)
        for f in sorted(stale):
            if prune and not check:
                os.remove(os.path.join(local_dir, f))
                print(f"[prune] {name}/references/{f} (not linked)")
            else:
                drift += 1
                print(f"[WARN ] {name}/references/{f} not linked by SKILL.md "
                      f"(use --prune to remove)")

    if check:
        print("OUT OF SYNC" if drift else "in sync")
        return 1 if drift else 0
    print("Sync complete." if not drift else f"Sync complete ({drift} change(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
