#!/usr/bin/env python3
"""Repository validator for CLAU-AI-CONTENT.

Checks (stdlib only; jsonschema is used when installed):
  - required repository files exist
  - rules follow the 10-section format and use all six evidence labels
  - prompts follow the prompt template sections
  - skills have name/description-only frontmatter, required sections,
    existing context files, and a matching agents/openai.yaml
  - JSON files parse; JSON schemas are valid when jsonschema is available
  - examples/**/brief.json files validate against the content brief schema
  - governance docs: frontmatter, Revision History, and README versions agree
  - task boards: unique IDs, required fields, status matches board
  - relative Markdown links resolve
  - no obvious secrets are committed

Usage: python scripts/validate.py
Exit code 0 = pass, 1 = failures found.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EVIDENCE_LABELS = [
    "DATA FINAL",
    "ASSUMPTION",
    "CLIENT CONFIRMATION",
    "FIELD VERIFICATION",
    "RISK",
    "NEXT ACTION",
]

REQUIRED_FILES = [
    "README.md",
    "ACKNOWLEDGMENT.md",
    "LICENSE",
    "CONTENT-CONSTITUTION.md",
    "CONTENT-BOUNDARY.md",
    "AGENTS.md",
    "WORKFLOW.md",
    "schemas/content-brief.schema.json",
    "prompts/templates/prompt-template.md",
]

RULE_SECTIONS = [
    "Purpose",
    "Scope",
    "Mandatory Rules",
    "Required Inputs",
    "Workflow",
    "Deliverables",
    "Validation/QC Checklist",
    "Risks & Mitigation",
    "Escalation Conditions",
    "References",
]

PROMPT_SECTIONS = [
    "Purpose",
    "When to Use",
    "Required Inputs",
    "Optional Inputs",
    "Prompt",
    "Expected Output",
    "Related Standards",
]

SKILL_SECTIONS = [
    "Load Required Context",
    "Workflow",
    "Output",
    "Self-Check",
    "Safety Boundary",
    "Exit Criteria",
]

OPENAI_YAML_KEYS = ["interface:", "display_name:", "short_description:", "default_prompt:"]

SECRET_PATTERNS = [
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "AWS access key"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"), "GitHub token"),
    (re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}\b"), "Slack token"),
    (re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"), "API secret key"),
    (re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"), "Google API key"),
    (re.compile(r"\bEAA[A-Za-z0-9]{40,}\b"), "Meta access token"),
]

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", ".build", "split"}
TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".py", ".txt", ".toml", ""}

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CONTEXT_PATH_RE = re.compile(r"`(\.\./\.\./[^`]+)`")


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.checked = 0

    def fail(self, path: Path | str, message: str) -> None:
        rel = path.relative_to(ROOT) if isinstance(path, Path) and path.is_absolute() else path
        self.failures.append(f"{rel}: {message}")


def iter_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.is_file():
            files.append(path)
    return sorted(files)


def headings(text: str, level: int = 2) -> list[str]:
    prefix = "#" * level + " "
    stripped = CODE_FENCE_RE.sub("", text)
    return [line[len(prefix):].strip() for line in stripped.splitlines() if line.startswith(prefix)]


def check_sections(path: Path, text: str, required: list[str], report: Report) -> None:
    found = headings(text, 2)
    missing = [s for s in required if not any(h == s or h.startswith(s + " ") for h in found)]
    if missing:
        report.fail(path, f"missing sections: {', '.join(missing)}")
        return
    order = [next(i for i, h in enumerate(found) if h == s or h.startswith(s + " ")) for s in required]
    if order != sorted(order):
        report.fail(path, "sections are not in the required order")


def check_required_files(report: Report) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            report.fail(rel, "required file is missing")


def check_rules(report: Report) -> None:
    rules = sorted((ROOT / "rules").glob("[0-9][0-9]-*.md"))
    if len(rules) < 9:
        report.fail("rules/", f"expected at least 9 rules, found {len(rules)}")
    for path in rules:
        report.checked += 1
        text = path.read_text(encoding="utf-8")
        check_sections(path, text, RULE_SECTIONS, report)
        missing = [label for label in EVIDENCE_LABELS if label not in text]
        if missing:
            report.fail(path, f"missing evidence labels: {', '.join(missing)}")
        number = path.name[:2]
        if not text.startswith(f"# {number} — "):
            report.fail(path, f"title must start with '# {number} — '")


def check_prompts(report: Report) -> None:
    for path in sorted((ROOT / "prompts").rglob("*.md")):
        report.checked += 1
        text = path.read_text(encoding="utf-8")
        check_sections(path, text, PROMPT_SECTIONS, report)
        if "```text" not in text:
            report.fail(path, "prompt must contain a ```text block")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        if ":" not in line or line.startswith((" ", "\t")):
            data.setdefault("__invalid__", line)
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def check_skills(report: Report) -> None:
    skill_dirs = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    if len(skill_dirs) < 6:
        report.fail("skills/", f"expected at least 6 skills, found {len(skill_dirs)}")
    for skill_dir in skill_dirs:
        report.checked += 1
        name = skill_dir.name
        skill_md = skill_dir / "SKILL.md"
        if not SKILL_NAME_RE.match(name):
            report.fail(skill_dir, "skill folder must be lowercase-hyphenated")
        if not skill_md.is_file():
            report.fail(skill_dir, "missing SKILL.md")
            continue
        text = skill_md.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        if meta is None:
            report.fail(skill_md, "missing or unterminated frontmatter")
        else:
            keys = set(meta)
            if keys != {"name", "description"}:
                report.fail(skill_md, f"frontmatter must contain only name and description, found: {sorted(keys)}")
            if meta.get("name") != name:
                report.fail(skill_md, f"frontmatter name '{meta.get('name')}' must equal folder name '{name}'")
            if len(meta.get("description", "")) < 40:
                report.fail(skill_md, "description is too short to trigger reliably")
        check_sections(skill_md, text, SKILL_SECTIONS, report)
        for target in CONTEXT_PATH_RE.findall(text):
            resolved = (skill_md.parent / target).resolve()
            if not resolved.exists():
                report.fail(skill_md, f"missing required context: {target}")

        yaml_path = skill_dir / "agents" / "openai.yaml"
        if not yaml_path.is_file():
            report.fail(skill_dir, "missing agents/openai.yaml")
            continue
        yaml_text = yaml_path.read_text(encoding="utf-8")
        for key in OPENAI_YAML_KEYS:
            if key not in yaml_text:
                report.fail(yaml_path, f"missing key '{key.rstrip(':')}'")
        if f"${name}" not in yaml_text:
            report.fail(yaml_path, f"default_prompt must reference ${name}")


GOVERNANCE_DOCS = [
    "CONTENT-CONSTITUTION.md",
    "CONTENT-BOUNDARY.md",
    "WORKFLOW.md",
    "AGENTS.md",
]
GOVERNANCE_FIELDS = ["document_title", "document_owner", "version", "status"]
DOC_STATUSES = {"Draft", "For Review", "Approved", "Superseded", "Archived"}
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
REVISION_ROW_RE = re.compile(r"^\|\s*(\d+\.\d+\.\d+)\s*\|\s*[^|]+\|\s*([^|]+?)\s*\|", re.MULTILINE)
README_VERSION_ROW_RE = re.compile(r"^\|\s*\[([^\]]+)\]\([^)]+\)\s*\|\s*(\d+\.\d+\.\d+)\s*\|\s*([^|]+?)\s*\|", re.MULTILINE)


def check_versions(report: Report) -> None:
    """Frontmatter, Revision History, and the README version table must agree."""
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    listed = {name: (ver, status) for name, ver, status in README_VERSION_ROW_RE.findall(readme)}
    for rel in GOVERNANCE_DOCS:
        path = ROOT / rel
        if not path.is_file():
            continue
        report.checked += 1
        text = path.read_text(encoding="utf-8")
        meta = parse_frontmatter(text) or {}
        meta = {k: v.strip('"') for k, v in meta.items()}
        missing = [f for f in GOVERNANCE_FIELDS if not meta.get(f)]
        if missing:
            report.fail(path, f"frontmatter missing: {', '.join(missing)}")
            continue
        version, status = meta["version"], meta["status"]
        if not SEMVER_RE.match(version):
            report.fail(path, f"version '{version}' is not SemVer")
        if status not in DOC_STATUSES:
            report.fail(path, f"status '{status}' not in {sorted(DOC_STATUSES)}")
        if status == "Approved" and not meta.get("approval_reference"):
            report.fail(path, "Approved document requires approval_reference")
        history = text.split("## Revision History", 1)
        rows = REVISION_ROW_RE.findall(history[1]) if len(history) == 2 else []
        if not rows:
            report.fail(path, "missing Revision History rows (| Version | Date | Status | Summary |)")
        elif rows[-1] != (version, status):
            report.fail(path, f"latest Revision History row {rows[-1]} does not match frontmatter ({version}, {status})")
        if listed.get(rel) != (version, status):
            report.fail("README.md", f"Versi Dokumen row for {rel} is {listed.get(rel)}, expected ({version}, {status})")


TASK_BOARDS = {
    "backlog.md": "Backlog",
    "in-progress.md": "In Progress",
    "review.md": "Review",
    "done.md": "Done",
}
TASK_FIELDS = ["ID", "Status", "Priority", "Assignee", "Created", "Due", "Description", "Acceptance Criteria", "Related"]
TASK_PRIORITIES = {"Low", "Normal", "High", "Urgent"}
TASK_HEADING_RE = re.compile(r"^## (TASK-\d{3}): .+$", re.MULTILINE)
DATE_OR_DASH_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}|—)$")


def check_tasks(report: Report) -> None:
    """Each task lives in one board file, with all fields and a status matching its board."""
    tasks_dir = ROOT / "tasks"
    if not tasks_dir.is_dir():
        return
    seen: dict[str, str] = {}
    for filename, column in TASK_BOARDS.items():
        path = tasks_dir / filename
        if not path.is_file():
            report.fail(f"tasks/{filename}", "task board file is missing")
            continue
        report.checked += 1
        text = path.read_text(encoding="utf-8")
        headings = list(TASK_HEADING_RE.finditer(text))
        for i, match in enumerate(headings):
            task_id = match.group(1)
            end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
            fields = dict(re.findall(r"^- ([A-Za-z ]+): (.+)$", text[match.end():end], re.MULTILINE))
            where = f"tasks/{filename} {task_id}"
            if task_id in seen:
                report.fail(where, f"duplicate task ID (also in tasks/{seen[task_id]})")
            seen[task_id] = filename
            missing = [f for f in TASK_FIELDS if f not in fields]
            if missing:
                report.fail(where, f"missing fields: {', '.join(missing)}")
                continue
            if fields["ID"] != task_id:
                report.fail(where, f"ID field '{fields['ID']}' does not match heading")
            if fields["Status"] != column:
                report.fail(where, f"Status '{fields['Status']}' does not match board '{column}'")
            if fields["Priority"] not in TASK_PRIORITIES:
                report.fail(where, f"Priority '{fields['Priority']}' not in {sorted(TASK_PRIORITIES)}")
            for date_field in ("Created", "Due"):
                if not DATE_OR_DASH_RE.match(fields[date_field]):
                    report.fail(where, f"{date_field} must be YYYY-MM-DD or —")


def check_json(report: Report) -> None:
    try:
        import jsonschema  # type: ignore
    except ImportError:
        jsonschema = None
    for path in sorted(ROOT.rglob("*.json")):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        report.checked += 1
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            report.fail(path, f"invalid JSON: {exc}")
            continue
        if path.parent.name == "schemas":
            if "$schema" not in data or "required" not in data:
                report.fail(path, "schema must declare $schema and required")
            if jsonschema is not None:
                try:
                    jsonschema.validators.validator_for(data).check_schema(data)
                except jsonschema.exceptions.SchemaError as exc:
                    report.fail(path, f"invalid JSON Schema: {exc.message}")
            labels = json.dumps(data.get("$defs", {}).get("evidence_label", {}))
            missing = [label for label in EVIDENCE_LABELS if label not in labels]
            if path.name == "content-brief.schema.json" and missing:
                report.fail(path, f"evidence_label enum missing: {', '.join(missing)}")
    brief_schema_path = ROOT / "schemas" / "content-brief.schema.json"
    if jsonschema is not None and brief_schema_path.is_file():
        brief_schema = json.loads(brief_schema_path.read_text(encoding="utf-8"))
        brief_validator = jsonschema.Draft202012Validator(
            brief_schema, format_checker=jsonschema.FormatChecker()
        )
        for brief_path in sorted((ROOT / "examples").rglob("brief.json")):
            report.checked += 1
            brief = json.loads(brief_path.read_text(encoding="utf-8"))
            for err in brief_validator.iter_errors(brief):
                location = "/".join(str(p) for p in err.path) or "(root)"
                report.fail(brief_path, f"schema violation at {location}: {err.message}")
    if jsonschema is None:
        print("note: jsonschema not installed; JSON Schema meta-validation skipped")


def check_links(report: Report) -> None:
    for path in sorted(ROOT.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        text = CODE_FENCE_RE.sub("", path.read_text(encoding="utf-8"))
        text = INLINE_CODE_RE.sub("", text)
        for target in LINK_RE.findall(text):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            file_part = target.split("#", 1)[0]
            if not file_part:
                continue
            resolved = (path.parent / file_part).resolve()
            if not resolved.exists():
                report.fail(path, f"broken relative link: {target}")


def check_secrets(report: Report) -> None:
    this_file = Path(__file__).resolve()
    for path in iter_files():
        if path.resolve() == this_file or path.suffix not in TEXT_SUFFIXES:
            continue
        if path.name.startswith(".env") and path.name != ".env.example":
            report.fail(path, ".env files must not be committed")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern, label in SECRET_PATTERNS:
            if pattern.search(text):
                report.fail(path, f"possible secret detected ({label}); value not printed")


def main() -> int:
    report = Report()
    check_required_files(report)
    check_rules(report)
    check_prompts(report)
    check_skills(report)
    check_versions(report)
    check_tasks(report)
    check_json(report)
    check_links(report)
    check_secrets(report)

    if report.failures:
        print(f"FAIL — {len(report.failures)} issue(s):")
        for failure in report.failures:
            print(f"  - {failure}")
        return 1
    print(f"PASS — {report.checked} items checked, no issues found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
