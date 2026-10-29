const test = require('node:test');
const assert = require('node:assert/strict');
const {searchDocuments} = require('../src/search.cjs');

const records = [
  {title: 'Invoice architecture', kind: 'guide', domain: '', href: '/invoice/', description: 'API tradeoffs', text: 'An API implemented with FastAPI.'},
  {title: 'FastAPI patterns', kind: 'skill', domain: 'languages', href: '/skills/python/', description: 'Build tenant-scoped endpoints.', text: 'Sync and async sessions and authorization checks.'},
  {title: 'Jörg', kind: 'agent', domain: 'general', href: '/agents/joerg/', description: 'General coordinator', text: 'Select a bounded specialist.'},
];

test('finds subject mentions while preferring a matching title', () => {
  const result = searchDocuments(records, 'FASTAPI');
  assert.equal(result.total, 2);
  assert.deepEqual(result.results.map(item => item.href), ['/skills/python/', '/invoice/']);
});

test('combines words across title, description, domain and content', () => {
  const result = searchDocuments(records, 'languages tenant sessions', 'skill');
  assert.deepEqual(result.results.map(item => item.href), ['/skills/python/']);
  assert.equal(searchDocuments(records, 'FastAPI authorization').total, 1);
  assert.equal(searchDocuments(records, 'FastAPI billing').total, 0);
});

test('document type restricts results and names can be typed without accents', () => {
  assert.equal(searchDocuments(records, 'fastapi', 'guide').total, 1);
  assert.equal(searchDocuments(records, 'fastapi', 'agent').total, 0);
  assert.equal(searchDocuments(records, 'jorg').results[0].title, 'Jörg');
});

test('empty queries avoid a catalog dump; result limits retain complete counts', () => {
  assert.deepEqual(searchDocuments(records, '  … '), {total: 0, results: []});
  const result = searchDocuments(records, 'fastapi', 'all', 1);
  assert.equal(result.total, 2);
  assert.equal(result.results.length, 1);
});
