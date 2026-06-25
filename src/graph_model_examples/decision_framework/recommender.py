from __future__ import annotations

from dataclasses import dataclass

from graph_model_examples.common.printing import simple_table

from .models import Requirements


@dataclass(frozen=True)
class Recommendation:
    model: str
    score: int
    explanation: str


MATRIX = {
    "RDF": {"semantic": 5, "metadata": 3, "nary": 4, "rules": 2, "traversal": 2, "graphrag": 5},
    "LPG": {"semantic": 2, "metadata": 3, "nary": 3, "rules": 1, "traversal": 5, "graphrag": 4},
    "RDF-star / RDF 1.2": {"semantic": 5, "metadata": 5, "nary": 4, "rules": 2, "traversal": 2, "graphrag": 5},
    "Hyper-relational": {"semantic": 4, "metadata": 5, "nary": 4, "rules": 1, "traversal": 2, "graphrag": 4},
    "Hypergraph": {"semantic": 3, "metadata": 4, "nary": 5, "rules": 1, "traversal": 3, "graphrag": 3},
    "Datalog rule layer": {"semantic": 3, "metadata": 2, "nary": 3, "rules": 5, "traversal": 3, "graphrag": 4},
    "Topic Maps": {"semantic": 4, "metadata": 3, "nary": 3, "rules": 1, "traversal": 2, "graphrag": 2},
    "EAV": {"semantic": 1, "metadata": 2, "nary": 2, "rules": 1, "traversal": 1, "graphrag": 1},
    "Hybrid RDF core + LPG projection + Datalog rule layer": {"semantic": 5, "metadata": 5, "nary": 4, "rules": 5, "traversal": 5, "graphrag": 5},
}


def _score(values: dict[str, int], requirements: Requirements) -> int:
    score = 0
    score += values["semantic"] if requirements.needs_semantic_interoperability else 0
    score += values["metadata"] if requirements.needs_statement_metadata else 0
    score += values["nary"] if requirements.needs_nary_relationships else 0
    score += values["rules"] if requirements.needs_recursive_rules else 0
    score += values["traversal"] if requirements.needs_fast_traversal else 0
    score += values["graphrag"] if requirements.needs_graph_rag else 0
    return score or sum(values.values()) // len(values)


def recommend_models(requirements: Requirements) -> list[Recommendation]:
    recommendations = []
    for model, values in MATRIX.items():
        score = _score(values, requirements)
        if (
            model.startswith("Hybrid")
            and requirements.needs_graph_rag
            and (requirements.needs_statement_metadata or requirements.needs_fast_traversal or requirements.needs_semantic_interoperability)
        ):
            score += 2
        explanation = "matches selected requirements" if score else "general comparison baseline"
        recommendations.append(Recommendation(model, score, explanation))
    return sorted(recommendations, key=lambda item: item.score, reverse=True)


def format_recommendations(recommendations: list[Recommendation]) -> str:
    rows = [[rec.model, str(rec.score), rec.explanation] for rec in recommendations[:5]]
    return simple_table(["model", "score", "explanation"], rows)
