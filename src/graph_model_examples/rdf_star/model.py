from __future__ import annotations

from pydantic import BaseModel


class AnnotatedTriple(BaseModel):
    subject: str
    predicate: str
    object_id: str
    source: str
    verified_by: str
    verified_on: str
    confidence: float
    start_date: str
    end_date: str


def canonical_statement() -> AnnotatedTriple:
    return AnnotatedTriple(
        subject="alice",
        predicate="ceoOf",
        object_id="acme",
        source="acme-2020-annual-report",
        verified_by="bob",
        verified_on="2023-04-05",
        confidence=0.93,
        start_date="2020-01-01",
        end_date="2023-03-31",
    )
