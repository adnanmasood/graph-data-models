from __future__ import annotations

from .store import load_hyperedges


def employment_edges() -> list[str]:
    return [edge.id for edge in load_hyperedges() if edge.type == "employment"]


def verification_edges() -> list[str]:
    return [edge.id for edge in load_hyperedges() if edge.type == "verification"]


def supply_chain_transactions() -> list[str]:
    return [edge.id for edge in load_hyperedges() if edge.type == "supply_chain_transaction"]


def participants(edge_id: str) -> dict[str, str]:
    return next(edge.participants for edge in load_hyperedges() if edge.id == edge_id)
