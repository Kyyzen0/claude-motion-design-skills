#!/usr/bin/env python3
"""Validate this pack's restricted YAML frontmatter, resource links, and Python syntax."""
import ast
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    failures = []
    paths = sorted((root / 'skills').glob('*/SKILL.md'))
    if not paths:
        return ['No skills found.']
    for path in paths:
        try:
            content = path.read_text(encoding='utf-8')
            match = re.fullmatch(r'---\n(.*?)\n---\n\n(.+)', content, re.S)
            if not match:
                raise ValueError('Missing frontmatter or instructions.')
            fields = {}
            for line in match[1].splitlines():
                key, value = line.split(': ', 1)
                if key in fields:
                    raise ValueError(f'Duplicate field: {key}')
                fields[key] = value if key == 'name' else json.loads(value)
            if set(fields) != {'name', 'description'}:
                raise ValueError('Expected name and description only.')
            name = fields['name']
            if name != path.parent.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
                raise ValueError('Invalid name or folder mismatch.')
            desc = fields['description']
            if not isinstance(desc, str) or not 1 <= len(desc) <= 1024 or '<' in desc or '>' in desc:
                raise ValueError('Invalid description.')
            if '[TODO:' in content:
                raise ValueError('Unfinished scaffold.')
        except (ValueError, OSError, TypeError) as error:
            failures.append(f'{path.relative_to(root)}: {error}')
    for path in root.rglob('*.md'):
        if '.git' in path.parts:
            continue
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if '://' in target or target.startswith('#'):
                continue
            resolved = (path.parent / target.split('#')[0]).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                failures.append(f'{path.relative_to(root)}: invalid local link {target}')
    for path in root.rglob('*.py'):
        if '.git' not in path.parts:
            try:
                ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
            except (SyntaxError, OSError) as error:
                failures.append(f'{path.relative_to(root)}: {error}')
    return failures


if __name__ == '__main__':
    errors = validate()
    for error in errors:
        print(error, file=sys.stderr)
    if not errors:
        print(f'Validated {len(list((ROOT / "skills").glob("*/SKILL.md")))} skills and their resources.')
    sys.exit(bool(errors))
