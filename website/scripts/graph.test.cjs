const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const { spawnSync } = require("node:child_process");
const { buildGraph, assertAcyclic } = require("./graph.cjs");
const { createViewIndex, writeViewData, LIMITS } = require("./graph-views.cjs");
const {
  loadKnowledgeSource,
  publicKnowledgeSource,
  KNOWLEDGE_INCLUDE,
} = require("../knowledge.config.cjs");

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

test("the actual ADR template can be copied into both graph publishers with unique IDs", (t) => {
  const root = fixture(t);
  const repository = path.resolve(__dirname, "../..");
  const template = fs.readFileSync(path.join(repository, "templates/architecture/decision.md"), "utf8");
  const demo = path.join(root, "demo");
  const legacy = path.join(root, "legacy");
  fs.cpSync(path.join(repository, "examples/engineering-demo/content"), demo, { recursive: true });
  fs.cpSync(path.join(repository, "examples/document-portal/workspace"), legacy, { recursive: true });
  for (const target of [demo, legacy]) {
    for (const id of ["ADR-2042", "ADR-2043"]) {
      fs.writeFileSync(path.join(target, "decisions", `${id.toLowerCase()}.md`),
        template.replaceAll("ADR-0000", id).replaceAll("adr-0000", id.toLowerCase()));
    }
  }
  const result = buildGraph(demo);
  for (const id of ["ADR-2042", "ADR-2043"]) {
    const node = result.nodes.find((node) => node.id === id);
    assert.equal(node.status, "proposed");
    assert.equal(node.area, "engineering");
    assert.equal(node.href, `/demo-knowledge/decisions/${id.toLowerCase()}/`);
  }
  // Reuse the repository's existing optional validation environment, without a new dependency.
  const virtualPython = path.join(repository, ".venv", process.platform === "win32" ? "Scripts/python.exe" : "bin/python");
  const python = fs.existsSync(virtualPython) ? virtualPython : "python3";
  const check = spawnSync(python, ["-c", [
    "import json, pathlib, runpy, sys",
    "graph = runpy.run_path(sys.argv[1])",
    "print(json.dumps(graph['load_graph'](pathlib.Path(sys.argv[2]).resolve())))",
  ].join("\n"), path.join(repository, "examples/document-portal/examples/knowledge_graph.py"), legacy], {
    encoding: "utf8",
  });
  assert.equal(check.status, 0,
    `Legacy template contract needs Python and the existing validation dependencies (uv sync --locked --group validation). ${check.stderr || check.error || ""}`);
  const legacyGraph = JSON.parse(check.stdout);
  for (const id of ["ADR-2042", "ADR-2043"]) {
    const node = legacyGraph.nodes.find((node) => node.id === id);
    assert.equal(node.status, "proposed");
    assert.equal(node.slug, `decisions/${id.toLowerCase()}`);
  }
});

test("relative and existing absolute slugs share one canonical route and duplicate check", (t) => {
  const root = fixture(t);
  record(root, "ADR-1");
  const file = path.join(root, "decisions/ADR-1.md");
  const absolute = buildGraph(root);
  fs.writeFileSync(file, fs.readFileSync(file, "utf8").replace("slug: /", "slug: "));
  assert.deepEqual(buildGraph(root), absolute);
  record(root, "ADR-2");
  const second = path.join(root, "decisions/ADR-2.md");
  fs.writeFileSync(second, fs.readFileSync(second, "utf8").replace("slug: /decisions/adr-2", "slug: /decisions/adr-1"));
  assert.throws(() => buildGraph(root), /duplicate route/);
});

test("invalid ID values cannot expose private paths in validation errors", (t) => {
  const root = fixture(t);
  record(root, "ADR-1");
  const file = path.join(root, "decisions/ADR-1.md");
  const privateValue = "/home/customer/private-vault";
  fs.writeFileSync(file, fs.readFileSync(file, "utf8").replace("knowledge_id: ADR-1", `knowledge_id: ${privateValue}`));
  assert.throws(() => buildGraph(root), (error) => {
    assert.match(error.message, /Invalid knowledge ID/);
    assert.ok(!error.message.includes(privateValue));
    return true;
  });
});

