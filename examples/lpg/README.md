# Labeled Property Graph Examples

Run with `make demo-lpg`.

The edge-property model puts role, dates, source, verifier, and confidence directly on the Alice to Acme edge. The event-node model creates a claim node so provenance and source documents are first-class traversal targets.

Elegant: LPGs are compact and developer-friendly for path queries and analytics. Awkward: statement metadata can create many edge properties, and supernodes can hurt unbounded traversal. The Neo4j Cypher files are optional snippets; the default executable path uses NetworkX.
