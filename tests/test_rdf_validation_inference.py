from graph_model_examples.rdf_examples.inference import has_inferred_claim_type
from graph_model_examples.rdf_examples.validate import validate_instance


def test_shacl_validation_and_inference():
    assert validate_instance("valid_instance.ttl")[0]
    assert not validate_instance("invalid_missing_source.ttl")[0]
    assert not validate_instance("invalid_bad_confidence.ttl")[0]
    assert has_inferred_claim_type()
