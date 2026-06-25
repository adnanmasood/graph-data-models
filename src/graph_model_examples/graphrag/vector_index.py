from __future__ import annotations

import math
import re
from collections import Counter

TOKEN_RE = re.compile(r"[a-z0-9]+")


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


def cosine(a: Counter, b: Counter) -> float:
    dot = sum(a[token] * b[token] for token in set(a) & set(b))
    norm_a = math.sqrt(sum(value * value for value in a.values()))
    norm_b = math.sqrt(sum(value * value for value in b.values()))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def top_documents(query: str, documents: list[dict], k: int = 2) -> list[dict]:
    qvec = Counter(tokenize(query))
    scored = []
    for doc in documents:
        dvec = Counter(tokenize(doc["text"] + " " + doc.get("title", "")))
        scored.append((cosine(qvec, dvec), doc))
    return [doc for score, doc in sorted(scored, key=lambda item: item[0], reverse=True)[:k] if score > 0]
