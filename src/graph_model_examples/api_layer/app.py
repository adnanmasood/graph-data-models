from __future__ import annotations

from graph_model_examples.common.printing import simple_table

from .resolvers import resolve_employment_claim, resolve_facts_verified_by, resolve_provenance


def demo() -> str:
    claim = resolve_employment_claim()
    provenance = resolve_provenance()
    rows = [
        ["employmentClaim", claim["id"], "API response shape over canonical fixtures"],
        ["provenance", provenance["source"], f"confidence {provenance['confidence']}"],
        ["factsVerifiedByBob", ", ".join(resolve_facts_verified_by("bob")), "GraphQL is an API query layer"],
    ]
    return simple_table(["API operation", "value", "note"], rows)
