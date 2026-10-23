const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const { buildGraph } = require("./graph.cjs");

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
    `---\nknowledge_id: ${id}\ntitle: Example\nowner: team\nstatus: accepted\nslug: /decisions/${id.toLowerCase()}\n${fields}---\n`,
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
  const root = path.resolve(__dirname, "../../examples/engineering-demo/content");
  const result = buildGraph(root);
  assert.deepEqual(result, buildGraph(root));
  assert.equal(result.nodes.length, 10);
  for (const node of result.nodes)
    assert.ok(fs.existsSync(path.join(root, node.path)));
  assert.ok(result.edges.some((e) => e.type === "supersedes"));
});
