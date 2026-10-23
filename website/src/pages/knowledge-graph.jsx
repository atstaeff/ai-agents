import React, { useEffect, useState } from "react";
import Layout from "@theme/Layout";
import Link from "@docusaurus/Link";
import useBaseUrl from "@docusaurus/useBaseUrl";
import useIsBrowser from "@docusaurus/useIsBrowser";
import { useHistory, useLocation } from "@docusaurus/router";
import overview from "@site/.generated/knowledge-overview.json";
import "@site/src/css/knowledge-graph.css";

const kinds = {
  decision: "Decision",
  topic: "AI topic",
  component: "Component",
};
const labels = {
  depends_on: "depends on",
  supersedes: "supersedes",
  relates_to: "relates to",
  governed_by: "governed by",
};
const incomingLabels = {
  depends_on: "required by",
  supersedes: "superseded by",
  relates_to: "relates to",
  governed_by: "governs",
};
const colors = {
  decision: "var(--ifm-color-primary)",
  topic: "#7f8bb5",
  component: "#b17c46",
};
const statuses = ["all", "accepted", "proposed", "superseded", "current"];
const areaById = new Map(overview.areas.map((area) => [area.id, area]));
const validId = (id) => /^[A-Z][A-Z0-9-]{0,127}$/.test(id);
const pageNumber = (value, total) =>
  Math.max(1, Math.min(Number(value) || 1, Math.max(1, total)) | 0);
const number = (value) => value.toLocaleString("en");

function useJson(path) {
  const base = useBaseUrl(`/knowledge-data/${overview.version}/`);
  const [attempt, setAttempt] = useState(0);
  const [state, setState] = useState({ path: null });
  useEffect(() => {
    if (!path) return;
    const controller = new AbortController();
    setState({ path, loading: true });
    fetch(base + path, { signal: controller.signal })
      .then(async (response) => {
        if (!response.ok)
          throw new Error(
            response.status === 404
              ? "This record or page was not found."
              : "This view could not be loaded.",
          );
        return response.json();
      })
      .then((data) => {
        if (!controller.signal.aborted) setState({ path, data });
      })
      .catch((error) => {
        if (!controller.signal.aborted)
          setState({ path, error: error.message });
      });
    return () => controller.abort();
  }, [base, path, attempt]);
  return {
    ...(state.path === path ? state : { loading: !!path }),
    retry: () => setAttempt((n) => n + 1),
  };
}

function Pager({ page, pages, label, onChange }) {
  if (pages <= 1) return null;
  return (
    <nav className="atlas-pager" aria-label={label}>
      <button
        type="button"
        disabled={page <= 1}
        onClick={() => onChange(page - 1)}
      >
        Previous
      </button>
      <span aria-live="polite">
        Page {number(page)} of {number(pages)}
      </span>
      <button
        type="button"
        disabled={page >= pages}
        onClick={() => onChange(page + 1)}
      >
        Next
      </button>
    </nav>
  );
}

function LoadingOrError({ resource }) {
  if (resource.error)
    return (
      <div className="atlas-message" role="alert">
        <h3>Unable to open this view</h3>
        <p>{resource.error}</p>
        <button type="button" onClick={resource.retry}>
          Try again
        </button>
      </div>
    );
  return (
    <p className="atlas-message" role="status">
      Loading this view…
    </p>
  );
}

function titleLines(title) {
  const lines = [""];
  for (const word of title.split(" ")) {
    if ((lines.at(-1) + " " + word).trim().length > 28) lines.push(word);
    else lines[lines.length - 1] = (lines.at(-1) + " " + word).trim();
  }
  return lines.slice(0, 2);
}

