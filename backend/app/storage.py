from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Iterable, List

from .schemas import DataItem

BASE_DIR = Path(__file__).resolve().parents[2]
CACHE_FILE = BASE_DIR / "data" / "cache.json"


def load_cached_items() -> List[DataItem]:
    if not CACHE_FILE.exists():
        return []
    with CACHE_FILE.open("r", encoding="utf-8") as handle:
        raw_items = json.load(handle)
    return [DataItem(**item) for item in raw_items]


def save_items(items: Iterable[DataItem]) -> None:
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    payload = [item.model_dump() for item in items]
    with CACHE_FILE.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, default=_json_default)


def _json_default(value):
    if isinstance(value, datetime):
        return value.isoformat()
    raise TypeError(f"Object of type {type(value)!r} is not JSON serializable")
