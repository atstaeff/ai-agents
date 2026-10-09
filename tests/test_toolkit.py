from __future__ import annotations

import csv
import http.client
import io
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import ai_toolkit as tk


class CatalogTests(unittest.TestCase):
    def test_complete_catalog_and_links(self):
        entries = tk.catalog()
        self.assertEqual(len([e for e in entries if e.kind == 'agent']), 23)
        self.assertEqual(len([e for e in entries if e.kind == 'skill']), 48)
        self.assertEqual(tk.check(), [])

    def test_frontmatter_rejects_duplicate_or_invalid_values(self):
        for text in ('No metadata', '---\nname: test\nname: other\n---\n', '---\nname: "broken\n---\n'):
            with self.subTest(text=text), self.assertRaises(tk.ToolkitError):
                tk.metadata(text)

    def test_unicode_and_slug_validation(self):
        meta, body = tk.metadata('---\nname: "joerg"\ndescription: "Act as Jörg"\n---\n\nBody')
        self.assertEqual((meta['description'], body), ('Act as Jörg', 'Body'))
        for name in ('../escape', 'Bad_Name', 'double--dash', 'x'*65, ''):
            with self.subTest(name=name), self.assertRaises(tk.ToolkitError):
                tk.slug(name)

    def test_obsidian_uri_encodes_every_component(self):
        self.assertEqual(tk.obsidian_uri('Jörgs Wissen & Ideen', '01_Projects/Kunden #1.md'),
                         'obsidian://open?vault=J%C3%B6rgs%20Wissen%20%26%20Ideen&file=01_Projects%2FKunden%20%231.md')
        self.assertIn('Projects%2FNote.md', tk.obsidian_uri('Vault', 'Projects\\Note.md'))

    def test_obsidian_uri_rejects_absolute_and_parent_paths(self):
        for path in ('/mnt/c/vault/note.md','C:\\vault\\note.md','../note.md','Projects/../note.md','Projects//note.md'):
            with self.subTest(path=path), self.assertRaises(tk.ToolkitError):
                tk.obsidian_uri('Vault', path)


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.output = Path(self.temp.name) / 'bundle'

    def test_all_native_layouts_and_rebased_links(self):
        for runtime, skills, agents in [('opencode','skills','agents'), ('copilot','.github/skills','.github/agents'), ('portable','.agents/skills','agents')]:
            with self.subTest(runtime=runtime):
                output = self.output / runtime
                result = tk.export(runtime, output)
                self.assertEqual((result['agents'], result['skills']), (23,48))
                self.assertEqual(len(list((output/skills).glob('*/SKILL.md'))),48)
                for path in list((output/skills).rglob('*.md')) + list((output/agents).glob('*.md')):
                    for target in tk.LINK.findall(path.read_text()):
                        if not tk.urlsplit(target).scheme:
                            self.assertTrue((path.parent / tk.unquote(target.split('#')[0])).exists(), (path,target))
                skill = output/skills/'api-design/SKILL.md'
                self.assertIn('references/api-design.md',skill.read_text())

    def test_opencode_primary_profiles_permissions_and_no_model_forcing(self):
        tk.export('opencode', self.output)
        config = json.loads((self.output/'opencode.json').read_text())
        self.assertEqual(config['default_agent'], 'joerg')
        self.assertNotIn('model', config)
        self.assertNotIn('plugin', config)
        self.assertTrue(Path(config['instructions'][0]).is_file())
        self.assertIn('mode: primary', (self.output/'agents/joerg.md').read_text())
        self.assertIn('mode: subagent', (self.output/'agents/python-expert.md').read_text())
        self.assertIn("'.ai/work/**': allow", (self.output/'agents/plan.md').read_text())
        self.assertIn('bash: deny', (self.output/'agents/code-reviewer.md').read_text())

    def test_update_is_idempotent_and_protects_human_edits(self):
        tk.export('opencode', self.output)
        before = (self.output/'opencode.json').read_bytes()
        tk.export('opencode', self.output)
        self.assertEqual((self.output/'opencode.json').read_bytes(), before)
        (self.output/'agents/joerg.md').write_text('My custom instructions')
        with self.assertRaisesRegex(tk.ToolkitError, 'edited file'):
            tk.export('opencode', self.output)
        self.assertEqual((self.output/'agents/joerg.md').read_text(), 'My custom instructions')

    def test_plannotator_opt_in_preserves_plan_permissions_and_catalog(self):
        options = tk.OpenCodeOptions(plannotator=True)
        tk.export('opencode', self.output, opencode_options=options)
        config = json.loads((self.output/'opencode.json').read_text())
        self.assertEqual(config['plugin'], [['@plannotator/opencode@latest', {'workflow': 'user-managed'}]])
        self.assertEqual(config['share'], 'disabled')
        self.assertEqual(config['permission']['submit_plan'], 'deny')
        self.assertNotIn('model', config)
        plan = (self.output/'agents/plan.md').read_text()
        self.assertIn('  submit_plan: allow\n  plan_exit: deny\n', plan)
        self.assertIn("'.ai/work/**': allow", plan)
        self.assertNotIn("'*.md': allow", plan)
        self.assertIn('  bash: deny\n  task: deny\n', plan)
        self.assertIn('installed tool schema', plan)
        self.assertNotIn('Plannotator plan review is enabled.', (self.output/'catalog/agents/plan.agent.md').read_text())
        with patch.object(tk, 'atomic_write', wraps=tk.atomic_write) as write:
            again = tk.export('opencode', self.output, opencode_options=options)
        write.assert_not_called()
        self.assertEqual(again['changed'], 0)

    def test_models_and_variants_are_independent_without_enabling_plugins(self):
        options = tk.OpenCodeOptions(plan_model='local/planner', plan_variant='high',
                                     build_model='other/coder', build_variant='medium')
        tk.export('opencode', self.output, opencode_options=options)
        config = json.loads((self.output/'opencode.json').read_text())
        self.assertEqual(config['agent'], {'plan': {'model': 'local/planner', 'variant': 'high'},
                                           'build': {'model': 'other/coder', 'variant': 'medium'}})
        self.assertNotIn('plugin', config)
        self.assertNotIn('model', config)
        self.assertIn('bash: deny', (self.output/'agents/plan.md').read_text())

    def test_opencode_options_reject_invalid_input_before_writing(self):
        for options in (tk.OpenCodeOptions(plan_variant='high'), tk.OpenCodeOptions(build_variant='medium'),
                        tk.OpenCodeOptions(plan_model='no-provider'), tk.OpenCodeOptions(build_model='provider/'),
                        tk.OpenCodeOptions(plan_model='provider/model#high'),
                        tk.OpenCodeOptions(plan_model='provider/model\nother'),
                        tk.OpenCodeOptions(plan_model='provider/model', plan_variant='bad name')):
            with self.subTest(options=options), self.assertRaises(tk.ToolkitError):
                tk.export('opencode', self.output, opencode_options=options)
            self.assertFalse(self.output.exists())
        for runtime in ('copilot', 'portable'):
            for options in (tk.OpenCodeOptions(plannotator=True), tk.OpenCodeOptions(build_model='provider/model')):
                with self.subTest(runtime=runtime, options=options), self.assertRaisesRegex(tk.ToolkitError, 'runtime opencode'):
                    tk.export(runtime, self.output, opencode_options=options)
                self.assertFalse(self.output.exists())

    def test_cli_exports_review_and_phase_settings_and_protects_edits(self):
        args = ['export', '--runtime', 'opencode', '--output', str(self.output), '--plannotator',
                '--plan-model', 'provider/planner', '--build-model', 'provider/coder',
                '--plan-variant', 'high', '--build-variant', 'medium']
        with patch('sys.stdout', new_callable=io.StringIO):
            self.assertEqual(tk.main(args + ['--dry-run']), 0)
            self.assertFalse(self.output.exists())
            self.assertEqual(tk.main(args), 0)
        path = self.output/'opencode.json'
        config = json.loads(path.read_text())
        self.assertEqual(config['agent']['plan']['variant'], 'high')
        self.assertEqual(config['agent']['build']['model'], 'provider/coder')
        config['agent']['build']['model'] = 'human/choice'
        path.write_text(json.dumps(config))
        with patch('sys.stderr', new_callable=io.StringIO):
            self.assertEqual(tk.main(args), 1)
        self.assertEqual(json.loads(path.read_text())['agent']['build']['model'], 'human/choice')

    def test_unchanged_exports_preserve_files_and_write_nothing(self):
        for runtime in ('opencode', 'copilot', 'portable'):
            with self.subTest(runtime=runtime):
                output = self.output / runtime
                first = tk.export(runtime, output)
                before = {p: (p.stat().st_ino, p.stat().st_mtime_ns)
                          for p in output.rglob('*') if p.is_file()}
                with patch.object(tk, 'atomic_write', wraps=tk.atomic_write) as write:
                    second = tk.export(runtime, output)
                write.assert_not_called()
                self.assertEqual((second['changed'], second['removed']), (0, 0))
                self.assertEqual(second['unchanged'], first['files'])
                self.assertEqual(before, {p: (p.stat().st_ino, p.stat().st_mtime_ns)
                                         for p in before})

    def source_fixture(self):
        root = Path(self.temp.name) / 'source'
        for folder, name in (('agents', 'one.agent.md'), ('agents', 'two.agent.md'),
                             ('skills/skill', 'SKILL.md')):
            path = root / folder / name
            path.parent.mkdir(parents=True, exist_ok=True)
            slug = 'skill' if name == 'SKILL.md' else name.removesuffix('.agent.md')
            path.write_text(f'---\nname: {slug}\ndescription: A focused profile\n---\n\nOriginal body.\n')
        return root

    def test_source_update_only_rewrites_affected_files(self):
        root = self.source_fixture()
        tk.export('portable', self.output, root)
        source = root / 'agents/one.agent.md'
        source.write_text(source.read_text().replace('Original body.', 'Updated body.'))
        with patch.object(tk, 'atomic_write', wraps=tk.atomic_write) as write:
            result = tk.export('portable', self.output, root)
        self.assertEqual({call.args[0].relative_to(self.output).as_posix()
                          for call in write.call_args_list},
                         {'catalog/agents/one.agent.md', 'agents/one.agent.md', '.ai-toolkit-manifest.json'})
        self.assertEqual(result['changed'], 2)
        self.assertIn('Updated body.', (self.output / 'agents/one.agent.md').read_text())

    def test_obsolete_files_are_removed_but_edited_ones_are_protected(self):
        root = self.source_fixture()
        tk.export('portable', self.output, root)
        (root / 'agents/two.agent.md').unlink()
        edited = self.output / 'agents/two.agent.md'
        edited.write_text('Keep this human edit.')
        with self.assertRaisesRegex(tk.ToolkitError, 'edited file'):
            tk.export('portable', self.output, root)
        self.assertEqual(edited.read_text(), 'Keep this human edit.')
        preview = tk.export('portable', self.output, root, force=True, dry_run=True)
        self.assertEqual((preview['changed'], preview['removed']), (1, 2))
        self.assertTrue(edited.exists())
        result = tk.export('portable', self.output, root, force=True)
        self.assertEqual((result['changed'], result['removed']), (1, 2))
        self.assertFalse(edited.exists())
        self.assertFalse((self.output / 'catalog/agents/two.agent.md').exists())
        self.assertTrue((self.output / 'agents/one.agent.md').is_file())

    def test_missing_owned_file_is_restored(self):
        tk.export('opencode', self.output)
        missing = self.output / 'agents/build.md'
        expected = missing.read_bytes()
        missing.unlink()
        with patch.object(tk, 'atomic_write', wraps=tk.atomic_write) as write:
            result = tk.export('opencode', self.output)
        self.assertEqual(result['changed'], 1)
        self.assertEqual([call.args[0] for call in write.call_args_list], [missing])
        self.assertEqual(missing.read_bytes(), expected)

    def test_unmanaged_configuration_is_not_overwritten(self):
        self.output.mkdir()
        (self.output/'opencode.json').write_text('{"model":"my-model"}')
        with self.assertRaises(tk.ToolkitError):
            tk.export('opencode', self.output)
        self.assertFalse((self.output/'catalog').exists())
        tk.export('opencode', self.output, force=True)
        self.assertEqual(json.loads((self.output/'opencode.json').read_text())['default_agent'], 'joerg')

    def test_dry_run_writes_nothing(self):
        tk.export('portable',self.output,dry_run=True)
        self.assertFalse(self.output.exists())

    def test_manifest_traversal_and_symlinks_are_rejected(self):
        self.output.mkdir()
        manifest = self.output/'.ai-toolkit-manifest.json'
        manifest.write_text(json.dumps({'files':{'../outside.txt':'anything'}}))
        with self.assertRaises(tk.ToolkitError):
            tk.export('opencode',self.output)
        manifest.unlink()
        outside = Path(self.temp.name)/'outside'
        outside.mkdir()
        (self.output/'catalog').symlink_to(outside,target_is_directory=True)
        with self.assertRaises(tk.ToolkitError):
            tk.export('opencode',self.output,force=True)
        self.assertEqual(list(outside.iterdir()),[])

    def test_sources_and_parent_cannot_be_export_destinations(self):
        for output in (tk.ROOT,tk.ROOT.parent,tk.ROOT/'skills/generated'):
            with self.subTest(output=output), self.assertRaises(tk.ToolkitError):
                tk.export('opencode',output,dry_run=True)


class WorkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.workspace = Path(self.temp.name)
        self.store = tk.WorkStore(self.workspace)
        self.record = self.store.create('feature', 'A useful feature', 'product')

    def test_create_read_and_duplicate_protection(self):
        self.assertEqual(self.record['title'],'A useful feature')
        self.assertEqual(self.record['tasks'][0]['status'],'open')
        self.assertEqual(len(self.store.list()),1)
        with self.assertRaises(tk.Conflict):
            self.store.create('feature','Duplicate')

    def test_feedback_preserves_plan_comments_and_task_evidence(self):
        first = self.store.feedback('feature','Keep my exact words: <script>alert(1)</script>',self.record['etag'])
        second = self.store.feedback('feature','A second\nmultiline comment',first['etag'])
        self.assertIn('### F1',second['markdown'])
        self.assertIn('### F2',second['markdown'])
        self.assertIn('> Keep my exact words: <script>alert(1)</script>',second['markdown'])
        updated = self.store.task('feature','T1','done','unittest: acceptance scenario passed',second['etag'])
        self.assertIn('A second',updated['markdown'])
        self.assertIn('## Plan',updated['markdown'])
        self.assertEqual(updated['tasks'][0]['status'],'done')

    def test_stale_update_does_not_drop_other_comments(self):
        current = self.store.feedback('feature','New human comment',self.record['etag'])
        with self.assertRaises(tk.Conflict):
            self.store.task('feature','T1','done','checked',self.record['etag'])
        self.assertEqual(self.store.read('feature')['markdown'],current['markdown'])

    def test_two_concurrent_feedback_writes_require_retry(self):
        def write(comment):
            try:
                self.store.feedback('feature',comment,self.record['etag'])
                return 'saved'
            except tk.Conflict:
                return 'conflict'
        with ThreadPoolExecutor(max_workers=2) as pool:
            outcomes = list(pool.map(write,['one','two']))
        self.assertCountEqual(outcomes,['saved','conflict'])
        self.assertEqual(self.store.read('feature')['markdown'].count('### F1'),1)

    def test_external_editor_change_is_detected(self):
        path = self.store.path('feature')
        path.write_text(path.read_text()+'\nHuman note from the editor.\n')
        with self.assertRaises(tk.Conflict):
            self.store.feedback('feature','comment',self.record['etag'])
        self.assertIn('Human note',path.read_text())

    def test_completed_task_needs_evidence_and_known_id(self):
        with self.assertRaises(tk.ToolkitError):
            self.store.task('feature','T1','done','',self.record['etag'])
        with self.assertRaises(tk.ToolkitError):
            self.store.task('feature','T9','open','',self.record['etag'])

    def test_archiving_requires_completion_and_preserves_record(self):
        with self.assertRaises(tk.ToolkitError):
            self.store.archive('feature',self.record['etag'])
        current = self.store.task('feature','T1','done','Acceptance checks passed',self.record['etag'])
        archived = self.store.archive('feature',current['etag'])
        self.assertEqual(archived['status'],'archived')
        self.assertEqual(len(self.store.list()),0)
        self.assertEqual(len(self.store.list(True)),1)
        self.assertIn('Acceptance checks passed',archived['markdown'])

    def test_malformed_or_duplicate_task_rows_are_not_silently_ignored(self):
        for replacement in ('| T1 | A task | unknown |  |','| T1 | A task | open |  |\n| T1 | Duplicate | done | test |'):
            with self.subTest(replacement=replacement):
                text = tk.TASK_ROW.sub(replacement,self.record['markdown'])
                self.store.path('feature').write_text(text)
                with self.assertRaises(tk.ToolkitError):
                    self.store.read('feature')

    def test_task_update_ignores_table_examples_outside_tasks_section(self):
        path = self.store.path('feature')
        example = '\n| T1 | Historical example | open |  |\n'
        path.write_text(path.read_text()+example)
        current = self.store.read('feature')
        updated = self.store.task('feature','T1','done','verified',current['etag'])
        self.assertTrue(updated['markdown'].endswith(example))

    def test_paths_and_symlinked_record_are_rejected(self):
        with self.assertRaises(tk.ToolkitError):
            self.store.create('../escape','Bad')
        target = self.workspace/'private.md'
        target.write_text('private')
        self.store.path('feature').unlink()
        (self.workspace/'.ai/work/feature.md').symlink_to(target)
        with self.assertRaises(tk.ToolkitError):
            self.store.read('feature')
        self.assertEqual(target.read_text(),'private')

    def test_csv_is_generated_and_formula_safe(self):
        path = self.store.path('feature')
        path.write_text(path.read_text().replace('Define and verify the outcome','=SUM(1,2)'))
        rows = list(csv.reader(io.StringIO(self.store.csv('feature'))))
        self.assertEqual(rows[0],['id','title','status','evidence'])
        self.assertEqual(rows[1][1],"'=SUM(1,2)")


class APITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.server = tk.serve(Path(cls.temp.name),0)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever,daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()
        cls.temp.cleanup()

    def request(self, method, path, data=None, headers=None):
        connection = http.client.HTTPConnection('127.0.0.1',self.port,timeout=3)
        body = json.dumps(data) if data is not None else None
        merged = {'Content-Type':'application/json',**(headers or {})}
        connection.request(method,path,body,merged)
        response = connection.getresponse()
        status, response_headers, raw = response.status, dict(response.getheaders()), response.read()
        connection.close()
        value = json.loads(raw) if 'application/json' in response_headers.get('Content-Type','') else raw.decode()
        return status,response_headers,value

    def test_catalog_frontend_and_contract_are_served_locally(self):
        status,headers,html = self.request('GET','/')
        self.assertEqual(status,200)
        self.assertIn('AI Workbench',html)
        self.assertIn("script-src 'self'",headers['Content-Security-Policy'])
        self.assertNotIn('https://',html)
        self.assertEqual(len(self.request('GET','/api/v1/catalog')[2]),71)
        self.assertEqual(self.request('GET','/api/v1/openapi.json')[2]['openapi'],'3.1.0')

    def test_full_create_comment_complete_flow_with_etags(self):
        status,headers,record = self.request('POST','/api/v1/work',{'id':'api-flow','title':'API flow'})
        self.assertEqual(status,201)
        old_etag = headers['ETag']
        status,_,record = self.request('POST','/api/v1/work/api-flow/feedback',{'text':'Keep this comment.'},{'If-Match':old_etag})
        self.assertEqual(status,200)
        status,_,_ = self.request('PATCH','/api/v1/work/api-flow/tasks/T1',{'status':'done','evidence':'checked'},{'If-Match':old_etag})
        self.assertEqual(status,412)
        status,_,updated = self.request('PATCH','/api/v1/work/api-flow/tasks/T1',{'status':'done','evidence':'Acceptance scenario checked'},{'If-Match':record['etag']})
        self.assertEqual(status,200)
        self.assertIn('Keep this comment.',updated['markdown'])

    def test_missing_if_match(self):
        self.request('POST','/api/v1/work',{'id':'missing-match','title':'Missing match'})
        self.assertEqual(self.request('POST','/api/v1/work/missing-match/feedback',{'text':'Hi'})[0],428)

    def test_untrusted_host_origin_and_cross_site_requests(self):
        for headers in ({'Host':'attacker.example'}, {'Origin':'https://attacker.example'}, {'Sec-Fetch-Site':'cross-site'}):
            with self.subTest(headers=headers):
                self.assertEqual(self.request('GET','/api/v1/work',headers=headers)[0],403)

    def test_bad_input_paths_media_types_and_methods(self):
        for data in ({'id':'../escape','title':'Bad'}, {'id':'bad-title','title':42}, [], {'id':'bad-kind','title':'Bad','kind':'other'}):
            with self.subTest(data=data):
                self.assertEqual(self.request('POST','/api/v1/work',data)[0],400)
        self.assertEqual(self.request('GET','/api/v1/work/%2e%2e%2fsecret')[0],404)
        self.assertEqual(self.request('GET','/missing')[0],404)
        self.assertEqual(self.request('DELETE','/api/v1/work')[0],405)
        self.assertEqual(self.request('POST','/api/v1/work',{'id':'x','title':'X'},{'Content-Type':'text/plain'})[0],415)
        self.assertEqual(self.request('POST','/api/v1/work',{'id':'large','title':'x'*17000})[0],413)


if __name__ == '__main__':
    unittest.main()
