#!/usr/bin/env python3
"""Mechanical caption checks for clau-content (stdlib only).

Checks each caption for:
  - hook (first line) length <= --max-hook characters (default 125)
  - total length <= --max-chars (default 2200; ASSUMPTION until TASK-011 verifies)
  - hashtag count within --min-tags..--max-tags (default 3..8) when hashtags are used
  - emoji count <= --max-emoji, and no emoji in the hook when --no-emoji-hook
  - forbidden terms: rule 02 positioning words + brief restrictions.forbidden_terms

It does NOT judge claims, tone, or truthfulness — that stays with the QA gates.

Usage:
  python scripts/check_caption.py caption.txt
  python scripts/check_caption.py --markdown drafts.md --brief brief.json
      (only ```text blocks with hashtags = captions; add --all-blocks for every block)
  echo "caption" | python scripts/check_caption.py -
Exit code 0 = all captions pass, 1 = at least one failure.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Rule 02 — positioning words that are claims (see rules/02, "Kata positioning & nama brand").
POSITIONING_TERMS = [
    "mewah", "luxury", "luxurious", "premium", "eksklusif", "exclusive",
    "5-star", "7-star", "bintang 5", "bintang lima", "world-class", "kelas dunia",
    "terbaik", "best", "nomor 1", "number one", "termurah",
]
# Voice guide — clichés.
CLICHES = [
    "hidden gem", "surga tersembunyi", "pengalaman tak terlupakan", "unforgettable experience",
    "nestled", "dream getaway", "kemewahan tiada tara", "unparalleled",
]
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
HASHTAG_RE = re.compile(r"#\w+")
FENCE_RE = re.compile(r"```text\n(.*?)```", re.DOTALL)


def load_captions(args: argparse.Namespace) -> list[tuple[str, str]]:
    if args.markdown:
        text = Path(args.markdown).read_text(encoding="utf-8")
        blocks = FENCE_RE.findall(text)
        return [
            (f"{args.markdown} block {i + 1}", b.strip("\n"))
            for i, b in enumerate(blocks)
            if args.all_blocks or HASHTAG_RE.search(b)
        ]
    source = args.file
    text = sys.stdin.read() if source == "-" else Path(source).read_text(encoding="utf-8")
    return [(source, text.strip("\n"))]


def forbidden_terms(brief_path: str | None) -> list[str]:
    terms = POSITIONING_TERMS + CLICHES
    if brief_path:
        brief = json.loads(Path(brief_path).read_text(encoding="utf-8"))
        terms += brief.get("restrictions", {}).get("forbidden_terms", [])
    return sorted({t.lower() for t in terms})


def term_hits(text: str, terms: list[str]) -> list[str]:
    lower = text.lower()
    return [t for t in terms if re.search(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])", lower)]


def check(caption: str, args: argparse.Namespace, terms: list[str]) -> list[str]:
    problems: list[str] = []
    lines = [line for line in caption.splitlines() if line.strip()]
    hook = lines[0] if lines else ""
    if len(hook) > args.max_hook:
        problems.append(f"hook {len(hook)} chars > {args.max_hook}")
    if len(caption) > args.max_chars:
        problems.append(f"length {len(caption)} chars > {args.max_chars} (limit is ASSUMPTION)")
    tags = HASHTAG_RE.findall(caption)
    if tags and not args.min_tags <= len(tags) <= args.max_tags:
        problems.append(f"{len(tags)} hashtags, expected {args.min_tags}-{args.max_tags}")
    if len(set(t.lower() for t in tags)) != len(tags):
        problems.append("duplicate hashtags")
    emojis = EMOJI_RE.findall(caption)
    if args.max_emoji is not None and len(emojis) > args.max_emoji:
        problems.append(f"{len(emojis)} emoji > {args.max_emoji}")
    if args.no_emoji_hook and EMOJI_RE.search(hook):
        problems.append("emoji in hook")
    hits = term_hits(caption, terms)
    if hits:
        problems.append("forbidden/positioning terms: " + ", ".join(hits))
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("file", nargs="?", default="-", help="caption file, or - for stdin")
    parser.add_argument("--markdown", help="check ```text blocks that contain hashtags (captions) in a Markdown file")
    parser.add_argument("--all-blocks", action="store_true", help="with --markdown, check every ```text block")
    parser.add_argument("--brief", help="brief.json; adds restrictions.forbidden_terms")
    parser.add_argument("--max-hook", type=int, default=125)
    parser.add_argument("--max-chars", type=int, default=2200)
    parser.add_argument("--min-tags", type=int, default=3)
    parser.add_argument("--max-tags", type=int, default=8)
    parser.add_argument("--max-emoji", type=int, default=None)
    parser.add_argument("--no-emoji-hook", action="store_true")
    args = parser.parse_args()

    terms = forbidden_terms(args.brief)
    failed = 0
    for name, caption in load_captions(args):
        problems = check(caption, args, terms)
        if problems:
            failed += 1
            print(f"FAIL  {name}")
            for p in problems:
                print(f"      - {p}")
        else:
            print(f"PASS  {name}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
