from __future__ import annotations

from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF, XSD

from .model import AnnotatedTriple, canonical_statement

EX = Namespace("http://example.org/kg/")


def lower_statement_to_nary(statement: AnnotatedTriple | None = None) -> Graph:
    statement = statement or canonical_statement()
    graph = Graph()
    claim = EX["claim-alice-acme-ceo"]
    graph.add((claim, RDF.type, EX.EmploymentRole))
    graph.add((claim, EX.employee, EX[statement.subject]))
    graph.add((claim, EX.employer, EX[statement.object_id]))
    graph.add((claim, EX.role, EX.ceo))
    graph.add((claim, EX.startDate, Literal(statement.start_date, datatype=XSD.date)))
    graph.add((claim, EX.endDate, Literal(statement.end_date, datatype=XSD.date)))
    graph.add((claim, EX.source, EX[statement.source]))
    graph.add((claim, EX.verifiedBy, EX[statement.verified_by]))
    graph.add((claim, EX.verifiedOn, Literal(statement.verified_on, datatype=XSD.date)))
    graph.add((claim, EX.confidence, Literal(statement.confidence, datatype=XSD.decimal)))
    return graph


def lowered_summary() -> dict[str, str | float]:
    statement = canonical_statement()
    return {"subject": statement.subject, "object": statement.object_id, "source": statement.source, "confidence": statement.confidence}
