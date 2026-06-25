from graph_model_examples.graphrag.retriever import answer


def test_graphrag_retrieves_source_and_context():
    result = answer("Who was CEO of Acme in 2021?")
    doc_ids = {doc["id"] for doc in result.retrieved_documents}
    assert "acme-2020-annual-report" in doc_ids
    assert any(fact["id"] == "claim-alice-acme-ceo" for fact in result.graph_facts)
    assert "confidence 0.93" in result.answer_summary
    assert result.caveats
