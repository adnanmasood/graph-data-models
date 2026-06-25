from __future__ import annotations


def loss_report() -> list[dict[str, str]]:
    return [
        {"path": "RDF n-ary to LPG event node", "status": "preserved", "detail": "source, verifier, dates, confidence, role, authority, and location remain explicit"},
        {"path": "RDF n-ary to LPG edge property", "status": "transformed", "detail": "metadata moves from claim node to edge properties"},
        {"path": "hypergraph to binary edges", "status": "transformed", "detail": "participant roles become event-node edges"},
        {"path": "EAV to canonical", "status": "transformed", "detail": "typed claim recovered only after pivoting attribute rows"},
        {"path": "plain binary edge", "status": "lost", "detail": "source, verifier, confidence, authority, and location are absent"},
    ]
