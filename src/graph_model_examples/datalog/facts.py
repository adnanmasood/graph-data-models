from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Fact:
    predicate: str
    args: tuple[str, ...]
    lineage: tuple[str, ...] = ()


def canonical_facts() -> set[Fact]:
    return {
        Fact("employment", ("alice", "acme", "ceo", "2020-01-01", "2023-03-31"), ("claim-alice-acme-ceo",)),
        Fact("verified_by", ("claim-alice-acme-ceo", "bob"), ("claim-alice-acme-ceo",)),
        Fact("confidence", ("claim-alice-acme-ceo", "0.93"), ("claim-alice-acme-ceo",)),
        Fact("owns", ("acme", "subsidiary-a"), ("ownership-file",)),
        Fact("owns", ("subsidiary-a", "plant-7"), ("ownership-file",)),
        Fact("network_edge", ("internet", "web-server"), ("security-file",)),
        Fact("network_edge", ("web-server", "database"), ("security-file",)),
        Fact("role_assignment", ("alice", "finance-admin"), ("policy-file",)),
        Fact("role_allows", ("finance-admin", "approve-invoice"), ("policy-file",)),
    }
