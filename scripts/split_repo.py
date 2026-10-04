#!/usr/bin/env python3
"""Split CLAU-AI-CONTENT into clau-ai-core, clau-ai-marketing, clau-ai-agents.

COPY, not move: this repository is left untouched as the archive/backup.

What it does:
  1. builds three local repositories under --out (must not exist yet)
     - clau-ai-core      : split/core/** + LICENSE, ACKNOWLEDGMENT, .gitignore, issue templates
     - clau-ai-marketing : rules, prompts, skills, knowledge, templates, qa, automations,
                           examples, schemas, scripts/check_caption.py, WORKFLOW.md ->
                           CONTENT-WORKFLOW.md, AGENTS.md, + split/marketing/** overrides
     - clau-ai-agents    : split/agents/** + LICENSE, ACKNOWLEDGMENT
  2. rewrites relative links in copied Markdown so references to
     CONTENT-CONSTITUTION.md / CONTENT-BOUNDARY.md point to core/AI-*.md
     (submodule) and links to tasks/ or docs/ (kept in the archive) become
     GitHub URLs of CLAU-AI-CONTENT
  3. git init -b main, adds core as a submodule at core/ in marketing and
     agents (URL = https://github.com/<owner>/clau-ai-core.git), commits
  4. with --push: adds origin remotes and pushes core first, then the others

Usage:
  python scripts/split_repo.py --out ../split-out
  python scripts/split_repo.py --out ../split-out --push
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent
SPLIT = SRC / "split"
TODAY = "2026-10-04"

CORE, MARKETING, AGENTS = "clau-ai-core", "clau-ai-marketing", "clau-ai-agents"

COMMON_FILES = ["LICENSE", "ACKNOWLEDGMENT.md"]
MARKETING_DIRS = ["rules", "prompts", "skills", "knowledge", "templates", "qa", "automations", "examples", "schemas"]
MARKETING_FILES = {  # old path -> new path
    "WORKFLOW.md": "CONTENT-WORKFLOW.md",
    "AGENTS.md": "AGENTS.md",
    "scripts/check_caption.py": "scripts/check_caption.py",
    ".gitignore": ".gitignore",
    ".github/workflows/validate.yml": ".github/workflows/validate.yml",
}
# Old-root documents that now live in core (reached through the core/ submodule).
MOVED_TO_CORE = {
    "CONTENT-CONSTITUTION.md": "core/AI-CONSTITUTION.md",
    "CONTENT-BOUNDARY.md": "core/AI-BOUNDARY.md",
}
RENAMED_IN_MARKETING = {"WORKFLOW.md": "CONTENT-WORKFLOW.md"}
ARCHIVE_PREFIXES = ("tasks/", "docs/")

LINK_RE = re.compile(r"(\]\()([^)\s]+)(\))")
BACKTICK_PATH_RE = re.compile(r"(`)((?:\.\./|\./)[^`\s]+)(`)")


def run(cmd: list[str], cwd: Path) -> str:
    result = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        raise SystemExit(f"command failed in {cwd}: {' '.join(cmd)}\n{result.stderr}")
    return result.stdout.strip()


def copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dst, dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__", "node_modules", ".next"))
    else:
        shutil.copy2(src, dst)


def overlay(src_dir: Path, dst: Path) -> list[str]:
    """Copy every file of src_dir into dst; return relative paths written."""
    written = []
    for path in sorted(src_dir.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts:
            rel = path.relative_to(src_dir).as_posix()
            copy(path, dst / rel)
            written.append(rel)
    return written


def rewrite_target(target: str, old_file: str, new_file: str, owner: str) -> str:
    if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
        return target
    path_part, _, anchor = target.partition("#")
    if not path_part:
        return target
    old_resolved = os.path.normpath(os.path.join(os.path.dirname(old_file), path_part)).replace(os.sep, "/")
    if old_resolved.startswith(".."):
        return target
    if old_resolved in MOVED_TO_CORE:
        new_target_root = MOVED_TO_CORE[old_resolved]
    elif old_resolved in RENAMED_IN_MARKETING:
        new_target_root = RENAMED_IN_MARKETING[old_resolved]
    elif old_resolved.startswith(ARCHIVE_PREFIXES) or old_resolved in ("tasks", "docs"):
        kind = "tree" if (SRC / old_resolved).is_dir() else "blob"
        url = f"https://github.com/{owner}/CLAU-AI-CONTENT/{kind}/main/{old_resolved}"
        return url + (f"#{anchor}" if anchor else "")
    else:
        new_target_root = old_resolved
    rel = os.path.relpath(new_target_root, os.path.dirname(new_file) or ".").replace(os.sep, "/")
    if not rel.startswith("."):
        rel = f"./{rel}" if path_part.startswith("./") else rel
    return rel + (f"#{anchor}" if anchor else "")


def rewrite_markdown(text: str, old_file: str, new_file: str, owner: str) -> str:
    text = LINK_RE.sub(lambda m: m.group(1) + rewrite_target(m.group(2), old_file, new_file, owner) + m.group(3), text)
    text = BACKTICK_PATH_RE.sub(lambda m: m.group(1) + rewrite_target(m.group(2), old_file, new_file, owner) + m.group(3), text)
    # Plain-text mentions (prose, code spans without paths)
    text = text.replace("CONTENT-CONSTITUTION", "AI-CONSTITUTION").replace("CONTENT-BOUNDARY", "AI-BOUNDARY")
    text = re.sub(r"(?<![-\w/])WORKFLOW\.md", "CONTENT-WORKFLOW.md", text)
    return text


def bump_doc(path: Path, old_version: str, new_version: str, summary: str) -> None:
    text = path.read_text(encoding="utf-8")
    if f'version: "{old_version}"' not in text:
        raise SystemExit(f"{path}: expected version {old_version}")
    text = text.replace(f'version: "{old_version}"', f'version: "{new_version}"', 1)
    text = text.rstrip("\n") + f"\n| {new_version} | {TODAY} | Draft | {summary} |\n"
    path.write_text(text, encoding="utf-8")


def fix_text_mentions(repo: Path, owner: str) -> None:
    """Update old file names in non-Markdown text files (.gitignore, issue templates)."""
    targets = [repo / ".gitignore", *sorted((repo / ".github" / "ISSUE_TEMPLATE").glob("*.yml"))]
    for path in targets:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        text = text.replace("CONTENT-BOUNDARY.md", "AI-BOUNDARY.md di clau-ai-core")
        text = text.replace("board Markdown di `tasks/`", f"board Markdown di repo arsip {owner}/CLAU-AI-CONTENT (`tasks/`)")
        path.write_text(text, encoding="utf-8")


def git_commit_all(repo: Path, message: str) -> str:
    run(["git", "add", "-A"], repo)
    run(["git", "commit", "-q", "-m", message], repo)
    return run(["git", "rev-parse", "--short", "HEAD"], repo)


def add_core_submodule(repo: Path, core_local: Path, owner: str) -> None:
    run(["git", "-c", "protocol.file.allow=always", "submodule", "add", "-q", str(core_local), "core"], repo)
    url = f"https://github.com/{owner}/{CORE}.git"
    run(["git", "config", "-f", ".gitmodules", "submodule.core.url", url], repo)
    run(["git", "config", "-f", ".gitmodules", "submodule.core.branch", "main"], repo)
    run(["git", "submodule", "sync", "-q"], repo)


def build_core(out: Path, owner: str) -> Path:
    repo = out / CORE
    overlay(SPLIT / "core", repo)
    for f in COMMON_FILES + [".gitignore"]:
        copy(SRC / f, repo / f)
    copy(SRC / ".github/ISSUE_TEMPLATE", repo / ".github/ISSUE_TEMPLATE")
    fix_text_mentions(repo, owner)
    run(["git", "init", "-q", "-b", "main"], repo)
    git_commit_all(repo, "feat: initial clau-ai-core (foundation split from CLAU-AI-CONTENT)")
    return repo


def build_marketing(out: Path, core_local: Path, owner: str) -> Path:
    repo = out / MARKETING
    for d in MARKETING_DIRS:
        copy(SRC / d, repo / d)
    for old, new in MARKETING_FILES.items():
        copy(SRC / old, repo / new)
    for f in COMMON_FILES:
        copy(SRC / f, repo / f)
    copy(SRC / ".github/ISSUE_TEMPLATE", repo / ".github/ISSUE_TEMPLATE")

    # Rewrite links in copied Markdown (map new path -> old path for resolution)
    new_to_old = {v: k for k, v in MARKETING_FILES.items()}
    for md in sorted(repo.rglob("*.md")):
        new_rel = md.relative_to(repo).as_posix()
        old_rel = new_to_old.get(new_rel, new_rel)
        md.write_text(rewrite_markdown(md.read_text(encoding="utf-8"), old_rel, new_rel, owner), encoding="utf-8")

    bump_doc(repo / "CONTENT-WORKFLOW.md", "0.1.3", "0.2.0",
             "Dipindah ke clau-ai-marketing sebagai CONTENT-WORKFLOW.md; constitution & boundary dirujuk dari core/ (split repo)")
    bump_doc(repo / "AGENTS.md", "0.1.3", "0.2.0",
             "Dipindah ke clau-ai-marketing (instruksi agent Pilar 1); instruksi lintas repo ada di core/AGENTS.md")

    overlay(SPLIT / "marketing", repo)  # README.md, scripts/validate.py (not rewritten)
    fix_text_mentions(repo, owner)
    run(["git", "init", "-q", "-b", "main"], repo)
    add_core_submodule(repo, core_local, owner)
    git_commit_all(repo, "feat: initial clau-ai-marketing (Pilar 1 split from CLAU-AI-CONTENT, core as submodule)")
    return repo


def build_agents(out: Path, core_local: Path, owner: str) -> Path:
    repo = out / AGENTS
    overlay(SPLIT / "agents", repo)
    for f in COMMON_FILES:
        copy(SRC / f, repo / f)
    run(["git", "init", "-q", "-b", "main"], repo)
    add_core_submodule(repo, core_local, owner)
    git_commit_all(repo, "feat: initial clau-ai-agents (platform scaffold, core as submodule)")
    return repo


def push(repo: Path, owner: str) -> None:
    url = f"https://github.com/{owner}/{repo.name}.git"
    run(["git", "remote", "add", "origin", url], repo)
    run(["git", "push", "-u", "origin", "main"], repo)
    print(f"pushed {repo.name} -> {url}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", required=True, help="output directory (each repo is created inside it)")
    parser.add_argument("--owner", default="d34faiza-commits", help="GitHub owner for submodule & remote URLs")
    parser.add_argument("--push", action="store_true", help="add origin remotes and push (repos must already exist on GitHub)")
    args = parser.parse_args()

    out = Path(args.out).resolve()
    for name in (CORE, MARKETING, AGENTS):
        if (out / name).exists():
            print(f"refusing to overwrite existing {out / name}; remove it or pick another --out", file=sys.stderr)
            return 1
    out.mkdir(parents=True, exist_ok=True)

    core = build_core(out, args.owner)
    marketing = build_marketing(out, core, args.owner)
    agents = build_agents(out, core, args.owner)
    for repo in (core, marketing, agents):
        print(f"built {repo}  ({run(['git', 'rev-parse', '--short', 'HEAD'], repo)})")

    if args.push:
        for repo in (core, marketing, agents):  # core first: submodule commits must exist upstream
            push(repo, args.owner)
    return 0


if __name__ == "__main__":
    sys.exit(main())
