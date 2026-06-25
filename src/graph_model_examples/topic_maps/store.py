from __future__ import annotations

import json

from graph_model_examples.common.fixtures import project_root


def load_topic_map() -> dict:
    path = project_root() / "examples" / "topic-maps" / "data" / "alice_acme_topic_map.json"
    return json.loads(path.read_text(encoding="utf-8"))


def merge_by_subject_identifier(topics: list[dict]) -> list[dict]:
    merged: dict[str, dict] = {}
    for topic in topics:
        key = next(iter(topic.get("subject_identifiers", [topic["id"]])))
        current = merged.setdefault(key, {"id": topic["id"], "names": [], "subject_identifiers": []})
        current["names"] = sorted(set(current["names"]) | set(topic.get("names", [])))
        current["subject_identifiers"] = sorted(set(current["subject_identifiers"]) | set(topic.get("subject_identifiers", [])))
    return list(merged.values())
