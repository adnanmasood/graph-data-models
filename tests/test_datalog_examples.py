from graph_model_examples.datalog.engine import FixedPointEngine, run_reasoning


def test_datalog_derivations():
    derived = run_reasoning()
    assert any(f.args[:3] == ("alice", "acme", "ceo") for f in derived["active"])
    assert any(f.args == ("acme", "plant-7") for f in derived["controls"])
    assert any(f.args == ("internet", "database") for f in derived["attack_paths"])
    assert any(f.args == ("alice", "approve-invoice") for f in derived["entitlements"])
    assert FixedPointEngine(max_iterations=1).max_iterations == 1
