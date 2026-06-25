from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Rule:
    name: str
    derives: str
    explanation: str


RULES = [
    Rule("active_employment", "active_employment", "employment interval contains the query date"),
    Rule("ownership_chain", "controls", "transitive closure over owns"),
    Rule("attack_path", "reachable", "transitive closure over network_edge"),
    Rule("policy_entitlement", "entitled", "role assignment plus role permission"),
]
