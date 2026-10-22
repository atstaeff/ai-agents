# Optional shortcuts. Runtime: Python 3.11+. Website: Node.js 22/24 LTS and npm.
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

setup:
    uv sync --locked --group validation
    npm --prefix website ci

setup-uv:
    uv sync --locked --group validation

docs:
    npm --prefix website start

docs-port port="8001":
    npm --prefix website start -- --port {{port}}

docs-generate:
    npm --prefix website run generate

docs-build:
    npm --prefix website run build

docs-clean:
    npm --prefix website run clear

docs-preview:
    npm --prefix website run serve

stats:
    python3 tools/ai_toolkit.py catalog

workbench workspace=".":
    python3 tools/ai_toolkit.py serve --workspace "{{workspace}}"

export-opencode output:
    python3 tools/ai_toolkit.py export --runtime opencode --output "{{output}}"
