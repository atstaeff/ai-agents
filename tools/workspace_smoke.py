#!/usr/bin/env python3
"""Exercise the local workflow in isolated generated fixtures; no models or tracker writes."""
from __future__ import annotations

import http.client
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
from datetime import UTC, datetime

import ai_toolkit as tk


def cli(*arguments: str, expected: int = 0):
    result = subprocess.run([sys.executable, str(tk.ROOT / 'tools/ai_toolkit.py'), *arguments],
                            cwd=tk.ROOT, capture_output=True, text=True, timeout=60)
    if result.returncode != expected:
        raise RuntimeError(f'CLI {arguments[0]} returned {result.returncode}: {result.stderr}')
    return json.loads(result.stdout) if expected == 0 else result.stderr


def require(condition, message: str):
    if not condition:
        raise RuntimeError(message)


def run() -> dict:
    generated = tk.ROOT / 'workspace/generated'
    generated.mkdir(parents=True, exist_ok=True)
    run_root = Path(tempfile.mkdtemp(prefix='workflow-smoke-', dir=generated))
    project = run_root / 'project'
    project.mkdir()
    results = []

    def passed(step: str, evidence: str):
        results.append({'step': step, 'result': 'passed', 'evidence': evidence})

    # This is a local-record fixture, not a second plan for a tracked repository task.
    record = cli('work', '--workspace', str(project), 'new', 'workflow-pilot',
                 '--title', 'Exercise the workspace delivery flow', '--kind', 'general')
    store = tk.WorkStore(project)
    current = store.read(record['id'])
    text = current['markdown'].replace('State the concrete outcome and important constraints.',
        'Verify a generated OpenCode bundle, preserve fixture feedback and resume from a saved handoff.')
    text = text.replace('- Describe observable success before implementation and how it can be checked.\n'
                        '- Distinguish delivered behavior from any business impact that needs later observation.',
        '- Exported OpenCode configuration selects joerg and contains the complete catalog.\n'
        '- Fixture feedback survives rejected stale writes.\n'
        '- A fresh store recovers task evidence and the next action before CLI archive.')
    text = text.replace('1. Inspect the relevant context and choose the smallest complete increment.\n2. Implement it and verify the acceptance criteria.',
        '1. Generate the native bundle.\n2. Exercise feedback and stale-write protection.\n3. Save evidence and resume before archiving.')
    text = text.replace('| T1 | Define and verify the outcome | open |  |',
        '| T1 | Generate and check the native bundle | open |  |\n'
        '| T2 | Preserve feedback and reject stale changes | open |  |\n'
        '| T3 | Resume from saved evidence and archive | open |  |')
    store.update(record['id'], current['etag'], lambda previous: text)
    passed('Plan', 'CLI created workspace/work/workflow-pilot.md; bounded plan and three criteria-linked tasks saved.')

    server = tk.serve(project, 0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    port = server.server_address[1]

    def request(method: str, path: str, payload=None, etag=None):
        connection = http.client.HTTPConnection('127.0.0.1', port, timeout=10)
        headers = {'Content-Type': 'application/json'} if payload is not None else {}
        if etag is not None:
            headers['If-Match'] = etag
        try:
            connection.request(method, path, json.dumps(payload) if payload is not None else None, headers)
            response = connection.getresponse()
            raw = response.read()
            value = json.loads(raw) if 'application/json' in response.getheader('Content-Type', '') else raw
            return response.status, value
        finally:
            connection.close()

    try:
        for path in ('/', '/app.js', '/style.css', '/api/v1/openapi.json'):
            require(request('GET', path)[0] == 200, f'Dashboard resource failed: {path}')
        status, entries = request('GET', '/api/v1/catalog')
        expected = tk.catalog()
        require(status == 200 and {(e['kind'], e['name']) for e in entries} ==
                {(e.kind, e.name) for e in expected}, 'Catalog was not served completely.')
        passed('Local dashboard', f'Loopback HTTP served HTML, JavaScript, CSS, API contract and {len(expected)} catalog entries.')

        route = '/api/v1/work/workflow-pilot'
        status, current = request('GET', route)
        require(status == 200, 'Record read failed.')
        stale = current['etag']
        feedback = 'Fixture feedback: keep the current plan and include evidence before completion.'
        status, current = request('POST', route + '/feedback', {'text': feedback}, stale)
        require(status == 200 and feedback in current['markdown'], 'Feedback was not preserved.')
        status, _ = request('PATCH', route + '/tasks/T2', {'status': 'in_progress'}, stale)
        require(status == 412, 'A stale write was accepted.')
        status, _ = request('POST', route + '/feedback', {'text': 'Must not be saved without an ETag'})
        require(status == 428, 'An unversioned write was accepted.')
        require(feedback in store.read('workflow-pilot')['markdown'], 'Feedback was lost.')
        passed('Feedback and conflicts', 'Fixture comment persisted; stale PATCH returned 412 and missing If-Match returned 428.')

        bundle = project / 'workspace/exports/opencode'
        export = cli('export', '--runtime', 'opencode', '--output', str(bundle))
        config = json.loads((bundle / 'opencode.json').read_text())
        require((export['agents'], export['skills']) == tuple(sum(e.kind == k for e in expected) for k in ('agent', 'skill')),
                'Wrong exported catalog size.')
        require(config['default_agent'] == 'joerg', 'Default agent is not Jörg.')
        require(cli('export', '--runtime', 'opencode', '--output', str(bundle))['changed'] == 0,
                'Unchanged export rewrote files.')
        profile = bundle / 'agents/joerg.md'
        original = profile.read_bytes()
        profile.write_text('Fixture human customization\n')
        try:
            error = cli('export', '--runtime', 'opencode', '--output', str(bundle), expected=1)
            require('edited' in error and profile.read_text() == 'Fixture human customization\n',
                    'A human-edited profile was not protected.')
        finally:
            profile.write_bytes(original)
        passed('Build and verify', 'OpenCode JSON selects joerg; complete native catalog; repeat is a no-op; human edit protected.')

        for task, evidence in [('T1', 'Native bundle and repeat-export checks passed.'),
                               ('T2', 'HTTP 412 and 428 observed; fixture feedback remains intact.')]:
            status, current = request('GET', route)
            require(status == 200, 'Could not reload before update.')
            status, _ = request('PATCH', route + '/tasks/' + task,
                {'status': 'done', 'evidence': evidence}, current['etag'])
            require(status == 200, f'Failed to complete {task}.')

        current = store.read('workflow-pilot')
        def save_handoff(previous):
            before = previous.split('\n## Handoff\n', 1)[0]
            return before.replace('Disposition: open', 'Disposition: addressed in this fixture; evidence recorded.') + (
                '\n## Handoff\n\n'
                'T1 and T2 verified. T3 remains: reload this record, confirm evidence and archive.\n'
                'Feedback above is a fixture, not human approval. No external writes are pending.\n')
        store.update('workflow-pilot', current['etag'], save_handoff)
        resumed = tk.WorkStore(project)
        recovered = resumed.read('workflow-pilot')
        require('T3 remains: reload this record' in recovered['markdown'] and feedback in recovered['markdown'],
                'Fresh store could not recover shared context.')
        require([t['status'] for t in recovered['tasks']] == ['done', 'done', 'open'],
                'Recovered task state is incorrect.')
        resumed.task('workflow-pilot', 'T3', 'done', 'Fresh store recovered plan, feedback, evidence and next action.',
                     recovered['etag'])
        archived = cli('work', '--workspace', str(project), 'archive', 'workflow-pilot')
        require(archived['path'] == 'workspace/archive/workflow-pilot.md' and archived['status'] == 'archived',
                'Archive did not use workspace/archive.')
        passed('Handoff and closeout', 'A fresh store recovered plan/feedback/evidence; CLI archived all completed tasks.')
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)

    # Exercise old-layout migration in a separate generated fixture, preserving bytes.
    legacy = run_root / 'migration-project'
    legacy.mkdir()
    cli('work', '--workspace', str(legacy), 'new', 'legacy-record', '--title', 'Preserve original context')
    old = legacy / '.ai'
    old.mkdir()
    (legacy / 'workspace/work').rename(old / 'work')
    before = (old / 'work/legacy-record.md').read_bytes()
    preview = cli('work', '--workspace', str(legacy), 'migrate', '--dry-run')
    require(len(preview['moves']) == 1 and (old / 'work/legacy-record.md').read_bytes() == before,
            'Migration dry-run changed data.')
    moved = cli('work', '--workspace', str(legacy), 'migrate')
    require(moved['legacy_directory_removed'] and not old.exists(), 'Empty .ai directory remained.')
    require((legacy / 'workspace/work/legacy-record.md').read_bytes() == before, 'Migration changed record bytes.')
    require(not cli('work', '--workspace', str(legacy), 'migrate')['moves'], 'Migration was not repeatable.')
    require(not list(run_root.rglob('.ai')), 'The pilot left an old working directory.')
    passed('Migration', 'Dry-run preserved data; migration retained bytes, removed empty .ai and safely repeated.')

    report = {'result': 'passed', 'completed_at': datetime.now(UTC).isoformat(timespec='seconds'),
              'output': run_root.relative_to(tk.ROOT).as_posix(), 'steps': results,
              'limits': ['No model invocation or installed-host permission check.',
                         'No live tracker write, human approval, merge or deployment.',
                         'HTTP resource checks do not replace visual browser verification.']}
    (run_root / 'report.json').write_text(json.dumps(report, indent=2) + '\n')
    return report


if __name__ == '__main__':
    try:
        print(json.dumps(run(), indent=2))
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as exc:
        print(f'Workflow smoke check failed: {exc}', file=sys.stderr)
        raise SystemExit(1)
