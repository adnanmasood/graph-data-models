from __future__ import annotations

import re

BASE_IRI = "http://example.org/kg/"


def iri_for(entity_id: str) -> str:
    return f"{BASE_IRI}{safe_curie(entity_id)}"


def safe_curie(entity_id: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]", "_", entity_id.strip())
