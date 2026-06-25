from __future__ import annotations

from pathlib import Path

from pyshacl import validate

from graph_model_examples.common.fixtures import project_root
from graph_model_examples.common.printing import simple_table

from .inference import has_inferred_claim_type


def validate_instance(instance_name: str) -> tuple[bool, str]:
    root = project_root() / "examples" / "rdf" / "ontology"
    conforms, _, report = validate(
        data_graph=str(root / instance_name),
        shacl_graph=str(root / "shapes.ttl"),
        ont_graph=str(root / "ontology.ttl"),
        inference="rdfs",
        abort_on_first=False,
    )
    return bool(conforms), str(report)


def demo() -> str:
    rows = []
    for name in ["valid_instance.ttl", "invalid_missing_source.ttl", "invalid_bad_confidence.ttl"]:
        conforms, _ = validate_instance(name)
        rows.append([name, str(conforms)])
    rows.append(["controlled subclass inference", str(has_inferred_claim_type())])
    return simple_table(["RDF validation check", "result"], rows)
