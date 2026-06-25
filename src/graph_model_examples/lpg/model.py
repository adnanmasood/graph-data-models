from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LPGClaim:
    employee: str
    employer: str
    role: str
    start_date: str
    end_date: str
    source: str
    verified_by: str
    confidence: float
