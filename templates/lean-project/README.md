# Lean project starter

Start with one required project manifest, a few linked entries, one current assignment and
knowledge created only when the work needs it. This is the default starter; the
[extended customer example](../customer-workspace/README.md) adds board roles, review
examples and publication options for larger coordination needs.

## Adopt in a new or existing repository

1. Inspect existing instructions, tracker, code, CI and known decisions. Reuse their
   authoritative homes. Preserve human wording and do not overwrite existing files.
2. Merge the rules from [AGENTS.md](AGENTS.md) into the project's agent entry. Adapt
   [PROJECT.md](PROJECT.md) at the project root: vision, goals, scope boundaries, owners
   and key source links. Merge [CONTRIBUTING.md](CONTRIBUTING.md) into the existing
   contribution guide: AI working process, skill selection and project rules.
3. Adapt [project.yaml](project.yaml). Its initial local configuration
   selects an optional work record, not a real connected tracker. If Jira/GitHub already
   owns work, map that system instead; do not retain a second editable local plan.
4. Merge [.gitignore](.gitignore) into existing ignore rules. Do not copy this README,
   fictional examples or the entire toolkit into the customer's workspace.
5. Validate using the toolkit checkout's `tools/project_config.py --config` with the
   adopted config's absolute path. The validator's optional dependencies are supplied by
   `uv run --locked --group validation python` from the toolkit checkout. It validates
   schema and required local source sections. The unchanged template intentionally fails
   completeness checks until its prompts are filled. Use `--structure-only` to inspect the
   schema during setup; that result is not adoption readiness. It never tests tool access.
   Add the normal validator command to the adopted project's CI; do not gate with `--structure-only`.
6. Take one real authorized assignment through clarification, a short plan, build,
   meaningful checks and required acceptance/integration. Try a fresh session before
   expanding automation or parallelism.

The four files have separate jobs: `AGENTS.md` starts a session, `PROJECT.md` explains
this project, `CONTRIBUTING.md` defines how to work and selects reusable skills, and
`project.yaml` is a flat map of source paths and URLs. The YAML's `process`
points to CONTRIBUTING.md and `responsibilities` to PROJECT.md. Keep owner roles and small
decisions inline until separate pages are useful. Existing equivalent entries remain
valid; adopt the information contract without creating duplicate documents.

Skill links lead to the central catalog. Use installed skill names or read their
canonical sources; copying these project files neither installs nor updates the catalog.
Only root `project.yaml` is a fixed file convention. All Markdown names and knowledge,
decision and process directories are project choices expressed in that manifest. The
provided PROJECT.md and CONTRIBUTING.md are small defaults, not required filenames.
Keep source locations in YAML and actual commands/rules in the contribution guide. The optional local workbench uses its own
workspace/work/ store only when selected; no workspace/ folder is needed for adoption.

## Use it on the next assignment

Open the adopted project in your existing AI host. If it does not load `AGENTS.md`
automatically, name that entry explicitly. Use a request such as:

```text
Read the host instructions and root project.yaml. Follow its context and process references. Work on [assigned issue or outcome].
Use the project's current sources, acceptance and permissions. Keep a short plan,
feedback, evidence and handoff at the existing work home. Add durable knowledge or a
significant decision only when needed. Report the result and actual remaining gaps.
```

For larger local work without an assigned tracker, the optional toolkit can create the
single record from any directory. Pass the project root, not its `workspace/` subdirectory:

```sh
python3 /path/to/ai-agents/tools/ai_toolkit.py work --workspace /path/to/project new upload-retries \
  --title "Make upload retries safe" --kind software
```

An ordinary small correction needs no record. Installing profiles or running a local
workbench is optional; the shared file convention works with the project's current host.
Use [runtime setup](../../toolkit/RUNTIMES.md) if native catalog discovery is needed.

## Add records when needed

| Need | Reuse | Suggested project home |
| --- | --- | --- |
| Capture an opportunity | [Ideas list](../knowledge/ideas.md) | Existing idea intake or `notes/ideas.md` |
| Explain an uncertain solution or feature contract | [Concept/spec](../knowledge/concept.md) | Existing specification home or `design/concepts/` |
| Preserve a significant choice | [Decision](../knowledge/decision.md) | The configured decision home, initially the entry's short decision section |
| Keep implemented behavior understandable | [Current knowledge](../knowledge/current.md) | Existing docs or `knowledge/` |
| Coordinate an increment | [Compact assignment](../delivery/assignment.md) | Assigned ticket; one optional local record only without a tracker |
| Learn from a significant/repeated failure | [Incident review](../quality/incident-review.md) | Existing incident system or `incidents/` |

Create no empty folders for future work. If decisions outgrow the entry, move them to
a project-chosen directory such as `architecture/decisions/`, preserve IDs/links and update the YAML location in the same change.
Knowledge graphs and a documentation site are optional views of explicitly selected sources.
Ideas, concepts and incidents are not automatically included in the extended customer's
publication allowlist; review access and publication scope before adding them.

## Completion and sessions

Keep current knowledge current, accepted rationale historical, and completed plans at
their original work home. Link actual source revisions and check evidence. No document
alone proves implementation, approval or deployment. Retain reusable conclusions before
removing disposable artifacts; do not depend solely on Git history for finding current facts.

Before a session change, leave one bounded handoff in the existing assignment: result,
sources/revisions, evidence/limits, blocker, pending writes and next action. The next
session checks those sources rather than following stale instructions blindly.

See the [operating model](../../toolkit/OPERATING-MODEL.md),
[worked example](../../toolkit/examples/lean-project.md) and
[knowledge lifecycle](../../toolkit/PROJECT-KNOWLEDGE.md) for the full default.