function Diagram({ nodes, edges, selected, onSelect, mode }) {
  const summary = mode === "areas";
  const neighborSlots = [
    [150, 75],
    [440, 75],
    [730, 75],
    [150, 235],
    [730, 235],
    [150, 395],
    [440, 395],
    [730, 395],
  ];
  const positions = new Map(
    nodes.map((node, i) => [
      node.id,
      summary
        ? { x: 225 + (i % 2) * 430, y: 85 + Math.floor(i / 2) * 180 }
        : i === 0
          ? { x: 440, y: 235 }
          : { x: neighborSlots[i - 1][0], y: neighborSlots[i - 1][1] },
    ]),
  );
  const height = summary
    ? Math.max(200, Math.ceil(nodes.length / 2) * 180)
    : 480;
  return (
    <svg
      className="knowledge-svg"
      viewBox={`0 0 880 ${height}`}
      role="group"
      aria-label={
        summary
          ? "Knowledge area overview"
          : "Direct relationships of selected record"
      }
    >
      <defs>
        <marker
          id="atlas-arrow"
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
        if (!a || !b) return null;
        const dx = b.x - a.x,
          dy = b.y - a.y;
        const scale = Math.min(
          dx ? 115 / Math.abs(dx) : Infinity,
          dy ? 52 / Math.abs(dy) : Infinity,
        );
        const sx = a.x + dx * scale,
          sy = a.y + dy * scale,
          tx = b.x - dx * scale,
          ty = b.y - dy * scale;
        const bend = summary ? 0 : (i % 2 ? 1 : -1) * 18;
        return (
          <g key={`${edge.source}-${edge.type || "area"}-${edge.target}`}>
            <path
              d={`M ${sx} ${sy} Q ${(sx + tx) / 2 + (dy ? bend : 0)} ${(sy + ty) / 2 + (dx ? bend : 0)} ${tx} ${ty}`}
              className={`graph-edge ${summary ? "" : "active"}`}
              markerEnd={summary ? undefined : "url(#atlas-arrow)"}
            >
              <title>
                {summary
                  ? `${edge.count} explicit cross-area relationships`
                  : `${edge.source} ${labels[edge.type]} ${edge.target}`}
              </title>
            </path>
            {summary && (
              <text
                className="area-edge-count"
                x={(sx + tx) / 2}
                y={(sy + ty) / 2 - 8}
                textAnchor="middle"
              >
                {number(edge.count)} links
              </text>
            )}
          </g>
        );
      })}
      {nodes.map((node) => {
        const p = positions.get(node.id),
          chosen = node.id === selected;
        return (
          <g
            key={node.id}
            transform={`translate(${p.x - 115} ${p.y - 52})`}
            className={`graph-node ${summary ? "area-node" : "record-node"} ${chosen ? "selected" : ""}`}
            tabIndex="0"
            role="button"
            aria-label={
              summary
                ? `${node.title}: ${node.counts["all-all"]} records`
                : `${node.id}: ${node.title}, ${node.status}`
            }
            aria-pressed={chosen}
            onClick={() => onSelect(node.id)}
            onKeyDown={(event) => {
              if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                onSelect(node.id);
              }
            }}
          >
            <rect width="230" height="104" rx="10" />
            <circle
              cx="17"
              cy="19"
              r="4"
              fill={summary ? "var(--ifm-color-primary)" : colors[node.kind]}
            />
            <text x="29" y="23" className="node-id">
              {summary ? `${number(node.counts["all-all"])} RECORDS` : node.id}
            </text>
            {titleLines(node.title).map((line, i) => (
              <text key={i} x="16" y={47 + i * 16} className="node-title">
                {line}
              </text>
            ))}
            <text x="16" y="91" className={`node-status ${node.status || ""}`}>
              {summary
                ? `${node.counts["decision-all"] || 0} decisions · ${node.counts["all-proposed"] || 0} proposed`
                : node.status.toUpperCase()}
            </text>
            <text x="213" y="91" textAnchor="end" className="node-open">
              ↗
            </text>
          </g>
        );
      })}
    </svg>
  );
}

