from __future__ import annotations

import typer
from rich.console import Console

from .runner import UnknownExample, list_examples_text, run_example

app = typer.Typer(no_args_is_help=True)
console = Console()


@app.command("list-examples")
def list_examples() -> None:
    """List runnable examples."""
    console.print(list_examples_text(), soft_wrap=True)


@app.command()
def run(example_name: str) -> None:
    """Run an example by slug."""
    try:
        console.print(run_example(example_name), soft_wrap=True)
    except UnknownExample as exc:
        console.print(str(exc), soft_wrap=True)
        raise typer.Exit(1) from exc


@app.command()
def recommend(
    semantic: bool = typer.Option(False, "--semantic", help="Require semantic interoperability."),
    provenance: bool = typer.Option(False, "--provenance", help="Require statement provenance."),
    graphrag: bool = typer.Option(False, "--graphrag", help="Require source-aware retrieval."),
    traversal: bool = typer.Option(False, "--traversal", help="Require traversal or graph analytics."),
    recursive_rules: bool = typer.Option(False, "--recursive-rules", help="Require recursive rules."),
    nary: bool = typer.Option(False, "--nary", help="Require n-ary relationships."),
) -> None:
    """Rank graph model families for selected requirements."""
    from .decision_framework.recommender import Requirements, format_recommendations, recommend_models

    req = Requirements(
        needs_semantic_interoperability=semantic,
        needs_statement_metadata=provenance,
        needs_graph_rag=graphrag,
        needs_fast_traversal=traversal,
        needs_recursive_rules=recursive_rules,
        needs_nary_relationships=nary,
    )
    console.print(format_recommendations(recommend_models(req)), soft_wrap=True)
