from __future__ import annotations

import json

from graph_model_examples.common.fixtures import project_root


def load_documents() -> list[dict]:
    path = project_root() / "examples" / "hybrid-graphrag" / "data" / "documents.jsonl"
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_graph_facts() -> list[dict]:
    path = project_root() / "examples" / "hybrid-graphrag" / "data" / "graph_facts.json"
    return json.loads(path.read_text(encoding="utf-8"))
