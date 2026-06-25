from __future__ import annotations

from graph_model_examples.common.printing import simple_table


def demo() -> str:
    return simple_table(["fraud detection", "value"], [['shared phone', 'acct-1 acct-2'], ['shared device', 'acct-2 acct-3'], ['ring score', 'high']])
