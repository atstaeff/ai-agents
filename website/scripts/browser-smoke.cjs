const assert = require("node:assert/strict");
const { spawn } = require("node:child_process");
const path = require("node:path");
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
    await page.goto(origin);
    if (process.env.ATLAS_SCREENSHOT)
      await page.screenshot({
        path: process.env.ATLAS_SCREENSHOT,
        fullPage: true,
      });
    await page.getByRole("button", { name: "Decisions", exact: true }).click();
    await page.waitForFunction(
      () => document.querySelectorAll("g.graph-node").length === 4,
    );
    await page.getByLabel("Record status").selectOption("proposed");
    await page.waitForFunction(
      () => document.querySelectorAll("g.graph-node").length === 1,
    );
    await page.getByRole("button", { name: /ADR-0004: Bound retries/ }).click();
    assert.match(
      await page.getByLabel("Selected record").innerText(),
      /proposed/i,
    );
    await page.getByRole("link", { name: /Open documentation/ }).click();
    await page.waitForURL("**/demo-knowledge/decisions/bounded-retries/");
    assert.match(
      await page.locator("article").innerText(),
      /no implementation or owner acceptance evidence/,
    );
    await page.goto(origin);
    await page.getByLabel("Search knowledge").fill("NONEXISTENT");
    await page
      .getByRole("heading", { name: "No matching knowledge" })
      .waitFor();
    await page.getByRole("button", { name: "Show all records" }).click();
    await page.waitForFunction(
      () => document.querySelectorAll("g.graph-node").length === 10,
    );
    const decision = page.getByRole("button", {
      name: /ADR-0003: Keep personal plans/,
    });
    await decision.focus();
    await decision.press("Enter");
    assert.match(
      await page.getByLabel("Selected record").innerText(),
      /Keep personal plans/,
    );
    await page
      .getByLabel("Selected record")
      .getByRole("button", { name: /Context and session continuity/ })
      .click();
    assert.match(
      await page.getByLabel("Selected record").innerText(),
      /TOPIC-CONTEXT/,
    );
    await page.locator("summary").click();
    assert.equal(await page.locator("tbody tr").count(), 10);
    const links = await page
      .locator("tbody a")
      .evaluateAll((elements) => elements.map((e) => e.href));
    for (const link of links)
      assert.equal((await fetch(link)).status, 200, link);
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(origin);
    assert.ok(
      await page.evaluate(
        () => document.documentElement.scrollWidth <= window.innerWidth,
      ),
      "Mobile page must not overflow",
    );
    await page.getByLabel("Search knowledge").fill("evidence");
    await page.waitForFunction(
      () => document.querySelectorAll("g.graph-node").length === 2,
    );
    assert.deepEqual(
      errors,
      [],
      "Browser must not emit uncaught JavaScript errors",
    );
    console.log(
      "Browser smoke passed: filters, proposal status, keyboard selection, related records, search/empty/reset, all document routes and mobile layout.",
    );
  } finally {
    if (browser) await browser.close();
    server.kill("SIGTERM");
  }
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
