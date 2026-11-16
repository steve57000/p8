"""Regression checks for the notebook's source-directory discovery cell.

Run with: python -m unittest discover -s tests -v
Windows-specific control flow is simulated; no native Windows execution is claimed.
The checks use only Python's standard library and never read the real datasets.
"""

from contextlib import ExitStack, contextmanager, redirect_stdout
from io import StringIO
import json
import os
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import MagicMock, patch


REPOSITORY = Path(__file__).resolve().parents[1]
NOTEBOOK_NAME = 'Bell_Steve_1_Notebook_102026.ipynb'
NOTEBOOK = REPOSITORY / 'livrables' / NOTEBOOK_NAME
CELLS = json.loads(NOTEBOOK.read_text(encoding='utf-8'))['cells']
PATH_CELL = next(
    ''.join(cell['source']) for cell in CELLS
    if cell['cell_type'] == 'code'
    and "'historique': 'historique_immobilier_paris_2017_2021.xlsx'" in ''.join(cell['source'])
    and 'DOSSIER_RESULTATS' in ''.join(cell['source'])
)
FILENAMES = (
    'historique_immobilier_paris_2017_2021.xlsx',
    'portefeuille_actifs.xlsx',
    'echantillon_a_classer2.xlsx',
)


@contextmanager
def working_directory(path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


def fake_tkinter(selection='', error=None):
    tkinter = types.ModuleType('tkinter')
    tkinter.TclError = type('TclError', (Exception,), {})
    window = MagicMock()
    tkinter.Tk = MagicMock(return_value=window)
    filedialog = types.ModuleType('tkinter.filedialog')
    filedialog.askdirectory = MagicMock(return_value=str(selection))
    if error is not None:
        tkinter.Tk.side_effect = tkinter.TclError(error)
    tkinter.filedialog = filedialog
    return tkinter, filedialog, window


class NotebookPathsTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='p8-paths-')
        self.addCleanup(self.temporary.cleanup)
        self.area = Path(self.temporary.name)
        self.external = self.area / 'Windows' / 'System32'
        self.external.mkdir(parents=True)
        self.project, self.raw = self.make_project('project')
        self.outside_interpreter = self.area / 'external-python'
        self.outside_interpreter.mkdir()

    def make_project(self, name, legacy=False, complete=True):
        project = self.area / name
        (project / 'livrables').mkdir(parents=True)
        (project / 'livrables' / NOTEBOOK_NAME).write_text('{}', encoding='utf-8')
        raw = project / ('livrables/data/raw' if legacy else 'data/raw')
        raw.mkdir(parents=True)
        for filename in FILENAMES if complete else FILENAMES[:1]:
            (raw / filename).write_bytes(b'test fixture')
        return project, raw

    def run_cell(self, *, cwd=None, prefix=None, executable=None,
                 project=None, data=None, env=None, system='Linux', tkinter=None):
        namespace = {
            'Path': Path,
            'platform': types.SimpleNamespace(system=lambda: system),
            'DOSSIER_PROJET': project,
            'DOSSIER_DONNEES': data,
        }
        cwd = self.external if cwd is None else cwd
        prefix = self.outside_interpreter if prefix is None else prefix
        executable = self.outside_interpreter / 'python' if executable is None else executable
        with ExitStack() as stack:
            stack.enter_context(working_directory(cwd))
            stack.enter_context(patch.object(sys, 'prefix', str(prefix)))
            stack.enter_context(patch.object(sys, 'executable', str(executable)))
            stack.enter_context(patch.dict(os.environ, env or {}, clear=True))
            if tkinter is not None:
                tk, dialog = tkinter
                stack.enter_context(patch.dict(sys.modules, {
                    'tkinter': tk,
                    'tkinter.filedialog': dialog,
                }))
            stack.enter_context(redirect_stdout(StringIO()))
            exec(compile(PATH_CELL, str(NOTEBOOK), 'exec'), namespace)
        return namespace

    def assert_destination(self, namespace, project=None, raw=None):
        project = self.project if project is None else project
        raw = self.raw if raw is None else raw
        self.assertEqual(namespace['RACINE'], project)
        self.assertEqual(namespace['DATA_DIR'], raw)
        self.assertEqual(namespace['DOSSIER_RESULTATS'], project / 'livrables')
        self.assertTrue((project / 'livrables/figures').is_dir())
        self.assertEqual(list(self.external.iterdir()), [])
        self.assertFalse((project / 'livrables/livrables').exists())

    def assert_no_exports(self, project=None):
        project = self.project if project is None else project
        self.assertFalse((project / 'livrables/figures').exists())
        self.assertEqual(list(self.external.iterdir()), [])

    def test_project_root(self):
        self.assert_destination(self.run_cell(cwd=self.project))

    def test_livrables_directory(self):
        self.assert_destination(self.run_cell(cwd=self.project / 'livrables'))

    def test_external_working_directory_uses_interpreter_prefix(self):
        self.assert_destination(self.run_cell(prefix=self.project / '.venv'))

    def test_external_working_directory_uses_interpreter_executable(self):
        self.assert_destination(self.run_cell(executable=self.project / '.venv/Scripts/python.exe'))

    def test_external_virtualenv_does_not_guess_a_project(self):
        with self.assertRaisesRegex(FileNotFoundError, 'DOSSIER_PROJET'):
            self.run_cell(prefix=self.area / 'venvs/p8')
        self.assert_no_exports()

    def test_explicit_absolute_project(self):
        self.assert_destination(self.run_cell(project=self.project))

    def test_explicit_absolute_data_also_locates_exports(self):
        self.assert_destination(self.run_cell(data=self.raw))

    def test_relative_project_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'absolu'):
            self.run_cell(project=Path('project'))
        self.assert_no_exports()

    def test_nonexistent_explicit_project_is_strict(self):
        with self.assertRaisesRegex(FileNotFoundError, 'DOSSIER_PROJET'):
            self.run_cell(prefix=self.project / '.venv', project=self.area / 'missing')
        self.assert_no_exports()

    def test_nonexistent_explicit_data_is_strict(self):
        with self.assertRaisesRegex(FileNotFoundError, 'portefeuille_actifs.xlsx'):
            self.run_cell(cwd=self.project, data=self.area / 'missing')
        self.assert_no_exports()

    def test_incomplete_explicit_data_is_strict(self):
        incomplete = self.area / 'incomplete'
        incomplete.mkdir()
        (incomplete / FILENAMES[0]).touch()
        with self.assertRaisesRegex(FileNotFoundError, 'echantillon_a_classer2.xlsx'):
            self.run_cell(cwd=self.project, data=incomplete)
        self.assert_no_exports()

    def test_relative_root_data_from_external_working_directory(self):
        self.assert_destination(self.run_cell(prefix=self.project / '.venv', data='data/raw'))

    def test_relative_parent_data_from_external_working_directory(self):
        # Exact reported trigger: kernel in System32 and old ../data/raw parameter.
        self.assert_destination(self.run_cell(prefix=self.project / '.venv', data='../data/raw'))

    def test_invalid_relative_data_does_not_fallback_to_complete_default(self):
        with self.assertRaisesRegex(FileNotFoundError, 'missing-data'):
            self.run_cell(prefix=self.project / '.venv', data='missing-data')
        self.assert_no_exports()

    def test_legacy_layout_from_livrables(self):
        project, raw = self.make_project('legacy', legacy=True)
        self.assert_destination(self.run_cell(cwd=project / 'livrables'), project, raw)

    def test_legacy_layout_from_external_interpreter_prefix(self):
        project, raw = self.make_project('legacy', legacy=True)
        self.assert_destination(self.run_cell(prefix=project / '.venv'), project, raw)

    def test_legacy_absolute_data_anchors_project(self):
        project, raw = self.make_project('legacy', legacy=True)
        self.assert_destination(self.run_cell(data=raw), project, raw)

    def test_multiple_projects_need_explicit_choice(self):
        other, _ = self.make_project('other')
        with self.assertRaisesRegex(ValueError, 'Plusieurs projets'):
            self.run_cell(cwd=self.project, prefix=other / '.venv')
        self.assert_no_exports()
        self.assert_no_exports(other)

    def test_explicit_project_resolves_other_interpreter_project(self):
        other, _ = self.make_project('other')
        self.assert_destination(self.run_cell(project=self.project, prefix=other / '.venv'))

    def test_ambiguous_relative_data_sources_are_rejected(self):
        # Two different complete directories match the same relative parameter.
        duplicate = self.project / 'livrables/data/raw'
        duplicate.mkdir(parents=True)
        for name in FILENAMES:
            (duplicate / name).touch()
        with self.assertRaisesRegex(ValueError, 'relatif est ambigu'):
            self.run_cell(cwd=self.project, data='data/raw')
        self.assert_no_exports()

    def test_stale_environment_is_ignored_when_kernel_project_is_known(self):
        other, _ = self.make_project('old-project')
        self.assert_destination(self.run_cell(prefix=self.project / '.venv', env={
            'VIRTUAL_ENV': str(other / '.venv'),
            'CONDA_PREFIX': str(other / 'conda'),
        }))
        self.assert_no_exports(other)

    def test_environment_fallback_with_unique_project(self):
        self.assert_destination(self.run_cell(env={'VIRTUAL_ENV': str(self.project / '.venv')}))

    def test_ambiguous_environment_fallback_is_rejected(self):
        other, _ = self.make_project('other')
        with self.assertRaisesRegex(ValueError, 'Plusieurs projets'):
            self.run_cell(env={
                'VIRTUAL_ENV': str(self.project / '.venv'),
                'CONDA_PREFIX': str(other / 'conda'),
            })
        self.assert_no_exports()

    def test_windows_directory_selection(self):
        tk, dialog, window = fake_tkinter(self.project)
        self.assert_destination(self.run_cell(system='Windows', tkinter=(tk, dialog)))
        dialog.askdirectory.assert_called_once()
        window.destroy.assert_called_once()

    def test_windows_directory_selection_cancellation(self):
        tk, dialog, window = fake_tkinter('')
        with self.assertRaisesRegex(FileNotFoundError, 'DOSSIER_PROJET'):
            self.run_cell(system='Windows', tkinter=(tk, dialog))
        window.destroy.assert_called_once()
        self.assert_no_exports()

    def test_windows_without_tkinter(self):
        with self.assertRaisesRegex(FileNotFoundError, 'DOSSIER_PROJET'):
            self.run_cell(system='Windows', tkinter=(None, None))
        self.assert_no_exports()

    def test_windows_unavailable_display(self):
        tk, dialog, _ = fake_tkinter(error='display unavailable')
        with self.assertRaisesRegex(FileNotFoundError, 'DOSSIER_PROJET'):
            self.run_cell(system='Windows', tkinter=(tk, dialog))
        dialog.askdirectory.assert_not_called()
        self.assert_no_exports()

    def test_windows_invalid_selected_directory(self):
        tk, dialog, window = fake_tkinter(self.external)
        with self.assertRaisesRegex(FileNotFoundError, 'DOSSIER_PROJET'):
            self.run_cell(system='Windows', tkinter=(tk, dialog))
        window.destroy.assert_called_once()
        self.assert_no_exports()


if __name__ == '__main__':
    unittest.main()
