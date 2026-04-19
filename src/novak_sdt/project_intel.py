from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import UTC, datetime
from pathlib import Path
import json
import re
import subprocess
from typing import Any


PLACEHOLDER_PATTERNS = [
    re.compile(r"\bfill in\b", re.IGNORECASE),
    re.compile(r"\btbd\b", re.IGNORECASE),
    re.compile(r"\btodo\b", re.IGNORECASE),
    re.compile(r"<[^>\n]+>"),
]


@dataclass
class InferredField:
    name: str
    value: str
    confidence: str
    evidence: list[str]


@dataclass
class ProjectModel:
    stamp_utc: str
    repo_path: str
    repo_name: str
    product_name: InferredField
    repo_type: InferredField
    primary_language: InferredField
    runtime: InferredField
    entrypoints: InferredField
    install_command: InferredField
    test_command: InferredField
    run_command: InferredField
    docs_command: InferredField
    product_statement: InferredField
    current_state: InferredField
    system_boundary: InferredField
    top_risks: list[str]
    confirmations_needed: list[str]
    placeholders_detected: list[str]
    change_doc_count: int
    trusted_floor_status: str
    latest_tag: str
    head_commit: str


def now_utc() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")


def git_output(repo: Path, *args: str) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=repo,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def list_files(repo: Path) -> list[Path]:
    files: list[Path] = []
    for path in repo.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file():
            files.append(path)
    return files


def read_text_safe(path: Path, limit: int = 200_000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:limit]
    except Exception:
        return ""


def exists_any(repo: Path, *names: str) -> bool:
    return any((repo / name).exists() for name in names)


def infer_product_name(repo: Path) -> InferredField:
    evidence = [f"repo directory name: {repo.name}"]
    fallback = repo.name.replace("-", " ").replace("_", " ").title()

    pyproject = repo / "pyproject.toml"
    if pyproject.exists():
        text = read_text_safe(pyproject)
        match = re.search(r'^\s*name\s*=\s*"([^"]+)"', text, re.MULTILINE)
        if match:
            return InferredField(
                name="product_name",
                value=match.group(1),
                confidence="LIKELY",
                evidence=evidence + ["pyproject.toml name field"],
            )

    package_json = repo / "package.json"
    if package_json.exists():
        try:
            data = json.loads(read_text_safe(package_json))
            name = data.get("name")
            if isinstance(name, str) and name.strip():
                return InferredField(
                    name="product_name",
                    value=name.strip(),
                    confidence="LIKELY",
                    evidence=evidence + ["package.json name field"],
                )
        except Exception:
            pass

    return InferredField(
        name="product_name",
        value=fallback,
        confidence="LIKELY",
        evidence=evidence,
    )


def infer_primary_language(repo: Path, files: list[Path]) -> InferredField:
    counts = {
        "Python": 0,
        "Shell": 0,
        "JavaScript": 0,
        "TypeScript": 0,
        "Go": 0,
        "Rust": 0,
    }

    for path in files:
        suffix = path.suffix.lower()
        if suffix == ".py":
            counts["Python"] += 1
        elif suffix in {".sh", ".bash"}:
            counts["Shell"] += 1
        elif suffix == ".js":
            counts["JavaScript"] += 1
        elif suffix in {".ts", ".tsx"}:
            counts["TypeScript"] += 1
        elif suffix == ".go":
            counts["Go"] += 1
        elif suffix == ".rs":
            counts["Rust"] += 1

    top = max(counts, key=counts.get)
    if counts[top] == 0:
        return InferredField(
            name="primary_language",
            value="unknown",
            confidence="UNKNOWN",
            evidence=["no recognized language markers found"],
        )

    evidence = [f"{name} files: {count}" for name, count in counts.items() if count > 0]
    return InferredField(
        name="primary_language",
        value=top,
        confidence="LIKELY",
        evidence=evidence,
    )


