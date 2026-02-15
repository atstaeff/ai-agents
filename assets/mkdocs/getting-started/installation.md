# Installation & Setup

## Prerequisites

- [VS Code](https://code.visualstudio.com/) (latest version)
- [GitHub Copilot](https://github.com/features/copilot) license (Individual, Business, or Enterprise)
- [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) extension
- Git

---

## Clone the Repository

```bash
git clone https://github.com/atstaeff/ai-agents.git
cd ai-agents
```

---

## Open in VS Code

```bash
code .
```

VS Code automatically recognizes `copilot-instructions.md` and loads the global context for Copilot.

---

## Making Agents Available

Agents are located under `agents/*.agent.md`. GitHub Copilot automatically recognizes `.agent.md` files as agent definitions.

!!! tip "VS Code Workspace Trust"
    Make sure you trust the workspace so that Copilot can load the agent files.

### Using Agents in Copilot Chat

Open **Copilot Chat** (`Ctrl+Shift+I` / `Cmd+Shift+I`) and reference an agent:

```
@workspace Use the Python Expert agent to refactor this service
using the Repository Pattern and Dependency Injection.
```

### Selecting an Agent Directly

In VS Code, you can also select agents directly via the Copilot menu:

1. Open Copilot Chat
2. Click the agent dropdown
3. Select the desired agent

---

## Referencing Skills

Skills provide the agent with additional expertise. You can reference them explicitly:

```
@workspace Apply the Clean Code skill to improve this function.
Follow SOLID Principles and the Repository Pattern.
```

---

## Project Structure

```
ai-agents/
├── agents/                     # 15 specialized AI Agents
│   ├── lead-architect.agent.md
│   ├── python-expert.agent.md
│   ├── golang-expert.agent.md
│   └── ...
├── skills/                     # Technical knowledge bases
│   ├── python-patterns/
│   ├── golang-patterns/
│   ├── software-engineering/
│   ├── architecture/
│   └── ...
├── marp-templates/             # Presentation templates
├── reference-repos/            # Reference architectures
├── copilot-instructions.md     # Global Copilot context
└── mkdocs.yml                  # Documentation configuration
```

---

## Next Steps

- :material-rocket-launch: [Quick Start](quick-start.md) — Try your first agent
- :material-robot: [Agent Catalog](../agents/index.md) — Overview of all 18 agents
- :material-book-open-variant: [Skills](../skills/index.md) — Available knowledge bases
