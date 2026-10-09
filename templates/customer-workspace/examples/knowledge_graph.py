# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML>=6,<7"]
# ///
"""Generate a local knowledge index, Mermaid map and JSON from Markdown metadata."""

import argparse
from collections import deque
import json
from pathlib import Path
import re
import sys

import yaml

MARKER = "<!-- generated-by: knowledge_graph.py; do not edit -->"
RELATIONS = {"depends_on", "supersedes", "relates_to", "governed_by", "reports_on"}
STATUSES = {"proposed", "accepted", "rejected", "deprecated", "superseded", "draft"}


def load_graph(root):
    nodes = {}
    slugs = set()
    for path in sorted(root.rglob("*.md")):
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            raise ValueError(f"Knowledge source must be inside workspace: {path}")
        text = path.read_text(encoding="utf-8")
        is_adr = path.relative_to(root).parts[0] == "decisions" and re.match(r"\d{4}-", path.name)
        if not text.startswith("---\n"):
            if is_adr:
                raise ValueError(f"ADR needs metadata: {path}")
            continue
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not frontmatter:
            raise ValueError(f"Unclosed frontmatter: {path}")
        meta = yaml.safe_load(frontmatter.group(1))
        if not isinstance(meta, dict):
            raise ValueError(f"Expected metadata mapping: {path}")
        if "knowledge_id" not in meta:
            if is_adr:
                raise ValueError(f"ADR needs knowledge_id: {path}")
            continue
        ident = meta["knowledge_id"]
        if not isinstance(ident, str) or not re.fullmatch(r"[A-Z][A-Z0-9-]*", ident):
            raise ValueError(f"Invalid knowledge_id: {path}")
        if ident in nodes:
            raise ValueError(f"Duplicate knowledge_id: {ident}")
        if meta.get("status") not in STATUSES:
            raise ValueError(f"Unknown status: {ident}")
        for key in ("title", "owner", "slug"):
            if not isinstance(meta.get(key), str) or not meta[key].strip():
                raise ValueError(f"Missing {key}: {ident}")
        slug = meta["slug"]
        if not re.fullmatch(r"[a-z0-9-]+(?:/[a-z0-9-]+)*", slug) or slug in slugs:
            raise ValueError(f"Invalid or duplicate slug: {ident}")
        slugs.add(slug)
        relations = meta.get("relations", {})
        if not isinstance(relations, dict) or not relations.keys() <= RELATIONS:
            raise ValueError(f"Unknown relation type: {ident}")
        for kind, targets in relations.items():
            if not isinstance(targets, list) or not all(isinstance(x, str) for x in targets):
                raise ValueError(f"{kind} must be a list of knowledge IDs: {ident}")
        sources = meta.get("sources", [])
        if not isinstance(sources, list) or not all(isinstance(x, str) and x.startswith("https://") for x in sources):
            raise ValueError(f"sources must contain HTTPS evidence links: {ident}")
        nodes[ident] = {"id": ident, "title": meta["title"], "status": meta["status"],
                        "owner": meta["owner"], "slug": slug,
                        "path": path.relative_to(root).as_posix(),
                        "sources": sources, "relations": relations}
    edges = []
    for ident, node in nodes.items():
        for kind, targets in sorted(node["relations"].items()):
            for target in sorted(set(targets)):
                if target not in nodes or target == ident:
                    raise ValueError(f"Unknown or self reference: {ident} {kind} {target}")
                if kind in {"depends_on", "supersedes"}:
                    if not ident.startswith("ADR-") or not target.startswith("ADR-"):
                        raise ValueError(f"{kind} connects ADRs only")
                if kind == "supersedes" and (node["status"] not in {"accepted", "superseded", "deprecated"} or nodes[target]["status"] != "superseded"):
                    raise ValueError("supersedes requires an agreed replacement and a superseded old ADR; use relates_to for a proposal")
                edges.append({"source": ident, "target": target, "type": kind})
    # Replacing or depending on a decision cannot form a directed cycle.
    for kind in ("depends_on", "supersedes"):
        indegree = dict.fromkeys(nodes, 0)
        neighbors = {ident: [] for ident in nodes}
        for edge in edges:
            if edge["type"] == kind:
                neighbors[edge["source"]].append(edge["target"])
                indegree[edge["target"]] += 1
        queue = deque(ident for ident in nodes if indegree[ident] == 0)
        visited = 0
        while queue:
            ident = queue.popleft()
            visited += 1
            for target in neighbors[ident]:
                indegree[target] -= 1
                if indegree[target] == 0:
                    queue.append(target)
        if visited != len(nodes):
            raise ValueError(f"Cycle in {kind} relations")
    return {"schema_version": 1, "nodes": list(nodes.values()), "edges": edges}


def cell(value):
    return str(value).replace("\n", " ").replace("|", "\\|").replace("[", "\\[").replace("]", "\\]").replace("<", "&lt;")


def render(graph):
    if not graph["nodes"]:
        return "---\ntitle: Knowledge map\nslug: knowledge-map\n---\n\n" + MARKER + "\n\n# Knowledge map\n\nNo records with knowledge_id were found.\n"
    lines = ["---", "title: Knowledge map", "slug: knowledge-map", "---", "", MARKER,
             "", "# Knowledge map", "", "Generated from workspace metadata. Statuses describe records, not deployed behavior.",
             "", "## Records", "", "| Record | Title | Status | Owner |", "| --- | --- | --- | --- |"]
    for n in graph["nodes"]:
        lines.append(f"| [{n['id']}]({n['path']}) | {cell(n['title'])} | {n['status']} | {cell(n['owner'])} |")
    lines += ["", "## Relationships", "", "```mermaid", "flowchart TD"]
    aliases = {n["id"]: f"n{i}" for i, n in enumerate(graph["nodes"])}
    for n in graph["nodes"]:
        lines.append(f"  {aliases[n['id']]}[\"{n['id']} ({n['status']})\"]")
    for e in graph["edges"]:
        lines.append(f"  {aliases[e['source']]} -->|{e['type']}| {aliases[e['target']]}")
    lines += ["```", "", "## Relationship links", "", "| Record | Relation | Target |", "| --- | --- | --- |"]
    paths = {n["id"]: n["path"] for n in graph["nodes"]}
    for e in graph["edges"]:
        lines.append(f"| [{e['source']}]({paths[e['source']]}) | {e['type']} | [{e['target']}]({paths[e['target']]}) |")
    return "\n".join(lines) + "\n"


def write_changed(path, text, protect=False):
    if path.exists():
        current = path.read_text(encoding="utf-8")
        if protect and MARKER not in current:
            raise ValueError(f"Refusing to overwrite a manual page: {path}")
        if current == text:
            return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument("--json", type=Path, required=True, help="Generated JSON path, outside workspace")
    args = parser.parse_args()
    root = args.workspace.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("workspace must be a directory")
    output = args.json.resolve()
    if output.is_relative_to(root):
        raise ValueError("Keep the JSON output outside workspace")
    graph = load_graph(root)
    page = root / "knowledge-map.md"
    write_changed(page, render(graph), protect=True)
    write_changed(output, json.dumps(graph, indent=2, ensure_ascii=False) + "\n")
    print(f"Generated {len(graph['nodes'])} records and {len(graph['edges'])} relations")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, yaml.YAMLError) as error:
        sys.exit(str(error))