def infer_repo_type(repo: Path) -> InferredField:
    evidence: list[str] = []

    if (repo / "mkdocs.yml").exists() and not exists_any(repo, "pyproject.toml", "package.json", "app", "src"):
        return InferredField(
            name="repo_type",
            value="documentation-site",
            confidence="LIKELY",
            evidence=["mkdocs.yml present"],
        )

    if exists_any(repo, "pyproject.toml"):
        evidence.append("pyproject.toml present")
        text = read_text_safe(repo / "pyproject.toml")
        if "fastapi" in text.lower() or "flask" in text.lower():
            evidence.append("FastAPI/Flask marker present")
            return InferredField("repo_type", "python-service-repository", "LIKELY", evidence)
        if "[project.scripts]" in text or "console_scripts" in text:
            evidence.append("python CLI script markers present")
            return InferredField("repo_type", "python-cli-repository", "LIKELY", evidence)
        return InferredField("repo_type", "python-repository", "LIKELY", evidence)

    if (repo / "package.json").exists():
        evidence.append("package.json present")
        pkg = read_text_safe(repo / "package.json").lower()
        if "next" in pkg:
            evidence.append("Next.js marker present")
            return InferredField("repo_type", "web-application-repository", "LIKELY", evidence)
        return InferredField("repo_type", "node-repository", "LIKELY", evidence)

    if (repo / "app").exists() or (repo / "src").exists():
        return InferredField(
            name="repo_type",
            value="application-repository",
            confidence="LIKELY",
            evidence=["app/ or src/ directory present"],
        )

    if (repo / "ops").exists() and (repo / "bin").exists():
        return InferredField(
            name="repo_type",
            value="operations-and-automation-repository",
            confidence="LIKELY",
            evidence=["ops/ and bin/ present"],
        )

    return InferredField(
        name="repo_type",
        value="unknown",
        confidence="UNKNOWN",
        evidence=["no decisive repo type markers found"],
    )


def infer_runtime(repo: Path) -> InferredField:
    evidence: list[str] = []

    if (repo / ".venv").exists():
        evidence.append(".venv present")

    if exists_any(repo, "pyproject.toml", "requirements.txt"):
        evidence.append("python dependency marker present")
        return InferredField("runtime", "python", "LIKELY", evidence)

    if (repo / "package.json").exists():
        evidence.append("package.json present")
        return InferredField("runtime", "node", "LIKELY", evidence)

    if (repo / "go.mod").exists():
        evidence.append("go.mod present")
        return InferredField("runtime", "go", "LIKELY", evidence)

    if (repo / "Cargo.toml").exists():
        evidence.append("Cargo.toml present")
        return InferredField("runtime", "rust", "LIKELY", evidence)

    return InferredField("runtime", "unknown", "UNKNOWN", ["no runtime markers found"])


def infer_entrypoints(repo: Path) -> InferredField:
    evidence: list[str] = []
    entries: list[str] = []

    for candidate in [
        "bin/run-hello-world.sh",
        "bin/run.sh",
        "main.py",
        "app/main.py",
        "app.py",
        "manage.py",
    ]:
        if (repo / candidate).exists():
            entries.append(candidate)
            evidence.append(f"entrypoint candidate present: {candidate}")

    pyproject = repo / "pyproject.toml"
    if pyproject.exists():
        text = read_text_safe(pyproject)
        if "[project.scripts]" in text:
            entries.append("pyproject project.scripts")
            evidence.append("pyproject [project.scripts] section present")

    package_json = repo / "package.json"
    if package_json.exists():
        try:
            data = json.loads(read_text_safe(package_json))
            scripts = data.get("scripts", {})
            if isinstance(scripts, dict):
                for name in ("start", "dev", "build", "test"):
                    if name in scripts:
                        entries.append(f"package.json::{name}")
                        evidence.append(f"package.json script present: {name}")
        except Exception:
            pass

    if not entries:
        return InferredField("entrypoints", "unknown", "UNKNOWN", ["no clear entrypoints found"])

    return InferredField("entrypoints", ", ".join(entries), "LIKELY", evidence)


