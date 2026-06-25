from __future__ import annotations

from datetime import date

from graph_model_examples.common.fixtures import canonical_names
from graph_model_examples.common.printing import simple_table

from .analytics import centrality_scores, shortest_path
from .networkx_store import build_edge_property_graph, build_event_node_graph


def _contains(edge_data: dict, year: int) -> bool:
    value = date(year, 6, 15)
    return date.fromisoformat(edge_data["start_date"]) <= value <= date.fromisoformat(edge_data["end_date"])


def ceo_in_year(year: int) -> list[str]:
    names = canonical_names()
    graph = build_edge_property_graph()
    result = []
    for source, target, data in graph.edges(data=True):
        if data.get("label") == "CEO_OF" and target == "acme" and _contains(data, year):
            result.append(names[source])
    return result


def facts_verified_by(verifier_id: str = "bob") -> list[str]:
    graph = build_edge_property_graph()
    return [key for _, _, key, data in graph.edges(keys=True, data=True) if data.get("verified_by") == verifier_id]


def low_confidence(threshold: float = 0.95) -> list[str]:
    graph = build_edge_property_graph()
    return [key for _, _, key, data in graph.edges(keys=True, data=True) if data.get("confidence", 1) < threshold]


def demo() -> str:
    edge_graph = build_edge_property_graph()
    event_graph = build_event_node_graph()
    rows = [
        ["edge-property model", f"nodes={edge_graph.number_of_nodes()} edges={edge_graph.number_of_edges()}", "compact edge metadata"],
        ["event-node model", f"nodes={event_graph.number_of_nodes()} edges={event_graph.number_of_edges()}", "provenance is traversable"],
        ["CEO in 2021", ", ".join(ceo_in_year(2021)), "Alice"],
        ["verified by Bob", ", ".join(facts_verified_by()), "claim id"],
        ["confidence below 0.95", ", ".join(low_confidence()), "0.93"],
        ["shortest path", " -> ".join(shortest_path("alice", "acme-2020-annual-report")), "via claim node"],
        ["centrality", str(round(centrality_scores()["claim-alice-acme-ceo"], 3)), "claim node is connective"],
    ]
    return simple_table(["LPG example", "value", "note"], rows)
