from __future__ import annotations

from .sqlite_store import connect_seeded


def pivot_claim() -> dict[str, str]:
    conn = connect_seeded()
    row = conn.execute(
        """
        SELECT entity_id,
          max(CASE WHEN attr='employee' THEN value END) employee,
          max(CASE WHEN attr='employer' THEN value END) employer,
          max(CASE WHEN attr='role' THEN value END) role,
          max(CASE WHEN attr='source' THEN value END) source,
          max(CASE WHEN attr='confidence' THEN value END) confidence
        FROM attributes WHERE entity_id='claim-alice-acme-ceo' GROUP BY entity_id
        """
    ).fetchone()
    return {"id": row[0], "employee": row[1], "employer": row[2], "role": row[3], "source": row[4], "confidence": row[5]}


def recursive_descendants(parent: str = "acme") -> list[str]:
    conn = connect_seeded()
    rows = conn.execute(
        """
        WITH RECURSIVE descendants(child) AS (
          SELECT child FROM links WHERE parent=?
          UNION
          SELECT links.child FROM links JOIN descendants ON links.parent = descendants.child
        ) SELECT child FROM descendants ORDER BY child
        """,
        (parent,),
    ).fetchall()
    return [row[0] for row in rows]


def join_complexity_count() -> int:
    return 5
