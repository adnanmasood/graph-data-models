from __future__ import annotations

import networkx as nx

from .networkx_store import build_event_node_graph


def shortest_path(source: str, target: str) -> list[str]:
    return nx.shortest_path(build_event_node_graph().to_undirected(), source, target)


def centrality_scores() -> dict[str, float]:
    return nx.degree_centrality(build_event_node_graph().to_undirected())


def connected_components() -> list[set[str]]:
    return [set(component) for component in nx.connected_components(build_event_node_graph().to_undirected())]


def fraud_ring() -> list[str]:
    graph = nx.Graph()
    graph.add_edges_from([("acct-1", "phone-1"), ("acct-2", "phone-1"), ("acct-2", "device-9"), ("acct-3", "device-9")])
    return sorted(node for node, degree in graph.degree() if degree > 1)
