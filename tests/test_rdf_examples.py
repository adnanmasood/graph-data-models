from rdflib import URIRef

from graph_model_examples.rdf_examples.build import build_named_graph_dataset, build_nary_graph, build_plain_lossy_graph, build_reification_graph
from graph_model_examples.rdf_examples.query import ceo_in_2021, confidence_below, facts_valid_on, facts_verified_by, source_for_claim


def test_rdf_graphs_and_queries():
    graph = build_nary_graph()
    assert (URIRef("http://example.org/kg/claim-alice-acme-ceo"), None, None) in graph
    assert len(build_plain_lossy_graph()) < len(graph)
    assert len(build_named_graph_dataset()) > 0
    assert len(build_reification_graph()) > 0
    assert ceo_in_2021() == ["Alice"]
    assert source_for_claim() == "Acme 2020 Annual Report"
    assert facts_verified_by() == ["claim-alice-acme-ceo"]
    assert confidence_below(0.95) == [("claim-alice-acme-ceo", 0.93)]
    assert facts_valid_on("2024-01-01") == []
