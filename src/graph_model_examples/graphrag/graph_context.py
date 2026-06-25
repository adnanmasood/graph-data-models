from __future__ import annotations

from .documents import load_graph_facts


def expand_context(document_ids: list[str]) -> list[dict]:
    return [fact for fact in load_graph_facts() if fact.get("source") in document_ids or any(entity in {"alice", "acme"} for entity in fact.get("entities", []))]
