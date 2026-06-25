from typer.testing import CliRunner

from graph_model_examples.cli import app


def test_package_imports():
    import graph_model_examples
    assert graph_model_examples.__version__ == "0.1.0"


def test_cli_list_examples():
    result = CliRunner().invoke(app, ["list-examples"])
    assert result.exit_code == 0
    assert "alice-acme-all" in result.output


def test_cli_run_alice_acme_all():
    result = CliRunner().invoke(app, ["run", "alice-acme-all"])
    assert result.exit_code == 0
    for text in ["Alice", "Acme", "RDF", "LPG", "hyper-relational", "hypergraph", "Datalog", "EAV"]:
        assert text in result.output
