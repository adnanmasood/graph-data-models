from __future__ import annotations

from graph_model_examples.common.printing import simple_table


def demo() -> str:
    return simple_table(["cybersecurity attack path", "value"], [['entry', 'internet'], ['target', 'database'], ['path', 'internet -> web-server -> database']])
