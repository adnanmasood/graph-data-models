from graph_model_examples.case_studies.biomedical import demo as biomedical_demo
from graph_model_examples.case_studies.supply_chain import demo as supply_chain_demo

def test_biomedical_and_supply_chain():
    assert "compound-a" in biomedical_demo()
    assert "weather-delay" in supply_chain_demo()
