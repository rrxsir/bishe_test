from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class DataItem(BaseModel):
    """Representation of a normalized intelligence record."""

    id: str = Field(..., description="Unique identifier for the record")
    title: str = Field(..., description="Short name of the event or project")
    category: str = Field(..., description="High level category such as trend, project or ecosystem")
    source: str = Field(..., description="Data source that produced the record")
    timestamp: datetime = Field(..., description="When the information was collected")
    summary: str = Field(..., description="Key facts extracted from the source")
    impact: str = Field(..., description="Estimated impact description")
    relations: List[str] = Field(default_factory=list, description="Identifiers related to this record")


class DataRefreshRequest(BaseModel):
    sources: Optional[List[str]] = Field(
        default=None,
        description="Subset of sources to refresh. Defaults to all available sources.",
    )


class DataCollectionResponse(BaseModel):
    updated_at: datetime
    items: List[DataItem]


class GraphNode(BaseModel):
    id: str
    label: str
    category: str


class GraphEdge(BaseModel):
    source: str
    target: str
    weight: float = 1.0
    relation: Optional[str] = None


class GraphResponse(BaseModel):
    generated_at: datetime
    nodes: List[GraphNode]
    edges: List[GraphEdge]


class InsightGroup(BaseModel):
    title: str
    insights: List[str]


class ReportResponse(BaseModel):
    generated_at: datetime
    highlights: List[str]
    sections: List[InsightGroup]
