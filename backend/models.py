from typing import Literal

from pydantic import BaseModel

class RelavancyDecission(BaseModel):
    is_relevant: bool
    reason: str


class SupersedingPaper(BaseModel):
    title: str
    url: str
    summary: str


class ClaimVerificationResult(BaseModel):
    is_superseded: bool
    verdict_summary: str
    superseding_papers: list[SupersedingPaper]