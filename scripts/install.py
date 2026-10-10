#!/usr/bin/env python3
"""Install selected Claude Code skills into an explicit project or user directory."""
import argparse
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]


def install(base, names=None, dry_run=False):
    base = Path(base).expanduser().resolve()
    if not base.is_dir():
        raise ValueError(f'Not an existing directory: {base}')
    available = {p.name: p for p in (ROOT / 'skills').iterdir() if (p / 'SKILL.md').is_file()}
    selected = sorted(available) if names is None else list(dict.fromkeys(names))
    if not selected:
        raise ValueError('Select at least one skill.')
    unknown = set(selected) - available.keys()
    if unknown:
        raise ValueError('Unknown skills: ' + ', '.join(sorted(unknown)))
    target = base / '.claude' / 'skills'
    for name in selected:
        dest = target / name
        if dest.exists() or dest.is_symlink():
            raise FileExistsError(f'Refusing to overwrite {dest}; inspect and move it first.')
        source = available[name].resolve()
        if target == source or source in target.parents:
            raise ValueError('Destination cannot be inside a source skill.')
    if dry_run:
        for name in selected:
            print(f'Would install {name} -> {target / name}')
        return
    target.mkdir(parents=True, exist_ok=True)
    for name in selected:
        try:
            shutil.copytree(available[name], target / name, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '*.pyo'))
        except OSError as error:
            raise OSError(f'Copy failed at {target / name}: {error}. Inspect any partial folder before retrying.') from error
        print(f'Installed {name} -> {target / name}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument('--project', type=Path, help='Existing project directory')
    scope.add_argument('--user', action='store_true', help='Install for the current user')
    parser.add_argument('--skill', action='append', help='Skill name; repeat to select several. Default: all.')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        install(Path.home() if args.user else args.project, args.skill, args.dry_run)
    except (ValueError, OSError) as error:
        print(f'Error: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