export default function KnowledgeGraphPage() {
  const base = useBaseUrl("/");
  const isBrowser = useIsBrowser();
  const location = useLocation(),
    history = useHistory();
  // Static HTML starts at the overview; apply deep links after hydration.
  const params = new URLSearchParams(isBrowser ? location.search : "");
  const requestedId = params.get("record");
  const recordId = requestedId && validId(requestedId) ? requestedId : null;
  const area = areaById.get(params.get("area"));
  const kind = Object.hasOwn(kinds, params.get("kind"))
    ? params.get("kind")
    : "all";
  const status = statuses.includes(params.get("status"))
    ? params.get("status")
    : "all";
  const areaTotal = area?.counts[`${kind}-${status}`] || 0;
  const areaPages = Math.ceil(areaTotal / overview.limits.records);
  const areaPage = pageNumber(params.get("page"), areaPages);
  const overviewPages = Math.ceil(
    overview.areas.length / overview.limits.areas,
  );
  const overviewPage = pageNumber(params.get("page"), overviewPages);
  const visibleAreas = overview.areas.slice(
    (overviewPage - 1) * overview.limits.areas,
    overviewPage * overview.limits.areas,
  );
  const visibleAreaIds = new Set(visibleAreas.map((item) => item.id));
  const records = useJson(
    !requestedId && area && areaTotal
      ? `areas/${area.id}/${kind}-${status}/${areaPage}.json`
      : null,
  );
  const detail = useJson(recordId ? `records/${recordId}/index.json` : null);
  const current = detail.data?.node;
  const relationshipPages = Math.ceil(
    (detail.data?.totalRelationships || 0) / overview.limits.relationships,
  );
  const relationshipPage = pageNumber(
    params.get("relations"),
    relationshipPages,
  );
  const relationships = useJson(
    current && relationshipPages
      ? `records/${current.id}/${relationshipPage}.json`
      : null,
  );
  const localNodes = current
    ? [
        current,
        ...(relationships.data?.nodes || []).filter(
          (node) => node.id !== current.id,
        ),
      ]
    : [];
  const related = relationships.data?.edges || [];
  const localById = new Map(localNodes.map((node) => [node.id, node]));
  const [jump, setJump] = useState("");
  const [inputError, setInputError] = useState("");
  function navigate(values = {}) {
    history.push({
      pathname: location.pathname,
      search: new URLSearchParams(values).toString(),
    });
  }
  const openArea = (id) => navigate({ area: id });
  const focus = (id) => navigate({ record: id });
  const href = (node) => base + node.href.slice(1);

  return (
    <Layout
      title="Knowledge map"
      description="Explore areas first, then inspect a bounded set of direct decision relationships."
    >
      <main className="atlas">
        <header className="atlas-heading">
          <p className="eyebrow">ENGINEERING ATLAS · FICTIONAL PROJECT DEMO</p>
          <h1>Project knowledge</h1>
          <p>Explore shared decisions and their context, one area at a time.</p>
          <Link to={base + "demo-knowledge/intro/"}>
            How this knowledge map works ↗
          </Link>
        </header>
        <section className="atlas-stats" aria-label="Knowledge summary">
          <div>
            <strong>{number(overview.areas.length)}</strong>
            <span>Areas</span>
          </div>
          <div>
            <strong>{number(overview.totals.kinds.decision)}</strong>
            <span>Decisions</span>
          </div>
          <div>
            <strong>{number(overview.totals.records)}</strong>
            <span>Shared records</span>
          </div>
          <div>
            <strong>{number(overview.totals.relationships)}</strong>
            <span>Explicit relationships</span>
          </div>
        </section>
        <section className="explore-section" id="explore">
          <div className="atlas-nav">
            <nav aria-label="Knowledge location">
              <button type="button" onClick={() => navigate()}>
                Overview
              </button>
              {(area || current) && (
                <>
                  <span>/</span>
                  <button
                    type="button"
                    onClick={() => openArea(current?.area || area.id)}
                  >
                    {areaById.get(current?.area)?.title || area?.title}
                  </button>
                </>
              )}
              {requestedId && (
                <>
                  <span>/</span>
                  <span>{requestedId}</span>
                </>
              )}
            </nav>
            <form
              onSubmit={(event) => {
                event.preventDefault();
                const id = jump.trim().toUpperCase();
                if (validId(id)) {
                  setInputError("");
                  focus(id);
                } else setInputError("Enter an ID such as ADR-0002.");
              }}
            >
              <input
                aria-label="Open record by ID"
                placeholder="Record ID, e.g. ADR-0002"
                value={jump}
                maxLength={128}
                onChange={(event) => setJump(event.target.value)}
                aria-invalid={!!inputError}
                aria-describedby={inputError ? "jump-error" : undefined}
              />
              <button type="submit">Open</button>
            </form>
          </div>
          {inputError && (
            <p id="jump-error" role="alert">
              {inputError}
            </p>
          )}
          {requestedId ? (
            <>
              {!recordId ? (
                <div className="atlas-message" role="alert">
                  Invalid record ID. Choose Overview or enter a valid ID.
                </div>
              ) : !current ? (
                <LoadingOrError resource={detail} />
              ) : (
                <>
                  <div className="section-heading">
                    <div>
                      <p className="eyebrow">ONE DECISION AT A TIME</p>
                      <h2>Direct context of {current.id}</h2>
                    </div>
                    <p>
                      {number(detail.data.totalRelationships)} direct
                      relationships.
                      <br />
                      Showing at most {overview.limits.relationships} at a time.
                    </p>
                  </div>
                  <div className="graph-workspace">
                    <div className="graph-canvas">
                      {relationships.loading || relationships.error ? (
                        <LoadingOrError resource={relationships} />
                      ) : (
                        <Diagram
                          nodes={localNodes}
                          edges={related}
                          selected={current.id}
                          onSelect={focus}
                          mode="records"
                        />
                      )}
                      <p className="graph-caption" aria-live="polite">
                        {related.length} of{" "}
                        {number(detail.data.totalRelationships)} direct
                        relationships shown. Arrows preserve the recorded
                        direction.
                      </p>
                      <Pager
                        page={relationshipPage}
                        pages={relationshipPages}
                        label="Relationship pages"
                        onChange={(page) =>
                          navigate({
                            record: current.id,
                            relations: String(page),
                          })
                        }
                      />
                    </div>
                    <aside
                      className="record-panel"
                      aria-label="Selected record"
                    >
                      <p className="eyebrow">{kinds[current.kind]}</p>
                      <div className="panel-id">
                        {current.id}
                        <span className={`status-badge ${current.status}`}>
                          {current.status}
                        </span>
                      </div>
                      <h3>{current.title}</h3>
                      <p className="owner-line">
                        Owner <strong>{current.owner}</strong>
                      </p>
                      <Link
                        className="atlas-button source-link"
                        to={href(current)}
                      >
                        Open documentation ↗
                      </Link>
                      <h4>Relationships on this page</h4>
                      <ul className="relationship-list">
                        {related.map((edge) => {
                          const outgoing = edge.source === current.id,
                            other = localById.get(
                              outgoing ? edge.target : edge.source,
                            );
                          return (
                            <li
                              key={`${edge.source}-${edge.type}-${edge.target}`}
                            >
                              <span>
                                {
                                  (outgoing ? labels : incomingLabels)[
                                    edge.type
                                  ]
                                }
                              </span>
                              <button
                                type="button"
                                onClick={() => focus(other.id)}
                              >
                                {other.title}
                                <small>{other.id} ↗</small>
                              </button>
                            </li>
                          );
                        })}
                      </ul>
                      {!related.length &&
                        !relationships.loading &&
                        !relationships.error && (
                          <p>No direct relationships recorded.</p>
                        )}
                      <p className="source-caption">
                        Source: <code>{current.path}</code>
                      </p>
                    </aside>
                  </div>
                </>
              )}
            </>
          ) : area ? (
            <>
              <div className="section-heading">
                <div>
                  <p className="eyebrow">BROWSE AN AREA</p>
                  <h2>{area.title}</h2>
                </div>
                <p>
                  {number(area.counts["all-all"])} records in this area.
                  <br />
                  Select one to see its direct context.
                </p>
              </div>
              <div className="graph-toolbar">
                <label>
                  Type{" "}
                  <select
                    aria-label="Record type"
                    value={kind}
                    onChange={(event) =>
                      navigate({
                        area: area.id,
                        kind: event.target.value,
                        status,
                      })
                    }
                  >
                    <option value="all">All records</option>
                    {Object.entries(kinds).map(([key, title]) => (
                      <option key={key} value={key}>
                        {title}
                      </option>
                    ))}
                  </select>
                </label>
                <label>
                  Status{" "}
                  <select
                    aria-label="Record status"
                    value={status}
                    onChange={(event) =>
                      navigate({
                        area: area.id,
                        kind,
                        status: event.target.value,
                      })
                    }
                  >
                    {statuses.map((item) => (
                      <option key={item} value={item}>
                        {item === "all" ? "All statuses" : item}
                      </option>
                    ))}
                  </select>
                </label>
                <span aria-live="polite">
                  {number(areaTotal)} matching records
                </span>
              </div>
              {!areaTotal ? (
                <p className="atlas-message" role="status">
                  No records match these filters in this area.
                </p>
              ) : !records.data ? (
                <LoadingOrError resource={records} />
              ) : (
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
                      {records.data.records.map((node) => (
                        <tr key={node.id}>
                          <td>
                            <button
                              type="button"
                              onClick={() => focus(node.id)}
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
              )}
              <Pager
                page={areaPage}
                pages={areaPages}
                label="Record pages"
                onChange={(page) =>
                  navigate({ area: area.id, kind, status, page: String(page) })
                }
              />
            </>
          ) : (
            <>
              <div className="section-heading">
                <div>
                  <p className="eyebrow">OVERVIEW</p>
                  <h2>Explore by area</h2>
                </div>
                <p>
                  Open an area to browse its records.
                  <br />
                  Lines combine explicit relationships across areas.
                </p>
              </div>
              <div className="graph-canvas overview-canvas">
                <Diagram
                  nodes={visibleAreas}
                  edges={overview.links.filter(
                    (link) =>
                      visibleAreaIds.has(link.source) &&
                      visibleAreaIds.has(link.target),
                  )}
                  onSelect={openArea}
                  mode="areas"
                />
                <p className="graph-caption">
                  Showing {visibleAreas.length} of{" "}
                  {number(overview.areas.length)} areas. Counts cover all
                  statuses. Lines are undirected summaries between visible
                  areas.
                </p>
              </div>
              <Pager
                page={overviewPage}
                pages={overviewPages}
                label="Area pages"
                onChange={(page) => navigate({ page: String(page) })}
              />
              <details className="area-list">
                <summary>Browse areas as a list</summary>
                <div className="area-directory" aria-label="Areas as a list">
                  {visibleAreas.map((item) => (
                    <button
                      type="button"
                      key={item.id}
                      onClick={() => openArea(item.id)}
                    >
                      <strong>{item.title}</strong>
                      <span>
                        {number(item.counts["all-all"])} records ·{" "}
                        {number(item.counts["all-proposed"] || 0)} proposed ·{" "}
                        {number(item.counts["all-superseded"] || 0)} superseded
                      </span>
                    </button>
                  ))}
                </div>
              </details>
            </>
          )}
        </section>
        <footer className="ownership-note">
          <p>
            Shared decisions and current knowledge. Personal plans stay in your
            Second Brain.
          </p>
          <Link to={base + "demo-knowledge/intro/#large-collections"}>
            Working with large decision collections ↗
          </Link>
        </footer>
      </main>
    </Layout>
  );
}
