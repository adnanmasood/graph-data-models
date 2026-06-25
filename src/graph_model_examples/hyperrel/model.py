from __future__ import annotations

from pydantic import BaseModel, Field


class Statement(BaseModel):
    id: str
    subject: str
    property: str
    value: str
    qualifiers: dict[str, str] = Field(default_factory=dict)
    references: list[str] = Field(default_factory=list)
    rank: str
    confidence: float
    verified_by: str | None = None
    verification_date: str | None = None
