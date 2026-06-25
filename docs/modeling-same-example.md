# Modeling the Same Alice/Acme Fact

- RDF n-ary Turtle: `ex:claim-alice-acme-ceo a ex:EmploymentRole` links employee, employer, role, dates, source, verifier, and confidence.
- RDF named graph TriG: claim triples live in a claim graph and provenance lives in a provenance graph.
- RDF-star / RDF 1.2-style syntax: `<< ex:alice ex:ceoOf ex:acme >> ex:confidence 0.93` keeps metadata near a statement.
- Cypher edge property: `(alice)-[:CEO_OF {confidence:0.93}]->(acme)` is compact.
- LPG event-node pattern: Alice connects to a claim node, and the claim node connects to source and verifier.
- Wikidata-style JSON statement: statement S1 has qualifiers, references, rank, and confidence.
- Hypergraph JSON: hyperedge H1 has participant roles for employee, employer, role, authority, location, and source.
- TypeQL-style relation: employment relates employee, employer, role, authority, and location.
- Datalog facts: `employment(alice, acme, ceo, 2020-01-01, 2023-03-31)` supports derived active employment.
- EAV rows: the claim is reconstructed by pivoting attribute rows.

Elegant aspects are strongest when the model matches the question. Awkward aspects appear when source, verifier, confidence, and qualifiers are flattened into a simple binary edge. Easy queries find Alice as CEO in 2021; hard queries preserve conversion semantics and conflict handling.