def infer_install_command(repo: Path) -> InferredField:
    if (repo / "pyproject.toml").exists():
        return InferredField("install_command", "python3 -m pip install -e .", "LIKELY", ["pyproject.toml present"])
    if (repo / "requirements.txt").exists():
        return InferredField("install_command", "python3 -m pip install -r requirements.txt", "LIKELY", ["requirements.txt present"])
    if (repo / "package.json").exists():
        return InferredField("install_command", "npm install", "LIKELY", ["package.json present"])
    return InferredField("install_command", "unknown", "UNKNOWN", ["no install markers found"])


def infer_test_command(repo: Path) -> InferredField:
    tests_dir = repo / "tests"

    if (repo / "pyproject.toml").exists():
        text = read_text_safe(repo / "pyproject.toml")
        if "pytest" in text.lower() or tests_dir.exists():
            return InferredField(
                "test_command",
                "python3 -m pytest -q tests",
                "LIKELY",
                ["pytest marker or tests/ directory present"],
            )

    if tests_dir.exists():
        return InferredField(
            "test_command",
            "python3 -m unittest discover -s tests -p 'test*.py'",
            "LIKELY",
            ["tests/ directory present"],
        )

    if (repo / "package.json").exists():
        try:
            data = json.loads(read_text_safe(repo / "package.json"))
            scripts = data.get("scripts", {})
            if isinstance(scripts, dict) and "test" in scripts:
                return InferredField("test_command", "npm test", "LIKELY", ["package.json test script present"])
        except Exception:
            pass

    return InferredField("test_command", "unknown", "UNKNOWN", ["no test markers found"])


def infer_run_command(repo: Path) -> InferredField:
    if (repo / "bin/run-hello-world.sh").exists():
        return InferredField("run_command", "bash bin/run-hello-world.sh", "LIKELY", ["bin/run-hello-world.sh present"])
    if (repo / "app/main.py").exists():
        return InferredField("run_command", "python3 app/main.py", "LIKELY", ["app/main.py present"])
    if (repo / "main.py").exists():
        return InferredField("run_command", "python3 main.py", "LIKELY", ["main.py present"])

    if (repo / "package.json").exists():
        try:
            data = json.loads(read_text_safe(repo / "package.json"))
            scripts = data.get("scripts", {})
            if isinstance(scripts, dict):
                if "start" in scripts:
                    return InferredField("run_command", "npm start", "LIKELY", ["package.json start script present"])
                if "dev" in scripts:
                    return InferredField("run_command", "npm run dev", "LIKELY", ["package.json dev script present"])
        except Exception:
            pass

    return InferredField("run_command", "unknown", "UNKNOWN", ["no run markers found"])


def infer_docs_command(repo: Path) -> InferredField:
    if (repo / "mkdocs.yml").exists():
        return InferredField("docs_command", "mkdocs serve", "LIKELY", ["mkdocs.yml present"])
    return InferredField("docs_command", "unknown", "UNKNOWN", ["no docs command markers found"])


def infer_product_statement(product_name: str, repo_type: str, primary_language: str) -> InferredField:
    value = f"{product_name} is a {repo_type.replace('-', ' ')} primarily implemented in {primary_language}."
    return InferredField(
        "product_statement",
        value,
        "LIKELY",
        [f"repo_type={repo_type}", f"primary_language={primary_language}"],
    )


def infer_current_state(files: list[Path], change_doc_count: int, latest_tag: str) -> InferredField:
    value = (
        f"Repository scan found {len(files)} files, "
        f"{change_doc_count} change document(s), and latest tag {latest_tag}."
    )
    return InferredField(
        "current_state",
        value,
        "LIKELY",
        [f"file_count={len(files)}", f"change_doc_count={change_doc_count}", f"latest_tag={latest_tag}"],
    )


def infer_system_boundary(repo_type: str, runtime: str) -> InferredField:
    value = (
        f"This repo appears to own a {repo_type.replace('-', ' ')} built or run with {runtime}. "
        "Production infrastructure, credentials, and external services are not assumed unless directly evidenced."
    )
    return InferredField(
        "system_boundary",
        value,
        "LIKELY",
        [f"repo_type={repo_type}", f"runtime={runtime}"],
    )


