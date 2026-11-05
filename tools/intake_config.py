"""Validate a project-owned Product Intake config (stdlib only, no side effects)."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

STAGES = ("backlog", "claimed", "working", "review", "ready")
FIELDS = ("problem", "outcome", "scope", "acceptance_criteria", "owner")
LEVELS = ("low", "medium", "high", "xhigh")


class ConfigError(ValueError):
    pass


def _mapping(value: object, keys: set[str], where: str) -> dict:
    if not isinstance(value, dict):
        raise ConfigError(f"{where}: expected object")
    unexpected = set(value) - keys
    missing = keys - set(value)
    if unexpected or missing:
        raise ConfigError(f"{where}: unknown={sorted(unexpected)}, missing={sorted(missing)}")
    return value


def _string(value: object, where: str) -> str:
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise ConfigError(f"{where}: expected nonempty trimmed string")
    return value


def _positive(value: object, where: str, maximum: int) -> None:
    if type(value) is not int or value < 1 or value > maximum:
        raise ConfigError(f"{where}: integer must be between 1 and {maximum}")


def validate(data: object) -> dict:
    d = _mapping(data, {"schema_version", "project", "workflow", "reviewers", "checks", "models", "limits", "automation"}, "root")
    if d["schema_version"] != "1":
        raise ConfigError("schema_version: unsupported; fail closed until migrated")
    project = _mapping(d["project"], {"repository", "project_number", "status_field"}, "project")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", _string(project["repository"], "project.repository")):
        raise ConfigError("project.repository: expected owner/repository")
    _positive(project["project_number"], "project.project_number", 1000000)
    _string(project["status_field"], "project.status_field")
    workflow = _mapping(d["workflow"], set(STAGES), "workflow")
    statuses = [_string(workflow[k], f"workflow.{k}") for k in STAGES]
    if len(set(statuses)) != len(statuses):
        raise ConfigError("workflow: statuses must be unique")
    reviewers = _mapping(d["reviewers"], {"product", "architecture", "security"}, "reviewers")
    for role, accounts in reviewers.items():
        if not isinstance(accounts, list) or not accounts or len(accounts) != len(set(map(str, accounts))):
            raise ConfigError(f"reviewers.{role}: expected nonempty unique account/role list")
        for account in accounts:
            _string(account, f"reviewers.{role}")
    checks = _mapping(d["checks"], {"required", "architecture", "security"}, "checks")
    required = checks["required"]
    if not isinstance(required, list) or any(not isinstance(x, str) or x not in FIELDS for x in required) or len(set(required)) != len(required):
        raise ConfigError("checks.required: invalid or duplicate field")
    if not set(FIELDS).issubset(required):
        raise ConfigError("checks.required: central readiness minimum cannot be disabled")
    for key in ("architecture", "security"):
        if checks[key] not in ("risk_based", "required"):
            raise ConfigError(f"checks.{key}: cannot disable control")
    models = _mapping(d["models"], {"specialist", "architecture"}, "models")
    for name, model in models.items():
        m = _mapping(model, {"provider", "id", "effort"}, f"models.{name}")
        _string(m["provider"], f"models.{name}.provider")
        _string(m["id"], f"models.{name}.id")
        if m["effort"] not in LEVELS:
            raise ConfigError(f"models.{name}.effort: invalid value")
    limits = _mapping(d["limits"], {"max_concurrent_issues", "max_agent_calls_per_issue", "max_attempts"}, "limits")
    _positive(limits["max_concurrent_issues"], "limits.max_concurrent_issues", 16)
    _positive(limits["max_agent_calls_per_issue"], "limits.max_agent_calls_per_issue", 20)
    _positive(limits["max_attempts"], "limits.max_attempts", 10)
    auto = _mapping(d["automation"], {"mode", "allow_engineering", "require_human_approval"}, "automation")
    if auto["mode"] != "dry_run":
        raise ConfigError("automation.mode: only dry_run is implemented")
    if auto["allow_engineering"] is not False or auto["require_human_approval"] is not True:
        raise ConfigError("automation: Product AI cannot perform engineering or bypass human approval")
    return d


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    args = parser.parse_args()
    try:
        validate(json.loads(args.config.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError, ConfigError) as exc:
        parser.exit(2, f"Invalid Product Intake configuration: {exc}\n")
    print("Product Intake configuration valid (offline contract; no live automation)")


if __name__ == "__main__":
    main()
