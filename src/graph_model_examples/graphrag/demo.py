from __future__ import annotations

from graph_model_examples.common.printing import simple_table

from .retriever import answer


def demo() -> str:
    result = answer("Who was CEO of Acme in 2021?")
    rows = [
        ["answer", result.answer_summary, "deterministic summary"],
        ["documents", ", ".join(doc["id"] for doc in result.retrieved_documents), "local bag-of-words retrieval"],
        ["graph facts", str(len(result.graph_facts)), "source-aware context expansion"],
        ["provenance", ", ".join(result.provenance), "citations retained"],
        ["caveats", "; ".join(result.caveats), "low-confidence conflict surfaced"],
    ]
    return simple_table(["GraphRAG item", "value", "note"], rows)
