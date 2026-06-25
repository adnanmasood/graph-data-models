from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Example:
    slug: str
    title: str
    model_family: str
    runner: str
    description: str
    article_section: str
    primary_files: tuple[str, ...]
    optional_external_dependencies: tuple[str, ...] = field(default_factory=tuple)


EXAMPLES: tuple[Example, ...] = (
    Example("alice-acme-all", "Alice/Acme across models", "cross-model", "graph_model_examples.runner:alice_acme_all", "Compact smoke view of the canonical fact across model families.", "Canonical running example", ("data/canonical/alice_acme_ceo.json", "docs/modeling-same-example.md")),
    Example("rdf", "RDF modeling patterns", "RDF", "graph_model_examples.rdf_examples.demo:demo", "Plain triples, n-ary relation, named graph, and reification.", "RDF", ("examples/rdf/README.md",)),
    Example("rdf-validation", "RDF ontology and SHACL", "RDF", "graph_model_examples.rdf_examples.validate:demo", "Ontology, SHACL validation, and controlled inference.", "RDF validation", ("examples/rdf/ontology/shapes.ttl",)),
    Example("rdf-star", "RDF-star / RDF 1.2", "RDF-star / RDF 1.2", "graph_model_examples.rdf_star.demo:demo", "Statement metadata syntax examples plus tested n-ary lowering.", "RDF-star / RDF 1.2", ("examples/rdf-star-rdf12/README.md",)),
    Example("lpg", "Labeled property graph", "LPG", "graph_model_examples.lpg.queries:demo", "NetworkX property graph, event-node model, Cypher snippets, and analytics.", "Labeled property graphs", ("examples/lpg/README.md",), ("Neo4j",)),
    Example("query-languages", "Query and API languages", "query/API", "graph_model_examples.query_languages.demo:demo", "SPARQL, Cypher, Gremlin, GQL, and GraphQL as technologies around graph data.", "Technologies confused with models", ("examples/query-languages/README.md",)),
    Example("hyperrel", "Hyper-relational statements", "hyper-relational", "graph_model_examples.hyperrel.demo:demo", "Wikidata-style claims with qualifiers, references, ranks, and confidence.", "Hyper-relational", ("examples/hyper-relational/README.md",)),
    Example("hypergraph", "Hypergraph n-ary relations", "hypergraph", "graph_model_examples.hypergraph.demo:demo", "Typed hyperedges with participant roles and TypeQL-style snippets.", "Hypergraphs", ("examples/hypergraph/README.md",)),
    Example("datalog", "Datalog-style reasoning", "Datalog", "graph_model_examples.datalog.demo:demo", "Deterministic recursive rules, derived facts, and rule lineage.", "Datalog", ("examples/datalog/README.md",)),
    Example("topic-maps", "Topic Maps", "Topic Maps", "graph_model_examples.topic_maps.demo:demo", "Topics, associations, occurrences, and subject identity merging.", "Topic Maps", ("examples/topic-maps/README.md",)),
    Example("eav", "EAV and network ancestry", "EAV", "graph_model_examples.eav.demo:demo", "SQLite EAV tables, pivot query, recursive CTE, and modeling limits.", "EAV/network", ("examples/eav-network/README.md",)),
    Example("conversions", "Conversions and loss audit", "cross-model", "graph_model_examples.conversions.demo:demo", "Canonical conversions among RDF, LPG, hyper-relational, hypergraph, Datalog, and EAV.", "Conversion loss", ("examples/conversions/README.md",)),
    Example("graphrag", "Hybrid GraphRAG", "hybrid graph + vector", "graph_model_examples.graphrag.demo:demo", "Deterministic local retrieval with graph context and citations.", "Hybrid architectures", ("examples/hybrid-graphrag/README.md",)),
    Example("case-data-catalog", "Data catalog lineage", "case study", "graph_model_examples.case_studies.data_catalog:demo", "Enterprise catalog and source-aware lineage.", "Case studies", ("case_studies/data-catalog-lineage/README.md",)),
    Example("case-fraud", "Fraud detection", "case study", "graph_model_examples.case_studies.fraud:demo", "Fraud ring detection with graph traversal patterns.", "Case studies", ("case_studies/fraud-detection/README.md",)),
    Example("case-customer360", "Customer 360", "case study", "graph_model_examples.case_studies.customer360:demo", "Identity resolution events and confidence.", "Case studies", ("case_studies/customer-360/README.md",)),
    Example("case-biomedical", "Biomedical KG", "case study", "graph_model_examples.case_studies.biomedical:demo", "Drug, gene, disease, evidence, and validation shapes.", "Case studies", ("case_studies/biomedical-kg/README.md",)),
    Example("case-supply-chain", "Supply chain risk", "case study", "graph_model_examples.case_studies.supply_chain:demo", "N-ary shipment, supplier, part, route, and risk modeling.", "Case studies", ("case_studies/supply-chain-risk/README.md",)),
    Example("case-cybersecurity", "Cybersecurity attack path", "case study", "graph_model_examples.case_studies.cybersecurity:demo", "Attack path reachability with rule-style derivation.", "Case studies", ("case_studies/cybersecurity-attack-path/README.md",)),
    Example("case-policy", "Policy entitlements", "case study", "graph_model_examples.case_studies.policy:demo", "Policy facts and derived access decisions.", "Case studies", ("case_studies/policy-entitlements/README.md",)),
    Example("case-product-kg", "Product KG", "case study", "graph_model_examples.case_studies.product_kg:demo", "Compatibility and product metadata across RDF and LPG projections.", "Case studies", ("case_studies/product-kg/README.md",)),
    Example("api-layer", "GraphQL API layer", "query/API", "graph_model_examples.api_layer.app:demo", "GraphQL schema and resolver-style backend over canonical fixtures.", "GraphQL service layer", ("examples/api-layer/README.md",)),
    Example("gotchas", "Gotchas labs", "gotchas", "graph_model_examples.gotchas.demo:demo", "Runnable demonstrations of modeling anti-patterns and tooling limits.", "Gotchas", ("examples/gotchas/README.md",)),
    Example("decision-framework", "Decision framework", "decision framework", "graph_model_examples.decision_framework.demo:demo", "Model-selection checklist and ranked recommendations.", "Decision framework", ("examples/decision-framework/README.md",)),
)


def get_example(slug: str) -> Example | None:
    return next((example for example in EXAMPLES if example.slug == slug), None)


def major_model_families() -> set[str]:
    return {example.model_family for example in EXAMPLES}