def detect_placeholders(repo: Path) -> list[str]:
    targets = [
        repo / "PROJECT_STATE.md",
        repo / "WHAT_IS_REAL_NOW.md",
        repo / "README.md",
        repo / "docs/product/PRODUCT_STATEMENT.md",
        repo / "docs/INSTALLATION.md",
    ]
    findings: list[str] = []

    for path in targets:
        if not path.exists():
            findings.append(f"{path.relative_to(repo)} missing")
            continue
        text = read_text_safe(path)
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(text):
                findings.append(f"{path.relative_to(repo)} contains placeholder-like text matching {pattern.pattern}")
                break

    return findings


def build_confirmations(model: dict[str, Any]) -> list[str]:
    prompts: list[str] = []

    def maybe_add(field_name: str, question: str) -> None:
        field = model[field_name]
        if field["confidence"] in {"UNKNOWN", "LIKELY"}:
            prompts.append(question)

    maybe_add("repo_type", f"I inferred repo_type={model['repo_type']['value']}. Confirm or correct the repo class.")
    maybe_add("product_name", f"I inferred product_name={model['product_name']['value']}. Confirm the canonical product name.")
    maybe_add("run_command", f"I inferred run_command={model['run_command']['value']}. Confirm the main run path.")
    maybe_add("test_command", f"I inferred test_command={model['test_command']['value']}. Confirm the preferred verification command.")
    maybe_add("system_boundary", "Confirm what this repo explicitly owns vs what is out of scope.")
    maybe_add("product_statement", "Confirm whether the inferred product statement matches the intended purpose.")

    return prompts[:10]


def completeness_score(model: dict[str, Any]) -> tuple[int, list[str]]:
    issues: list[str] = []
    score = 100

    required_fields = [
        "product_name",
        "repo_type",
        "primary_language",
        "runtime",
        "install_command",
        "test_command",
        "run_command",
        "product_statement",
        "current_state",
        "system_boundary",
    ]

    for field_name in required_fields:
        field = model[field_name]
        if field["value"] == "unknown":
            score -= 10
            issues.append(f"{field_name} is unknown")
        elif field["confidence"] == "UNKNOWN":
            score -= 8
            issues.append(f"{field_name} confidence unknown")
        elif field["confidence"] == "LIKELY":
            score -= 2

    placeholder_count = len(model["placeholders_detected"])
    if placeholder_count:
        score -= min(20, placeholder_count * 4)
        issues.extend(model["placeholders_detected"])

    if model["change_doc_count"] == 0:
        score -= 5
        issues.append("no change documents detected")

    score = max(0, score)
    return score, issues


def build_drift_findings(repo: Path, model: dict[str, Any]) -> list[str]:
    findings: list[str] = []

    readme = read_text_safe(repo / "README.md")
    if "Operator shell entry" not in readme and (repo / "tools/install_novak_shell_shortcuts.sh").exists():
        findings.append("README.md does not mention operator shell entry even though shortcut installer exists")

    product_doc = read_text_safe(repo / "docs/product/PRODUCT_STATEMENT.md")
    inferred_name = model["product_name"]["value"]
    if inferred_name not in product_doc:
        findings.append("docs/product/PRODUCT_STATEMENT.md does not mention inferred product name")

    current_state_doc = read_text_safe(repo / "PROJECT_STATE.md")
    if "SDT:BEGIN inferred project state" not in current_state_doc:
        findings.append("PROJECT_STATE.md missing managed inferred project state section")

    what_is_real_doc = read_text_safe(repo / "WHAT_IS_REAL_NOW.md")
    if "SDT:BEGIN inferred what is real now" not in what_is_real_doc:
        findings.append("WHAT_IS_REAL_NOW.md missing managed inferred truth section")

    latest_tag = model["latest_tag"]
    head_commit = model["head_commit"]
    if latest_tag != "unknown":
        tag_commit = git_output(repo, "rev-list", "-n", "1", latest_tag)
        if tag_commit != "unknown" and tag_commit != head_commit:
            findings.append(f"HEAD {head_commit} is ahead of latest tag {latest_tag}")

    return findings


