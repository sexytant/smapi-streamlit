from __future__ import annotations

import uuid
from typing import Dict, List
from dataclasses import dataclass, field

from .base import BaseDataModel
from .choice import Choice


@dataclass(frozen=True)
class PlayerSet(BaseDataModel):
    has_capacity: bool
    is_ranked: bool
    name: str
    choices: List[Choice]
    playerset_id: str = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, "playerset_id", uuid.uuid4().hex)

    def to_dict(self) -> Dict[str, str]:
        return dict(
            playerset_id=self.playerset_id,
            has_capacity=self.has_capacity,
            is_ranked=self.is_ranked,
            name=self.name,
            choices=[c.to_dict() for c in self.choices],
        )

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> PlayerSet:
        assert "playerset_id" not in data, "playerset_id should not be in data"
        ps = PlayerSet(
            has_capacity=data["has_capacity"],
            is_ranked=data["is_ranked"],
            name=data["name"],
            choices=[Choice.from_dict(choice) for choice in data["choices"]],
        )
        return ps
