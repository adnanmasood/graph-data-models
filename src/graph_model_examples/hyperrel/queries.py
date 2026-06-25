from __future__ import annotations

from .store import load_statements


def preferred_statement(subject: str = "alice", prop: str = "position_held"):
    candidates = [s for s in load_statements() if s.subject == subject and s.property == prop]
    return next(s for s in candidates if s.rank == "preferred")


def sources_for_statement(statement_id: str) -> list[str]:
    return next(s.references for s in load_statements() if s.id == statement_id)


def qualifiers_for_statement(statement_id: str) -> dict[str, str]:
    return next(s.qualifiers for s in load_statements() if s.id == statement_id)


def claims_verified_by(verifier: str = "bob") -> list[str]:
    return [s.id for s in load_statements() if s.verified_by == verifier]


def conflicting_claims() -> list[str]:
    return [s.id for s in load_statements() if s.rank == "deprecated"]
