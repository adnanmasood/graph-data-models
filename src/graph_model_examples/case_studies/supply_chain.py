from __future__ import annotations

from graph_model_examples.common.printing import simple_table


def demo() -> str:
    return simple_table(["supply chain risk", "value"], [['transaction', 'supplier-a sensor-9 acme'], ['risk', 'weather-delay'], ['model', 'hyperedge']])
