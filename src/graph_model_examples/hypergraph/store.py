from __future__ import annotations

import json

from graph_model_examples.common.fixtures import project_root

from .model import Hyperedge


def load_hyperedges() -> list[Hyperedge]:
    path = project_root() / "examples" / "hypergraph" / "data" / "hyperedges.json"
    return [Hyperedge(**item) for item in json.loads(path.read_text(encoding="utf-8"))]
