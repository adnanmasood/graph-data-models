from graph_model_examples.conversions.canonical import canonical_record
from graph_model_examples.conversions.loss_audit import loss_report


def test_conversion_loss_audit():
    record = canonical_record()
    assert record["confidence"] == 0.93
    report = loss_report()
    statuses = {item["status"] for item in report}
    assert {"preserved", "transformed", "lost"} <= statuses
    assert any("plain binary edge" in item["path"] and item["status"] == "lost" for item in report)
