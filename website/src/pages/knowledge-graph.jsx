import React, { useMemo, useState } from "react";
import Layout from "@theme/Layout";
import Link from "@docusaurus/Link";
import useBaseUrl from "@docusaurus/useBaseUrl";
import graph from "@site/.generated/knowledge-graph.json";
import "@site/src/css/knowledge-graph.css";

const kinds = {
  decision: "Decision",
  topic: "AI topic",
  component: "Component",
};
const colors = { decision: "var(--ifm-color-primary)", topic: "#7f8bb5", component: "#b17c46" };
const incomingLabels = {
  depends_on: "required by",
  supersedes: "superseded by",
  relates_to: "relates to",
  governed_by: "governs",
};
const labels = {
  depends_on: "depends on",
  supersedes: "supersedes",
  relates_to: "relates to",
  governed_by: "governed by",
};
const byId = new Map(graph.nodes.map((node) => [node.id, node]));
const counts = Object.fromEntries(
  Object.keys(kinds).map((kind) => [
    kind,
    graph.nodes.filter((n) => n.kind === kind).length,
  ]),
);
function shortTitle(title) {
  const words = title.split(" "),
    lines = [""];
  for (const word of words) {
    if ((lines.at(-1) + " " + word).trim().length > 27) lines.push(word);
    else lines[lines.length - 1] = (lines.at(-1) + " " + word).trim();
  }
  return lines;
}

