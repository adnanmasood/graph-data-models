from __future__ import annotations


def simple_table(headers: list[str], rows: list[list[str]]) -> str:
    widths = [len(header) for header in headers]
    for row in rows:
        for index, cell in enumerate(row):
            widths[index] = max(widths[index], len(str(cell)))
    def fmt(row: list[str]) -> str:
        return " | ".join(str(cell).ljust(widths[index]) for index, cell in enumerate(row))
    line = "-+-".join("-" * width for width in widths)
    return "\n".join([fmt(headers), line, *(fmt(row) for row in rows)])
