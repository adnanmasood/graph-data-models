from __future__ import annotations

from graph_model_examples.common.printing import simple_table

from .store import load_topic_map, merge_by_subject_identifier


def demo() -> str:
    topic_map = load_topic_map()
    merged = merge_by_subject_identifier(topic_map["topics"])
    rows = [
        ["topics before merge", str(len(topic_map["topics"])), "Acme appears twice"],
        ["topics after merge", str(len(merged)), "subject identifier merges Acme"],
        ["association", topic_map["associations"][0]["type"], str(topic_map["associations"][0]["roles"])],
    ]
    return simple_table(["Topic Maps example", "value", "note"], rows)
