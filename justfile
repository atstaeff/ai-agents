# Copilot Expert Hub — Development Commands
# Install just: https://github.com/casey/just

# Default recipe — show available commands
default:
    @just --list

# ============================================================================
# Documentation
# ============================================================================

# Serve documentation locally (http://localhost:8000)
docs:
    mkdocs serve -f assets/mkdocs.yml

# Serve documentation on custom port
docs-port port="8001":
    mkdocs serve -f assets/mkdocs.yml -a localhost:{{port}}

# Build documentation site
docs-build:
    mkdocs build -f assets/mkdocs.yml

# Build documentation (clean)
docs-clean:
    mkdocs build -f assets/mkdocs.yml --clean

# Deploy documentation to GitHub Pages
docs-deploy:
    mkdocs gh-deploy -f assets/mkdocs.yml --force

# ============================================================================
# Validation
# ============================================================================

# Validate all agent files exist and have correct format
validate-agents:
    #!/usr/bin/env bash
    set -euo pipefail
    echo "🔍 Validating agents..."
    ok=true
    for f in agents/*.agent.md; do
        if [ ! -f "$f" ]; then
            echo "❌ Missing: $f"
            ok=false
            continue
        fi
        for section in "## Identity" "## Core Responsibilities" "## Instructions" "## Example Prompts" "## Related Skills"; do
            if ! grep -q "$section" "$f"; then
                echo "⚠️  $f: missing \"$section\" section"
            fi
        done
        if head -1 "$f" | grep -q '````'; then
            echo "⚠️  $f: starts with code fence (should be plain markdown)"
            ok=false
        fi
        echo "✅ $f"
    done
    echo ""
    if [ "$ok" = false ]; then
        echo "❌ Some agents have issues!"
        exit 1
    fi
    echo "✅ All agents valid!"

# Validate all skill directories have SKILL.md with proper frontmatter
validate-skills:
    #!/usr/bin/env bash
    set -euo pipefail
    echo "🔍 Validating skills..."
    ok=true
    for d in skills/*/; do
        skill_file="${d}SKILL.md"
        if [ ! -f "$skill_file" ]; then
            echo "❌ Missing: $skill_file"
            ok=false
            continue
        fi
        first_line=$(head -1 "$skill_file")
        if [ "$first_line" != "---" ]; then
            echo "❌ $skill_file: missing YAML frontmatter (must start with ---)"
            ok=false
            continue
        fi
        if ! head -5 "$skill_file" | grep -q 'name:'; then
            echo "❌ $skill_file: missing 'name:' in frontmatter"
            ok=false
            continue
        fi
        if ! head -5 "$skill_file" | grep -q 'description:'; then
            echo "❌ $skill_file: missing 'description:' in frontmatter"
            ok=false
            continue
        fi
        echo "✅ $skill_file"
    done
    echo ""
    if [ "$ok" = false ]; then
        echo "❌ Some skills have issues!"
        exit 1
    fi
    echo "✅ All skills valid!"

# Validate all templates
validate-templates:
    @echo "🔍 Validating templates..."
    @for f in marp-templates/*.md; do \
        echo "✅ $$f"; \
    done
    @echo ""
    @echo "✅ Templates valid!"

# Run all validations
validate: validate-agents validate-skills validate-templates
    @echo ""
    @echo "✅ All validations passed!"

# ============================================================================
# Statistics
# ============================================================================

# Show project statistics
stats:
    @echo "📊 Copilot Expert Hub Statistics"
    @echo "================================"
    @echo ""
    @echo "Agents:     $(find agents -name '*.agent.md' | wc -l | tr -d ' ')"
    @echo "Skills:     $(find skills -name '*.md' | wc -l | tr -d ' ')"
    @echo "Templates:  $(find marp-templates -name '*.md' | wc -l | tr -d ' ')"
    @echo "Ref Repos:  $(ls -d reference-repos/*/ 2>/dev/null | wc -l | tr -d ' ')"
    @echo "Doc Pages:  $(find assets/mkdocs -name '*.md' | wc -l | tr -d ' ')"
    @echo ""
    @echo "Lines of Documentation:"
    @find assets/mkdocs -name '*.md' | xargs wc -l 2>/dev/null | tail -1

# Count lines in all markdown files
loc:
    @echo "Agents:"
    @find agents -name '*.md' | xargs wc -l 2>/dev/null | tail -1
    @echo "Skills:"
    @find skills -name '*.md' | xargs wc -l 2>/dev/null | tail -1
    @echo "Documentation:"
    @find assets/mkdocs -name '*.md' | xargs wc -l 2>/dev/null | tail -1
    @echo "Templates:"
    @find marp-templates -name '*.md' | xargs wc -l 2>/dev/null | tail -1

# ============================================================================
# Setup
# ============================================================================

# Install documentation dependencies (requires pip/uv)
setup:
    pip install mkdocs-material
    @echo "✅ Dependencies installed!"

# Install with uv
setup-uv:
    uv pip install mkdocs-material
    @echo "✅ Dependencies installed with uv!"

# ============================================================================
# Development
# ============================================================================

# Create a new agent from template
new-agent name:
    @if [ -f "agents/{{name}}.agent.md" ]; then \
        echo "❌ Agent '{{name}}' already exists!"; \
        exit 1; \
    fi
    @echo '# {{name}}' > agents/{{name}}.agent.md
    @echo "" >> agents/{{name}}.agent.md
    @echo "## Identity" >> agents/{{name}}.agent.md
    @echo "" >> agents/{{name}}.agent.md
    @echo "You are a **{{name}}** — [description]." >> agents/{{name}}.agent.md
    @echo "" >> agents/{{name}}.agent.md
    @echo "## Core Responsibilities" >> agents/{{name}}.agent.md
    @echo "" >> agents/{{name}}.agent.md
    @echo "- [responsibility 1]" >> agents/{{name}}.agent.md
    @echo "- [responsibility 2]" >> agents/{{name}}.agent.md
    @echo "" >> agents/{{name}}.agent.md
    @echo "## Instructions" >> agents/{{name}}.agent.md
    @echo "" >> agents/{{name}}.agent.md
    @echo "✅ Agent template created: agents/{{name}}.agent.md"

# Create a new skill from template
new-skill name:
    @if [ -d "skills/{{name}}" ]; then \
        echo "❌ Skill '{{name}}' already exists!"; \
        exit 1; \
    fi
    @mkdir -p skills/{{name}}
    @cp templates/skill-template.md skills/{{name}}/SKILL.md
    @echo "✅ Skill template created: skills/{{name}}/SKILL.md"

# ============================================================================
# Git Helpers
# ============================================================================

# Quick commit with message
commit msg:
    git add -A
    git commit -m "{{msg}}"

# Commit and push
push msg:
    git add -A
    git commit -m "{{msg}}"
    git push

# ============================================================================
# Cleanup
# ============================================================================

# Clean build artifacts
clean:
    rm -rf site/
    @echo "✅ Build artifacts cleaned!"

# Show project info
info:
    @echo "Project: Copilot Expert Hub"
    @echo "Repo:    https://github.com/atstaeff/ai-agents"
    @echo "Docs:    https://atstaeff.github.io/ai-agents/"
    @echo ""
    @just stats
