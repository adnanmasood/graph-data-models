from __future__ import annotations

from .fixtures import load_competency_questions


def canonical_expected_answers() -> dict[str, str]:
    return {answer.id: answer.answer for answer in load_competency_questions()}
