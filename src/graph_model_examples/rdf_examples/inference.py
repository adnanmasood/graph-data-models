from __future__ import annotations

from pathlib import Path

from rdflib import Graph, URIRef
from rdflib.namespace import RDF, RDFS

from graph_model_examples.common.fixtures import project_root


def infer_subclass_types() -> Graph:
    root = project_root()
    graph = Graph()
    graph.parse(root / "examples" / "rdf" / "ontology" / "ontology.ttl")
    graph.parse(root / "examples" / "rdf" / "ontology" / "valid_instance.ttl")
    changed = True
    while changed:
        changed = False
        for instance, _, cls in list(graph.triples((None, RDF.type, None))):
            for _, _, parent in graph.triples((cls, RDFS.subClassOf, None)):
                triple = (instance, RDF.type, parent)
                if triple not in graph:
                    graph.add(triple)
                    changed = True
    return graph


def has_inferred_claim_type() -> bool:
    graph = infer_subclass_types()
    return (URIRef("http://example.org/kg/claim-alice-acme-ceo"), RDF.type, URIRef("http://example.org/kg/Claim")) in graph
