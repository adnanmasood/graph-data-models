from __future__ import annotations

import sqlite3

from graph_model_examples.common.fixtures import project_root


def connect_seeded() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    base = project_root() / "examples" / "eav-network" / "sql"
    for script in ["00_schema.sql", "01_seed_alice_acme.sql"]:
        conn.executescript((base / script).read_text(encoding="utf-8"))
    return conn
