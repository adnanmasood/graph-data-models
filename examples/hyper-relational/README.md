# Hyper-relational Statements

Run with `make demo-hyperrel`.

This model follows a Wikidata-style pattern: a statement has a main claim, qualifiers, references, rank, confidence, and verification metadata.

Elegant: qualifiers and references are first-class and conflicting/deprecated claims can coexist. Awkward: applications must decide rank semantics and export mappings. Easy query: preferred CEO statement. Hard query: flattening to a binary edge without losing qualifiers.
