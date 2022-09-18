from __future__ import annotations
import uuid
from dataclasses import dataclass, field
from datetime import date, datetime

from .base import BaseDataModel
from .playerset import PlayerSet
from smapi.const import MatchingProblem, MailSendMode


@dataclass(frozen=True)
class Matching(BaseDataModel):
    problem: MatchingProblem
    name: str
    created_by: str  # author's user_id
    expire_at: date
    randomize: bool
    mail_send_mode: MailSendMode
    voters: PlayerSet
    candidates: PlayerSet = None
    subjects: PlayerSet = None
    input_subjects_by_candidates: bool = False
    matching_id: str = field(init=False)
    created_at: datetime = datetime.now()
    published: bool = False
    published_at: date = None

    def __post_init__(self):
        object.__setattr__(self, "matching_id", uuid.uuid4().hex)

    def to_dict(self) -> dict[str, str]:
        return dict(
            matching_id=self.matching_id,
            problem=int(self.problem),
            name=self.name,
            created_by=self.created_by,
            created_at=self.created_at.isoformat(),
            published=self.published,
            published_at=self.published_at.isoformat() if self.published_at else None,
            expire_at=self.expire_at.isoformat(),
            randomize=self.randomize,
            mail_send_mode=int(self.mail_send_mode),
            voters=self.voters.to_dict(),
            candidates=self.candidates.to_dict() if self.candidates else None,
            subjects=self.subjects.to_dict() if self.subjects else None,
            input_subjects_by_candidates=self.input_subjects_by_candidates,
        )

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> Matching:
        assert "matching_id" not in data, "matching_id should not be in data"
        m = Matching(
            problem=MatchingProblem(data["problem"]),
            name=data["name"],
            created_by=data["created_by"],
            expire_at=datetime.fromisoformat(data["expire_at"]).date(),
            randomize=data["randomize"],
            mail_send_mode=MailSendMode(data["mail_send_mode"]),
            voters=data["voters"],  # if isinstance(data["voters"], PlayerSet) else PlayerSet.from_dict(data["voters"]),
            candidates=data["candidates"] if "candidates" in data else None,
            subjects=data["subjects"] if "subjects" in data else None,
            input_subjects_by_candidates=data["input_subjects_by_candidates"]
            if "input_subjects_by_candidates" in data
            else False,
            created_at=datetime.fromisoformat(data["created_at"]) if "created_at" in data else datetime.now(),
            published=data["published"] if "published" in data else False,
            published_at=datetime.fromisoformat(data["published_at"]).date() if "published_at" in data else None,
        )
        return m
