from __future__ import annotations

from datetime import datetime
from typing import Iterable, List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .analysis import run_multi_agent_analysis
from .data_sources import ConfigDataSource, DataSource, LocalFileDataSource, WebDataSource
from .graph_builder import build_causal_graph
from .schemas import (
    DataCollectionResponse,
    DataItem,
    DataRefreshRequest,
    GraphResponse,
    ReportResponse,
)
from .storage import load_cached_items, save_items

app = FastAPI(title="Causal Intelligence Platform", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_sources() -> List[DataSource]:
    return [WebDataSource(), LocalFileDataSource(), ConfigDataSource()]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}


@app.get("/api/data", response_model=DataCollectionResponse)
def get_data() -> DataCollectionResponse:
    items = load_cached_items()
    return DataCollectionResponse(updated_at=datetime.utcnow(), items=items)


@app.post("/api/data/refresh", response_model=DataCollectionResponse)
def refresh_data(
    payload: DataRefreshRequest,
    sources: Iterable[DataSource] = Depends(get_sources),
) -> DataCollectionResponse:
    requested_sources = set(payload.sources or [source.name for source in sources])

    collected: List[DataItem] = []
    for source in sources:
        if source.name not in requested_sources:
            continue
        collected.extend(source.load())

    if not collected:
        raise HTTPException(status_code=404, detail="No data collected from selected sources")

    save_items(collected)
    return DataCollectionResponse(updated_at=datetime.utcnow(), items=collected)


@app.get("/api/graph", response_model=GraphResponse)
def get_graph() -> GraphResponse:
    items = load_cached_items()
    if not items:
        raise HTTPException(status_code=404, detail="No cached data available to build graph")
    return build_causal_graph(items)


@app.get("/api/report", response_model=ReportResponse)
def get_report() -> ReportResponse:
    items = load_cached_items()
    if not items:
        raise HTTPException(status_code=404, detail="No cached data available for analysis")
    return run_multi_agent_analysis(items)
