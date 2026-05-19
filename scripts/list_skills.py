#!/usr/bin/env python3
"""List every skill in the pack with its description. Read-only.

A skill = a directory (at the repo root) that contains a SKILL.md.

Usage:
    python3 scripts/list_skills.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_skill_structure import parse_frontmatter  # noqa: E402


def repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def find_skills(root):
    skills = []
    for entry in sorted(os.listdir(root)):
        d = os.path.join(root, entry)
        if os.path.isdir(d) and os.path.isfile(os.path.join(d, "SKILL.md")):
            skills.append(d)
    return skills


def main():
    root = repo_root()
    skills = find_skills(root)
    if not skills:
        print("No skills found.")
        return 1
    print(f"{len(skills)} skill(s) in {os.path.basename(root)}:\n")
    for d in skills:
        name = os.path.basename(d)
        with open(os.path.join(d, "SKILL.md"), "r",
                  encoding="utf-8", errors="ignore") as fh:
            fm, _ = parse_frontmatter(fh.read())
        desc = (fm or {}).get("description", "(no description)")
        short = desc if len(desc) <= 160 else desc[:157] + "..."
        print(f"- {name}\n    {short}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
