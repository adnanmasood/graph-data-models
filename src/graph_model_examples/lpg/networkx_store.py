from __future__ import annotations

import networkx as nx

from graph_model_examples.common.fixtures import canonical_names, load_canonical_claim


def build_edge_property_graph() -> nx.MultiDiGraph:
    claim = load_canonical_claim()
    names = canonical_names()
    graph = nx.MultiDiGraph()
    for node_id, name in names.items():
        graph.add_node(node_id, name=name)
    graph.add_edge(
        claim.subject_id,
        claim.employer_id,
        key=claim.id,
        label="CEO_OF",
        role=claim.role_id,
        start_date=claim.interval.start_date.isoformat(),
        end_date=claim.interval.end_date.isoformat(),
        source=claim.references[0].document_id,
        verified_by=claim.verification.verifier_id,
        confidence=claim.confidence,
        appointed_by=claim.qualifier_entity("appointed_by"),
        location=claim.qualifier_entity("location"),
    )
    return graph


def build_event_node_graph() -> nx.MultiDiGraph:
    claim = load_canonical_claim()
    graph = build_edge_property_graph()
    graph.add_node(claim.id, label="EmploymentClaim", confidence=claim.confidence)
    graph.add_edge(claim.subject_id, claim.id, label="EMPLOYEE_IN")
    graph.add_edge(claim.id, claim.employer_id, label="EMPLOYER")
    graph.add_edge(claim.id, claim.role_id, label="ROLE")
    graph.add_edge(claim.id, claim.references[0].document_id, label="SOURCE")
    graph.add_edge(claim.id, claim.verification.verifier_id, label="VERIFIED_BY")
    return graph
