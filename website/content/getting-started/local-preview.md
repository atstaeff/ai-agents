# Preview this website locally

The [website source guide](https://github.com/atstaeff/ai-agents/blob/main/website/README.md)
owns supported prerequisites, build commands and publication details. From the repository root:

```sh
npm --prefix website ci
npm --prefix website start
```

Open **http://localhost:3000/ai-agents/**. Stop with Ctrl+C. After editing canonical
sources or navigation, regenerate the pages and restart after configuration changes.

For a production preview, including the GitHub Pages base path:

```sh
npm --prefix website run build
npm --prefix website run serve
```

The build generates current pages and rejects broken links. Edit `website/content/`
for website-specific introductions and the page's linked canonical source for process,
catalog or template changes. `.generated/`, `website/build/` and root `docs/` are generated
output. See the [ownership map](../architecture.md). A local preview does not publish the site.
