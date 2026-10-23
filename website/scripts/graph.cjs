const fs = require("node:fs");
const path = require("node:path");
const matter = require("gray-matter");

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
        slug,
        relations = {},
      } = data;
      if (
        typeof id !== "string" ||
        !/^[A-Z][A-Z0-9-]*$/.test(id) ||
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
  for (const type of ["supersedes", "depends_on"]) {
    const active = new Set(),
      complete = new Set();
    function walk(id) {
      if (active.has(id)) throw new Error(`Cycle in ${type}`);
      if (complete.has(id)) return;
      active.add(id);
      for (const edge of edges.filter(
        (e) => e.source === id && e.type === type,
      ))
        walk(edge.target);
      active.delete(id);
      complete.add(id);
    }
    for (const node of nodes) walk(node.id);
  }
  return { nodes, edges };
}

if (require.main === module) {
  const site = path.resolve(__dirname, "..");
  const graph = buildGraph(path.resolve(site, "../examples/engineering-demo/content"));
  const output = path.join(site, ".generated");
  fs.mkdirSync(output, { recursive: true });
  fs.writeFileSync(
    path.join(output, "knowledge-graph.json"),
    JSON.stringify(graph, null, 2) + "\n",
  );
  console.log(
    `Knowledge graph: ${graph.nodes.length} records, ${graph.edges.length} relationships`,
  );
}
module.exports = { buildGraph };
