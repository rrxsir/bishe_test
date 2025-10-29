from __future__ import annotations

import json
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List

import yaml

from .schemas import DataItem

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
CONFIG_DIR = Path(__file__).resolve().parents[2] / "config"


class DataSource(ABC):
    """Abstract base class for every data source."""

    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def load(self) -> Iterable[DataItem]:
        """Collect data from the source and yield :class:`DataItem` instances."""


class WebDataSource(DataSource):
    """Simulates pulling data from online endpoints defined in a configuration file."""

    def __init__(self) -> None:
        super().__init__("web")
        self._samples_path = CONFIG_DIR / "web_sources.json"

    def load(self) -> Iterable[DataItem]:
        if not self._samples_path.exists():
            return []

        with self._samples_path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)

        items: List[DataItem] = []
        for record in payload.get("signals", []):
            items.append(
                DataItem(
                    id=record["id"],
                    title=record["title"],
                    category=record["category"],
                    source="web",
                    timestamp=_parse_timestamp(record.get("timestamp")),
                    summary=record["summary"],
                    impact=record.get("impact", ""),
                    relations=record.get("relations", []),
                )
            )
        return items


class LocalFileDataSource(DataSource):
    def __init__(self) -> None:
        super().__init__("local")
        self._file = DATA_DIR / "local_insights.json"

    def load(self) -> Iterable[DataItem]:
        if not self._file.exists():
            return []
        with self._file.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)

        items: List[DataItem] = []
        for record in payload:
            items.append(
                DataItem(
                    id=record["id"],
                    title=record["title"],
                    category=record["category"],
                    source=record.get("source", "local"),
                    timestamp=_parse_timestamp(record.get("timestamp")),
                    summary=record["summary"],
                    impact=record.get("impact", ""),
                    relations=record.get("relations", []),
                )
            )
        return items


class ConfigDataSource(DataSource):
    def __init__(self) -> None:
        super().__init__("config")
        self._file = CONFIG_DIR / "custom_sources.yaml"

    def load(self) -> Iterable[DataItem]:
        if not self._file.exists():
            return []
        with self._file.open("r", encoding="utf-8") as handle:
            payload: Dict[str, List[Dict[str, str]]] = yaml.safe_load(handle) or {}

        items: List[DataItem] = []
        for record in payload.get("entries", []):
            items.append(
                DataItem(
                    id=record["id"],
                    title=record["title"],
                    category=record["category"],
                    source=record.get("source", "config"),
                    timestamp=_parse_timestamp(record.get("timestamp")),
                    summary=record["summary"],
                    impact=record.get("impact", ""),
                    relations=record.get("relations", []),
                )
            )
        return items


def _parse_timestamp(value: str | None) -> datetime:
    if not value:
        return datetime.utcnow()
    return datetime.fromisoformat(value)
