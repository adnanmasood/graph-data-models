from graph_model_examples.query_languages.catalog import CATALOG, classify


def test_query_languages_are_not_data_models():
    assert len(CATALOG) == 5
    assert classify("GraphQL")["kind"] == "API query language"
    assert all(entry["data_model"] is False for entry in CATALOG)
