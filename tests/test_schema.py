import json
import sys
from pathlib import Path
from datetime import datetime, timezone

# Add src paths for imports
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.append(str(SRC))
sys.path.append(str(SRC / "extractors"))

from normalize import normalize_item, TikTokMusicItem  # type: ignore

def test_normalization_model_loads_sample():
    sample_path = ROOT / "data" / "sample_output.json"
    with sample_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, list) and len(data) >= 1

    iso_now = datetime.now(timezone.utc).isoformat()
    first = data[0]
    model: TikTokMusicItem = normalize_item(first, region="US", scraped_at=iso_now)
    dumped = model.model_dump()

    # Basic expectations
    assert dumped["region"] == "US"
    assert "id" in dumped and isinstance(dumped["id"], int)
    assert "id_str" in dumped and isinstance(dumped["id_str"], str)
    # Optional fields exist or are None
    assert "title" in dumped
    assert "author" in dumped
    # Covers are nested objects or None
    assert "cover_thumb" in dumped
    assert "cover_medium" in dumped
    assert "cover_large" in dumped