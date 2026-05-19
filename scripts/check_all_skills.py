#!/usr/bin/env python3
"""Validate every skill in the pack. Read-only. CI-friendly.

Iterates check_skill_structure.check() over every skill folder
(directories at the repo root containing a SKILL.md) and prints a
summary table. Exit 0 only if all skills pass.

Usage:
    python3 scripts/check_all_skills.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_skill_structure import check  # noqa: E402


def repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def find_skills(root):
    return [
        os.path.join(root, e)
        for e in sorted(os.listdir(root))
        if os.path.isdir(os.path.join(root, e))
        and os.path.isfile(os.path.join(root, e, "SKILL.md"))
    ]


def main():
    root = repo_root()
    skills = find_skills(root)
    if not skills:
        print("No skills found — nothing to validate.")
        return 1

    passed, failed = [], []
    print(f"Validating {len(skills)} skill(s) in "
          f"{os.path.basename(root)}\n" + "=" * 60)
    for d in skills:
        ok, errors, info = check(d)
        tag = "PASS" if ok else "FAIL"
        print(f"[{tag}] {info.get('folder')}  "
              f"({info.get('test_prompts', 'n/a')})")
        if ok:
            passed.append(info.get("folder"))
        else:
            failed.append(info.get("folder"))
            for e in errors:
                print(f"   - {e}")

    print("=" * 60)
    print(f"PASSED: {len(passed)}   FAILED: {len(failed)}   "
          f"TOTAL: {len(skills)}")
    if failed:
        print("Failed skills: " + ", ".join(failed))
        return 1
    print("All skills passed structure validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
