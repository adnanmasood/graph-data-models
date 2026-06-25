from graph_model_examples.gotchas.datalog_runaway import runaway_guard
from graph_model_examples.gotchas.open_world_vs_shacl import open_world_vs_shacl
from graph_model_examples.gotchas.qualifier_loss import qualifier_loss
from graph_model_examples.gotchas.vector_not_facts import vector_limit


def test_gotcha_labs():
    assert open_world_vs_shacl()["shacl_closed_check"]
    assert qualifier_loss()["after_flattening"] == []
    assert runaway_guard()["terminated"] is True
    assert vector_limit()["factual_confidence"] == "graph field"
