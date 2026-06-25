from __future__ import annotations

from pydantic import BaseModel


class Requirements(BaseModel):
    needs_semantic_interoperability: bool = False
    needs_statement_metadata: bool = False
    needs_nary_relationships: bool = False
    needs_recursive_rules: bool = False
    needs_fast_traversal: bool = False
    needs_graph_rag: bool = False
