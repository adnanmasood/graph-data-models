from graph_model_examples.common.answers import canonical_expected_answers
from graph_model_examples.common.fixtures import is_valid_on, load_canonical_claim, load_competency_questions, load_entities
from graph_model_examples.common.ids import iri_for, safe_curie


def test_json_fixtures_load_and_dates():
    entities = load_entities()
    claim = load_canonical_claim()
    assert entities["alice"].name == "Alice"
    assert is_valid_on(claim, "2021-06-15")
    assert not is_valid_on(claim, "2024-01-01")
    assert claim.confidence == 0.93
    assert claim.references[0].document_id == "acme-2020-annual-report"
    assert claim.verification.verifier_id == "bob"


def test_ids_and_answers_are_deterministic():
    assert iri_for("new-york") == "http://example.org/kg/new_york"
    assert safe_curie("claim-alice-acme-ceo") == "claim_alice_acme_ceo"
    assert len(load_competency_questions()) == 10
    assert canonical_expected_answers()["cq1"] == "Alice"
