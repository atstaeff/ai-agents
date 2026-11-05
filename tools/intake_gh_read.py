"""Read-only GitHub Projects discovery for the WSL Product Intake pilot.

Uses GitHub CLI; does not create comments, assign issues or change project fields.
This discovery adapter is capped and is NOT the eventual paginated GraphQL service.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess

from intake_workflow import validate_profile, WorkflowError


def parse_items(payload: object, repository: str, statuses: set[str]) -> list[dict]:
    if not isinstance(payload, dict) or not isinstance(payload.get("items"), list):
        raise WorkflowError("GitHub Projects response: expected object containing items array")
    found = []
    for item in payload["items"]:
        if not isinstance(item, dict) or not isinstance(item.get("content"), dict):
            continue
        content = item["content"]
        if content.get("repository") != repository:
            continue
        if item.get("status") not in statuses:
            continue
        if type(content.get("number")) is not int or content["number"] < 1:
            continue
        if content.get("type") not in (None, "Issue"):
            continue
        found.append({
            "project_item_id": item.get("id"),
            "repository": repository,
            "issue_number": content["number"],
            "title": content.get("title", item.get("title", "")),
            "status": item["status"],
            "url": content.get("url"),
            "action": "observe_only",
        })
    return found


def list_candidates(profile: dict, *, limit: int = 100, runner=subprocess.run) -> dict:
    config = validate_profile(profile)
    if type(limit) is not int or not 1 <= limit <= 100:
        raise WorkflowError("limit must be between 1 and 100 for the CLI pilot")
    repository = config["project"]["repository"]
    owner = repository.split("/", 1)[0]
    project_no = str(config["project"]["project_number"])
    argv = ["gh", "project", "item-list", project_no, "--owner", owner,
            "--format", "json", "--limit", str(limit)]
    try:
        result = runner(argv, text=True, capture_output=True, timeout=30, check=True)
        payload = json.loads(result.stdout)
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError) as exc:
        raise WorkflowError("GitHub Project read failed; confirm gh authentication, "
                            "project access and API availability") from exc
    stages = config["process"]
    statuses = {stages["stages"][stages["entry"]]}
    # Observe items already claimed by a controller too, but never move them.
    if "claimed" in stages["stages"]:
        statuses.add(stages["stages"]["claimed"])
    candidates = parse_items(payload, repository, statuses)
    return {
        "team": config["team"]["id"], "repository": repository,
        "items": candidates, "count": len(candidates),
        "possibly_truncated": len(payload["items"]) >= limit,
        "remote_changes": False, "actual_ai_execution": False,
        "warning": "Read-only bounded CLI pilot; for large boards use paginated GraphQL",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    parser.add_argument("--limit", type=int, default=100)
    args = parser.parse_args()
    try:
        p = json.loads(args.config.read_text(encoding="utf-8"))
        output = list_candidates(p, limit=args.limit)
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Read-only discovery failed: {exc}\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
