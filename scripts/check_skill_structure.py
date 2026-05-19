#!/usr/bin/env python3
"""Validate one LeadUp skill folder against the pack rules.

Read-only. Usable as a CLI or imported by check_all_skills.py.

Checks:
  - folder contains SKILL.md
  - folder name is kebab-case
  - frontmatter present, valid, has `name` and `description`
  - frontmatter `name` == folder name
  - no XML tags / angle brackets in name or description
  - no README.md anywhere in the skill folder (project template ships as
    assets/README.template.md, never README.md)
  - self-contained: every `references/<name>.md` linked in SKILL.md exists
    in the skill's own references/ folder
  - all 10 required H2 sections present
  - Test prompts: >=5 should-trigger, >=3 should-NOT, >=2 functional
  - no leaked-secret patterns (placeholders using __SET_ME__ are allowed)

Exit 0 = pass, 1 = fail (CLI mode).
"""
import os
import re
import sys

REQUIRED_SECTIONS = [
    "## Purpose",
    "## When to use",
    "## Inputs needed",
    "## Step-by-step workflow",
    "## Required output format",
    "## Safety rules",
    "## Common mistakes",
    "## Troubleshooting",
    "## Test prompts",
    "## Success criteria",
]

KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ANGLE = re.compile(r"[<>]")

SECRET_PATTERNS = [
    ("OpenAI key", re.compile(r"sk-(proj-)?[A-Za-z0-9]{20,}")),
    ("Google API key", re.compile(r"AIza[0-9A-Za-z\-_]{30,}")),
    ("GitHub token", re.compile(r"gh[pousr]_[0-9A-Za-z]{30,}")),
    ("GitHub PAT", re.compile(r"github_pat_[0-9A-Za-z_]{30,}")),
    ("Slack token", re.compile(r"xox[baprs]-[0-9A-Za-z-]{12,}")),
    ("Razorpay key", re.compile(r"rzp_(live|test)_[0-9A-Za-z]{12,}")),
    ("AWS access key id", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("Private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("DB URI with password",
     re.compile(r"(postgres|postgresql|mysql|mongodb(\+srv)?)://[^:\s]+:[^@\s]+@")),
]


def parse_frontmatter(text):
    """Minimal flat-YAML frontmatter parser (no PyYAML dependency).

    Returns (data_dict, error_or_None). Handles the simple
    `key: value` scalars this pack uses.
    """
    if not text.startswith("---"):
        return None, "no opening '---' frontmatter fence"
    end = text.find("\n---", 3)
    if end == -1:
        return None, "no closing '---' frontmatter fence"
    block = text[3:end].strip("\n")
    data = {}
    for raw in block.splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            return None, f"frontmatter line not key:value -> {line!r}"
        key, val = line.split(":", 1)
        val = val.strip()
        if (val.startswith('"') and val.endswith('"')) or \
           (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        data[key.strip()] = val
    return data, None


def _count_numbered(block: str) -> int:
    return len(re.findall(r"^\s*\d+\.\s+\S", block, re.MULTILINE))


def check(skill_dir: str):
    """Return (ok: bool, errors: list[str], info: dict)."""
    errors = []
    info = {}
    name = os.path.basename(os.path.normpath(skill_dir))
    info["folder"] = name

    if not KEBAB.match(name):
        errors.append(f"folder name '{name}' is not kebab-case")

    skill_md = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(skill_md):
        errors.append("missing SKILL.md")
        return False, errors, info

    # No README.md anywhere in a skill folder. The project README template
    # ships as assets/README.template.md, never README.md.
    for dp, dn, fns in os.walk(skill_dir):
        dn[:] = [d for d in dn if d not in {".git", "__pycache__"}]
        if "README.md" in fns:
            rel = os.path.relpath(os.path.join(dp, "README.md"), skill_dir)
            errors.append(
                f"README.md must not be inside a skill folder ({rel}); "
                f"use README.template.md for templates")

    with open(skill_md, "r", encoding="utf-8", errors="ignore") as fh:
        text = fh.read()

    # Self-contained: every `references/<name>.md` linked in SKILL.md must
    # exist in this skill's own references/ folder.
    for ref in sorted(set(re.findall(r"references/([a-z0-9][a-z0-9-]*\.md)",
                                     text))):
        if not os.path.isfile(os.path.join(skill_dir, "references", ref)):
            errors.append(
                f"linked reference 'references/{ref}' missing from skill "
                f"(not self-contained)")

    fm, fm_err = parse_frontmatter(text)
    if fm_err:
        errors.append(f"frontmatter: {fm_err}")
    else:
        if "name" not in fm:
            errors.append("frontmatter missing 'name'")
        if "description" not in fm:
            errors.append("frontmatter missing 'description'")
        if fm.get("name") and fm["name"] != name:
            errors.append(
                f"frontmatter name '{fm.get('name')}' != folder '{name}'")
        for k in ("name", "description"):
            if k in fm and ANGLE.search(fm[k]):
                errors.append(f"angle bracket / XML tag in frontmatter '{k}'")
        desc = fm.get("description", "")
        info["description"] = desc
        if desc and len(desc) < 40:
            errors.append("description too short to be useful")

    for sec in REQUIRED_SECTIONS:
        if not re.search(r"^" + re.escape(sec) + r"\s*$", text, re.MULTILINE):
            errors.append(f"missing required section '{sec}'")

    # Test-prompt sub-counts.
    def section_body(header):
        m = re.search(r"^" + re.escape(header) + r"\s*$", text, re.MULTILINE)
        if not m:
            return ""
        start = m.end()
        nxt = re.search(r"^#{2,3}\s", text[start:], re.MULTILINE)
        return text[start:start + nxt.start()] if nxt else text[start:]

    trig = _count_numbered(section_body("### Should trigger (5)"))
    anti = _count_numbered(section_body("### Should NOT trigger (3)"))
    func = _count_numbered(section_body("### Functional test cases (2)"))
    info["test_prompts"] = f"{trig} trigger / {anti} anti / {func} functional"
    if trig < 5:
        errors.append(f"need >=5 should-trigger prompts, found {trig}")
    if anti < 3:
        errors.append(f"need >=3 should-NOT-trigger prompts, found {anti}")
    if func < 2:
        errors.append(f"need >=2 functional test cases, found {func}")

    # Secret sweep across the whole skill folder.
    for dp, dn, fns in os.walk(skill_dir):
        dn[:] = [d for d in dn if d not in {".git", "__pycache__"}]
        for fn in fns:
            p = os.path.join(dp, fn)
            try:
                with open(p, "r", encoding="utf-8", errors="ignore") as fh:
                    for i, line in enumerate(fh, 1):
                        if "__SET_ME__" in line:
                            continue
                        for label, pat in SECRET_PATTERNS:
                            if pat.search(line):
                                rel = os.path.relpath(p, skill_dir)
                                errors.append(
                                    f"possible {label} in {rel}:{i} "
                                    f"(value redacted)")
            except OSError:
                continue

    return (not errors), errors, info


def main(argv):
    if len(argv) < 2:
        print("usage: check_skill_structure.py <skill-folder>")
        return 2
    ok, errors, info = check(argv[1])
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {info.get('folder')}  "
          f"({info.get('test_prompts', 'n/a')})")
    for e in errors:
        print(f"  - {e}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
