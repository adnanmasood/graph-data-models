from __future__ import annotations

from graph_model_examples.common.printing import simple_table


def demo() -> str:
    return simple_table(["customer 360", "value"], [['merged profile', 'cust-golden-1'], ['evidence', 'email hash plus device'], ['confidence', '0.88']])
