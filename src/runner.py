import argparse
import json
import os
import sys
from pathlib import Path
from datetime import datetime, timezone

# Ensure local module imports without needing __init__.py packages
BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "client"))
sys.path.append(str(BASE_DIR / "extractors"))
sys.path.append(str(BASE_DIR / "outputs"))

from tiktok_music_api import TikTokMusicAPI  # type: ignore
from normalize import normalize_item, TikTokMusicItem  # type: ignore
from dataset_writer import write_jsonl  # type: ignore
from exporters import write_csv  # type: ignore

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="TikTok Music Trend API Scraper (mock-friendly, production-ready scaffolding)."
    )
    p.add_argument("--region", type=str, help="Two-letter region code, e.g. US", default=None)
    p.add_argument("--limit", type=int, help="Max items to fetch", default=None)
    p.add_argument(
        "--input",
        type=str,
        help="Optional input JSON file (expects keys: region, limit). CLI flags override these keys.",
        default=None,
    )
    p.add_argument("--out", type=str, help="Output JSONL file path", default=str(PROJECT_DIR / "data" / "out.jsonl"))
    p.add_argument("--csv", type=str, help="Optional CSV path to also export flattened rows", default=None)
    p.add_argument("--mock", type=str, help="Mock mode (true/false). Defaults to env MOCK or true if no endpoint provided.", default=None)
    p.add_argument("--endpoint", type=str, help="Optional HTTP endpoint override for live runs", default=None)
    return p.parse_args()

def load_inputs_file(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input file not found: {p}")
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)

def coalesce_bool(value: str | None, default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y"}

def main() -> None:
    args = parse_args()

    file_inputs = {}
    if args.input:
        file_inputs = load_inputs_file(args.input)

    region = (args.region or file_inputs.get("region") or os.getenv("REGION") or "US").upper()
    limit = int(args.limit or file_inputs.get("limit") or os.getenv("LIMIT") or 50)

    endpoint = args.endpoint or os.getenv("TTMUSIC_ENDPOINT")
    # Default to mock when no live endpoint set
    mock_default = endpoint is None
    mock = coalesce_bool(args.mock, coalesce_bool(os.getenv("MOCK"), mock_default))

    api = TikTokMusicAPI(endpoint=endpoint, mock=mock, project_dir=str(PROJECT_DIR))

    print(f"[{datetime.now(timezone.utc).isoformat()}] Starting run | region={region} limit={limit} mock={mock}")

    raw_items = api.fetch_trending_music(region=region, limit=limit)
    print(f"[info] Retrieved {len(raw_items)} raw item(s)")

    normalized: list[dict] = []
    iso_now = datetime.now(timezone.utc).isoformat()

    for raw in raw_items:
        try:
            model: TikTokMusicItem = normalize_item(raw, region=region, scraped_at=iso_now)
            normalized.append(model.model_dump())
        except Exception as e:
            # Keep going; log and skip bad items
            print(f"[warn] Failed to normalize item: {e!r}")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    write_jsonl(out_path, normalized)
    print(f"[ok] Wrote JSONL: {out_path} ({len(normalized)} item(s))")

    if args.csv:
        csv_path = Path(args.csv)
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        write_csv(csv_path, normalized)
        print(f"[ok] Wrote CSV: {csv_path} ({len(normalized)} row(s))")

    print(f"[done] Completed successfully.")

if __name__ == "__main__":
    main()