#!/usr/bin/env python3
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[3]

REQUIRED_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".github/copilot-instructions.md",
    ".ai/identity.yaml",
    ".ai/principles.md",
    ".ai/knowledge/glossary.yaml",
    ".ai/interfaces/exports.yaml",
    ".ai/interfaces/imports.yaml",
    ".ai/memory/decisions.md",
    ".github/skills/_index.yaml",
]


def check_required_files(issues):
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            issues.append(("FAIL", f"missing required file: {rel}"))


def check_skill_index(issues):
    index_file = ROOT / ".github/skills/_index.yaml"
    if not index_file.exists():
        return
    raw = index_file.read_text(encoding="utf-8").strip()
    if raw.startswith("```"):
        lines = raw.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        raw = "\n".join(lines)
    data = yaml.safe_load(raw) or {}
    for skill in data.get("skills", []):
        path = skill.get("path")
        if not path:
            issues.append(("WARN", f"skill without path: {skill.get('alias', '<unknown>')}"))
            continue
        if not (ROOT / path).exists():
            issues.append(("FAIL", f"indexed skill path not found: {path}"))


def check_cards_index_naming(issues):
    index_dir = ROOT / "010_CardNotes/01_Index"
    if not index_dir.exists():
        issues.append(("FAIL", "010_CardNotes/01_Index not found"))
        return
    pattern = re.compile(r"^(README|\d{2}_.+)\.md$")
    for file in index_dir.glob("*.md"):
        if not pattern.match(file.name):
            issues.append(("WARN", f"index naming anomaly: {file.name}"))


def check_bridge_semantics(issues):
    agents = ROOT / "AGENTS.md"
    claude = ROOT / "CLAUDE.md"
    gemini = ROOT / "GEMINI.md"
    if agents.exists() and "AGENTS.md" not in agents.read_text(encoding="utf-8")[:200]:
        issues.append(("WARN", "AGENTS.md header does not explicitly mark itself as core source"))
    if claude.exists() and "AGENTS.md" not in claude.read_text(encoding="utf-8"):
        issues.append(("FAIL", "CLAUDE.md does not reference AGENTS.md"))
    if gemini.exists() and "@./AGENTS.md" not in gemini.read_text(encoding="utf-8"):
        issues.append(("WARN", "GEMINI.md does not use @./AGENTS.md bridge pattern"))


def main():
    issues = []
    check_required_files(issues)
    check_skill_index(issues)
    check_cards_index_naming(issues)
    check_bridge_semantics(issues)

    if not issues:
        print("PASS | no structure issues detected")
        return

    order = {"FAIL": 0, "WARN": 1}
    issues.sort(key=lambda item: order.get(item[0], 9))

    summary = "FAIL" if any(level == "FAIL" for level, _ in issues) else "WARN"
    print(f"{summary} | structure issues detected: {len(issues)}")
    for level, message in issues:
        print(f"- {level}: {message}")


if __name__ == "__main__":
    main()
