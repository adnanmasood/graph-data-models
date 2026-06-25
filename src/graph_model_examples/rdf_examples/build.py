from __future__ import annotations

from rdflib import Dataset, Graph, Literal, Namespace
from rdflib.namespace import RDF, XSD

from graph_model_examples.common.fixtures import canonical_names, load_canonical_claim

EX = Namespace("http://example.org/kg/")


def _add_entities(graph: Graph) -> None:
    for entity_id, name in canonical_names().items():
        graph.add((EX[entity_id], EX.name, Literal(name)))


def build_plain_lossy_graph() -> Graph:
    graph = Graph()
    _add_entities(graph)
    graph.add((EX.alice, EX.ceoOf, EX.acme))
    graph.add((EX.alice, EX.positionHeld, EX.ceo))
    return graph


def build_nary_graph() -> Graph:
    claim = load_canonical_claim()
    graph = Graph()
    _add_entities(graph)
    node = EX[claim.id]
    graph.add((node, RDF.type, EX.EmploymentRole))
    graph.add((node, EX.employee, EX[claim.subject_id]))
    graph.add((node, EX.employer, EX[claim.employer_id]))
    graph.add((node, EX.role, EX[claim.role_id]))
    graph.add((node, EX.startDate, Literal(claim.interval.start_date.isoformat(), datatype=XSD.date)))
    graph.add((node, EX.endDate, Literal(claim.interval.end_date.isoformat(), datatype=XSD.date)))
    graph.add((node, EX.source, EX[claim.references[0].document_id]))
    graph.add((node, EX.verifiedBy, EX[claim.verification.verifier_id]))
    graph.add((node, EX.verifiedOn, Literal(claim.verification.verified_on.isoformat(), datatype=XSD.date)))
    graph.add((node, EX.confidence, Literal(claim.confidence, datatype=XSD.decimal)))
    graph.add((node, EX.appointedBy, EX[claim.qualifier_entity("appointed_by")]))
    graph.add((node, EX.location, EX[claim.qualifier_entity("location")]))
    return graph


def build_named_graph_dataset() -> Dataset:
    dataset = Dataset()
    claim_graph = dataset.graph(EX.claimGraph)
    metadata_graph = dataset.graph(EX.provenanceGraph)
    nary = build_nary_graph()
    for triple in nary:
        claim_graph.add(triple)
    node = EX[load_canonical_claim().id]
    metadata_graph.add((node, EX.source, EX["acme-2020-annual-report"]))
    metadata_graph.add((node, EX.verifiedBy, EX.bob))
    return dataset


def build_reification_graph() -> Graph:
    claim = load_canonical_claim()
    graph = build_plain_lossy_graph()
    statement = EX[claim.id + "-reified"]
    graph.add((statement, RDF.type, RDF.Statement))
    graph.add((statement, RDF.subject, EX.alice))
    graph.add((statement, RDF.predicate, EX.ceoOf))
    graph.add((statement, RDF.object, EX.acme))
    graph.add((statement, EX.source, EX[claim.references[0].document_id]))
    graph.add((statement, EX.confidence, Literal(claim.confidence, datatype=XSD.decimal)))
    return graph
