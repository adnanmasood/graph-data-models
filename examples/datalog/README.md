# Datalog-style Reasoning

Run with `make demo-datalog`.

The engine is a small deterministic fixed-point evaluator for active employment, ownership chains, attack paths, data lineage, and policy entitlements. It separates source facts from derived facts by carrying lineage labels.

Elegant: recursive rules are compact and auditable. Awkward: unrestricted recursion needs iteration limits and clear predicates.
