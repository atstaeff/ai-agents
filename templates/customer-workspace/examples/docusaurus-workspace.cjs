// Options fragment for an existing classic preset's docs configuration.
// Assumes the actual Docusaurus config is under CUSTOMER_REPO/website/.
// Keep existing site, authentication, URL and deployment configuration.
module.exports = {
  path: '../workspace',
  // Publish only adopted entry pages and durable knowledge. Local work is private.
  include: ['README.md', 'working-agreement.md', 'stakeholders.md', 'handoff.md', 'knowledge-map.md',
    'knowledge/**/*.{md,mdx}', 'decisions/**/*.{md,mdx}', 'iterations/**/*.{md,mdx}'],
  exclude: ['work/**', 'archive/**', 'generated/**', 'exports/**', '**/_*/**', '**/_*.{md,mdx}'],
  routeBasePath: 'workspace',
  sidebarPath: undefined, // Let Docusaurus derive navigation from the content files.
};
