"""Configurable multi-team Product AI workflow (offline, standard library only).

This reference runtime plans transitions; it never calls an agent, GitHub or a
shell, and never claims a human has approved anything.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path


class WorkflowError(ValueError):
    """Invalid workflow specification or requested transition."""


@dataclass(frozen=True)
class Transition:
    source: str
    target: str
    actor: str
    gate: str


def require_mapping(value: object, name: str) -> dict:
    if not isinstance(value, dict):
        raise WorkflowError(f"{name}: expected object")
    return value


def require_string(value: object, name: str) -> str:
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise WorkflowError(f"{name}: expected nonempty trimmed string")
    return value


def validate_profile(profile: object) -> dict:
    p = require_mapping(profile, "profile")
    allowed = {"schema_version", "team", "project", "process", "roles", "models",
               "skills", "prompts", "limits", "automation"}
    if set(p) != allowed:
        raise WorkflowError(f"profile: missing={sorted(allowed-set(p))}, unknown={sorted(set(p)-allowed)}")
    if p["schema_version"] != "2":
        raise WorkflowError("schema_version: expected 2")
    team = require_mapping(p["team"], "team")
    if set(team) != {"id", "size"}:
        raise WorkflowError("team: expected id and size")
    require_string(team["id"], "team.id")
    if type(team["size"]) is not int or not 1 <= team["size"] <= 100:
        raise WorkflowError("team.size: expected integer 1..100")
    project = require_mapping(p["project"], "project")
    if set(project) != {"repository", "project_number"}:
        raise WorkflowError("project: expected repository and project_number")
    repository = require_string(project["repository"], "project.repository")
    if repository.count("/") != 1 or any(not x for x in repository.split("/")):
        raise WorkflowError("project.repository: expected owner/repo")
    if type(project["project_number"]) is not int or project["project_number"] < 1:
        raise WorkflowError("project.project_number: expected positive integer")
    process = require_mapping(p["process"], "process")
    if set(process) != {"stages", "transitions", "entry", "review", "handoff"}:
        raise WorkflowError("process: invalid fields")
    stages = require_mapping(process["stages"], "process.stages")
    if len(stages) < 3 or len(stages) > 30:
        raise WorkflowError("process.stages: expected 3..30 stages")
    labels = []
    for key, label in stages.items():
        require_string(key, "process.stage key")
        labels.append(require_string(label, f"process.stages.{key}"))
    if len(set(labels)) != len(labels):
        raise WorkflowError("process.stages: labels must be unique")
    entry, review, handoff = [require_string(process[k], f"process.{k}")
                              for k in ("entry", "review", "handoff")]
    if len({entry, review, handoff}) != 3 or not {entry, review, handoff} <= set(stages):
        raise WorkflowError("process: entry, review and handoff must be distinct valid stages")
    transitions = process["transitions"]
    if not isinstance(transitions, list) or not transitions or len(transitions) > 100:
        raise WorkflowError("process.transitions: expected 1..100 transitions")
    edges = set()
    graph = {key: set() for key in stages}
    for ix, item in enumerate(transitions):
        t = require_mapping(item, f"transitions[{ix}]")
        if set(t) != {"from", "to", "actor", "gate"}:
            raise WorkflowError(f"transitions[{ix}]: expected from/to/actor/gate")
        a, b = t["from"], t["to"]
        if a not in stages or b not in stages or a == b:
            raise WorkflowError(f"transitions[{ix}]: invalid endpoints")
        actor = require_string(t["actor"], "transition.actor")
        if actor not in ("controller", "human"):
            raise WorkflowError("transition.actor: only controller or human")
        if t["gate"] not in ("none", "human_approval"):
            raise WorkflowError("transition.gate: invalid")
        if (a, b) in edges:
            raise WorkflowError("process.transitions: duplicate edge")
        edges.add((a, b))
        graph[a].add(b)
        if b == handoff and (a != review or actor != "controller"
                             or t["gate"] != "human_approval"):
            raise WorkflowError("handoff: every incoming edge must be controller + verified human_approval from review")
        if t["gate"] == "human_approval" and (b != handoff or a != review):
            raise WorkflowError("human_approval gate is reserved for final review handoff")
    if (review, handoff) not in edges:
        raise WorkflowError("process: missing human-approved handoff")
    visited = {entry}
    queue = [entry]
    for node in queue:
        for target in graph[node]:
            if target not in visited:
                visited.add(target)
                queue.append(target)
    if review not in visited or handoff not in visited:
        raise WorkflowError("process: no reachable review/handoff path")
    if any(a == handoff for a, _ in edges):
        raise WorkflowError("handoff: terminal stage cannot start another transition")
    roles = require_mapping(p["roles"], "roles")
    if not roles or "product" not in roles:
        raise WorkflowError("roles: must include product")
    for key, value in roles.items():
        require_string(key, "role")
        members = require_mapping(value, f"roles.{key}")
        if set(members) != {"reviewers", "model", "skills", "prompt"}:
            raise WorkflowError(f"roles.{key}: invalid fields")
        if not isinstance(members["reviewers"], list) or not members["reviewers"]:
            raise WorkflowError(f"roles.{key}.reviewers: nonempty list required")
        if len(set(members["reviewers"])) != len(members["reviewers"]):
            raise WorkflowError(f"roles.{key}: duplicate reviewer")
        for v in members["reviewers"]:
            require_string(v, "reviewer")
        for field in ("model", "prompt"):
            require_string(members[field], f"roles.{key}.{field}")
        if not isinstance(members["skills"], list):
            raise WorkflowError(f"roles.{key}.skills: expected array")
        for v in members["skills"]:
            require_string(v, "skill")
    models = require_mapping(p["models"], "models")
    if not models:
        raise WorkflowError("models: at least one route")
    for key, m in models.items():
        require_string(key, "models key")
        require_mapping(m, f"models.{key}")
        if set(m) != {"provider", "model", "effort"}:
            raise WorkflowError(f"models.{key}: invalid fields")
        require_string(m["provider"], "provider")
        require_string(m["model"], "model")
        if m["effort"] not in ("low", "medium", "high", "xhigh"):
            raise WorkflowError("models.effort: invalid")
    if not isinstance(p["skills"], list) or not isinstance(p["prompts"], list):
        raise WorkflowError("skills/prompts: expected arrays")
    for name in p["skills"] + p["prompts"]:
        require_string(name, "asset reference")
        if name.startswith("/") or ".." in name.split("/") or "://" in name:
            raise WorkflowError("asset reference: must be a project-relative, non-traversing identifier")
    for name, role in roles.items():
        if role["model"] not in models or role["prompt"] not in p["prompts"]:
            raise WorkflowError(f"roles.{name}: unknown model or prompt")
        if not set(role["skills"]) <= set(p["skills"]):
            raise WorkflowError(f"roles.{name}: unknown skill")
    limits = require_mapping(p["limits"], "limits")
    if set(limits) != {"concurrency", "max_agent_calls", "max_attempts"}:
        raise WorkflowError("limits: invalid fields")
    for key, maximum in (("concurrency", 16), ("max_agent_calls", 20), ("max_attempts", 10)):
        val = limits[key]
        if type(val) is not int or not 1 <= val <= maximum:
            raise WorkflowError(f"limits.{key}: expected integer 1..{maximum}")
    automation = require_mapping(p["automation"], "automation")
    if set(automation) != {"mode", "require_human_approval", "allow_implementation"}:
        raise WorkflowError("automation: invalid fields")
    if automation != {"mode": "dry_run", "require_human_approval": True,
                      "allow_implementation": False}:
        raise WorkflowError("automation: only human-gated, no-implementation dry_run is available")
    return p


def plan_transition(profile: dict, current: str, target: str,
                    actor: str = "controller", approved: bool = False) -> dict:
    """Plan only; supplied approval is NOT trusted evidence, even if true."""
    p = validate_profile(profile)
    if current not in p["process"]["stages"] or target not in p["process"]["stages"]:
        raise WorkflowError("transition: unknown stage")
    match = next((edge for edge in p["process"]["transitions"]
                  if edge["from"] == current and edge["to"] == target), None)
    if match is None:
        raise WorkflowError("transition: edge not declared")
    if match["actor"] != actor:
        raise WorkflowError("transition: actor not authorized")
    gated = match["gate"] == "human_approval"
    return {"from": current, "to": target, "team": p["team"]["id"],
            "requires_verified_human_approval": gated,
            "status": "blocked_pending_external_approval_verifier" if gated else "proposed",
            "remote_changes": False, "approval_claim_ignored": approved}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    parser.add_argument("--from-stage", dest="source")
    parser.add_argument("--to-stage", dest="target")
    args = parser.parse_args()
    try:
        p = validate_profile(json.loads(args.config.read_text(encoding="utf-8")))
        if (args.source is None) != (args.target is None):
            parser.error("--from-stage and --to-stage must be supplied together")
        result = plan_transition(p, args.source, args.target) if args.source else {
            "valid": True, "team": p["team"]["id"], "stages": p["process"]["stages"],
            "roles": list(p["roles"]), "remote_changes": False}
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Invalid workflow: {exc}\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
