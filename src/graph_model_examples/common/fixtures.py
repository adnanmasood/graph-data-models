from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from .domain import CanonicalClaim, Entity, ExpectedAnswer

PROJECT_ROOT = Path(__file__).resolve().parents[3]
CANONICAL_DIR = PROJECT_ROOT / "data" / "canonical"


def project_root() -> Path:
    return PROJECT_ROOT


def _read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_entities() -> dict[str, Entity]:
    return {item["id"]: Entity(**item) for item in _read_json(CANONICAL_DIR / "entities.json")}


def load_canonical_claim() -> CanonicalClaim:
    return CanonicalClaim(**_read_json(CANONICAL_DIR / "alice_acme_ceo.json"))


def load_competency_questions() -> list[ExpectedAnswer]:
    return [ExpectedAnswer(**item) for item in _read_json(CANONICAL_DIR / "competency_questions.json")]


def is_valid_on(claim: CanonicalClaim, value: date | str) -> bool:
    if isinstance(value, str):
        value = date.fromisoformat(value)
    return claim.interval.contains(value)


def canonical_names() -> dict[str, str]:
    return {entity_id: entity.name for entity_id, entity in load_entities().items()}
