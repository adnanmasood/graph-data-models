PYTHON ?= python3
export PYTHONPATH := $(PWD)/src

.PHONY: setup test smoke validate-rdf demo-rdf demo-lpg demo-hyperrel demo-hypergraph demo-datalog demo-eav demo-graphrag format

setup:
	$(PYTHON) -m pip install -e ".[dev]"

test:
	$(PYTHON) -m pytest

smoke:
	$(PYTHON) -m graph_model_examples run alice-acme-all

validate-rdf:
	$(PYTHON) -m graph_model_examples run rdf-validation

demo-rdf:
	$(PYTHON) -m graph_model_examples run rdf

demo-lpg:
	$(PYTHON) -m graph_model_examples run lpg

demo-hyperrel:
	$(PYTHON) -m graph_model_examples run hyperrel

demo-hypergraph:
	$(PYTHON) -m graph_model_examples run hypergraph

demo-datalog:
	$(PYTHON) -m graph_model_examples run datalog

demo-eav:
	$(PYTHON) -m graph_model_examples run eav

demo-graphrag:
	$(PYTHON) -m graph_model_examples run graphrag

format:
	$(PYTHON) -m compileall -q src tests
