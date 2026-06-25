from __future__ import annotations

from graph_model_examples.common.printing import simple_table

from .build import build_named_graph_dataset, build_nary_graph, build_plain_lossy_graph, build_reification_graph
from .query import ceo_in_2021, confidence_below, facts_valid_on, facts_verified_by, source_for_claim


def demo() -> str:
    rows = [
        ["plain triples", str(len(build_plain_lossy_graph())), "compact but loses source, dates, and verifier"],
        ["n-ary relation", str(len(build_nary_graph())), "keeps role, dates, qualifiers, provenance, confidence"],
        ["named graph", str(len(build_named_graph_dataset())), "separates claim graph and provenance graph"],
        ["classic reification", str(len(build_reification_graph())), "standard but verbose"],
        ["CEO in 2021", ", ".join(ceo_in_2021()), "expected Alice"],
        ["source", source_for_claim(), "Acme 2020 Annual Report"],
        ["verified by Bob", ", ".join(facts_verified_by()), "statement-level provenance"],
        ["confidence below 0.95", str(confidence_below(0.95)), "0.93 is surfaced"],
        ["valid on 2024-01-01", str(facts_valid_on("2024-01-01")), "empty after end date"],
    ]
    return simple_table(["RDF example", "value", "note"], rows)