def managed_section(doc_path: Path, section_name: str, body: str) -> None:
    begin = f"<!-- SDT:BEGIN {section_name} -->"
    end = f"<!-- SDT:END {section_name} -->"
    block = f"{begin}\n{body.rstrip()}\n{end}\n"

    existing = read_text_safe(doc_path, limit=2_000_000)
    if not existing:
        doc_path.parent.mkdir(parents=True, exist_ok=True)
        doc_path.write_text(block, encoding="utf-8")
        return

    pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end) + r"\n?", re.DOTALL)
    if pattern.search(existing):
        updated = pattern.sub(block, existing)
    else:
        updated = existing.rstrip() + "\n\n" + block

    doc_path.write_text(updated, encoding="utf-8")


def render_project_state(model: dict[str, Any]) -> str:
    risk_lines = [f"- {item}" for item in model["top_risks"]]
    if not risk_lines:
        risk_lines = ["- none detected"]

    confirm_lines = [f"- {item}" for item in model["confirmations_needed"]]
    if not confirm_lines:
        confirm_lines = ["- none"]

    lines = [
        "# Inferred Project State",
        "",
        f"- stamp_utc: {model['stamp_utc']}",
        f"- repo_name: {model['repo_name']}",
        f"- repo_type: {model['repo_type']['value']} ({model['repo_type']['confidence']})",
        f"- primary_language: {model['primary_language']['value']} ({model['primary_language']['confidence']})",
        f"- runtime: {model['runtime']['value']} ({model['runtime']['confidence']})",
        f"- head_commit: {model['head_commit']}",
        f"- latest_tag: {model['latest_tag']}",
        "",
        "## Current inferred state",
        model["current_state"]["value"],
        "",
        "## Top risks",
    ]
    lines.extend(risk_lines)
    lines.extend(["", "## Confirmation needed"])
    lines.extend(confirm_lines)
    return "\n".join(lines)


def render_what_is_real_now(model: dict[str, Any]) -> str:
    unknown_lines = [f"- {item}" for item in model["confirmations_needed"]]
    if not unknown_lines:
        unknown_lines = ["- none"]

    lines = [
        "# Inferred What Is Real Now",
        "",
        f"- repo path: `{model['repo_path']}`",
        f"- product name: `{model['product_name']['value']}`",
        f"- run command: `{model['run_command']['value']}`",
        f"- test command: `{model['test_command']['value']}`",
        f"- docs command: `{model['docs_command']['value']}`",
        "",
        "## Proven or likely facts",
        f"- repo_type: `{model['repo_type']['value']}` ({model['repo_type']['confidence']})",
        f"- runtime: `{model['runtime']['value']}` ({model['runtime']['confidence']})",
        f"- entrypoints: `{model['entrypoints']['value']}` ({model['entrypoints']['confidence']})",
        f"- install_command: `{model['install_command']['value']}` ({model['install_command']['confidence']})",
        "",
        "## Unknowns or confirmations needed",
    ]
    lines.extend(unknown_lines)
    return "\n".join(lines)


def render_product_statement(model: dict[str, Any]) -> str:
    lines = [
        "# Inferred Product Statement",
        "",
        model["product_statement"]["value"],
        "",
        "## Confidence",
        f"- {model['product_statement']['confidence']}",
        "",
        "## Evidence",
    ]
    lines.extend([f"- {item}" for item in model["product_statement"]["evidence"]])
    return "\n".join(lines)


def render_installation(model: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Inferred Installation",
            "",
            "## Likely install command",
            f"- `{model['install_command']['value']}`",
            "",
            "## Likely run command",
            f"- `{model['run_command']['value']}`",
            "",
            "## Likely test command",
            f"- `{model['test_command']['value']}`",
            "",
            "## Likely docs command",
            f"- `{model['docs_command']['value']}`",
        ]
    )


