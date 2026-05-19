#!/usr/bin/env python3
"""Lightweight stack detector for leadup-existing-repo-analyzer.

Read-only. Inspects manifest files at the repo root to report the
detected stack and likely run/test commands. Never reads .env values.

Usage:
    python3 detect_stack.py [path]   # default: current directory
"""
import json
import os
import sys


def read(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            return fh.read()
    except OSError:
        return ""


def detect(root: str) -> None:
    found = []
    cmds = []

    pkg = os.path.join(root, "package.json")
    if os.path.exists(pkg):
        try:
            data = json.loads(read(pkg) or "{}")
        except json.JSONDecodeError:
            data = {}
        deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
        if "next" in deps:
            found.append("Next.js (Node/TypeScript)")
        elif "react" in deps:
            found.append("React (Node)")
        else:
            found.append("Node.js")
        scripts = data.get("scripts", {})
        for key in ("dev", "start", "build", "test"):
            if key in scripts:
                cmds.append(f"npm run {key}  # {scripts[key]}")

    if os.path.exists(os.path.join(root, "pubspec.yaml")):
        found.append("Flutter / Dart")
        cmds += ["flutter pub get", "flutter run", "flutter test"]

    if os.path.exists(os.path.join(root, "composer.json")):
        comp = read(os.path.join(root, "composer.json"))
        found.append("Laravel/Bagisto (PHP)" if "laravel" in comp.lower()
                      or "bagisto" in comp.lower() else "PHP (Composer)")
        cmds += ["composer install", "php artisan serve", "php artisan migrate"]

    if os.path.exists(os.path.join(root, "requirements.txt")) or \
       os.path.exists(os.path.join(root, "pyproject.toml")):
        found.append("Python")

    if os.path.exists(os.path.join(root, "Dockerfile")):
        found.append("Docker")
        cmds.append("docker build -t app .")
    if os.path.exists(os.path.join(root, "docker-compose.yml")) or \
       os.path.exists(os.path.join(root, "compose.yaml")):
        found.append("Docker Compose")
        cmds.append("docker compose up --build")

    print("Detected stack:", ", ".join(found) if found else "unknown (no manifest)")
    print("\nLikely commands:")
    for c in dict.fromkeys(cmds) or ["(none detected — inspect README/Makefile)"]:
        print("  -", c)

    print("\nProject memory files:")
    for f in ("PROJECT.md", "CLAUDE.md", "STATUS.md", "DEPLOY.md",
              "SECURITY.md", "README.md", ".env.example"):
        mark = "present" if os.path.exists(os.path.join(root, f)) else "MISSING"
        print(f"  - {f}: {mark}")


if __name__ == "__main__":
    detect(sys.argv[1] if len(sys.argv) > 1 else ".")
