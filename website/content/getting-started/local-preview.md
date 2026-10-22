# Preview this website locally

Use Python 3.11+, Node.js 22 or 24 LTS and npm. From the repository checkout in WSL:

```sh
npm --prefix website ci
npm --prefix website start
```

Open **http://localhost:3000/ai-agents/** in your Windows browser. Stop with Ctrl+C.
Docusaurus reloads website files. After editing canonical agent, skill or toolkit sources,
run `npm --prefix website run generate` again and restart after navigation changes.

For a production preview, including the GitHub Pages base path:

```sh
npm --prefix website run build
npm --prefix website run serve
```

The build generates current content automatically and rejects broken links. Its output
stays in ignored `website/build/`; previewing does not publish it. Edit canonical sources,
not `.generated/` Markdown. See the [ownership map](../architecture.md), follow
[the assignment](../customer-workspace/assignment.md), then explore
[the knowledge map](../customer-workspace/knowledge-map.md).
