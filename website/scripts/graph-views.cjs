const fs = require("node:fs");
const path = require("node:path");
const { createHash } = require("node:crypto");

const SCHEMA_VERSION = 1;
const LIMITS = { areas: 6, records: 20, relationships: 8 };
const KINDS = ["all", "decision", "topic", "component"];
const STATUSES = ["all", "accepted", "proposed", "superseded", "current"];
const compare = (a, b) => (a < b ? -1 : a > b ? 1 : 0);
const publicNode = ({ relations, ...node }) => node;

function createViewIndex(graph) {
  const byId = new Map(graph.nodes.map((node) => [node.id, publicNode(node)]));
  const adjacent = new Map(graph.nodes.map((node) => [node.id, []]));
  const areas = new Map();
  const links = new Map();
  const kinds = Object.fromEntries(KINDS.slice(1).map((kind) => [kind, 0]));
  for (const original of graph.nodes) {
    const node = byId.get(original.id);
    if (!areas.has(node.area))
      areas.set(node.area, {
        id: node.area,
        title:
          node.area[0].toUpperCase() + node.area.slice(1).replaceAll("-", " "),
        counts: {},
        internalRelationships: 0,
        records: [],
      });
    const area = areas.get(node.area);
    area.records.push(node);
    kinds[node.kind]++;
    for (const kind of ["all", node.kind])
      for (const status of ["all", node.status]) {
        const key = `${kind}-${status}`;
        area.counts[key] = (area.counts[key] || 0) + 1;
      }
  }
  for (const edge of graph.edges) {
    adjacent.get(edge.source).push(edge);
    adjacent.get(edge.target).push(edge);
    const sourceArea = byId.get(edge.source).area;
    const targetArea = byId.get(edge.target).area;
    if (sourceArea === targetArea) {
      areas.get(sourceArea).internalRelationships++;
      continue;
    }
    // The overview is an undirected rollup, never an inferred dependency.
    const [source, target] = [sourceArea, targetArea].sort(compare);
    const key = `${source}|${target}`;
    if (!links.has(key))
      links.set(key, { source, target, count: 0, types: {} });
    const link = links.get(key);
    link.count++;
    link.types[edge.type] = (link.types[edge.type] || 0) + 1;
  }
  const sortedAreas = [...areas.values()].sort((a, b) => compare(a.id, b.id));
  for (const area of sortedAreas)
    area.records.sort((a, b) => compare(a.id, b.id));
  const overview = {
    schemaVersion: SCHEMA_VERSION,
    version: createHash("sha256")
      .update(
        JSON.stringify({
          schemaVersion: SCHEMA_VERSION,
          limits: LIMITS,
          graph,
        }),
      )
      .digest("hex")
      .slice(0, 16),
    limits: LIMITS,
    totals: {
      records: graph.nodes.length,
      relationships: graph.edges.length,
      kinds,
    },
    areas: sortedAreas.map(({ records, ...area }) => area),
    links: [...links.values()].sort((a, b) =>
      compare(`${a.source}|${a.target}`, `${b.source}|${b.target}`),
    ),
  };
  return { overview, byId, adjacent, areas: sortedAreas };
}

function writeViewData(graph, output) {
  const index = createViewIndex(graph);
  const { overview, byId, adjacent, areas } = index;
  const dataRoot = path.join(output, "static/knowledge-data");
  fs.rmSync(dataRoot, { recursive: true, force: true });
  const root = path.join(dataRoot, overview.version);
  function write(relative, data) {
    const file = path.join(root, relative);
    fs.mkdirSync(path.dirname(file), { recursive: true });
    fs.writeFileSync(file, JSON.stringify(data) + "\n");
  }
  for (const area of areas) {
    for (const kind of KINDS)
      for (const status of STATUSES) {
        const records = area.records.filter(
          (node) =>
            (kind === "all" || node.kind === kind) &&
            (status === "all" || node.status === status),
        );
        for (let offset = 0; offset < records.length; offset += LIMITS.records)
          write(
            `areas/${area.id}/${kind}-${status}/${offset / LIMITS.records + 1}.json`,
            {
              records: records.slice(offset, offset + LIMITS.records),
              total: records.length,
            },
          );
      }
  }
  for (const [id, node] of byId) {
    const edges = adjacent.get(id);
    write(`records/${id}/index.json`, {
      node,
      totalRelationships: edges.length,
    });
    for (
      let offset = 0;
      offset < edges.length;
      offset += LIMITS.relationships
    ) {
      const page = edges.slice(offset, offset + LIMITS.relationships);
      const ids = new Set([
        id,
        ...page.flatMap((edge) => [edge.source, edge.target]),
      ]);
      write(`records/${id}/${offset / LIMITS.relationships + 1}.json`, {
        edges: page,
        nodes: [...ids].map((nodeId) => byId.get(nodeId)),
      });
    }
  }
  fs.mkdirSync(output, { recursive: true });
  fs.writeFileSync(
    path.join(output, "knowledge-overview.json"),
    JSON.stringify(overview, null, 2) + "\n",
  );
  fs.rmSync(path.join(output, "knowledge-graph.json"), { force: true });
  return overview;
}

module.exports = { createViewIndex, writeViewData, LIMITS };
