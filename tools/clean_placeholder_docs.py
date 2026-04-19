from __future__ import annotations

from pathlib import Path
import re
import sys

repo = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
targets = [
    repo / 'docs' / 'INSTALLATION.md',
    repo / 'PROJECT_STATE.md',
    repo / 'WHAT_IS_REAL_NOW.md',
]

placeholder_patterns = [
    re.compile(r'<[^>\n]+>'),
    re.compile(r'fill me in', re.IGNORECASE),
    re.compile(r'tbd', re.IGNORECASE),
]

for path in targets:
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    updated = text
    for pattern in placeholder_patterns:
        updated = pattern.sub('UNVERIFIED - operator confirmation required', updated)
    if updated != text:
        path.write_text(updated, encoding='utf-8')
        print(f'UPDATED {path}')
