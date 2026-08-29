from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "template"
REQUIRED = (
    "README.md",
    "AGENTS.md",
    "CODE_OF_CONDUCT.md",
    "SUPPORT.md",
    "skill-pack.lock.json",
    "template/AGENTS.md",
    "template/Home.md",
    "template/System/Agent Spaces.md",
    "template/System/Skill Packs.md",
    "template/System/Privacy.md",
    "template/Learning/AGENTS.md",
    "template/Learning/.agents/README.md",
    "template/Learning/Learning.md",
    "template/Learning/Rules.md",
    "template/Learning/Courses/Index.md",
    "template/Learning/Courses/_templates/Lesson Template.md",
    "template/Learning/Concepts/Concept Map.md",
    "template/Learning/Recall/Index.md",
    "template/Learning/Open Questions/Index.md",
    "template/Work/AGENTS.md",
    "template/Work/.agents/README.md",
    "template/Work/Work.md",
    "template/Work/Project Lifecycle.md",
    "template/Work/Companies/Index.md",
    "template/Work/Companies/_templates/Company.md",
    "template/Work/Companies/_templates/Project.md",
    "template/Work/Companies/_templates/Plan.md",
    "template/Work/Companies/Example Company/Projects/Atlas Notes/Plans/README.md",
    "template/Studio/AGENTS.md",
    "template/Studio/Video/AGENTS.md",
    "template/Studio/Video/.agents/README.md",
    "template/Studio/Video/Video.md",
    "template/Studio/Video/Concepts/Concept Template.md",
)
EXPECTED_PACKS = {
    "template/Learning/.agents/skills/doc-learning/SKILL.md",
    "template/Learning/.agents/skills/video-learning/SKILL.md",
    "template/Work/.agents/skills/project-learning/SKILL.md",
    "template/Work/.agents/skills/project-planning/SKILL.md",
    "template/Studio/Video/.agents/skills/video-research/SKILL.md",
    "template/Studio/Video/.agents/skills/video-concept/SKILL.md",
    "template/Studio/Video/.agents/skills/video-review/SKILL.md",
}
WIKILINK = re.compile(r"(?<!!)\[\[([^\]]+)\]\]")
PRIVATE_TEXT = re.compile(
    r"C:\\Users\\|/Users/[^/<]+/|BEGIN (?:RSA |OPENSSH )?PRIVATE KEY",
    re.IGNORECASE,
)
REMOTE_LINE = re.compile(r"^repository:\s*(.+?)\s*$", re.MULTILINE)
COMPANY_HEADINGS = (
    "## Purpose, customers, and business model",
    "## Operating model",
    "## Domain vocabulary",
    "## Engineering and delivery",
    "## Security, privacy, and compliance",
    "## Shared platforms and cross-project decisions",
)


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in TEMPLATE.rglob("*.md")
        if ".agents" not in path.parts
    )


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            return text[end + 5 :]
    return text


def normalise_remote(value: str) -> str:
    value = value.strip().strip("`\"'").rstrip("/")
    value = re.sub(r"\.git$", "", value, flags=re.IGNORECASE)
    parsed = urlsplit(value)
    if "://" in value and parsed.hostname and parsed.path:
        return f"{parsed.hostname}/{parsed.path.lstrip('/')}".lower()
    scp_match = re.fullmatch(r"(?:[^@/\s]+@)?([^:/\s]+):(.+)", value)
    if scp_match:
        return f"{scp_match.group(1)}/{scp_match.group(2).lstrip('/')}".lower()
    return value.lower()


def project_remotes(text: str) -> list[str]:
    frontmatter = text.split("---", 2)[1] if text.startswith("---") and text.count("---") >= 2 else ""
    remotes = [match.group(1) for match in REMOTE_LINE.finditer(frontmatter)]
    lines = frontmatter.splitlines()
    for index, line in enumerate(lines):
        if line.strip() != "repositories:":
            continue
        for item in lines[index + 1 :]:
            if not item.startswith((" ", "\t", "-")):
                break
            match = re.match(r"\s*-\s*(.+?)\s*$", item)
            if match:
                remotes.append(match.group(1))
    return [normalise_remote(remote) for remote in remotes if remote.strip() and remote.strip() != "[]"]


def has_frontmatter_value(text: str, key: str, expected: str) -> bool:
    if not text.startswith("---\n"):
        return False
    frontmatter = text.split("---", 2)[1]
    return bool(re.search(rf"^{re.escape(key)}:\s*{re.escape(expected)}\s*$", frontmatter, re.MULTILINE))


def link_resolves(path: Path, target: str, pages: set[str], basenames: set[str]) -> bool:
    target = target.split("|", 1)[0].split("#", 1)[0].strip()
    if not target or target.startswith(("http:", "https:", "mailto:")):
        return True
    target = target.removesuffix(".md")
    relative = path.relative_to(TEMPLATE).with_suffix("").as_posix()
    parent = PurePosixPath(relative).parent
    if "/" in target or target.startswith("."):
        candidates = {
            PurePosixPath(target).as_posix(),
            (parent / target).as_posix(),
        }
        return any(candidate in pages for candidate in candidates)
    return target in basenames


