const fs = require("node:fs");
const path = require("node:path");
const matter = require("gray-matter");
const { writeViewData } = require("./graph-views.cjs");

const SOURCE_KINDS = {
  decisions: "decision",
  topics: "topic",
  components: "component",
};
const RELATIONS = new Set([
  "depends_on",
  "supersedes",
  "relates_to",
  "governed_by",
]);
const STATUSES = new Set(["accepted", "proposed", "superseded", "current"]);

function buildGraph(contentRoot) {
  if (fs.lstatSync(contentRoot).isSymbolicLink())
    throw new Error("Knowledge root must not be a symlink");
  const root = fs.realpathSync(contentRoot);
  const intro = path.join(root, "intro.md");
  if (fs.existsSync(intro) && fs.lstatSync(intro).isSymbolicLink())
    throw new Error("Knowledge sources must not be symlinks");
  const nodes = [];
  const ids = new Set();
  const slugs = new Set();
  function visit(directory, folder) {
    const stat = fs.lstatSync(directory);
    if (stat.isSymbolicLink())
      throw new Error("Knowledge sources must not be symlinks");
    for (const name of fs.readdirSync(directory).sort()) {
      const file = path.join(directory, name);
      const stat = fs.lstatSync(file);
      if (stat.isSymbolicLink())
        throw new Error("Knowledge sources must not be symlinks");
      if (stat.isDirectory()) {
        visit(file, folder);
        continue;
      }
      if (!name.endsWith(".md")) continue;
      const { data } = matter(fs.readFileSync(file, "utf8"));
      const {
        knowledge_id: id,
        title,
        status,
        owner,
        area,
        slug,
        relations = {},
      } = data;
      if (
        typeof id !== "string" ||
        !/^[A-Z][A-Z0-9-]{0,127}$/.test(id) ||
        ids.has(id)
      ) {
        throw new Error(`Invalid or duplicate ID: ${id}`);
      }
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
      if (
        typeof slug !== "string" ||
        !new RegExp(`^/${folder}/[a-z0-9-]+$`).test(slug) ||
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
        href: `/demo-knowledge${slug}/`,
        path: path.relative(root, file).split(path.sep).join("/"),
        relations,
      });
    }
  }
  // This is a publication allowlist, not a recursive scan of a repository or vault.
  for (const folder of Object.keys(SOURCE_KINDS)) {
    const directory = path.join(root, folder);
    if (fs.existsSync(directory)) visit(directory, folder);
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
  const graph = buildGraph(
    path.resolve(site, "../examples/engineering-demo/content"),
  );
  const output = path.join(site, ".generated");
  fs.mkdirSync(output, { recursive: true });
  writeViewData(graph, output);
  console.log(
    `Knowledge graph: ${graph.nodes.length} records, ${graph.edges.length} relationships`,
  );
}
module.exports = { buildGraph, assertAcyclic };
