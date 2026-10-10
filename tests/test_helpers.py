import contextlib
from fractions import Fraction
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


installer = load('installer', ROOT / 'scripts' / 'install.py')
timing = load('timing', ROOT / 'skills' / 'motion-storyboard' / 'scripts' / 'frame_plan.py')


class TimingTests(unittest.TestCase):
    def test_whole_frame_duration_excludes_duplicate_endpoint(self):
        result = timing.frame_plan('30', seconds='6')
        self.assertEqual(result['frame_count'], 180)
        self.assertEqual(result['frame_range']['end_exclusive'], 180)
        self.assertEqual([s['frame'] for s in result['samples']], [0, 44, 89, 134, 179])
        self.assertEqual(Fraction(result['samples'][-1]['time_seconds_exact']), Fraction(179, 30))

    def test_fractional_rate_stays_exact(self):
        result = timing.frame_plan('30000/1001', frames=300)
        self.assertEqual(Fraction(result['duration_seconds_exact']), Fraction(1001, 100))
        self.assertEqual(result['fps_exact'], '30000/1001')

    def test_nonintegral_duration_requires_explicit_frame_choice(self):
        with self.assertRaises(ValueError):
            timing.frame_plan('30000/1001', seconds='10')

    def test_invalid_ranges_are_rejected(self):
        for kwargs in [dict(seconds='0'), dict(frames=0), dict(frames=1, samples=2), dict(frames=5, samples=0), dict(frames=2.5), dict(frames=5, samples=1.5)]:
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                timing.frame_plan('30', **kwargs)
        with self.assertRaises(ValueError):
            timing.frame_plan('0', frames=30)

    def test_one_frame_and_sample(self):
        result = timing.frame_plan('30', frames=1, samples=1)
        self.assertEqual(result['samples'][0]['frame'], 0)
        self.assertEqual(result['duration_seconds_exact'], '1/30')

    def test_samples_are_distinct_and_inside_bounds(self):
        for frames in range(1, 30):
            for count in range(1, frames + 1):
                indices = [x['frame'] for x in timing.frame_plan('24', frames=frames, samples=count)['samples']]
                self.assertEqual(len(set(indices)), count)
                self.assertTrue(all(0 <= i < frames for i in indices))


class InstallTests(unittest.TestCase):
    def call(self, *args, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            installer.install(*args, **kwargs)

    def test_complete_resources_and_installed_helper_execute(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.call(tmp)
            target = Path(tmp) / '.claude' / 'skills'
            self.assertEqual(len(list(target.iterdir())), 6)
            for source in (ROOT / 'skills').rglob('*'):
                if source.is_file() and '__pycache__' not in source.parts:
                    self.assertEqual(source.read_bytes(), (target / source.relative_to(ROOT / 'skills')).read_bytes())
            script = target / 'motion-storyboard' / 'scripts' / 'frame_plan.py'
            result = subprocess.run([sys.executable, str(script), '--seconds', '6', '--fps', '30'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('180', result.stdout)

    def test_conflict_leaves_existing_files_and_no_partial_selection(self):
        with tempfile.TemporaryDirectory() as tmp:
            existing = Path(tmp) / '.claude' / 'skills' / 'ui-motion-design'
            existing.mkdir(parents=True)
            sentinel = existing / 'local.txt'
            sentinel.write_text('keep')
            with self.assertRaises(FileExistsError):
                self.call(tmp, ['motion-storyboard', 'ui-motion-design'])
            self.assertEqual(sentinel.read_text(), 'keep')
            self.assertFalse((existing.parent / 'motion-storyboard').exists())

    def test_dry_run_and_unknown_selection_write_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.call(tmp, dry_run=True)
            with self.assertRaises(ValueError):
                self.call(tmp, ['../escape'])
            self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_selection_installs_only_requested_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.call(tmp, ['kinetic-typography'])
            self.assertEqual([p.name for p in (Path(tmp) / '.claude' / 'skills').iterdir()], ['kinetic-typography'])


if __name__ == '__main__':
    unittest.main()
