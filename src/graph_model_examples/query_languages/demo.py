from __future__ import annotations

from graph_model_examples.common.printing import simple_table

from .catalog import CATALOG


def demo() -> str:
    rows = [[entry["name"], entry["kind"], entry["common_backend"], str(entry["data_model"])] for entry in CATALOG]
    rows.append(["Equivalent question", "Who was CEO of Acme in 2021?", "expressed in all snippets", "False"])
    return simple_table(["technology", "kind", "typical backend", "is data model"], rows)
