from __future__ import annotations

from pathlib import Path

MARKERS = ["TO" + "DO", "FIX" + "ME", "pass  # place" + "holder", "lorem" + " ipsum", "coming" + " soon", "not" + " implemented"]
SKIP_DIRS = {".git", ".venv", "__pycache__", ".pytest_cache", "dist", "build"}
TEXT_SUFFIXES = {".py", ".md", ".ttl", ".trig", ".rq", ".graphql", ".json", ".jsonl", ".yaml", ".yml", ".txt", ".cypher", ".tql", ".dl", ".facts", ".sql", ".mmd", ".toml"}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix in TEXT_SUFFIXES:
            yield path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures = []
    for path in iter_files(root):
        text = path.read_text(encoding="utf-8", errors="ignore")
        lower = text.lower()
        for marker in MARKERS:
            if marker.lower() in lower:
                failures.append(f"{path.relative_to(root)} contains marker {marker}")
    if failures:
        print("\n".join(failures))
        return 1
    print("No unfinished markers found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
