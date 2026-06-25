from __future__ import annotations

from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF, XSD

from .store import load_statements

EX = Namespace("http://example.org/kg/")


def export_statements_to_rdf() -> Graph:
    graph = Graph()
    for statement in load_statements():
        node = EX[statement.id]
        graph.add((node, RDF.type, EX.HyperRelationalStatement))
        graph.add((node, EX.subject, EX[statement.subject]))
        graph.add((node, EX.property, Literal(statement.property)))
        graph.add((node, EX.value, EX[statement.value]))
        graph.add((node, EX.rank, Literal(statement.rank)))
        graph.add((node, EX.confidence, Literal(statement.confidence, datatype=XSD.decimal)))
    return graph
