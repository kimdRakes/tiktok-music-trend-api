from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, Mapping, Any

def write_jsonl(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    """
    Writes an iterable of dict-like rows to JSONL with UTF-8 encoding.
    Creates directories as needed.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")