function customerSource(root) {
  fs.writeFileSync(path.join(root, "intro.md"), "---\ntitle: Customer knowledge\nslug: intro\n---\n");
  fs.writeFileSync(path.join(root, "sidebars.cjs"), "module.exports = {knowledge: [{type: 'autogenerated', dirName: '.'}]};\n");
  return {
    id: "customer-knowledge",
    publication: "curated-public-content",
    root,
    routeBasePath: "customer/knowledge",
    sidebarPath: path.join(root, "sidebars.cjs"),
    title: "Customer knowledge",
    description: "Approved decisions and system knowledge.",
    example: false,
  };
}

test("trusted customer source configuration controls graph routes and public source metadata", (t) => {
  const root = fixture(t);
  record(root, "ADR-1");
  fs.mkdirSync(path.join(root, "private"));
  fs.writeFileSync(path.join(root, "private/secret.md"), "---\ninvalid: [private unclosed YAML\n---\n");
  const source = loadKnowledgeSource({ ...customerSource(root), include: ["**/*.md"] });
  assert.deepEqual(source.include, KNOWLEDGE_INCLUDE);
  assert.equal(source.root, root);
  assert.equal(source.routeBasePath, "customer/knowledge");
  const graph = buildGraph(source.root, source);
  assert.equal(graph.nodes[0].href, "/customer/knowledge/decisions/adr-1/");
  const sourceMetadata = publicKnowledgeSource(source);
  const plain = createViewIndex(graph).overview;
  const output = fixture(t);
  const published = writeViewData(graph, output, { source: sourceMetadata });
  assert.equal(plain.source, undefined);
  assert.deepEqual(published.source, {
    id: "customer-knowledge",
    routeBasePath: "customer/knowledge",
    introHref: "/customer/knowledge/intro/",
    title: "Customer knowledge",
    description: "Approved decisions and system knowledge.",
    example: false,
  });
  assert.notEqual(plain.version, published.version);
  assert.ok(!JSON.stringify(published).includes(root));
  const demo = loadKnowledgeSource();
  assert.equal(demo.id, "engineering-demo");
  assert.equal(demo.routeBasePath, "demo-knowledge");
  assert.equal(demo.example, true);
});

test("source configuration rejects accidental broad publication and invalid routes without exposing paths", (t) => {
  const root = fixture(t);
  record(root, "ADR-1");
  const source = customerSource(root);
  for (const changes of [
    { publication: undefined },
    { root: path.join(root, "not-present") },
    { routeBasePath: "../private" },
    { routeBasePath: "/customer" },
    { sidebarPath: path.join(root, "not-present.cjs") },
    { example: undefined },
  ]) {
    assert.throws(() => loadKnowledgeSource({ ...source, ...changes }), (error) => {
      assert.ok(!error.message.includes(root));
      return true;
    });
  }
  fs.mkdirSync(path.join(root, ".obsidian"));
  assert.throws(() => loadKnowledgeSource(source), /raw vault/);
});

test("private markers and nested private directories fail before graph or docs publication", (t) => {
  const root = fixture(t);
  record(root, "ADR-1");
  const source = customerSource(root);
  const file = path.join(root, "decisions/ADR-1.md");
  const original = fs.readFileSync(file, "utf8");
  for (const marker of ["private: true", "draft: true", "visibility: private", "visibility: internal"]) {
    fs.writeFileSync(file, original.replace("status: accepted", `status: accepted\n${marker}`));
    assert.throws(() => buildGraph(root), /Private or draft/);
    assert.throws(() => loadKnowledgeSource(source), /Private or draft/);
  }
  fs.writeFileSync(file, original);
  fs.mkdirSync(path.join(root, "decisions/private"));
  assert.throws(() => buildGraph(root), /Private directories/);
  assert.throws(() => loadKnowledgeSource(source), /Private directories/);
});

test("publication rejects symlinked parents, sidebars and dangling source links", (t) => {
  const root = fixture(t);
  const content = path.join(root, "content");
  fs.mkdirSync(content);
  record(content, "ADR-1");
  const source = customerSource(content);
  const linked = path.join(root, "linked");
  fs.symlinkSync(root, linked, "dir");
  assert.throws(() => buildGraph(path.join(linked, "content")), /symlinks/);
  const sidebar = path.join(content, "linked-sidebar.cjs");
  fs.symlinkSync(source.sidebarPath, sidebar);
  assert.throws(() => loadKnowledgeSource({ ...source, sidebarPath: sidebar }), /symlinks/);
  fs.rmSync(path.join(content, "intro.md"));
  fs.symlinkSync(path.join(root, "missing.md"), path.join(content, "intro.md"));
  assert.throws(() => buildGraph(content), /symlinks/);
});
