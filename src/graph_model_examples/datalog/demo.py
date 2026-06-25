from __future__ import annotations

from graph_model_examples.common.printing import simple_table

from .engine import run_reasoning


def _fmt(facts) -> str:
    return "; ".join(f"{fact.predicate}{fact.args}" for fact in sorted(facts, key=lambda item: (item.predicate, item.args)))


def demo() -> str:
    derived = run_reasoning()
    rows = [[name, _fmt(facts), "derived with lineage"] for name, facts in derived.items()]
    return simple_table(["Datalog example", "derived facts", "note"], rows)
