const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const { buildGraph, assertAcyclic } = require("./graph.cjs");
const { createViewIndex, writeViewData, LIMITS } = require("./graph-views.cjs");

function fixture(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), "atlas-"));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  return root;
}
function record(root, id, fields = "") {
  const folder = path.join(root, "decisions");
  fs.mkdirSync(folder, { recursive: true });
  fs.writeFileSync(
    path.join(folder, `${id}.md`),
    `---\nknowledge_id: ${id}\ntitle: Example\nowner: team\narea: engineering\nstatus: accepted\nslug: /decisions/${id.toLowerCase()}\n${fields}---\n`,
  );
}
test("only allowlisted shared content enters the graph", (t) => {
  const root = fixture(t);
  record(root, "ADR-1");
  for (const folder of ["plans", "work", "archive", "private"]) {
    fs.mkdirSync(path.join(root, folder));
    fs.writeFileSync(
      path.join(root, folder, "secret.md"),
      "---\nthis is invalid YAML\n",
    );
  }
  assert.deepEqual(
    buildGraph(root).nodes.map((n) => n.id),
    ["ADR-1"],
  );
});
test("broken references and cycles fail before publication", (t) => {
  const root = fixture(t);
  record(root, "ADR-1", "relations: {depends_on: [ADR-2]}\n");
  assert.throws(() => buildGraph(root), /Unknown/);
  record(root, "ADR-2", "relations: {depends_on: [ADR-1]}\n");
  assert.throws(() => buildGraph(root), /Cycle/);
});
test("private source symlinks cannot enter shared output", (t) => {
  const root = fixture(t);
  record(root, "ADR-1");
  fs.symlinkSync(
    path.join(root, "decisions", "ADR-1.md"),
    path.join(root, "decisions", "linked.md"),
  );
  assert.throws(() => buildGraph(root), /symlinks/);
});
test("a proposal cannot replace an accepted decision", (t) => {
  const root = fixture(t);
  record(root, "ADR-1");
  record(root, "ADR-2", "relations: {supersedes: [ADR-1]}\n");
  assert.throws(() => buildGraph(root), /cannot supersede/);
});
test("demo graph is deterministic and every record has a documentation source", () => {
  const root = path.resolve(
    __dirname,
    "../../examples/engineering-demo/content",
  );
  const result = buildGraph(root);
  assert.deepEqual(result, buildGraph(root));
  assert.equal(result.nodes.length, 10);
  for (const node of result.nodes)
    assert.ok(fs.existsSync(path.join(root, node.path)));
  assert.ok(result.edges.some((e) => e.type === "supersedes"));
});

test("area metadata is required and cannot escape the public data directory", (t) => {
  const root = fixture(t);
  record(root, "ADR-1");
  const file = path.join(root, "decisions/ADR-1.md");
  const source = fs.readFileSync(file, "utf8");
  for (const area of ["", "../private", "A new group"]) {
    fs.writeFileSync(
      file,
      source.replace("area: engineering", `area: ${area}`),
    );
    assert.throws(() => buildGraph(root), /invalid area/);
  }
});

function synthetic(count) {
  const nodes = Array.from({ length: count }, (_, i) => ({
    id: `ADR-${String(i).padStart(6, "0")}`,
    title: `Decision ${i}`,
    status: i % 2 ? "accepted" : "proposed",
    owner: "team",
    kind: "decision",
    area: ["processing", "retrieval", "engineering"][i % 3],
    href: `/demo-knowledge/decisions/record-${i}/`,
    path: `decisions/record-${i}.md`,
    relations: {},
  }));
  return {
    nodes,
    edges: nodes
      .slice(1)
      .map((node) => ({
        source: nodes[0].id,
        target: node.id,
        type: "relates_to",
      })),
  };
}

test("large collections collapse into exact area totals without individual records in the overview", () => {
  const graph = synthetic(50000);
  const { overview } = createViewIndex(graph);
  assert.equal(overview.totals.records, 50000);
  assert.equal(overview.areas.length, 3);
  assert.equal(
    overview.areas.reduce((sum, area) => sum + area.counts["all-all"], 0),
    50000,
  );
  assert.equal(
    overview.areas.reduce((sum, area) => sum + area.counts["all-proposed"], 0),
    25000,
  );
  assert.equal(
    overview.links.reduce((sum, link) => sum + link.count, 0) +
      overview.areas.reduce((sum, area) => sum + area.internalRelationships, 0),
    graph.edges.length,
  );
  assert.ok(!JSON.stringify(overview).includes("ADR-000000"));
  assert.ok(
    JSON.stringify(overview).length < 4000,
    "Initial payload depends on areas, not ADR count",
  );
});

test("a high-degree record and area are delivered in bounded complete pages", (t) => {
  const output = fixture(t);
  const graph = synthetic(80);
  const overview = writeViewData(graph, output);
  const data = path.join(output, "static/knowledge-data", overview.version);
  const read = (file) =>
    JSON.parse(fs.readFileSync(path.join(data, file), "utf8"));
  const current = read("records/ADR-000000/index.json");
  assert.equal(current.totalRelationships, 79);
  assert.equal(
    current.node.relations,
    undefined,
    "A hub's full adjacency must not leak into its metadata",
  );
  const allEdges = [];
  for (
    let page = 1;
    page <= Math.ceil(current.totalRelationships / LIMITS.relationships);
    page++
  ) {
    const result = read(`records/ADR-000000/${page}.json`);
    assert.ok(result.edges.length <= LIMITS.relationships);
    assert.ok(result.nodes.length <= LIMITS.relationships + 1);
    allEdges.push(...result.edges);
  }
  assert.deepEqual(allEdges, graph.edges);
  for (const area of overview.areas) {
    const records = [];
    for (
      let page = 1;
      page <= Math.ceil(area.counts["all-all"] / LIMITS.records);
      page++
    ) {
      const result = read(`areas/${area.id}/all-all/${page}.json`);
      assert.ok(result.records.length <= LIMITS.records);
      records.push(...result.records);
    }
    assert.deepEqual(
      records.map((node) => node.id),
      graph.nodes
        .filter((node) => node.area === area.id)
        .map((node) => node.id),
    );
    const accepted = read(`areas/${area.id}/decision-accepted/1.json`);
    assert.ok(
      accepted.records.every(
        (node) => node.kind === "decision" && node.status === "accepted",
      ),
    );
    assert.equal(accepted.total, area.counts["decision-accepted"]);
  }
  assert.deepEqual(
    writeViewData(graph, output),
    overview,
    "Publication snapshot must be deterministic",
  );
});

test("long decision histories do not overflow the call stack and still reject cycles", () => {
  const nodes = Array.from({ length: 30000 }, (_, i) => ({ id: `ADR-${i}` }));
  const edges = nodes
    .slice(1)
    .map((node, i) => ({
      source: nodes[i].id,
      target: node.id,
      type: "depends_on",
    }));
  assert.doesNotThrow(() => assertAcyclic(nodes, edges, "depends_on"));
  assert.throws(
    () =>
      assertAcyclic(
        nodes,
        [
          ...edges,
          { source: nodes.at(-1).id, target: nodes[0].id, type: "depends_on" },
        ],
        "depends_on",
      ),
    /Cycle/,
  );
});
