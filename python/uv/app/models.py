"""Domain models written against the Pydantic v1 API.

The whole point of this demo is that every Pydantic-v1 idiom used here changes
in Pydantic v2 (which FastAPI >=0.100 pulls in), so an upgrade breaks the code.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_validator


class UserIn(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

    # v2: @field_validator replaces v1 @validator (now requires @classmethod).
    @field_validator("email")
    @classmethod
    def email_must_contain_at(cls, v: str) -> str:
        if "@" not in v:
            raise ValueError("invalid email")
        return v.lower()

    # v2: `always=` removed; validator is a no-op on the None default, so
    # behaviour is unchanged without it.
    @field_validator("age")
    @classmethod
    def age_non_negative(cls, v: Optional[int]) -> Optional[int]:
        if v is not None and v < 0:
            raise ValueError("age must be >= 0")
        return v


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

    # v2: `class Config` + `orm_mode` becomes `model_config` + `from_attributes`.
    model_config = ConfigDict(from_attributes=True)


def serialize_user(user: UserOut) -> dict:
    # v2: .dict() -> .model_dump().
    return user.model_dump()


def serialize_user_json(user: UserOut) -> str:
    # v2: .json() -> .model_dump_json().
    return user.model_dump_json()
