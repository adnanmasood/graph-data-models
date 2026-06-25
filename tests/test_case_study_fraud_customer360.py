from graph_model_examples.case_studies.fraud import demo as fraud_demo
from graph_model_examples.case_studies.customer360 import demo as customer_demo

def test_fraud_and_customer360():
    assert "ring score" in fraud_demo()
    assert "cust-golden-1" in customer_demo()
