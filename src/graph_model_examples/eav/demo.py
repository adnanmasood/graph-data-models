from __future__ import annotations

from graph_model_examples.common.printing import simple_table

from .queries import join_complexity_count, pivot_claim, recursive_descendants


def demo() -> str:
    claim = pivot_claim()
    rows = [
        ["pivoted claim", claim["employee"], f"{claim['role']} of {claim['employer']}"],
        ["source", claim["source"], f"confidence {claim['confidence']}"],
        ["recursive CTE", ", ".join(recursive_descendants()), "network-model ancestry"],
        ["join complexity", str(join_complexity_count()), "many attribute joins for typed facts"],
    ]
    return simple_table(["EAV example", "value", "note"], rows)
