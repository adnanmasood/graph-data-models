from rdflib import URIRef

from graph_model_examples.rdf_star.lower_to_nary import lower_statement_to_nary, lowered_summary


def test_rdf_star_lowering_preserves_metadata():
    graph = lower_statement_to_nary()
    claim = URIRef("http://example.org/kg/claim-alice-acme-ceo")
    assert (claim, URIRef("http://example.org/kg/source"), URIRef("http://example.org/kg/acme-2020-annual-report")) in graph
    assert lowered_summary()["confidence"] == 0.93
