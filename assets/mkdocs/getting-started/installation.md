# Installation & Setup

## Voraussetzungen

- [VS Code](https://code.visualstudio.com/) (aktuelle Version)
- [GitHub Copilot](https://github.com/features/copilot) Lizenz (Individual, Business oder Enterprise)
- [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) Extension
- Git

---

## Repository klonen

```bash
git clone https://github.com/atstaeff/ai-agents.git
cd ai-agents
```

---

## In VS Code oeffnen

```bash
code .
```

VS Code erkennt automatisch die `copilot-instructions.md` und laedt den globalen Kontext fuer Copilot.

---

## Agents verfuegbar machen

Die Agents liegen unter `agents/*.agent.md`. GitHub Copilot erkennt `.agent.md`-Dateien automatisch als Agent-Definitionen.

!!! tip "VS Code Workspace Trust"
    Stelle sicher, dass du dem Workspace vertraust, damit Copilot die Agent-Dateien laden kann.

### Agents in Copilot Chat verwenden

Oeffne den **Copilot Chat** (`Ctrl+Shift+I` / `Cmd+Shift+I`) und referenziere einen Agent:

```
@workspace Nutze den Python Expert Agent um diesen Service
mit dem Repository Pattern und Dependency Injection zu refactoren.
```

### Agent direkt auswaehlen

In VS Code kannst du Agents auch direkt ueber das Copilot-Menue auswaehlen:

1. Oeffne Copilot Chat
2. Klicke auf das Agent-Dropdown
3. Waehle den gewuenschten Agent

---

## Skills referenzieren

Skills liefern dem Agent zusaetzliches Fachwissen. Du kannst sie explizit referenzieren:

```
@workspace Wende den Clean Code Skill an um diese Funktion zu verbessern.
Beachte dabei SOLID Principles und das Repository Pattern.
```

---

## Projektstruktur

```
ai-agents/
├── agents/                     # 15 spezialisierte AI-Agents
│   ├── lead-architect.agent.md
│   ├── python-expert.agent.md
│   ├── golang-expert.agent.md
│   └── ...
├── skills/                     # Technische Wissensdatenbanken
│   ├── python-patterns/
│   ├── golang-patterns/
│   ├── software-engineering/
│   ├── architecture/
│   └── ...
├── marp-templates/             # Praesentationsvorlagen
├── reference-repos/            # Referenzarchitekturen
├── copilot-instructions.md     # Globaler Copilot-Kontext
└── mkdocs.yml                  # Dokumentationskonfiguration
```

---

## Naechste Schritte

- :material-rocket-launch: [Schnellstart](quick-start.md) — Ersten Agent ausprobieren
- :material-robot: [Agent-Katalog](../agents/index.md) — Alle 15 Agents im Ueberblick
- :material-book-open-variant: [Skills](../skills/index.md) — Verfuegbare Wissensdatenbanken
