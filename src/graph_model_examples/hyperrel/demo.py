from __future__ import annotations

from graph_model_examples.common.printing import simple_table

from .queries import claims_verified_by, conflicting_claims, preferred_statement, qualifiers_for_statement, sources_for_statement


def demo() -> str:
    statement = preferred_statement()
    rows = [
        ["preferred statement", statement.id, f"{statement.subject} {statement.property} {statement.value}"],
        ["qualifiers", str(qualifiers_for_statement(statement.id)), "dates, authority, location"],
        ["references", ", ".join(sources_for_statement(statement.id)), "source-aware claim"],
        ["verified by Bob", ", ".join(claims_verified_by()), "provenance query"],
        ["conflicts", ", ".join(conflicting_claims()), "deprecated claim is retained"],
    ]
    return simple_table(["hyper-relational query", "value", "note"], rows)
