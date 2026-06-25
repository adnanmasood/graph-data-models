from graph_model_examples.hyperrel.export_rdf import export_statements_to_rdf
from graph_model_examples.hyperrel.queries import claims_verified_by, conflicting_claims, preferred_statement, qualifiers_for_statement, sources_for_statement


def test_hyperrel_queries():
    statement = preferred_statement()
    assert statement.subject == "alice"
    assert statement.confidence == 0.93
    assert sources_for_statement(statement.id) == ["acme-2020-annual-report"]
    assert qualifiers_for_statement(statement.id)["location"] == "new-york"
    assert claims_verified_by() == ["S1"]
    assert conflicting_claims() == ["S2"]
    assert len(export_statements_to_rdf()) > 0
