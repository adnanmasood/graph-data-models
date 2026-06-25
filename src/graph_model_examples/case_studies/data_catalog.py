from __future__ import annotations

from graph_model_examples.common.printing import simple_table


def demo() -> str:
    return simple_table(["data catalog", "value"], [['downstream reports', 'finance-dashboard'], ['source columns', 'erp.invoice_total'], ['verified by', 'data-steward']])
