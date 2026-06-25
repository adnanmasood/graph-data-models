from __future__ import annotations

from pathlib import Path
import re

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    missing = []
    for path in (root / "docs").rglob("*.md"):
        for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#")):
                continue
            candidate = (path.parent / target).resolve()
            if not candidate.exists():
                missing.append(f"{path.relative_to(root)} -> {target}")
    if missing:
        print("\n".join(missing))
        return 1
    print("Documentation links checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
