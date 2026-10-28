const fs = require("node:fs");
const path = require("node:path");
const matter = require("gray-matter");

// Change this trusted file deliberately to publish a customer's curated content export.
// Keep private plans and raw vaults outside this source; there is no environment override.
const selectedSource = {
  id: "engineering-demo",
  publication: "curated-public-content",
  root: "../examples/engineering-demo/content",
  routeBasePath: "demo-knowledge",
  sidebarPath: "../examples/engineering-demo/sidebars.js",
  title: "Engineering Atlas",
  description:
    "A fictional Document Understanding project with shared decisions, components and AI topics.",
  example: true,
};

const SOURCE_KINDS = Object.freeze({
  decisions: "decision",
  topics: "topic",
  components: "component",
});
const KNOWLEDGE_INCLUDE = Object.freeze([
  "intro.md",
  ...Object.keys(SOURCE_KINDS).map((folder) => `${folder}/**/*.md`),
]);
const PRIVATE_DIRECTORIES = new Set([
  "private",
  "plans",
  "work",
  "archive",
  "generated",
  "exports",
  ".obsidian",
]);

function routeBasePath(value) {
  if (typeof value !== "string" || !/^[a-z0-9-]+(?:\/[a-z0-9-]+)*$/.test(value))
    throw new Error("Knowledge routeBasePath must be a relative public route");
  return value;
}

function assertSourcePath(file, type) {
  // Checking every component also rejects a source reached through a symlinked parent.
  const absolute = path.resolve(file);
  const parsed = path.parse(absolute);
  let current = parsed.root;
  for (const part of absolute.slice(parsed.root.length).split(path.sep)) {
    current = path.join(current, part);
    if (fs.lstatSync(current).isSymbolicLink())
      throw new Error("Knowledge sources must not be symlinks");
  }
  const stat = fs.lstatSync(absolute);
  if (
    (type === "directory" && !stat.isDirectory()) ||
    (type === "file" && !stat.isFile())
  )
    throw new Error("Knowledge source has an invalid file type");
  return absolute;
}

function sourceError(error) {
  // Filesystem errors contain absolute customer paths. Keep those out of build logs.
  if (error && typeof error.code === "string")
    return new Error("Knowledge source is unavailable; check the trusted knowledge configuration");
  return error;
}

function existingSource(file) {
  try {
    return fs.lstatSync(file);
  } catch (error) {
    if (error.code === "ENOENT") return null;
    throw error;
  }
}

function listKnowledgeFiles(contentRoot) {
  try {
    const root = assertSourcePath(contentRoot, "directory");
    if (
      path.basename(root).startsWith(".") ||
      PRIVATE_DIRECTORIES.has(path.basename(root).toLowerCase()) ||
      existingSource(path.join(root, ".obsidian"))
    )
      throw new Error("A private directory or raw vault cannot be a knowledge publication source");
    const files = [];
    const intro = path.join(root, "intro.md");
    if (existingSource(intro)) {
      assertSourcePath(intro, "file");
      files.push({ file: intro, folder: null });
    }
    function visit(directory, folder) {
      assertSourcePath(directory, "directory");
      for (const name of fs.readdirSync(directory).sort()) {
        const file = path.join(directory, name);
        const stat = fs.lstatSync(file);
        if (stat.isSymbolicLink())
          throw new Error("Knowledge sources must not be symlinks");
        if (stat.isDirectory()) {
          if (name.startsWith(".") || PRIVATE_DIRECTORIES.has(name.toLowerCase()))
            throw new Error("Private directories cannot enter published knowledge");
          visit(file, folder);
        } else if (name.endsWith(".md")) {
          if (!stat.isFile()) throw new Error("Knowledge source has an invalid file type");
          files.push({ file, folder });
        }
      }
    }
    // This is a publication allowlist, never a recursive scan of a repository or vault.
    for (const folder of Object.keys(SOURCE_KINDS)) {
      const directory = path.join(root, folder);
      if (existingSource(directory)) visit(directory, folder);
    }
    return { root, files };
  } catch (error) {
    throw sourceError(error);
  }
}

function readPublishedMatter(file) {
  let result;
  try {
    result = matter(fs.readFileSync(file, "utf8"));
  } catch (error) {
    if (error && typeof error.code === "string") throw sourceError(error);
    throw new Error("Invalid published knowledge frontmatter");
  }
  const { data } = result;
  if (
    data.private === true ||
    data.draft === true ||
    ["private", "internal"].includes(data.visibility)
  )
    throw new Error("Private or draft knowledge cannot enter published output");
  return result;
}

function loadKnowledgeSource(source = selectedSource) {
  if (
    !source ||
    typeof source !== "object" ||
    Array.isArray(source) ||
    source.publication !== "curated-public-content"
  )
    throw new Error("Knowledge configuration must explicitly select curated public content");
  if (typeof source.id !== "string" || !/^[a-z][a-z0-9-]*$/.test(source.id))
    throw new Error("Knowledge configuration needs a stable source ID");
  for (const key of ["root", "sidebarPath", "title", "description"])
    if (typeof source[key] !== "string" || !source[key].trim())
      throw new Error(`Knowledge configuration needs ${key}`);
  if (typeof source.example !== "boolean")
    throw new Error("Knowledge configuration must identify whether its content is fictional");
  const route = routeBasePath(source.routeBasePath);
  try {
    const { root, files } = listKnowledgeFiles(path.resolve(__dirname, source.root));
    const intro = files.find((entry) => entry.folder === null);
    if (!intro) throw new Error("Knowledge publication needs an intro.md page");
    let introSlug;
    for (const { file, folder } of files) {
      const { data } = readPublishedMatter(file);
      if (folder === null) introSlug = data.slug;
    }
    if (introSlug !== undefined && !["intro", "/intro"].includes(introSlug))
      throw new Error("Knowledge intro page must use the intro route");
    const sidebarPath = assertSourcePath(path.resolve(__dirname, source.sidebarPath), "file");
    return Object.freeze({
      id: source.id,
      root,
      routeBasePath: route,
      sidebarPath,
      include: KNOWLEDGE_INCLUDE,
      title: source.title,
      description: source.description,
      example: source.example,
      introHref: `/${route}/intro/`,
    });
  } catch (error) {
    throw sourceError(error);
  }
}

function publicKnowledgeSource(source) {
  const { id, routeBasePath, introHref, title, description, example } = source;
  return { id, routeBasePath, introHref, title, description, example };
}

module.exports = {
  SOURCE_KINDS,
  KNOWLEDGE_INCLUDE,
  DEFAULT_ROUTE_BASE_PATH: selectedSource.routeBasePath,
  listKnowledgeFiles,
  readPublishedMatter,
  routeBasePath,
  loadKnowledgeSource,
  publicKnowledgeSource,
};