def render_confirmation_packet(model: dict[str, Any]) -> str:
    lines = [
        "# SDT Confirmation Packet",
        "",
        f"- stamp_utc: {model['stamp_utc']}",
        f"- repo_name: {model['repo_name']}",
        "",
        "## Confirm or correct",
    ]
    if model["confirmations_needed"]:
        lines.extend([f"- {item}" for item in model["confirmations_needed"]])
    else:
        lines.append("- No confirmation questions were generated.")
    return "\n".join(lines)


def render_completeness_report(model: dict[str, Any], score: int, issues: list[str]) -> str:
    lines = [
        "# SDT Completeness Report",
        "",
        f"- stamp_utc: {model['stamp_utc']}",
        f"- score: {score}/100",
        "",
        "## Issues",
    ]
    if issues:
        lines.extend([f"- {item}" for item in issues])
    else:
        lines.append("- none")
    return "\n".join(lines)


def render_drift_report(model: dict[str, Any], findings: list[str]) -> str:
    lines = [
        "# SDT Drift Report",
        "",
        f"- stamp_utc: {model['stamp_utc']}",
        "",
        "## Findings",
    ]
    if findings:
        lines.extend([f"- {item}" for item in findings])
    else:
        lines.append("- no obvious drift findings")
    return "\n".join(lines)


def build_project_model(repo: Path) -> ProjectModel:
    files = list_files(repo)

    product_name = infer_product_name(repo)
    primary_language = infer_primary_language(repo, files)
    repo_type = infer_repo_type(repo)
    runtime = infer_runtime(repo)
    entrypoints = infer_entrypoints(repo)
    install_command = infer_install_command(repo)
    test_command = infer_test_command(repo)
    run_command = infer_run_command(repo)
    docs_command = infer_docs_command(repo)

    change_doc_count = len(list((repo / "docs/changes").glob("*.md"))) if (repo / "docs/changes").exists() else 0
    latest_tag = git_output(repo, "describe", "--tags", "--abbrev=0")
    head_commit = git_output(repo, "rev-parse", "HEAD")

    product_statement = infer_product_statement(product_name.value, repo_type.value, primary_language.value)
    current_state = infer_current_state(files, change_doc_count, latest_tag)
    system_boundary = infer_system_boundary(repo_type.value, runtime.value)

    placeholders = detect_placeholders(repo)

    top_risks: list[str] = []
    if placeholders:
        top_risks.append("placeholder-like text still exists in core truth docs")
    if test_command.value == "unknown":
        top_risks.append("test command is not inferred")
    if run_command.value == "unknown":
        top_risks.append("run command is not inferred")
    if latest_tag == "unknown":
        top_risks.append("no git tag detected for trusted floor")

    tag_commit = git_output(repo, "rev-list", "-n", "1", latest_tag) if latest_tag != "unknown" else "unknown"
    trusted_floor_status = "HEAD_EQUALS_LATEST_TAG" if latest_tag != "unknown" and tag_commit == head_commit else "HEAD_AHEAD_OR_TAG_UNKNOWN"

    base_model = {
        "stamp_utc": now_utc(),
        "repo_path": str(repo),
        "repo_name": repo.name,
        "product_name": asdict(product_name),
        "repo_type": asdict(repo_type),
        "primary_language": asdict(primary_language),
        "runtime": asdict(runtime),
        "entrypoints": asdict(entrypoints),
        "install_command": asdict(install_command),
        "test_command": asdict(test_command),
        "run_command": asdict(run_command),
        "docs_command": asdict(docs_command),
        "product_statement": asdict(product_statement),
        "current_state": asdict(current_state),
        "system_boundary": asdict(system_boundary),
        "top_risks": top_risks,
        "confirmations_needed": [],
        "placeholders_detected": placeholders,
        "change_doc_count": change_doc_count,
        "trusted_floor_status": trusted_floor_status,
        "latest_tag": latest_tag,
        "head_commit": head_commit,
    }

    base_model["confirmations_needed"] = build_confirmations(base_model)

    return ProjectModel(
        stamp_utc=base_model["stamp_utc"],
        repo_path=base_model["repo_path"],
        repo_name=base_model["repo_name"],
        product_name=InferredField(**base_model["product_name"]),
        repo_type=InferredField(**base_model["repo_type"]),
        primary_language=InferredField(**base_model["primary_language"]),
        runtime=InferredField(**base_model["runtime"]),
        entrypoints=InferredField(**base_model["entrypoints"]),
        install_command=InferredField(**base_model["install_command"]),
        test_command=InferredField(**base_model["test_command"]),
        run_command=InferredField(**base_model["run_command"]),
        docs_command=InferredField(**base_model["docs_command"]),
        product_statement=InferredField(**base_model["product_statement"]),
        current_state=InferredField(**base_model["current_state"]),
        system_boundary=InferredField(**base_model["system_boundary"]),
        top_risks=base_model["top_risks"],
        confirmations_needed=base_model["confirmations_needed"],
        placeholders_detected=base_model["placeholders_detected"],
        change_doc_count=base_model["change_doc_count"],
        trusted_floor_status=base_model["trusted_floor_status"],
        latest_tag=base_model["latest_tag"],
        head_commit=base_model["head_commit"],
    )


