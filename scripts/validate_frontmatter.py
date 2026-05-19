#!/usr/bin/env python3
"""Validate a skill's SKILL.md YAML frontmatter.

Tries PyYAML (yaml.safe_load) for a strict parse; falls back to the
built-in flat parser from check_skill_structure.py if PyYAML is not
installed. Read-only.

Usage:
    python3 validate_frontmatter.py <skill-folder>
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_skill_structure import parse_frontmatter  # noqa: E402

ANGLE = re.compile(r"[<>]")


def extract_block(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return text[3:end].strip("\n")


def validate(skill_dir):
    name = os.path.basename(os.path.normpath(skill_dir))
    md = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(md):
        print(f"[FAIL] {name}: no SKILL.md")
        return 1
    with open(md, "r", encoding="utf-8", errors="ignore") as fh:
        text = fh.read()

    block = extract_block(text)
    if block is None:
        print(f"[FAIL] {name}: no valid frontmatter fence")
        return 1

    data = None
    parser = "fallback"
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(block)
        parser = "PyYAML"
        if not isinstance(data, dict):
            print(f"[FAIL] {name}: frontmatter is not a YAML mapping")
            return 1
    except ImportError:
        data, err = parse_frontmatter(text)
        if err:
            print(f"[FAIL] {name}: {err}")
            return 1
    except Exception as exc:  # noqa: BLE001 - report any YAML error
        print(f"[FAIL] {name}: YAML parse error: {exc}")
        return 1

    errs = []
    if "name" not in data:
        errs.append("missing 'name'")
    if "description" not in data:
        errs.append("missing 'description'")
    if data.get("name") and data["name"] != name:
        errs.append(f"name '{data.get('name')}' != folder '{name}'")
    for k in ("name", "description"):
        v = data.get(k)
        if isinstance(v, str) and ANGLE.search(v):
            errs.append(f"angle bracket / XML in '{k}'")
    desc = data.get("description", "")
    if isinstance(desc, str):
        if len(desc) < 40:
            errs.append("description too short")
        if len(desc) > 1024:
            errs.append(f"description too long ({len(desc)} chars)")

    if errs:
        print(f"[FAIL] {name} (parser={parser})")
        for e in errs:
            print(f"  - {e}")
        return 1
    print(f"[PASS] {name} (parser={parser}, desc {len(desc)} chars)")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: validate_frontmatter.py <skill-folder>")
        sys.exit(2)
    sys.exit(validate(sys.argv[1]))
