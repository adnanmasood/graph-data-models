# Hybrid GraphRAG

Run with `make demo-graphrag`.

This demo performs local bag-of-words retrieval, expands graph context connected to the retrieved documents and entities, and returns a deterministic answer with citations. It does not call an LLM or external vector database.

Elegant: vector retrieval finds candidate text while graph facts preserve source, confidence, temporal validity, and conflicts. Awkward: retrieval scores are not factual truth, so graph validation and provenance remain necessary.
