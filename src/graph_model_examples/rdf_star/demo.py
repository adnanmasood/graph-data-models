from __future__ import annotations

from graph_model_examples.common.printing import simple_table

from .lower_to_nary import lower_statement_to_nary, lowered_summary


def demo() -> str:
    summary = lowered_summary()
    graph = lower_statement_to_nary()
    rows = [
        ["syntax", "RDF-star / RDF 1.2 annotation files are kept as examples"],
        ["parser stance", "default code does not assume every RDFLib parser supports annotation syntax"],
        ["lowered triples", str(len(graph))],
        ["source", str(summary["source"])],
        ["confidence", str(summary["confidence"])],
    ]
    return simple_table(["RDF-star item", "value"], rows)
