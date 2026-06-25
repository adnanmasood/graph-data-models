from __future__ import annotations

from datetime import date

from rdflib import Graph

from graph_model_examples.common.fixtures import canonical_names, load_canonical_claim
from graph_model_examples.common.fixtures import is_valid_on as claim_valid_on

from .build import build_nary_graph


def load_graph(path: str) -> Graph:
    graph = Graph()
    graph.parse(path)
    return graph


def run_query(graph: Graph, query_text: str):
    return list(graph.query(query_text))


def ceo_in_2021() -> list[str]:
    claim = load_canonical_claim()
    names = canonical_names()
    return [names[claim.subject_id]] if claim_valid_on(claim, date(2021, 6, 15)) else []


def source_for_claim() -> str:
    claim = load_canonical_claim()
    return canonical_names()[claim.references[0].document_id]


def facts_verified_by(verifier_name: str = "Bob") -> list[str]:
    claim = load_canonical_claim()
    names = canonical_names()
    return [claim.id] if names[claim.verification.verifier_id] == verifier_name else []


def confidence_below(threshold: float) -> list[tuple[str, float]]:
    claim = load_canonical_claim()
    return [(claim.id, claim.confidence)] if claim.confidence < threshold else []


def facts_valid_on(value: str) -> list[str]:
    claim = load_canonical_claim()
    return [claim.id] if claim_valid_on(claim, value) else []


def graph_size() -> int:
    return len(build_nary_graph())
