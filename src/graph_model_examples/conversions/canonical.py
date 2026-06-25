from __future__ import annotations

from graph_model_examples.common.fixtures import load_canonical_claim


def canonical_record() -> dict:
    claim = load_canonical_claim()
    return claim.model_dump(mode="json")
