from __future__ import annotations

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, AwareDatetime, field_validator

class Cover(BaseModel):
    height: Optional[int] = None
    width: Optional[int] = None
    uri: Optional[str] = None
    url_list: list[str] = Field(default_factory=list)
    url_prefix: Optional[str] = None

class MediaUrl(BaseModel):
    height: Optional[int] = None
    width: Optional[int] = None
    uri: Optional[str] = None
    url_list: list[str] = Field(default_factory=list)
    url_prefix: Optional[str] = None

class TikTokMusicItem(BaseModel):
    id: int
    id_str: str
    title: Optional[str] = None
    author: Optional[str] = None
    duration: Optional[int] = None
    user_count: Optional[int] = None
    status: Optional[int] = None
    is_original: Optional[bool] = None
    cover_thumb: Optional[Cover] = None
    cover_medium: Optional[Cover] = None
    cover_large: Optional[Cover] = None
    play_url: Optional[MediaUrl] = None
    external_song_info: Optional[dict] = None
    tt_to_dsp_song_infos: Optional[dict] = None
    extra: Optional[str] = None
    region: str
    scraped_at: AwareDatetime

    @field_validator("region")
    @classmethod
    def region_upper(cls, v: str) -> str:
        return (v or "").upper()

    @field_validator("id_str", mode="before")
    @classmethod
    def coerce_id_str(cls, v: Any) -> str:
        return str(v)

    @field_validator("id", mode="before")
    @classmethod
    def coerce_id(cls, v: Any) -> int:
        try:
            return int(v)
        except Exception:
            return 0

def pick_first_url(urls: list[str] | None) -> list[str]:
    if not urls:
        return []
    return [u for u in urls if isinstance(u, str)]

def _cover_from_raw(raw: dict | None) -> Optional[Cover]:
    if not isinstance(raw, dict):
        return None
    return Cover(
        height=raw.get("height"),
        width=raw.get("width"),
        uri=raw.get("uri"),
        url_list=pick_first_url(raw.get("url_list")),
        url_prefix=raw.get("url_prefix"),
    )

def _media_from_raw(raw: dict | None) -> Optional[MediaUrl]:
    if not isinstance(raw, dict):
        return None
    return MediaUrl(
        height=raw.get("height"),
        width=raw.get("width"),
        uri=raw.get("uri"),
        url_list=pick_first_url(raw.get("url_list")),
        url_prefix=raw.get("url_prefix"),
    )

def normalize_item(raw: Dict[str, Any], region: str, scraped_at: str) -> TikTokMusicItem:
    """
    Convert a raw TikTok music object into our normalized schema.
    Expects keys similar to the sample JSON provided in the README.
    """

    # Many fields may be optional/missing; keep this robust.
    id_val = raw.get("id") or raw.get("mid") or raw.get("id_str") or 0
    item = TikTokMusicItem(
        id=id_val,
        id_str=str(raw.get("id_str") or raw.get("id") or id_val),
        title=raw.get("title"),
        author=raw.get("author"),
        duration=raw.get("duration"),
        user_count=raw.get("user_count"),
        status=raw.get("status"),
        is_original=raw.get("is_original"),
        cover_thumb=_cover_from_raw(raw.get("cover_thumb")),
        cover_medium=_cover_from_raw(raw.get("cover_medium")),
        cover_large=_cover_from_raw(raw.get("cover_large")),
        play_url=_media_from_raw(raw.get("play_url")),
        external_song_info=raw.get("external_song_info"),
        tt_to_dsp_song_infos=raw.get("tt_to_dsp_song_infos"),
        extra=raw.get("extra"),
        region=region,
        scraped_at=scraped_at,
    )
    return item