export default function Home() {
  const base = useBaseUrl("/");
  const href = (node) => base + node.href.slice(1);
  const [query, setQuery] = useState("");
  const [kind, setKind] = useState("all");
  const [status, setStatus] = useState("all");
  const [selected, setSelected] = useState("ADR-0002");
  const nodes = useMemo(
    () =>
      graph.nodes.filter(
        (n) =>
          (kind === "all" || n.kind === kind) &&
          (status === "all" || n.status === status) &&
          `${n.title} ${n.id} ${n.owner}`
            .toLowerCase()
            .includes(query.toLowerCase()),
      ),
    [query, kind, status],
  );
  const positions = new Map(
    nodes.map((n, i) => [
      n.id,
      { x: 138 + (i % 3) * 258, y: 74 + Math.floor(i / 3) * 148 },
    ]),
  );
  const edges = graph.edges.filter(
    (e) => positions.has(e.source) && positions.has(e.target),
  );
  const current = nodes.find((n) => n.id === selected);
  const related = current
    ? graph.edges.filter(
        (e) => e.source === current.id || e.target === current.id,
      )
    : [];
  const neighbors = new Set(related.flatMap((e) => [e.source, e.target]));
  function focus(id) {
    setQuery("");
    setKind("all");
    setStatus("all");
    setSelected(id);
  }
  function reset() {
    setQuery("");
    setKind("all");
    setStatus("all");
  }

  return (
    <Layout
      title="Knowledge graph"
      description="Explore shared engineering decisions, components and AI knowledge."
    >
      <main className="atlas">
        <section className="atlas-hero">
          <div>
            <p className="eyebrow">
              <span className="live-dot" /> SHARED KNOWLEDGE / DOCUMENT
              UNDERSTANDING
            </p>
            <h1>
              Decisions outlast
              <br />
              <em>conversations.</em>
            </h1>
            <p className="hero-copy">
              A clear view of what we chose, why it matters, and what it
              changes.
              <br className="desktop-break" /> Personal plans stay in your
              Second Brain. Useful knowledge stays here.
            </p>
            <div className="hero-links">
              <a className="atlas-button" href="#explore">
                Explore the graph <span>↘</span>
              </a>
              <Link className="quiet-link" to={base + "demo-knowledge/intro/"}>
                Read the engineering model <span>↗</span>
              </Link>
            </div>
          </div>
          <div className="hero-aside">
            <span className="aside-number">01 / 03</span>
            <h2>
              Plan privately.
              <br />
              Build with evidence.
              <br />
              Preserve the why.
            </h2>
            <p>
              A small project knowledge system,
              <br />
              generated from shared Markdown.
            </p>
            <span className="demo-label">FICTIONAL PROJECT DEMO</span>
          </div>
        </section>
        <section className="atlas-stats" aria-label="Knowledge summary">
          {[
            ["decision", "Decisions with rationale"],
            ["topic", "AI knowledge topics"],
            ["component", "System components"],
          ].map(([key, title]) => (
            <div key={key}>
              <strong>{String(counts[key]).padStart(2, "0")}</strong>
              <span>{title}</span>
              <i style={{ background: colors[key] }} />
            </div>
          ))}
          <div>
            <strong>{graph.edges.length}</strong>
            <span>Explicit relationships</span>
            <i className="relationship-mark">↗</i>
          </div>
        </section>
        <section className="explore-section" id="explore">
          <div className="section-heading">
            <div>
              <p className="eyebrow">EXPLORE THE CONTEXT</p>
              <h2>Connected, not scattered.</h2>
            </div>
            <p>
              Select a record to see its relationships.
              <br />
              Open the original document for the full context.
            </p>
          </div>
          <div className="graph-toolbar">
            <label className="search-label">
              <span aria-hidden="true">⌕</span>
              <input
                aria-label="Search knowledge"
                type="search"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Search decisions, topics, components…"
              />
            </label>
            <div className="kind-filters" role="group" aria-label="Record type">
              {[
                ["all", "All records"],
                ["decision", "Decisions"],
                ["topic", "AI topics"],
                ["component", "Components"],
              ].map(([value, label]) => (
                <button
                  key={value}
                  type="button"
                  aria-pressed={kind === value}
                  onClick={() => setKind(value)}
                >
                  {label}
                </button>
              ))}
            </div>
            <select
              aria-label="Record status"
              value={status}
              onChange={(e) => setStatus(e.target.value)}
            >
              <option value="all">All statuses</option>
              <option value="accepted">Accepted</option>
              <option value="proposed">Proposed</option>
              <option value="superseded">Superseded</option>
              <option value="current">Current knowledge</option>
            </select>
          </div>
          <div className="graph-workspace">
            <div className="graph-canvas">
              <div className="graph-meta">
                <span aria-live="polite">
                  {nodes.length} records · {edges.length} relationships
                </span>
                <button type="button" className="reset-button" onClick={reset}>
                  Reset filters ↺
                </button>
              </div>
              {nodes.length === 0 ? (
                <div className="empty-state">
                  <h3>No matching knowledge</h3>
                  <p>Try a different term or clear the filters.</p>
                  <button className="atlas-button" onClick={reset}>
                    Show all records
                  </button>
                </div>
              ) : (
                <svg
                  className="knowledge-svg"
                  viewBox={`0 0 792 ${Math.max(200, Math.ceil(nodes.length / 3) * 148 + 18)}`}
                  role="group"
                  aria-label="Interactive engineering knowledge graph"
                >
                  <defs>
                    <marker
                      id="arrow"
                      viewBox="0 0 10 10"
                      refX="9"
                      refY="5"
                      markerWidth="5"
                      markerHeight="5"
                      orient="auto-start-reverse"
                    >
                      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor" />
                    </marker>
                  </defs>
                  {edges.map((edge, i) => {
                    const a = positions.get(edge.source),
                      b = positions.get(edge.target);
                    const dx = b.x - a.x,
                      dy = b.y - a.y;
                    const scale = Math.min(
                      dx ? 111 / Math.abs(dx) : Infinity,
                      dy ? 49 / Math.abs(dy) : Infinity,
                    );
                    const active =
                      current &&
                      (edge.source === selected || edge.target === selected);
                    // Slightly separate opposite directed relationships, retaining clear node endpoints.
                    const bend = (i % 2 ? 1 : -1) * 24;
                    const sx = a.x + dx * scale,
                      sy = a.y + dy * scale;
                    const tx = b.x - dx * scale,
                      ty = b.y - dy * scale;
                    return (
                      <path
                        key={`${edge.source}-${edge.type}-${edge.target}`}
                        d={`M ${sx} ${sy} Q ${(sx + tx) / 2 + (dy ? bend : 0)} ${(sy + ty) / 2 + (dx ? bend : 0)} ${tx} ${ty}`}
                        className={`graph-edge ${active ? "active" : ""}`}
                        markerEnd="url(#arrow)"
                      >
                        <title>{`${edge.source} ${labels[edge.type]} ${edge.target}`}</title>
                      </path>
                    );
                  })}
                  {nodes.map((node) => {
                    const p = positions.get(node.id),
                      lines = shortTitle(node.title);
                    const chosen = node.id === selected;
                    return (
                      <g
                        key={node.id}
                        transform={`translate(${p.x - 111} ${p.y - 49})`}
                        className={`graph-node ${chosen ? "selected" : ""} ${current && !neighbors.has(node.id) ? "muted" : ""}`}
                        tabIndex="0"
                        role="button"
                        aria-label={`${node.id}: ${node.title}, ${node.status}`}
                        aria-pressed={chosen}
                        onClick={() => setSelected(node.id)}
                        onKeyDown={(e) => {
                          if (e.key === "Enter" || e.key === " ") {
                            e.preventDefault();
                            setSelected(node.id);
                          }
                        }}
                      >
                        <rect width="222" height="98" rx="10" />
                        <circle
                          cx="17"
                          cy="20"
                          r="4"
                          fill={colors[node.kind]}
                        />
                        <text x="29" y="24" className="node-id">
                          {node.id}
                        </text>
                        {lines.slice(0, 2).map((line, i) => (
                          <text
                            key={i}
                            x="16"
                            y={47 + i * 16}
                            className="node-title"
                          >
                            {line}
                          </text>
                        ))}
                        <text
                          x="16"
                          y="84"
                          className={`node-status ${node.status}`}
                        >
                          {node.status.toUpperCase()}
                        </text>
                        <text
                          x="202"
                          y="84"
                          textAnchor="end"
                          className="node-open"
                        >
                          ↗
                        </text>
                      </g>
                    );
                  })}
                </svg>
              )}
              <div className="graph-legend">
                {Object.entries(kinds).map(([key, label]) => (
                  <span key={key}>
                    <i style={{ background: colors[key] }} />
                    {label}
                  </span>
                ))}
                <span className="legend-note">
                  Edges follow explicit Markdown relationships
                </span>
              </div>
            </div>
            <aside
              className="record-panel"
              aria-label="Selected record"
              aria-live="polite"
            >
              {current ? (
                <>
                  <p className="eyebrow">
                    SELECTED {kinds[current.kind].toUpperCase()}
                  </p>
                  <div className="panel-id">
                    {current.id}
                    <span className={`status-badge ${current.status}`}>
                      {current.status}
                    </span>
                  </div>
                  <h3>{current.title}</h3>
                  <p className="owner-line">
                    OWNER <strong>{current.owner}</strong>
                  </p>
                  <Link className="atlas-button source-link" to={href(current)}>
                    Open documentation <span>↗</span>
                  </Link>
                  <h4>
                    Connected knowledge <span>{related.length}</span>
                  </h4>
                  <ul className="relationship-list">
                    {related.map((edge, i) => {
                      const outgoing = edge.source === current.id;
                      const other = byId.get(
                        outgoing ? edge.target : edge.source,
                      );
                      return (
                        <li key={i}>
                          <span>
                            {outgoing
                              ? labels[edge.type]
                              : incomingLabels[edge.type]}
                          </span>
                          <button type="button" onClick={() => focus(other.id)}>
                            {other.title}
                            <small>{other.id} ↗</small>
                          </button>
                        </li>
                      );
                    })}
                  </ul>
                  <p className="source-caption">
                    Source: <code>{current.path}</code>
                  </p>
                </>
              ) : (
                <div className="panel-placeholder">
                  <span>↖</span>
                  <h3>Pick a record</h3>
                  <p>
                    Select a node or a record below to inspect its context and
                    relationships.
                  </p>
                </div>
              )}
            </aside>
          </div>
          <details className="record-directory">
            <summary>
              Browse records as a list <span>{nodes.length} records</span>
            </summary>
            <div className="record-table-wrap">
              <table>
                <thead>
                  <tr>
                    <th>Record</th>
                    <th>Type</th>
                    <th>Status</th>
                    <th>Documentation</th>
                  </tr>
                </thead>
                <tbody>
                  {nodes.map((node) => (
                    <tr key={node.id}>
                      <td>
                        <button
                          type="button"
                          onClick={() => setSelected(node.id)}
                        >
                          {node.title}
                        </button>
                        <small>{node.id}</small>
                      </td>
                      <td>{kinds[node.kind]}</td>
                      <td>
                        <span className={`status-badge ${node.status}`}>
                          {node.status}
                        </span>
                      </td>
                      <td>
                        <Link to={href(node)}>Read record ↗</Link>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </details>
        </section>
        <section className="ownership-note">
          <span>KEEP THE BOUNDARY CLEAR</span>
          <h2>
            Your plan is personal.
            <br />
            The result belongs to the project.
          </h2>
          <p>
            This atlas contains shared decisions and current knowledge. It never
            imports
            <br className="desktop-break" /> private working plans, chat
            histories or Obsidian vault content.
          </p>
          <Link to={base + "demo-knowledge/decisions/private-plans/"}>
            Read the decision ↗
          </Link>
        </section>
      </main>
    </Layout>
  );
}
