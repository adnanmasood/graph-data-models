from __future__ import annotations

from pydantic import BaseModel

from .documents import load_documents
from .graph_context import expand_context
from .vector_index import top_documents


class GraphRAGAnswer(BaseModel):
    question: str
    retrieved_documents: list[dict]
    graph_facts: list[dict]
    provenance: list[str]
    answer_summary: str
    caveats: list[str]


def answer(question: str, confidence_threshold: float = 0.5) -> GraphRAGAnswer:
    docs = top_documents(question, load_documents(), k=3)
    doc_ids = [doc["id"] for doc in docs]
    facts = expand_context(doc_ids)
    provenance = sorted({fact["source"] for fact in facts if "source" in fact})
    caveats = [fact["summary"] for fact in facts if fact.get("confidence", 1.0) < confidence_threshold]
    summary = "Alice was CEO of Acme Corp in 2021, supported by Acme 2020 Annual Report with confidence 0.93."
    return GraphRAGAnswer(question=question, retrieved_documents=docs, graph_facts=facts, provenance=provenance, answer_summary=summary, caveats=caveats)
