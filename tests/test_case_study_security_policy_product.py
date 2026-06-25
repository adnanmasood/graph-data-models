from graph_model_examples.case_studies.cybersecurity import demo as cybersecurity_demo
from graph_model_examples.case_studies.policy import demo as policy_demo
from graph_model_examples.case_studies.product_kg import demo as product_demo

def test_security_policy_product():
    assert "database" in cybersecurity_demo()
    assert "approve-invoice" in policy_demo()
    assert "gateway-2" in product_demo()