def model_to_dict(model: ProjectModel) -> dict[str, Any]:
    return {
        "stamp_utc": model.stamp_utc,
        "repo_path": model.repo_path,
        "repo_name": model.repo_name,
        "product_name": asdict(model.product_name),
        "repo_type": asdict(model.repo_type),
        "primary_language": asdict(model.primary_language),
        "runtime": asdict(model.runtime),
        "entrypoints": asdict(model.entrypoints),
        "install_command": asdict(model.install_command),
        "test_command": asdict(model.test_command),
        "run_command": asdict(model.run_command),
        "docs_command": asdict(model.docs_command),
        "product_statement": asdict(model.product_statement),
        "current_state": asdict(model.current_state),
        "system_boundary": asdict(model.system_boundary),
        "top_risks": model.top_risks,
        "confirmations_needed": model.confirmations_needed,
        "placeholders_detected": model.placeholders_detected,
        "change_doc_count": model.change_doc_count,
        "trusted_floor_status": model.trusted_floor_status,
        "latest_tag": model.latest_tag,
        "head_commit": model.head_commit,
    }


def write_outputs(repo: Path, apply_docs: bool = True) -> dict[str, Any]:
    model = build_project_model(repo)
    data = model_to_dict(model)

    status_dir = repo / "docs/status"
    status_dir.mkdir(parents=True, exist_ok=True)

    (status_dir / "PROJECT_MODEL.json").write_text(
        json.dumps(data, indent=2) + "\n",
        encoding="utf-8",
    )

    score, issues = completeness_score(data)
    drift_findings = build_drift_findings(repo, data)

    (status_dir / "SDT_CONFIRMATION_PACKET.md").write_text(
        render_confirmation_packet(data) + "\n",
        encoding="utf-8",
    )
    (status_dir / "SDT_COMPLETENESS_REPORT.md").write_text(
        render_completeness_report(data, score, issues) + "\n",
        encoding="utf-8",
    )
    (status_dir / "SDT_DRIFT_REPORT.md").write_text(
        render_drift_report(data, drift_findings) + "\n",
        encoding="utf-8",
    )

    if apply_docs:
        managed_section(repo / "PROJECT_STATE.md", "inferred project state", render_project_state(data))
        managed_section(repo / "WHAT_IS_REAL_NOW.md", "inferred what is real now", render_what_is_real_now(data))
        managed_section(repo / "docs/product/PRODUCT_STATEMENT.md", "inferred product statement", render_product_statement(data))
        managed_section(repo / "docs/INSTALLATION.md", "inferred installation", render_installation(data))

    return {
        "model": data,
        "score": score,
        "issues": issues,
        "drift_findings": drift_findings,
        "status_dir": str(status_dir),
    }
