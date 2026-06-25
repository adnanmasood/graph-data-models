from graph_model_examples.topic_maps.store import load_topic_map, merge_by_subject_identifier


def test_topic_map_subject_identity_merge():
    topic_map = load_topic_map()
    merged = merge_by_subject_identifier(topic_map["topics"])
    assert len(topic_map["topics"]) == 4
    assert len(merged) == 3
    assert topic_map["associations"][0]["roles"]["employee"] == "alice-topic"
