from __future__ import annotations

from graph_model_examples.common.printing import simple_table


def demo() -> str:
    return simple_table(["biomedical KG", "value"], [['drug', 'compound-a'], ['target', 'gene-brca1'], ['evidence', 'curated publication']])
