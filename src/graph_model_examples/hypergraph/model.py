from __future__ import annotations

from pydantic import BaseModel, Field


class Hyperedge(BaseModel):
    id: str
    type: str
    participants: dict[str, str]
    attributes: dict[str, str | float] = Field(default_factory=dict)
