from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from http_client import HttpClient

class TikTokMusicAPI:
    """
    Minimal facade to fetch trending music.

    - Live mode: if `endpoint` is provided, GET {endpoint}?region=US&limit=50 expecting JSON array response.
    - Mock mode: reads from data/sample_output.json and slices by limit.
    """

    def __init__(self, endpoint: Optional[str], mock: bool, project_dir: str) -> None:
        self.endpoint = endpoint
        self.mock = mock
        self.project_dir = Path(project_dir)
        self.http = HttpClient()

    def fetch_trending_music(self, region: str, limit: int = 50) -> List[Dict[str, Any]]:
        if self.mock:
            sample_path = self.project_dir / "data" / "sample_output.json"
            if not sample_path.exists():
                raise FileNotFoundError(f"Mock file missing: {sample_path}")
            with sample_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            # ensure list
            if isinstance(data, dict):
                data = [data]
            return data[: max(0, int(limit))]
        # Live HTTP call to custom endpoint (user-provided)
        if not self.endpoint:
            # Safety fallback to mock if endpoint missing
            return self._fallback_mock(region, limit)

        params = {"region": region, "limit": int(limit)}
        res = self.http.get(self.endpoint, params=params)
        if res.status_code >= 400:
            # Fall back to mock to keep runs robust
            print(f"[warn] Live endpoint returned {res.status_code}; falling back to mock data.")
            return self._fallback_mock(region, limit)
        try:
            payload = res.json()
        except Exception as e:
            print(f"[warn] Failed to parse live JSON ({e!r}); falling back to mock.")
            return self._fallback_mock(region, limit)

        if not isinstance(payload, list):
            print("[warn] Live payload is not a list; falling back to mock.")
            return self._fallback_mock(region, limit)

        return payload[: max(0, int(limit))]

    def _fallback_mock(self, region: str, limit: int) -> List[Dict[str, Any]]:
        # Allow override via env var for tests
        path = os.getenv("MOCK_PATH") or str(self.project_dir / "data" / "sample_output.json")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            data = [data]
        return data[: max(0, int(limit))]