from graph_model_examples.lpg.analytics import connected_components, fraud_ring, shortest_path
from graph_model_examples.lpg.networkx_store import build_edge_property_graph, build_event_node_graph
from graph_model_examples.lpg.queries import ceo_in_year, facts_verified_by, low_confidence


def test_lpg_queries_and_analytics():
    assert build_edge_property_graph().number_of_edges() == 1
    assert build_event_node_graph().has_node("claim-alice-acme-ceo")
    assert ceo_in_year(2021) == ["Alice"]
    assert ceo_in_year(2024) == []
    assert facts_verified_by() == ["claim-alice-acme-ceo"]
    assert low_confidence() == ["claim-alice-acme-ceo"]
    assert shortest_path("alice", "acme-2020-annual-report") == ["alice", "claim-alice-acme-ceo", "acme-2020-annual-report"]
    assert connected_components()
    assert fraud_ring() == ["acct-2", "device-9", "phone-1"]
