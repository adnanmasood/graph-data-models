from __future__ import annotations

from pathlib import Path

from graph_model_examples.runner import run_example


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    out = root / "examples" / "expected_outputs"
    out.mkdir(parents=True, exist_ok=True)
    (out / "alice_acme_all.txt").write_text(run_example("alice-acme-all") + "\n", encoding="utf-8")
    (out / "decision_framework.txt").write_text(run_example("decision-framework") + "\n", encoding="utf-8")
    print("Rendered expected outputs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
