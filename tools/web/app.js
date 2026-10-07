"use strict";
const $ = (id) => document.getElementById(id);
let entries = [], records = [], current = null;
function notice(message, error = false) {
  $("notice").hidden = !message;
  $("notice").textContent = message;
  $("notice").classList.toggle("error", error);
}
async function request(path, options = {}) {
  const response = await fetch(path, { ...options, headers: { "Content-Type": "application/json", ...options.headers } });
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || `Request failed (${response.status}).`);
  return data;
}
function element(tag, text, className) {
  const node = document.createElement(tag);
  if (text !== undefined) node.textContent = text;
  if (className) node.className = className;
  return node;
}
async function copy(text) {
  try { await navigator.clipboard.writeText(text); notice("Copied to clipboard."); }
  catch { notice("Clipboard access is unavailable. Select and copy the visible text.", true); }
}
function switchView(name) {
  for (const view of ["work", "catalog"]) {
    $(`${view}-view`).hidden = view !== name;
    $(`nav-${view}`).classList.toggle("active", view === name);
    $(`nav-${view}`).setAttribute("aria-pressed", String(view === name));
  }
}
function renderCatalog() {
  const query = $("search").value.toLowerCase().trim(), kind = $("kind-filter").value;
  const filtered = entries.filter(e => (kind === "all" || kind === e.kind) && `${e.name} ${e.description}`.toLowerCase().includes(query));
  $("results-count").textContent = `${filtered.length} entries`;
  $("catalog-cards").replaceChildren();
  if (!filtered.length) $("catalog-cards").append(element("p", "No entries match. Try a broader search.", "muted"));
  for (const entry of filtered.sort((a,b) => (a.name === "joerg" ? -1 : b.name === "joerg" ? 1 : a.name.localeCompare(b.name)))) {
    const card = element("article", undefined, `card${entry.name === "joerg" ? " featured" : ""}`);
    card.append(element("span", entry.kind.toUpperCase(), "type"), element("h2", entry.name === "joerg" ? "Jörg · Your assistant" : entry.name), element("p", entry.description));
    const button = element("button", entry.kind === "skill" ? "Copy skill request" : "Copy agent request", "secondary");
    button.addEventListener("click", () => copy(entry.kind === "skill" ? `Use the ${entry.name} skill for this task.` : `@${entry.name} `));
    card.append(button); $("catalog-cards").append(card);
  }
}
function renderRecords() {
  $("work-count").textContent = records.length;
  $("records").replaceChildren();
  if (!records.length) $("records").append(element("p", "No active work yet. Create a record for your next larger outcome.", "muted"));
  for (const record of records) {
    const button = element("button", undefined, `record-button${current?.id === record.id ? " selected" : ""}`);
    button.setAttribute("aria-pressed", String(current?.id === record.id));
    const done = record.tasks.filter(t => t.status === "done").length;
    button.append(element("strong", record.title), element("small", `${record.kind} · ${done}/${record.tasks.length} tasks verified`));
    button.addEventListener("click", () => select(record.id));
    $("records").append(button);
  }
}
function renderDetail() {
  $("record-empty").hidden = !!current; $("record-detail").hidden = !current;
  if (!current) return;
  $("record-title").textContent = current.title;
  $("record-kind").textContent = current.kind.toUpperCase();
  $("record-path").textContent = current.path;
  $("markdown").textContent = current.markdown;
  $("task-list").replaceChildren();
  for (const task of current.tasks) {
    const form = element("form", undefined, "task"), header = element("div", undefined, "task-header");
    const state = element("select"); state.setAttribute("aria-label", `Status of ${task.id}`);
    for (const status of ["open", "in_progress", "blocked", "done"]) {
      const option = element("option", status.replaceAll("_", " ")); option.value = status; state.append(option);
    }
    state.value = task.status;
    header.append(element("strong", `${task.id} · ${task.title.replaceAll("&#124;", "|")}`), state);
    const label = element("label", "Evidence"), evidence = element("input");
    evidence.value = task.evidence.replaceAll("&#124;", "|"); evidence.placeholder = "Check, result or changed file"; evidence.maxLength = 4000;
    label.append(evidence);
    const actions = element("div", undefined, "actions"), button = element("button", "Save task", "secondary");
    actions.append(button); form.append(header, label, actions);
    form.addEventListener("submit", async event => {
      event.preventDefault(); button.disabled = true;
      try {
        current = await request(`/api/v1/work/${current.id}/tasks/${task.id}`, { method:"PATCH", headers:{"If-Match":current.etag}, body:JSON.stringify({status:state.value,evidence:evidence.value}) });
        renderDetail(); await refresh(false); notice(`${task.id} updated.`);
      } catch (error) { notice(error.message, true); }
      finally { button.disabled = false; }
    });
    $("task-list").append(form);
  }
}
async function select(id) {
  try { current = await request(`/api/v1/work/${id}`); renderRecords(); renderDetail(); }
  catch (error) { notice(error.message, true); }
}
async function refresh(reloadSelected = true) {
  try {
    records = await request("/api/v1/work");
    if (reloadSelected && current) {
      if (records.some(r => r.id === current.id)) await select(current.id);
      else { current = null; renderDetail(); }
    }
    renderRecords();
  } catch (error) { notice(error.message, true); }
}
$("nav-work").addEventListener("click", () => switchView("work"));
$("nav-catalog").addEventListener("click", () => switchView("catalog"));
$("search").addEventListener("input", renderCatalog);
$("kind-filter").addEventListener("change", renderCatalog);
$("refresh").addEventListener("click", () => refresh());
$("new-button").addEventListener("click", () => { $("new-form").hidden = false; $("new-form").elements.title.focus(); });
$("cancel-new").addEventListener("click", () => { $("new-form").hidden = true; $("new-button").focus(); });
$("new-form").addEventListener("submit", async event => {
  event.preventDefault(); const button = event.target.querySelector("button"); button.disabled = true;
  try {
    const data = Object.fromEntries(new FormData(event.target));
    current = await request("/api/v1/work", {method:"POST",body:JSON.stringify(data)});
    event.target.reset(); event.target.hidden = true; renderDetail(); await refresh(false); notice("Work record created. Edit the plan in your editor; comments and task states can be updated here.");
  } catch (error) { notice(error.message, true); }
  finally { button.disabled = false; }
});
$("feedback-form").addEventListener("submit", async event => {
  event.preventDefault(); if (!current) return; const button = event.target.querySelector("button"); button.disabled = true;
  try {
    current = await request(`/api/v1/work/${current.id}/feedback`, {method:"POST",headers:{"If-Match":current.etag},body:JSON.stringify({text:$("feedback").value})});
    $("feedback").value = ""; renderDetail(); notice("Comment added to the work record.");
  } catch (error) { notice(error.message, true); }
  finally { button.disabled = false; }
});
$("copy-path").addEventListener("click", () => current && copy(current.path));
Promise.all([request("/api/v1/catalog"), refresh()]).then(([catalog]) => {
  entries = catalog; $("catalog-count").textContent = entries.length; renderCatalog();
}).catch(error => notice(error.message, true));
