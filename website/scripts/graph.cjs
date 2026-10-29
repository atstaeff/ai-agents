const fs = require("node:fs");
const path = require("node:path");
const { writeViewData } = require("./graph-views.cjs");
const {
  SOURCE_KINDS,
  DEFAULT_ROUTE_BASE_PATH,
  listKnowledgeFiles,
  readPublishedMatter,
  routeBasePath: validateRouteBasePath,
  loadKnowledgeSource,
  publicKnowledgeSource,
} = require("../knowledge.config.cjs");
const RELATIONS = new Set([
  "depends_on",
  "supersedes",
  "relates_to",
  "governed_by",
]);
const STATUSES = new Set(["accepted", "proposed", "superseded", "current"]);

function buildGraph(contentRoot, { routeBasePath = DEFAULT_ROUTE_BASE_PATH } = {}) {
  validateRouteBasePath(routeBasePath);
  const { root, files } = listKnowledgeFiles(contentRoot);
  const nodes = [];
  const ids = new Set();
  const slugs = new Set();
  for (const { file, folder } of files) {
    const { data } = readPublishedMatter(file);
    if (folder === null) continue;
    const {
      knowledge_id: id,
      title,
      status,
      owner,
      area,
      slug: sourceSlug,
      relations = {},
    } = data;
    if (typeof id !== "string" || !/^[A-Z][A-Z0-9-]{0,127}$/.test(id)) {
      throw new Error("Invalid knowledge ID");
    }
    if (ids.has(id)) throw new Error(`Duplicate knowledge ID: ${id}`);
    if (
      typeof title !== "string" ||
      !title.trim() ||
      typeof owner !== "string" ||
      !owner.trim()
    ) {
      throw new Error(`Missing title or owner: ${id}`);
    }
    if (
      typeof area !== "string" ||
      !/^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$/.test(area)
    )
      throw new Error(`Missing or invalid area: ${id}`);
    if (!STATUSES.has(status)) throw new Error(`Unknown status: ${id}`);
    // Portable source slugs are relative; retain the existing leading-slash spelling.
    const slug =
      typeof sourceSlug === "string"
        ? sourceSlug.replace(/^\//, "")
        : sourceSlug;
    if (
      typeof slug !== "string" ||
      !new RegExp(`^${folder}/[a-z0-9-]+$`).test(slug) ||
      slugs.has(slug)
    ) {
      throw new Error(`Invalid or duplicate route: ${id}`);
    }
    if (
      !relations ||
      typeof relations !== "object" ||
      Array.isArray(relations)
    ) {
      throw new Error(`Invalid relations: ${id}`);
    }
    for (const [type, targets] of Object.entries(relations)) {
      if (
        !RELATIONS.has(type) ||
        !Array.isArray(targets) ||
        targets.some((t) => typeof t !== "string")
      ) {
        throw new Error(`Invalid relation: ${id}`);
      }
    }
    ids.add(id);
    slugs.add(slug);
    nodes.push({
      id,
      title,
      status,
      owner,
      area,
      kind: SOURCE_KINDS[folder],
      href: `/${routeBasePath}/${slug}/`,
      path: path.relative(root, file).split(path.sep).join("/"),
      relations,
    });
  }
  const byId = new Map(nodes.map((n) => [n.id, n]));
  const edges = [];
  for (const node of nodes) {
    for (const [type, targets] of Object.entries(node.relations).sort()) {
      for (const target of [...new Set(targets)].sort()) {
        const dest = byId.get(target);
        if (!dest || target === node.id)
          throw new Error(`Unknown or self reference: ${node.id} → ${target}`);
        if (
          type === "supersedes" &&
          (node.kind !== "decision" ||
            dest.kind !== "decision" ||
            !["accepted", "superseded"].includes(node.status) ||
            dest.status !== "superseded")
        ) {
          throw new Error(
            "A proposed decision cannot supersede an accepted one",
          );
        }
        edges.push({ source: node.id, target, type });
      }
    }
  }
  for (const type of ["supersedes", "depends_on"])
    assertAcyclic(nodes, edges, type);
  return { nodes, edges };
}

// Iterative traversal avoids a full edge scan per node and call-stack overflow on long histories.
function assertAcyclic(nodes, edges, type) {
  const adjacency = new Map(nodes.map((node) => [node.id, []]));
  for (const edge of edges)
    if (edge.type === type) adjacency.get(edge.source).push(edge.target);
  const state = new Map();
  for (const node of nodes) {
    if (state.get(node.id) === 2) continue;
    const stack = [{ id: node.id, next: 0 }];
    state.set(node.id, 1);
    while (stack.length) {
      const frame = stack.at(-1);
      const targets = adjacency.get(frame.id);
      if (frame.next === targets.length) {
        state.set(frame.id, 2);
        stack.pop();
        continue;
      }
      const target = targets[frame.next++];
      if (state.get(target) === 1) throw new Error(`Cycle in ${type}`);
      if (state.get(target) === 2) continue;
      state.set(target, 1);
      stack.push({ id: target, next: 0 });
    }
  }
}

if (require.main === module) {
  const site = path.resolve(__dirname, "..");
  const source = loadKnowledgeSource();
  const graph = buildGraph(source.root, source);
  const output = path.join(site, ".generated");
  fs.mkdirSync(output, { recursive: true });
  writeViewData(graph, output, { source: publicKnowledgeSource(source) });
  console.log(
    `Knowledge graph: ${graph.nodes.length} records, ${graph.edges.length} relationships`,
  );
}
module.exports = { buildGraph, assertAcyclic };
