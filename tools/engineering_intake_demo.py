"""Safe offline simulation of a GitHub Projects Engineering Intake board."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COLUMNS = (
    "Backlog", "AI Takes Over", "AI Working", "Human Review", "Changes Requested", "Ready for Engineering",
)
MODEL_ROUTES = {
    "default": {"model": "opencode/gpt-6.1-sol", "effort": "medium"},
    "architecture": {"model": "opencode/gpt-6-astra", "effort": "xhigh"},
}


def assess(issue: dict, adrs: list[dict]) -> dict:
    """Return a proposed board action; never mutate a remote resource."""
    required = ("problem", "outcome", "scope", "owner")
    missing = [key for key in required if not str(issue.get(key, "")).strip()]
    acceptance = issue.get("acceptance_criteria")
    if not isinstance(acceptance, list) or not acceptance or not all(
        isinstance(x, str) and x.strip() for x in acceptance
    ):
        missing.append("acceptance_criteria")
    known = {d["id"]: d for d in adrs}
    ids = issue.get("referenced_adrs", [])
    unknown = [key for key in ids if key not in known]
    accepted = [key for key in ids if key in known and known[key]["status"] == "accepted"]
    informative = [key for key in ids if key in known and known[key]["status"] != "accepted"]
    review_roles = ["product-owner"]
    if issue.get("architecture_change"):
        review_roles.append("architecture-owner")
    if issue.get("security_impact"):
        review_roles.append("security-owner")
    questions = [f"Provide {key}" for key in missing]
    questions += [f"Resolve ADR reference {key}" for key in unknown]
    if issue.get("architecture_change") and not accepted:
        questions.append("Architecture owner must verify applicable accepted decisions")
    proposed = "Human Review"
    fingerprint = hashlib.sha256(json.dumps(
        {"issue": issue, "adrs": adrs}, sort_keys=True
    ).encode()).hexdigest()[:16]
    return {
        "issue": issue.get("number"),
        "previous_column": "AI Working",
        "proposed_column": proposed,
        "review_roles": review_roles,
        "questions": questions,
        "review_blocked": bool(questions),
        "accepted_adr_evidence": accepted,
        "informative_adrs": informative,
        "architecture_assessment": "human_required" if issue.get("architecture_change") else "not_applicable",
        "fingerprint": fingerprint,
        "model_routes": MODEL_ROUTES,
        "remote_changes": False,
        "actual_ai_execution": False,
    }


def simulate(data: dict) -> dict:
    board = [{"column": "Backlog", "event": "Issue opened"},
             {"column": "AI Takes Over", "event": "Intake claimed issue"},
             {"column": "AI Working", "event": "Mechanical checks started"}]
    report = assess(data["issue"], data["decisions"])
    board.append({"column": report["proposed_column"], "event": "Proposal only; no GitHub write"})
    return {"board": board, "report": report,
            "approval_gate": "Only authorized human approval on the same issue revision may reach Ready for Engineering"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=ROOT / "examples/intake/fixture.json")
    args = parser.parse_args()
    data = json.loads(args.fixture.read_text(encoding="utf-8"))
    print(json.dumps(simulate(data), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
