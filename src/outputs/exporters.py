from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Dict, Iterable

def _flatten_for_csv(record: Dict[str, Any]) -> Dict[str, Any]:
    """
    Keep top-level primitives; stringify nested dicts/lists to preserve structure in CSV.
    """
    out: Dict[str, Any] = {}
    for k, v in record.items():
        if isinstance(v, (str, int, float)) or v is None:
            out[k] = v
        else:
            out[k] = json.dumps(v, ensure_ascii=False)
    return out

def write_csv(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    rows = list(rows)
    if not rows:
        # Create empty file with header row for consistency
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([])
        return

    flattened = [_flatten_for_csv(r) for r in rows]
    # Union of keys across all rows
    header = sorted({k for r in flattened for k in r.keys()})
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        writer.writeheader()
        for r in flattened:
            writer.writerow(r)