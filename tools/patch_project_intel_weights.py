from __future__ import annotations

from pathlib import Path
import re
import sys

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/root/novak-sdt/src/novak_sdt/project_intel.py')
text = path.read_text(encoding='utf-8')
original = text

if 'APPLICATION_CODE_HINTS' not in text:
    insertion = '''\n\nAPPLICATION_CODE_HINTS = (\n    "app",\n    "src",\n    "tests",\n)\n\nIGNORED_WEIGHT_DIRS = {\n    ".venv",\n    "node_modules",\n    "site",\n    "build",\n    "dist",\n    "__pycache__",\n}\n\n'''
    text = text.replace('from pathlib import Path\n', 'from pathlib import Path\n' + insertion, 1)

marker = 'primary_language'
if marker not in text:
    raise SystemExit('FAILED: project_intel.py does not look like expected file')

if 'Weight runtime/language inference toward application code' not in text:
    helper = '''\n\ndef _sdt_truth_closure_weight_path(path_text: str, default_weight: int) -> int:\n    normalized = path_text.replace('\\\\', '/').lower()\n    if any(part in normalized.split('/') for part in IGNORED_WEIGHT_DIRS):\n        return 0\n    if any(f'/{hint}/' in f'/{normalized}/' for hint in APPLICATION_CODE_HINTS):\n        return default_weight * 5\n    return default_weight\n\n'''
    text = text + helper

path.write_text(text, encoding='utf-8')
print(f'PATCHED {path}')
