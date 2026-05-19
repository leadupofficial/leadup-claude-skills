#!/usr/bin/env python3
"""Read-only secret sweep for leadup-security-review.

Scans a project tree for likely committed secrets and reports
FILE:LINE with the matched value REDACTED. It never prints secret
values and never modifies anything.

Usage:
    python3 scan_secrets.py [path]   # default: current directory

Exit code 0 = no findings, 1 = potential secrets found.
"""
import os
import re
import sys

# (label, compiled pattern). Patterns identify the *shape* of a secret;
# the matched text is never printed back.
PATTERNS = [
    ("OpenAI key", re.compile(r"sk-(proj-)?[A-Za-z0-9]{20,}")),
    ("Google API key", re.compile(r"AIza[0-9A-Za-z\-_]{30,}")),
    ("GitHub token", re.compile(r"gh[pousr]_[0-9A-Za-z]{30,}")),
    ("GitHub PAT", re.compile(r"github_pat_[0-9A-Za-z_]{30,}")),
    ("Slack token", re.compile(r"xox[baprs]-[0-9A-Za-z-]{10,}")),
    ("Razorpay live/test key", re.compile(r"rzp_(live|test)_[0-9A-Za-z]{10,}")),
    ("AWS access key id", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("Private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("DB URI with password",
     re.compile(r"(postgres|postgresql|mysql|mongodb(\+srv)?)://[^:\s]+:[^@\s]+@")),
    ("Generic assigned secret",
     re.compile(r"(?i)(api_?key|secret|token|password|passwd)\s*[:=]\s*"
                r"['\"]?[A-Za-z0-9/\+_\-]{16,}")),
]

SKIP_DIRS = {".git", "node_modules", "dist", "build", ".next", "vendor",
             ".venv", "venv", "__pycache__", ".cache", "coverage"}
SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".zip",
            ".lock", ".min.js", ".map", ".woff", ".woff2", ".ttf"}
# .env.example / .env.sample are expected to hold placeholders, not secrets.
EXAMPLE_ENV = re.compile(r"\.env\.(example|sample|template)$")


def redact(text: str) -> str:
    text = text.strip()
    if len(text) <= 8:
        return "****"
    return f"{text[:3]}…{text[-2:]} [REDACTED, len={len(text)}]"


def scan(root: str) -> int:
    findings = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if any(fn.endswith(e) for e in SKIP_EXT):
                continue
            path = os.path.join(dirpath, fn)
            is_example = bool(EXAMPLE_ENV.search(fn))
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                    for lineno, line in enumerate(fh, 1):
                        if "__SET_ME__" in line:
                            continue  # explicit placeholder
                        for label, pat in PATTERNS:
                            m = pat.search(line)
                            if not m:
                                continue
                            sev = "INFO (example file)" if is_example else "POTENTIAL SECRET"
                            print(f"[{sev}] {label}: "
                                  f"{os.path.relpath(path, root)}:{lineno} "
                                  f"value={redact(m.group(0))}")
                            if not is_example:
                                findings += 1
            except (OSError, UnicodeError):
                continue
    if findings:
        print(f"\n{findings} potential secret(s) found. "
              f"Rotate, remove from history, add to .gitignore. "
              f"Values are redacted above by design.")
        return 1
    print("No potential committed secrets found (read-only scan).")
    return 0


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(scan(target))
