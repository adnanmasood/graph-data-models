from __future__ import annotations

from graph_model_examples.common.printing import simple_table


def demo() -> str:
    return simple_table(["policy entitlements", "value"], [['user', 'alice'], ['action', 'approve-invoice'], ['decision', 'allowed by finance-admin']])
