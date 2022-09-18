from __future__ import annotations

import uuid
from typing import Dict, List
from dataclasses import dataclass, field
from .base import BaseDataModel


@dataclass(frozen=True)
class Choice(BaseDataModel):
    name: str
    capacity: int = 1
    choice_id: str = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, "choice_id", uuid.uuid4().hex)

    def to_dict(self) -> Dict[str, str]:
        return dict(
            choice_id=self.choice_id,
            name=self.name,
            capacity=self.capacity,
        )

    @classmethod
    def from_lines(cls, choice_txt: str) -> List[Choice]:
        choices = []
        if not choice_txt:
            return choices
        for line in choice_txt.splitlines():
            if line.count(",") == 1:
                name, capacity = line.split(",")
                choices += [Choice(name, capacity=int(capacity))]
            elif line.count(",") == 0 and line:
                name = line
                choices += [Choice(name)]
            else:
                continue
        return choices

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> Choice:
        assert "choice_id" not in data, "choice_id should not be in data"
        c = Choice(
            name=data["name"],
            capacity=data["capacity"],
        )
        return c
