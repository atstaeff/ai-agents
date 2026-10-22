const navigation = require('./navigation.json');

const config = {
  title: 'AI Agents',
  tagline: 'Engineering expertise. Shared knowledge. Verifiable delivery.',
  favicon: 'img/mark.svg',
  url: 'https://atstaeff.github.io',
  baseUrl: '/ai-agents/',
  organizationName: 'atstaeff',
  projectName: 'ai-agents',
  trailingSlash: true,
  onBrokenLinks: 'throw',
  onBrokenAnchors: 'throw',
  // SWC avoids the observed long JavaScript minification step on this catalog.
  future: {faster: {swcJsMinimizer: true}},
  markdown: {
    format: 'detect',
    mermaid: true,
    hooks: {onBrokenMarkdownLinks: 'throw'},
  },
  i18n: {defaultLocale: 'en', locales: ['en']},
  presets: [['classic', {
    docs: {
      path: '.generated/docs',
      routeBasePath: '/',
      sidebarPath: require.resolve('./.generated/sidebars.json'),
      breadcrumbs: true,
    },
    blog: false,
    theme: {customCss: require.resolve('./src/css/custom.css')},
  }]],
  themes: ['@docusaurus/theme-mermaid'],
  themeConfig: {
    colorMode: {defaultMode: 'light', respectPrefersColorScheme: true},
    navbar: {
      title: 'AI Agents',
      logo: {alt: 'AI Agents', src: 'img/mark.svg'},
      items: [
        ...Object.entries(navigation).map(([sidebarId, section]) => ({
          type: 'docSidebar', sidebarId, label: section.label, position: 'left',
        })),
        {href: 'https://github.com/atstaeff/ai-agents', label: 'GitHub', position: 'right'},
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {title: 'Use', items: [
          {label: 'Choose expertise', to: '/catalog/'},
          {label: 'Adopt in a project', to: '/getting-started/adopt-workspace/'},
        ]},
        {title: 'Understand', items: [
          {label: 'Operating model', to: '/concept/'},
          {label: 'Project knowledge', to: '/operating-model/knowledge/'},
        ]},
        {title: 'Contribute', items: [
          {label: 'Maintain the catalog', to: '/catalog/maintain/'},
          {label: 'Source repository', href: 'https://github.com/atstaeff/ai-agents'},
        ]},
      ],
      copyright: 'AI Agents · Reusable expertise and project-owned knowledge.',
    },
  },
};
module.exports = config;
