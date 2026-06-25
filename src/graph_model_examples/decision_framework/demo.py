from __future__ import annotations

from .models import Requirements
from .recommender import format_recommendations, recommend_models


def demo() -> str:
    req = Requirements(needs_semantic_interoperability=True, needs_statement_metadata=True, needs_graph_rag=True)
    return format_recommendations(recommend_models(req))
