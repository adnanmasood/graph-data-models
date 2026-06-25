from __future__ import annotations

from importlib import import_module

from .common.fixtures import canonical_names, load_canonical_claim
from .common.printing import simple_table
from .registry import EXAMPLES, get_example


class UnknownExample(ValueError):
    pass


def _load_runner(path: str):
    module_name, function_name = path.split(":", 1)
    module = import_module(module_name)
    return getattr(module, function_name)


def run_example(slug: str) -> str:
    example = get_example(slug)
    if example is None:
        available = ", ".join(sorted(item.slug for item in EXAMPLES))
        raise UnknownExample(f"Unknown example '{slug}'. Available examples: {available}")
    return str(_load_runner(example.runner)())


def list_examples_text() -> str:
    rows = [[e.slug, e.model_family, e.title] for e in EXAMPLES]
    return simple_table(["slug", "family", "title"], rows)


def alice_acme_all() -> str:
    claim = load_canonical_claim()
    names = canonical_names()
    fact = f"{names[claim.subject_id]} was {names[claim.role_id]} of {names[claim.employer_id]} from {claim.interval.start_date} to {claim.interval.end_date}"
    provenance = f"source={names[claim.references[0].document_id]}, verified_by={names[claim.verification.verifier_id]}, confidence={claim.confidence}"
    rows = [
        ["RDF", fact, "n-ary role node keeps source and dates"],
        ["LPG", fact, "edge properties are compact; event node keeps provenance"],
        ["hyper-relational", fact, provenance],
        ["hypergraph", fact, "employment hyperedge has employee, employer, role, authority, location"],
        ["Datalog", "active_ceo(Alice, Acme, 2021) is derived", "source fact remains separate from derived fact"],
        ["Topic Maps", fact, "association roles and subject identity"],
        ["EAV", fact, "pivot rows recover the claim but validation is weaker"],
        ["GraphRAG", "retrieves Alice/Acme graph context", provenance],
    ]
    return simple_table(["model", "canonical fact", "modeling note"], rows)
