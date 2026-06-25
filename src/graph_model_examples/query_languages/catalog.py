from __future__ import annotations

CATALOG = [
    {"name": "SPARQL", "kind": "query language", "common_backend": "RDF stores", "data_model": False},
    {"name": "Cypher", "kind": "query language", "common_backend": "labeled property graphs", "data_model": False},
    {"name": "Gremlin", "kind": "traversal language", "common_backend": "TinkerPop-compatible graphs", "data_model": False},
    {"name": "GQL", "kind": "standard graph query language", "common_backend": "property graph databases", "data_model": False},
    {"name": "GraphQL", "kind": "API query language", "common_backend": "any service backend", "data_model": False},
]


def classify(name: str) -> dict:
    for entry in CATALOG:
        if entry["name"].lower() == name.lower():
            return entry
    raise KeyError(name)
