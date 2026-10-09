# Preview this website locally

Run from the AI Agents checkout in WSL. Python 3.11+ and uv are needed for documentation
development; the locked docs group installs MkDocs and its theme.

```sh
uv run --locked --group docs mkdocs serve -f assets/mkdocs.yml -a 127.0.0.1:8000
```

Open **http://localhost:8000** in your Windows browser. The server rebuilds on source
changes. Stop with Ctrl+C. This previews the MkDocs catalog; a customer's Docusaurus
site uses its own existing configuration.

For a static build without writing to the tracked Pages output:

```sh
uv run --locked --group docs mkdocs build -f assets/mkdocs.yml --strict --site-dir .ai/generated/site
python3 -m http.server 8000 --bind 127.0.0.1 --directory .ai/generated/site
```

Local preview does not deploy a site. Read [the concept](../concept.md), follow
[the assignment](../customer-workspace/assignment.md), then explore
[the knowledge map](../customer-workspace/knowledge-map.md).
