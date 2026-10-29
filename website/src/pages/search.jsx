import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import {useHistory, useLocation} from '@docusaurus/router';
import useIsBrowser from '@docusaurus/useIsBrowser';
import records from '@site/.generated/search-index.json';
import search from '@site/src/search.cjs';
import '@site/src/css/search.css';

const kinds = {all: 'All documentation', agent: 'Agents', skill: 'Skills', template: 'Templates', guide: 'Guides'};

export default function Search() {
  const history = useHistory();
  const location = useLocation();
  const browser = useIsBrowser();
  const parameters = new URLSearchParams(browser ? location.search : '');
  const query = (parameters.get('q') || '').slice(0, 200);
  const selectedKind = parameters.get('kind') || 'all';
  const kind = Object.hasOwn(kinds, selectedKind) ? selectedKind : 'all';
  const {total, results} = search.searchDocuments(records, query, kind);
  function update(value, nextKind) {
    const next = new URLSearchParams();
    if (value.trim()) next.set('q', value.slice(0, 200));
    if (nextKind !== 'all') next.set('kind', nextKind);
    history.replace({pathname: location.pathname, search: next.toString() ? `?${next}` : ''});
  }
  return (
    <Layout title="Search documentation" description="Find agents, skills, templates and engineering guidance in the published documentation.">
      <main className="container docs-search">
        <p className="eyebrow">Find the next useful source</p>
        <h1>Search documentation</h1>
        <p>Search the published catalog and guides. Results stay on this site; project knowledge has its own selected sources.</p>
        <form className="docs-search-controls" role="search" onSubmit={event => event.preventDefault()}>
          <div><label htmlFor="docs-query">What do you need?</label>
            <input id="docs-query" type="search" value={query} maxLength={200} placeholder="FastAPI, Terraform, stakeholder, decision…"
              onChange={event => update(event.target.value, kind)} /></div>
          <div><label htmlFor="docs-kind">Document type</label>
            <select id="docs-kind" value={kind} onChange={event => update(query, event.target.value)}>
              {Object.entries(kinds).map(([value, label]) => <option key={value} value={value}>{label}</option>)}
            </select></div>
        </form>
        {!query.trim() ? <p>Try a stack, an outcome or a quality concern. Start with the <Link to="/getting-started/quick-start/">first useful task</Link> if you are new.</p> : <>
          <p role="status">{total} {total === 1 ? 'result' : 'results'}{total > results.length ? ` · showing the first ${results.length}` : ''}</p>
          {total === 0 && <p>No matching documents. Try fewer words or another document type.</p>}
          <ul className="docs-search-results">
            {results.map(record => <li key={record.href}>
              <p className="eyebrow">{record.kind}{record.domain ? ` · ${record.domain}` : ''}</p>
              <h2><Link to={record.href}>{record.title}</Link></h2>
              <p>{record.description}</p>
            </li>)}
          </ul>
        </>}
      </main>
    </Layout>
  );
}
