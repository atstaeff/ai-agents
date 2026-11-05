"""Create a project-local Product Intake starter without editing existing files.

Offline scaffolding only: no GitHub API writes, no LLM or Herdr execution.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
PROFILES = ROOT / "examples" / "intake" / "profiles"
PROMPTS = ROOT / "examples" / "intake" / "prompts"
SNIPPET = """## Product AI Intake

- Read .product-intake/config.json (schema v2) and the adopted Product Intake
  policy pinned to a reviewed ai-agents release/commit.
- Product AI performs requirements refinement and consults read-only specialists.
- It must not write implementation code, self-approve, or start Engineering AI.
- Human approvals are required before Ready for Engineering.
- GitHub Project remains the authoritative status and issue record.
- This starter is OFFLINE ONLY; no GitHub watcher or OpenCode runtime is installed.
"""


def scaffold(target: Path, size: int) -> list[Path]:
    if size not in (3, 10, 20):
        raise ValueError("size must be 3, 10 or 20")
    root = target.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("target must be an existing directory")
    directory = root / ".product-intake"
    source = PROFILES / f"team-{size}.json"
    outputs = [(source, directory / "config.json")]
    outputs.extend((p, directory / "prompts" / p.name) for p in sorted(PROMPTS.glob("*.md")))
    snippet = directory / "AGENTS.snippet.md"
    # Fail as a unit: no overwrites or partial writes on normal conflicts.
    if any(out.exists() or out.is_symlink() for _, out in outputs) or snippet.exists() or snippet.is_symlink():
        raise FileExistsError("Product Intake scaffold already exists; review and migrate manually")
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "prompts").mkdir(parents=True, exist_ok=True)
    created = []
    for src, dest in outputs:
        shutil.copyfile(src, dest)
        created.append(dest)
    snippet.write_text(SNIPPET, encoding="utf-8")
    created.append(snippet)
    return created


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--team-size", type=int, choices=(3, 10, 20), required=True)
    args = parser.parse_args()
    try:
        paths = scaffold(args.target, args.team_size)
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Scaffolding failed: {exc}\n")
    for path in paths:
        print(path)
    print("Review project IDs, approvers and approved models; merge AGENTS.snippet.md manually.")


if __name__ == "__main__":
    main()
