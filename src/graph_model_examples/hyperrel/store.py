from __future__ import annotations

import json
from pathlib import Path

from graph_model_examples.common.fixtures import project_root

from .model import Statement


def load_statements() -> list[Statement]:
    path = project_root() / "examples" / "hyper-relational" / "data" / "statements.json"
    return [Statement(**item) for item in json.loads(path.read_text(encoding="utf-8"))]
