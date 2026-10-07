# Optional shortcuts. Python 3.11+; uv is needed only for documentation commands.
default:
    @just --list

validate:
    python3 tools/ai_toolkit.py check

validate-agents: validate
validate-skills: validate
validate-templates: validate

test:
    python3 -m unittest discover -s tests -v

check: validate test

docs:
    uv run --group docs mkdocs serve -f assets/mkdocs.yml

docs-port port="8001":
    uv run --group docs mkdocs serve -f assets/mkdocs.yml -a "127.0.0.1:{{port}}"

docs-build:
    uv run --group docs mkdocs build -f assets/mkdocs.yml --strict

docs-clean:
    uv run --group docs mkdocs build -f assets/mkdocs.yml --strict --clean

setup:
    uv sync --locked --group docs

setup-uv: setup

stats:
    python3 tools/ai_toolkit.py catalog

workbench workspace=".":
    python3 tools/ai_toolkit.py serve --workspace "{{workspace}}"

export-opencode output:
    python3 tools/ai_toolkit.py export --runtime opencode --output "{{output}}"
