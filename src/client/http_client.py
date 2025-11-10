from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests
from requests.adapters import HTTPAdapter, Retry

@dataclass
class HttpResponse:
    status_code: int
    headers: Dict[str, str]
    text: str

    def json(self) -> Any:
        return json.loads(self.text)

class HttpClient:
    """
    Thin wrapper over requests with retries and sane defaults.
    """

    def __init__(
        self,
        timeout: float = 20.0,
        user_agent: Optional[str] = None,
        total_retries: int = 3,
        backoff_factor: float = 0.3,
    ) -> None:
        self.timeout = timeout
        self.session = requests.Session()
        retries = Retry(
            total=total_retries,
            backoff_factor=backoff_factor,
            status_forcelist=(429, 500, 502, 503, 504),
            allowed_methods=("GET", "POST"),
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retries, pool_connections=10, pool_maxsize=20)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        self.session.headers.update(
            {
                "Accept": "application/json, */*;q=0.8",
                "User-Agent": user_agent
                or "Mozilla/5.0 (compatible; Bitbash-TikTokMusicScraper/1.0; +https://bitbash.dev)",
            }
        )

    def get(self, url: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> HttpResponse:
        res = self.session.get(url, params=params, headers=headers, timeout=self.timeout)
        return HttpResponse(status_code=res.status_code, headers=dict(res.headers), text=res.text)

    def post(self, url: str, json_data: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> HttpResponse:
        res = self.session.post(url, json=json_data, headers=headers, timeout=self.timeout)
        return HttpResponse(status_code=res.status_code, headers=dict(res.headers), text=res.text)