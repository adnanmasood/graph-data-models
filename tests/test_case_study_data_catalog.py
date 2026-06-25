from graph_model_examples.case_studies.data_catalog import demo

def test_case_data_catalog():
    output = demo()
    assert "finance-dashboard" in output
    assert "source columns" in output
