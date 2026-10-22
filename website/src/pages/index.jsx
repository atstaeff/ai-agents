import React from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import counts from '../../.generated/catalog.json';

const paths = [
  {number: '01', title: 'Choose expertise', to: '/catalog/', text: 'Find the roles and focused skills your next outcome needs. One catalog, seven disciplines.'},
  {number: '02', title: 'Work from a shared model', to: '/concept/', text: 'Start with a clear project map, contribution guide and one assignment. Add useful knowledge as you deliver.'},
  {number: '03', title: 'Make quality observable', to: '/operating-model/quality/', text: 'Turn maintainability, security and reliability into concrete scenarios and meaningful checks.'},
  {number: '04', title: 'Start with a useful template', to: '/templates/', text: 'Project briefs, architecture reviews, decisions and handoffs. Use only the artifact the assignment needs.'},
];

export default function Home() {
  return (
    <Layout title="Engineering with AI" description="A portable engineering catalog and a practical operating model for teams working with AI.">
      <main>
        <header className="home-hero">
          <div className="container hero-layout">
            <div>
              <p className="eyebrow">Engineering with AI</p>
              <h1>Build products.<br /><span>Preserve the reasoning.</span></h1>
              <p className="hero-description">Reusable expertise. Clear decisions. Shared project knowledge that another person or session can continue from.</p>
              <div className="hero-actions">
                <Link className="button button--primary button--lg" to="/getting-started/lean-project/">Start a team project</Link>
                <Link className="button button--secondary button--lg" to="/catalog/">Explore the catalog</Link>
              </div>
            </div>
            <aside className="hero-note" aria-label="What the repository provides">
              <p className="eyebrow">One connected system</p>
              <dl>
                <div><dt>{counts.agent} agents</dt><dd>Accountable roles and bounded handoffs</dd></div>
                <div><dt>{counts.skill} skills</dt><dd>Focused procedures and references</dd></div>
                <div><dt>Your project</dt><dd>Project-owned context, decisions and knowledge</dd></div>
              </dl>
              <p className="note-caption">Portable profiles. Your tools. Your model.</p>
            </aside>
          </div>
        </header>
        <section className="container home-section" aria-labelledby="paths-heading">
          <p className="eyebrow">Start with your outcome</p>
          <h2 id="paths-heading">The right next step, in one place.</h2>
          <div className="path-grid">
            {paths.map(path => (
              <Link className="path-card" key={path.number} to={path.to}>
                <span className="path-number" aria-hidden="true">{path.number}</span>
                <h3>{path.title}<span aria-hidden="true"> ↗</span></h3>
                <p>{path.text}</p>
              </Link>
            ))}
          </div>
        </section>
        <section className="home-memory" aria-labelledby="memory-heading">
          <div className="container memory-layout">
            <div><p className="eyebrow">Small context. Durable knowledge.</p><h2 id="memory-heading">Make the next session<br />a continuation.</h2></div>
            <div><p>Keep the live plan in one issue or ticket, significant rationale in decisions, and a bounded handoff at the existing planning home. Load what the assignment needs.</p>
              <Link to="/operating-model/knowledge/">Read the knowledge guide →</Link><br />
              <Link to="/customer-workspace/assignment/">Follow a worked project →</Link>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
