// Search the public documentation snapshot. Customer knowledge uses its own index.
function normalize(value) {
  return value.normalize('NFKD').replace(/\p{M}/gu, '').toLocaleLowerCase('en');
}

function searchDocuments(records, query, kind = 'all', limit = 20) {
  const terms = [...new Set(normalize(query.slice(0, 200)).match(/[\p{L}\p{N}]+/gu) || [])];
  if (!terms.length) return {total: 0, results: []};
  const matches = [];
  for (const record of records) {
    if (kind !== 'all' && record.kind !== kind) continue;
    const title = normalize(record.title);
    const description = normalize(record.description);
    const text = normalize(`${record.domain} ${record.text}`);
    if (!terms.every(term => `${title} ${description} ${text}`.includes(term))) continue;
    const score = terms.reduce((sum, term) => sum + (title.includes(term) ? 10 : 0) + (description.includes(term) ? 3 : 0), 0);
    matches.push({...record, score});
  }
  matches.sort((a, b) => b.score - a.score || a.title.localeCompare(b.title, 'en') || a.href.localeCompare(b.href, 'en'));
  return {total: matches.length, results: matches.slice(0, limit)};
}

module.exports = {searchDocuments};
