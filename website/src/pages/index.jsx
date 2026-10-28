import React from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import counts from '../../.generated/catalog.json';

const paths = [
  {number: '01', title: 'Try one small task', to: '/getting-started/quick-start/', text: 'Export a small catalog into a temporary directory, then use your host for a harmless documentation exercise.'},
  {number: '02', title: 'Choose focused expertise', to: '/catalog/', text: 'Find the roles and procedures your next outcome needs. Load a selected skill without starting another agent.'},
  {number: '03', title: 'Adopt in your project', to: '/getting-started/lean-project/', text: 'Merge a short project entry into your existing rules. Keep assignments, decisions and evidence at their owners.'},
  {number: '04', title: 'Start with a useful template', to: '/templates/', text: 'Project briefs, architecture reviews, decisions and handoffs. Use only the artifact the assignment needs.'},
];

export default function Home() {
  return (
    <Layout title="Engineering with AI" description="Try a focused AI engineering catalog, then adopt reusable skills, project instructions and templates in your own workflow.">
      <main>
        <header className="home-hero">
          <div className="container hero-layout">
            <div>
              <p className="eyebrow">Engineering with AI · by Stefan Poss</p>
              <h1>Build products.<br /><span>Preserve the reasoning.</span></h1>
              <p className="hero-description">Reusable AI roles, focused skills and practical project templates. Start with one small task, then keep the context and evidence your team needs to continue.</p>
              <div className="hero-actions">
                <Link className="button button--primary button--lg" to="/getting-started/quick-start/">Try the first task</Link>
                <Link className="button button--secondary button--lg" to="/catalog/">Explore the catalog</Link>
              </div>
            </div>
            <aside className="hero-note" aria-label="What the repository provides">
              <p className="eyebrow">Use what the task needs</p>
              <dl>
                <div><dt>{counts.agent} agents</dt><dd>Role profiles and handoff guidance</dd></div>
                <div><dt>{counts.skill} skills</dt><dd>Focused procedures and references</dd></div>
                <div><dt>Your project</dt><dd>Project-owned context, decisions and knowledge</dd></div>
              </dl>
              <p className="note-caption">Your host runs the work. Check its capabilities before relying on them.</p>
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
            <div><p>Keep personal working plans private, shared outcomes in your issue or PR, and significant reasons in project decisions. Load only what the next step needs.</p>
              <Link to="/operating-model/knowledge/">Read the knowledge guide →</Link><br />
              <Link to="/customer-workspace/assignment/">Follow a worked project →</Link>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
