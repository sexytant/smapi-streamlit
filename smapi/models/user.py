from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .base import BaseDataModel


@dataclass(frozen=True)
class User(BaseDataModel):
    user_id: str
    name: str
    created_at: datetime
    email: str

    def to_dict(self) -> dict[str, str]:
        return dict(
            user_id=self.user_id,
            name=self.name,
            created_at=self.created_at.isoformat(),
            email=self.email,
        )

    @classmethod
    def from_user_info(cls, data: dict[str, str]) -> User:
        return User(
            user_id=data["sid"],
            name=data["name"],
            created_at=datetime.fromisoformat(data["updated_at"][:-1]),
            email=data["email"],
        )

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> User:
        created_at = datetime.fromisoformat(data["created_at"])
        return User(
            user_id=data["user_id"],
            name=data["name"],
            created_at=created_at.date(),
            email=data["email"],
        )
