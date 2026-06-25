from graph_model_examples.decision_framework.models import Requirements
from graph_model_examples.decision_framework.recommender import recommend_models


def _top(requirements):
    return recommend_models(requirements)[:3]


def test_decision_framework_rankings():
    assert any("RDF" in rec.model for rec in _top(Requirements(needs_semantic_interoperability=True)))
    assert any("LPG" in rec.model or "Hybrid" in rec.model for rec in _top(Requirements(needs_fast_traversal=True)))
    assert any("Hyper-relational" in rec.model or "RDF-star" in rec.model or "Hybrid" in rec.model for rec in _top(Requirements(needs_statement_metadata=True)))
    assert any("Hypergraph" in rec.model or "Hybrid" in rec.model for rec in _top(Requirements(needs_nary_relationships=True)))
    assert any("Datalog" in rec.model or "Hybrid" in rec.model for rec in _top(Requirements(needs_recursive_rules=True)))
    assert recommend_models(Requirements(needs_graph_rag=True, needs_statement_metadata=True, needs_fast_traversal=True))[0].model.startswith("Hybrid")
