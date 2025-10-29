from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from typing import Dict, Iterable, List

from .schemas import DataItem, InsightGroup, ReportResponse


CATEGORY_ALIASES = {
    "trend": ["trend", "technology", "monitor"],
    "project": ["project", "repository", "library"],
    "ecosystem": ["ecosystem", "community", "organization"],
}


def run_multi_agent_analysis(items: Iterable[DataItem]) -> ReportResponse:
    grouped: Dict[str, List[DataItem]] = defaultdict(list)
    for item in items:
        key = _normalize_category(item.category)
        grouped[key].append(item)

    sections: List[InsightGroup] = []
    highlights: List[str] = []

    for category, records in grouped.items():
        if not records:
            continue
        insights = _build_insights(category, records)
        sections.append(InsightGroup(title=category.title(), insights=insights))
        highlights.extend(insights[:2])

    highlights = highlights[:5]

    return ReportResponse(
        generated_at=datetime.utcnow(),
        highlights=highlights,
        sections=sections,
    )


def _normalize_category(category: str) -> str:
    category_lower = category.lower()
    for canonical, aliases in CATEGORY_ALIASES.items():
        if category_lower in aliases:
            return canonical
    return category_lower


def _build_insights(category: str, records: List[DataItem]) -> List[str]:
    sorted_records = sorted(records, key=lambda item: item.timestamp, reverse=True)
    insights: List[str] = []

    if category == "trend":
        insights.append(
            f"Top emerging trend: {sorted_records[0].title} — {sorted_records[0].summary}"
        )
        if len(sorted_records) > 1:
            insights.append(
                f"Momentum shift detected in {sorted_records[1].title} impacting {', '.join(sorted_records[1].relations) or 'multiple domains'}."
            )
    elif category == "project":
        active_projects = [record for record in sorted_records if record.relations]
        if active_projects:
            project = active_projects[0]
            insights.append(
                f"Project {project.title} shows strong activity with links to {', '.join(project.relations)}."
            )
        insights.append(f"Latest repository update: {sorted_records[0].title} — {sorted_records[0].impact}")
    elif category == "ecosystem":
        ecosystem_summary = ", ".join(record.title for record in sorted_records[:3])
        insights.append(f"Ecosystem actors involved: {ecosystem_summary}")
        insights.append(
            f"Collaboration density increased via {len(sorted_records[0].relations)} new relationships."
        )
    else:
        for record in sorted_records[:3]:
            insights.append(f"{record.title}: {record.summary}")

    return insights
