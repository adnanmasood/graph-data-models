from graph_model_examples.eav.queries import join_complexity_count, pivot_claim, recursive_descendants


def test_eav_pivot_and_recursive_cte():
    claim = pivot_claim()
    assert claim["employee"] == "alice"
    assert claim["confidence"] == "0.93"
    assert recursive_descendants() == ["division-a", "team-7"]
    assert join_complexity_count() == 5
