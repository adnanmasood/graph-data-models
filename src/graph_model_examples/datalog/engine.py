from __future__ import annotations

from datetime import date

from .facts import Fact, canonical_facts


class FixedPointEngine:
    def __init__(self, facts: set[Fact] | None = None, max_iterations: int = 20):
        self.facts = set(facts or canonical_facts())
        self.max_iterations = max_iterations

    def derive_active_employment(self, value: str) -> set[Fact]:
        when = date.fromisoformat(value)
        derived = set()
        for fact in self.facts:
            if fact.predicate == "employment":
                employee, employer, role, start, end = fact.args
                if date.fromisoformat(start) <= when <= date.fromisoformat(end):
                    derived.add(Fact("active_employment", (employee, employer, role, value), fact.lineage + ("active_employment",)))
        self.facts |= derived
        return derived

    def derive_transitive(self, source_predicate: str, target_predicate: str) -> set[Fact]:
        edges = {(f.args[0], f.args[1]) for f in self.facts if f.predicate == source_predicate}
        closure = set(edges)
        for _ in range(self.max_iterations):
            additions = {(a, d) for a, b in closure for c, d in closure if b == c and (a, d) not in closure}
            if not additions:
                break
            closure |= additions
        derived = {Fact(target_predicate, pair, (source_predicate, target_predicate)) for pair in closure}
        self.facts |= derived
        return derived

    def derive_entitlements(self) -> set[Fact]:
        assignments = [(f.args[0], f.args[1]) for f in self.facts if f.predicate == "role_assignment"]
        allows = [(f.args[0], f.args[1]) for f in self.facts if f.predicate == "role_allows"]
        derived = {Fact("entitled", (user, action), ("policy_entitlement",)) for user, role in assignments for allow_role, action in allows if role == allow_role}
        self.facts |= derived
        return derived


def run_reasoning() -> dict[str, set[Fact]]:
    engine = FixedPointEngine()
    return {
        "active": engine.derive_active_employment("2021-06-15"),
        "controls": engine.derive_transitive("owns", "controls"),
        "attack_paths": engine.derive_transitive("network_edge", "reachable"),
        "entitlements": engine.derive_entitlements(),
    }
