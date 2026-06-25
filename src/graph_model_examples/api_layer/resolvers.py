from __future__ import annotations

from .backends import get_company, get_employment_claim, get_person


def resolve_person(person_id: str) -> dict | None:
    return get_person(person_id)


def resolve_company(company_id: str) -> dict | None:
    return get_company(company_id)


def resolve_employment_claim() -> dict:
    return get_employment_claim()


def resolve_provenance() -> dict:
    claim = get_employment_claim()
    return {"source": claim["references"][0]["document_id"], "confidence": claim["confidence"], "verified_by": claim["verification"]["verifier_id"]}


def resolve_facts_verified_by(verifier_id: str) -> list[str]:
    claim = get_employment_claim()
    return [claim["id"]] if claim["verification"]["verifier_id"] == verifier_id else []
