from __future__ import annotations

import os


def is_enabled() -> bool:
    return os.getenv("NEO4J_URI") is not None


def load_if_enabled() -> str:
    if not is_enabled():
        return "Neo4j integration skipped because NEO4J_URI is unset. Offline NetworkX examples are active."
    return "Neo4j integration would use the Cypher files in examples/lpg/cypher."
