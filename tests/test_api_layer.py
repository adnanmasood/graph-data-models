from graph_model_examples.api_layer.resolvers import resolve_employment_claim, resolve_facts_verified_by, resolve_provenance


def test_api_layer_resolvers():
    claim = resolve_employment_claim()
    provenance = resolve_provenance()
    assert claim["id"] == "claim-alice-acme-ceo"
    assert provenance["source"] == "acme-2020-annual-report"
    assert provenance["confidence"] == 0.93
    assert resolve_facts_verified_by("bob") == ["claim-alice-acme-ceo"]
