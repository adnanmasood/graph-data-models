from pathlib import Path

from graph_model_examples.registry import EXAMPLES, major_model_families
from graph_model_examples.runner import list_examples_text, run_example

ROOT = Path(__file__).resolve().parents[1]


def test_every_registered_example_has_documentation():
    for example in EXAMPLES:
        assert any((ROOT / path).exists() for path in example.primary_files), example.slug


def test_runner_and_docs_cover_major_models():
    text = list_examples_text()
    for family in ["RDF", "LPG", "hyper-relational", "hypergraph", "Datalog", "Topic Maps", "EAV", "hybrid graph + vector"]:
        assert family in text or family in major_model_families()
    assert "Alice" in run_example("alice-acme-all")


def test_modeling_doc_and_mermaid_files():
    doc = (ROOT / "docs" / "modeling-same-example.md").read_text(encoding="utf-8")
    for text in ["RDF n-ary Turtle", "RDF named graph TriG", "RDF-star", "Cypher edge property", "LPG event-node", "Wikidata-style JSON", "Hypergraph JSON", "TypeQL-style", "Datalog facts", "EAV rows"]:
        assert text in doc
    for path in (ROOT / "docs" / "diagrams").glob("*.mmd"):
        assert path.read_text(encoding="utf-8").strip()
