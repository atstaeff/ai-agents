# Frequently Asked Questions (FAQ)

## General

### What is the Copilot Expert Hub?

An open-source repository with 18 specialized AI agents, 35+ skills, and templates for GitHub Copilot. It turns Copilot into a team of senior engineers covering the entire Software Delivery Lifecycle.

### Do I need a GitHub Copilot license?

Yes, you need an active GitHub Copilot subscription (Individual, Business, or Enterprise) to use the agents in VS Code.

### Which VS Code version is required?

VS Code 1.99+ (or newer) with the GitHub Copilot Extension. The agent functionality (`@workspace`) is available in current Copilot versions.

### Does it work with other IDEs?

Currently, the Hub is optimized for **VS Code**, as `.agent.md` files are recognized by GitHub Copilot in VS Code. JetBrains support depends on Copilot plugin development.

---

## Usage

### How do I use an agent?

```
@workspace Use the [Agent Name] agent to [task].
```

Example:
```
@workspace Use the Python Expert agent to refactor this service
using the Repository Pattern and Dependency Injection.
```

### Can I use multiple agents sequentially?

Yes! That's actually the recommended workflow. Use the agent chain:

```
Task Orchestrator → Lead Architect → Python Expert → Test Strategist → Code Reviewer
```

### Do I have to use all agents?

No. Use only the agents you need. Each agent works independently. The agent chain is a recommendation, not a requirement.

### How do skills work?

Skills are automatically provided as context when you have the repository open in VS Code. You can also reference them explicitly:

```
@workspace Apply the Python Patterns from the skills catalog.
```

---

## Contributing

### Can I create my own agents?

Yes! Use the template or the Justfile:

```bash
just new-agent my-agent
```

Then edit `agents/my-agent.agent.md` and create a PR.

Details: [Create a New Agent](contributing/new-agent.md)

### Can I add my own skills?

Yes, just like agents:

```bash
just new-skill my-skill
```

Details: [Create a New Skill](contributing/new-skill.md)

### What language should I contribute in?

Agent and skill files should be written in **English**. Documentation (MkDocs) is in English as well.

### How is my contribution recognized?

All contributors are mentioned in the README and on the docs site. We follow the [All Contributors](https://allcontributors.org/) standard.

---

## Technical

### How are the agents implemented?

Agents are Markdown files with the `.agent.md` format. GitHub Copilot recognizes these files and provides them as specialized agents in the chat. Each file defines:

- **Identity** — Role and expertise
- **Core Responsibilities** — Main tasks
- **Instructions** — Behavioral rules and workflows
- **Templates** — Output formats

### Which programming languages are supported?

The agents support:

| Agent | Language/Framework |
|-------|-------------------|
| Python Expert | Python 3.12+ |
| Golang Expert | Go 1.22+ |
| Flutter & iOS Expert | Dart/Flutter |
| Frontend Expert | TypeScript, Vue.js, Angular |
| GCP Architect | Terraform, GCP Services |

### Can I create agents for other languages (Rust, Java, etc.)?

Absolutely! That's one of the most important contributions the community can make. Use an existing agent as a template.

### How do I build the documentation locally?

```bash
# Using just:
just docs

# Or directly:
mkdocs serve
```

The docs are then available at `http://localhost:8000`.

---

## Troubleshooting

### Copilot doesn't recognize the agents

1. Make sure you're using VS Code 1.99+
2. Check that the GitHub Copilot Extension is up to date
3. Open the repository as the workspace root in VS Code
4. Restart VS Code

### `mkdocs serve` fails

```bash
# Install dependencies:
just setup

# Or manually:
pip install mkdocs-material
```

### `just` command not found

Install [just](https://github.com/casey/just):

```bash
# macOS
brew install just

# Linux
cargo install just

# Windows
winget install Casey.Just
```