def main() -> int:
    findings: list[str] = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            findings.append(f"missing required file: {relative}")

    pages = {path.relative_to(TEMPLATE).with_suffix("").as_posix() for path in markdown_files()}
    basenames = {PurePosixPath(page).name for page in pages}
    for path in markdown_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in WIKILINK.finditer(strip_frontmatter(text)):
            if not link_resolves(path, match.group(1), pages, basenames):
                findings.append(
                    f"broken wikilink in {path.relative_to(ROOT)}: [[{match.group(1)}]]"
                )

    for path in ROOT.rglob("*"):
        if (
            not path.is_file()
            or path.relative_to(ROOT).as_posix() == "scripts/validate.py"
            or ".git" in path.parts
            or "__pycache__" in path.parts
            or path.suffix.lower() not in {".md", ".py", ".yml", ".yaml"}
        ):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if PRIVATE_TEXT.search(text):
            findings.append(f"private or machine-specific data: {path.relative_to(ROOT)}")

    for required_guide in TEMPLATE.rglob("AGENTS.md"):
        if len(required_guide.read_text(encoding="utf-8").splitlines()) > 80:
            findings.append(f"agent guide is too long: {required_guide.relative_to(ROOT)}")

    seen_remotes: dict[str, Path] = {}
    project_root = TEMPLATE / "Work" / "Companies"
    for project in project_root.rglob("Project.md"):
        if "_templates" in project.parts:
            continue
        relative = project.relative_to(project_root)
        parts = relative.parts
        if len(parts) != 4 or parts[1] != "Projects":
            findings.append(f"project is outside company hierarchy: {project.relative_to(ROOT)}")
            continue
        company_dir = project_root / parts[0]
        company_page = company_dir / "Company.md"
        if not company_page.is_file():
            findings.append(f"project parent has no Company.md: {project.relative_to(ROOT)}")
        if not (company_dir / "AGENTS.md").is_file():
            findings.append(f"project parent has no AGENTS.md: {project.relative_to(ROOT)}")
        if not (project.parent / "AGENTS.md").is_file():
            findings.append(f"project has no AGENTS.md: {project.relative_to(ROOT)}")
        if not (project.parent / "Plans").is_dir():
            findings.append(f"project has no Plans directory: {project.relative_to(ROOT)}")
        text = project.read_text(encoding="utf-8")
        if not has_frontmatter_value(text, "company", parts[0]):
            findings.append(f"project company frontmatter mismatch: {project.relative_to(ROOT)}")
        remotes = project_remotes(text)
        if not remotes:
            findings.append(f"project has no repository identity: {project.relative_to(ROOT)}")
        for remote in remotes:
            if remote.startswith("<") or "://" not in remote and "/" not in remote:
                findings.append(f"invalid repository identity in {project.relative_to(ROOT)}: {remote}")
                continue
            if remote in seen_remotes:
                findings.append(
                    "duplicate repository identity: "
                    f"{remote} in {project.relative_to(ROOT)} and {seen_remotes[remote].relative_to(ROOT)}"
                )
            else:
                seen_remotes[remote] = project

    for company in project_root.rglob("Company.md"):
        if "_templates" in company.parts:
            continue
        text = company.read_text(encoding="utf-8")
        if not (company.parent / "AGENTS.md").is_file():
            findings.append(f"company has no AGENTS.md: {company.relative_to(ROOT)}")
        missing = [heading for heading in COMPANY_HEADINGS if heading not in text]
        if missing:
            findings.append(
                f"company operating context incomplete: {company.relative_to(ROOT)} ({'; '.join(missing)})"
            )

    plan_template = project_root / "_templates" / "Plan.md"
    try:
        plan_text = plan_template.read_text(encoding="utf-8")
        if not has_frontmatter_value(plan_text, "type", "plan"):
            findings.append("plan template must declare type: plan")
        if not has_frontmatter_value(plan_text, "status", "draft"):
            findings.append("plan template must start with status: draft")
    except OSError:
        pass

    discovered_skills = {
        path.relative_to(ROOT).as_posix()
        for path in TEMPLATE.rglob("SKILL.md")
    }
    for path in sorted(EXPECTED_PACKS - discovered_skills):
        findings.append(f"missing scoped skill: {path}")
    unexpected = discovered_skills - EXPECTED_PACKS
    for path in sorted(unexpected):
        findings.append(f"skill outside a scoped destination: {path}")
    for relative in sorted(discovered_skills & EXPECTED_PACKS):
        text = (ROOT / relative).read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\nname:" not in text or "\ndescription:" not in text:
            findings.append(f"invalid scoped skill frontmatter: {relative}")

    try:
        lock = json.loads((ROOT / "skill-pack.lock.json").read_text(encoding="utf-8"))
        if lock.get("source") != "https://github.com/furkanilkturk/pi-skills":
            findings.append("skill lock has an unexpected canonical source")
        if not re.fullmatch(r"[0-9a-f]{40}", str(lock.get("revision", ""))):
            findings.append("skill lock revision must be a full lowercase Git SHA")
        locked_skills = lock.get("skills")
        if not isinstance(locked_skills, dict):
            findings.append("skill lock must contain a skills object")
            locked_skills = {}
        if set(locked_skills) != EXPECTED_PACKS:
            findings.append("skill lock paths do not match the scoped destinations")
        for relative in sorted(discovered_skills & EXPECTED_PACKS):
            digest = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
            if locked_skills.get(relative) != digest:
                findings.append(f"vendored skill hash mismatch: {relative}")
    except (OSError, json.JSONDecodeError) as error:
        findings.append(f"invalid skill-pack.lock.json: {error}")

    if findings:
        print("VALIDATION FAILED")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("VALIDATION CLEAN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
