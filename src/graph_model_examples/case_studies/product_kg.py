from __future__ import annotations

from graph_model_examples.common.printing import simple_table


def demo() -> str:
    return simple_table(["product KG", "value"], [['product', 'sensor-9'], ['compatible with', 'gateway-2'], ['source', 'product catalog']])
