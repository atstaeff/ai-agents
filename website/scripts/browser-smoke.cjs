const assert = require("node:assert/strict");
const { spawn } = require("node:child_process");
const path = require("node:path");
const fs = require("node:fs");
const { buildGraph } = require("./graph.cjs");
const { chromium } = require("playwright");

(async () => {
  const site = path.resolve(__dirname, "..");
  const port = 3017;
  const origin = `http://127.0.0.1:${port}/ai-agents/knowledge-graph/`;
  const server = spawn(
    process.execPath,
    [
      path.join(site, "node_modules/@docusaurus/core/bin/docusaurus.mjs"),
      "serve",
      "--host",
      "127.0.0.1",
      "--port",
      String(port),
      "--no-open",
    ],
    { cwd: site, stdio: "ignore" },
  );
  let browser;
  try {
    let ready = false;
    for (let i = 0; i < 100; i++) {
      if (server.exitCode !== null)
        throw new Error("Demo server exited before becoming ready");
      try {
        if ((await fetch(origin)).ok) {
          ready = true;
          break;
        }
      } catch {}
      await new Promise((resolve) => setTimeout(resolve, 200));
    }
    assert.ok(ready, "Built site must become available");
    browser = await chromium.launch({
      headless: true,
      ...(process.env.ATLAS_BROWSER_EXECUTABLE
        ? {
            executablePath: process.env.ATLAS_BROWSER_EXECUTABLE,
            args: ["--no-sandbox"],
          }
        : {}),
    });
    const page = await browser.newPage({
      viewport: { width: 1440, height: 1100 },
    });
    const errors = [];
    page.on("pageerror", (error) => errors.push(error.message));
    const previews = path.join(site, ".generated/browser-preview");
    fs.mkdirSync(previews, { recursive: true });
    const dataRequests = [];
    page.on("request", (request) => {
      if (request.url().includes("/knowledge-data/"))
        dataRequests.push(request.url());
    });
    await page.goto(origin);
    await page
      .getByRole("group", { name: "Knowledge area overview" })
      .waitFor();
    assert.equal(await page.locator("g.area-node").count(), 3);
    assert.equal(await page.locator("g.record-node").count(), 0);
    assert.ok(
      (await page.locator("main.atlas").boundingBox()).width >= 1100,
      "Desktop map must use its available width",
    );
    assert.equal(
      dataRequests.length,
      0,
      "Overview must not fetch individual records",
    );
    await page.screenshot({
      path: path.join(previews, "overview.png"),
      fullPage: true,
    });

    await page
      .getByRole("button", {
        name: "Document processing: 3 records",
        exact: true,
      })
      .focus();
    await page
      .getByRole("button", {
        name: "Document processing: 3 records",
        exact: true,
      })
      .press("Enter");
    await page.waitForURL("**/?area=document-processing");
    await page.getByLabel("Record type").selectOption("decision");
    await page.getByLabel("Record status").selectOption("accepted");
    await page
      .getByText("No records match these filters in this area.")
      .waitFor();
    await page.getByLabel("Record status").selectOption("proposed");
    await page
      .getByRole("button", {
        name: "Bound retries for document processing",
        exact: true,
      })
      .waitFor();
    assert.equal(await page.locator("tbody tr").count(), 1);
    await page
      .getByRole("button", {
        name: "Bound retries for document processing",
        exact: true,
      })
      .click();
    await page
      .getByRole("group", { name: "Direct relationships of selected record" })
      .waitFor();
    assert.match(
      await page.getByLabel("Selected record", { exact: true }).innerText(),
      /proposed/i,
    );
    assert.ok((await page.locator("g.record-node").count()) <= 9);
    await page.screenshot({
      path: path.join(previews, "decision.png"),
      fullPage: true,
    });
    await page.getByRole("link", { name: /Open documentation/ }).click();
    await page.waitForURL("**/demo-knowledge/decisions/bounded-retries/");
    assert.match(
      await page.locator("article").innerText(),
      /no implementation or owner acceptance evidence/,
    );

    await page.goto(origin + "?record=ADR-0003");
    await page
      .getByLabel("Selected record", { exact: true })
      .getByRole("button", { name: /Context and session continuity/ })
      .click();
    await page.waitForURL("**/?record=TOPIC-CONTEXT");
    await page
      .getByLabel("Selected record", { exact: true })
      .getByText("TOPIC-CONTEXT", { exact: false })
      .first()
      .waitFor();
    await page.goBack();
    await page
      .getByRole("group", { name: "Direct relationships of selected record" })
      .waitFor();
    assert.match(
      await page.getByLabel("Selected record", { exact: true }).innerText(),
      /ADR-0003/,
    );

    // ID lookup stays bounded; network failure is visible and retryable.
    await page.route("**/records/ADR-0004/index.json", (route) =>
      route.fulfill({ status: 503, body: "Unavailable" }),
    );
    await page.getByLabel("Open record by ID").fill("adr-0004");
    await page.getByRole("button", { name: "Open", exact: true }).click();
    await page
      .getByRole("heading", { name: "Unable to open this view" })
      .waitFor();
    await page.unroute("**/records/ADR-0004/index.json");
    await page.getByRole("button", { name: "Try again", exact: true }).click();
    await page
      .getByLabel("Selected record", { exact: true })
      .getByRole("heading", { name: "Bound retries for document processing" })
      .waitFor();
    await page.getByLabel("Open record by ID").fill("ADR-MISSING");
    await page.getByRole("button", { name: "Open", exact: true }).click();
    await page
      .getByRole("heading", { name: "Unable to open this view" })
      .waitFor();
    await page.getByRole("button", { name: "Overview", exact: true }).click();
    await page
      .getByRole("group", { name: "Knowledge area overview" })
      .waitFor();

    const graph = buildGraph(
      path.resolve(site, "../examples/engineering-demo/content"),
    );
    for (const node of graph.nodes) {
      const url = new URL("/ai-agents" + node.href, origin).href;
      assert.equal((await fetch(url)).status, 200, url);
    }
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(origin);
    await page
      .getByRole("group", { name: "Knowledge area overview" })
      .waitFor();
    assert.ok(
      await page.evaluate(
        () => document.documentElement.scrollWidth <= window.innerWidth,
      ),
      "Mobile overview must not overflow",
    );
    await page.screenshot({
      path: path.join(previews, "mobile.png"),
      fullPage: true,
    });
    await page.goto(origin + "?record=ADR-0002");
    await page
      .getByRole("group", { name: "Direct relationships of selected record" })
      .waitFor();
    assert.ok(
      await page.evaluate(
        () => document.documentElement.scrollWidth <= window.innerWidth,
      ),
      "Mobile detail must not overflow",
    );
    assert.deepEqual(
      errors,
      [],
      "Browser must not emit uncaught JavaScript errors",
    );
    console.log(
      "Browser smoke passed: aggregate overview, lazy data, area/status filters, direct ID lookup, error/retry, keyboard, history, source routes and mobile layout.",
    );
  } finally {
    if (browser) await browser.close();
    server.kill("SIGTERM");
  }
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
