from __future__ import annotations

from graph_model_examples.common.printing import simple_table

from .queries import employment_edges, participants, supply_chain_transactions, verification_edges


def demo() -> str:
    edge_id = employment_edges()[0]
    rows = [
        ["employment hyperedge", edge_id, str(participants(edge_id))],
        ["verification hyperedge", ", ".join(verification_edges()), "points to employment edge"],
        ["supply chain n-ary transaction", ", ".join(supply_chain_transactions()), "supplier, buyer, part, route, risk"],
    ]
    return simple_table(["hypergraph example", "value", "note"], rows)
