// Options fragment for an existing classic preset's docs configuration.
// Assumes the actual Docusaurus config is under CUSTOMER_REPO/website/.
// Keep existing site, authentication, URL and deployment configuration.
module.exports = {
  path: '../workspace',
  routeBasePath: 'workspace',
  sidebarPath: undefined, // Let Docusaurus derive navigation from the content files.
};
