from __future__ import annotations

from graph_model_examples.common.fixtures import canonical_names, load_canonical_claim, load_entities


def get_person(person_id: str) -> dict | None:
    entity = load_entities().get(person_id)
    return entity.model_dump(mode="json") if entity and entity.type == "person" else None


def get_company(company_id: str) -> dict | None:
    entity = load_entities().get(company_id)
    return entity.model_dump(mode="json") if entity and entity.type == "company" else None


def get_employment_claim() -> dict:
    claim = load_canonical_claim().model_dump(mode="json")
    claim["names"] = canonical_names()
    return claim
