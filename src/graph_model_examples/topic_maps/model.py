from __future__ import annotations

from pydantic import BaseModel, Field


class Topic(BaseModel):
    id: str
    names: list[str]
    subject_identifiers: list[str] = Field(default_factory=list)


class Association(BaseModel):
    id: str
    type: str
    roles: dict[str, str]


class Occurrence(BaseModel):
    topic_id: str
    type: str
    value: str
