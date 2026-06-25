from graph_model_examples.hypergraph.queries import employment_edges, participants, supply_chain_transactions, verification_edges


def test_hypergraph_nary_relationships():
    assert employment_edges() == ["H1"]
    assert participants("H1")["employee"] == "alice"
    assert verification_edges() == ["H2"]
    assert supply_chain_transactions() == ["H3"]
