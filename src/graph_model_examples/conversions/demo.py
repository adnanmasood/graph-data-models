from __future__ import annotations

from graph_model_examples.common.printing import simple_table

from .loss_audit import loss_report


def demo() -> str:
    rows = [[item["path"], item["status"], item["detail"]] for item in loss_report()]
    return simple_table(["conversion path", "status", "detail"], rows)
