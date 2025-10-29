from __future__ import annotations

from datetime import datetime
from typing import Iterable, List

import networkx as nx

from .schemas import DataItem, GraphEdge, GraphNode, GraphResponse


def build_causal_graph(items: Iterable[DataItem]) -> GraphResponse:
    graph = nx.DiGraph()

    for item in items:
        graph.add_node(
            item.id,
            label=item.title,
            category=item.category,
        )

    for item in items:
        for related_id in item.relations:
            if related_id in graph:
                weight = graph[item.id].get(related_id, {}).get("weight", 0) + 1
                graph.add_edge(item.id, related_id, weight=weight, relation="influences")

    nodes: List[GraphNode] = []
    for node_id, data in graph.nodes(data=True):
        nodes.append(
            GraphNode(
                id=node_id,
                label=data.get("label", node_id),
                category=data.get("category", "unknown"),
            )
        )

    edges: List[GraphEdge] = []
    for source, target, data in graph.edges(data=True):
        edges.append(
            GraphEdge(
                source=source,
                target=target,
                weight=float(data.get("weight", 1.0)),
                relation=data.get("relation"),
            )
        )

    return GraphResponse(
        generated_at=datetime.utcnow(),
        nodes=nodes,
        edges=edges,
    )
