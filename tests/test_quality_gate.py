import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_command(args):
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=True)


def test_quality_scripts_and_core_commands():
    assert (ROOT / "docker-compose.optional.yml").exists()
    run_command([sys.executable, "scripts/check_no_placeholders.py"])
    list_result = run_command([sys.executable, "-m", "graph_model_examples", "list-examples"])
    assert "decision-framework" in list_result.stdout
    smoke = run_command([sys.executable, "-m", "graph_model_examples", "run", "alice-acme-all"])
    assert "Acme 2020 Annual Report" in smoke.stdout


def test_readme_mentions_major_model_families():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for text in ["RDF", "labeled property graphs", "RDF-star", "hyper-relational", "hypergraphs", "Datalog", "Topic Maps", "EAV", "GraphRAG"]:
        assert text in readme
