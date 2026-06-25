from __future__ import annotations

from datetime import date
from pydantic import BaseModel, Field


class Entity(BaseModel):
    id: str
    name: str
    type: str
    aliases: list[str] = Field(default_factory=list)
    subject_identifiers: list[str] = Field(default_factory=list)
    published_on: date | None = None


class Document(Entity):
    type: str = "document"


class TemporalInterval(BaseModel):
    start_date: date
    end_date: date | None = None

    def contains(self, value: date) -> bool:
        if value < self.start_date:
            return False
        if self.end_date is not None and value > self.end_date:
            return False
        return True


class Qualifier(BaseModel):
    name: str
    value: str
    entity_id: str | None = None


class Reference(BaseModel):
    document_id: str
    citation: str


class Verification(BaseModel):
    verifier_id: str
    verified_on: date


class CanonicalClaim(BaseModel):
    id: str
    subject_id: str
    relation: str
    employer_id: str
    role_id: str
    interval: TemporalInterval
    qualifiers: list[Qualifier]
    references: list[Reference]
    verification: Verification
    confidence: float
    asserted: bool = True
    fact_type: str = "source"

    def qualifier_value(self, name: str) -> str | None:
        for qualifier in self.qualifiers:
            if qualifier.name == name:
                return qualifier.value
        return None

    def qualifier_entity(self, name: str) -> str | None:
        for qualifier in self.qualifiers:
            if qualifier.name == name:
                return qualifier.entity_id
        return None


class ExpectedAnswer(BaseModel):
    id: str
    question: str
    answer: str
    evidence_ids: list[str]
