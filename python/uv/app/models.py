"""Domain models written against the Pydantic v1 API.

The whole point of this demo is that every Pydantic-v1 idiom used here changes
in Pydantic v2 (which FastAPI >=0.100 pulls in), so an upgrade breaks the code.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator


class UserIn(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

    # v1: @validator. In v2 this is removed in favour of @field_validator.
    @validator("email")
    def email_must_contain_at(cls, v: str) -> str:
        if "@" not in v:
            raise ValueError("invalid email")
        return v.lower()

    # v1: @validator(..., always=True). `always=` no longer exists in v2.
    @validator("age", always=True)
    def age_non_negative(cls, v: Optional[int]) -> Optional[int]:
        if v is not None and v < 0:
            raise ValueError("age must be >= 0")
        return v


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

    class Config:
        # v1 config. In v2 this becomes `model_config = ConfigDict(...)`
        # and `orm_mode` is renamed to `from_attributes`.
        orm_mode = True


def serialize_user(user: UserOut) -> dict:
    # v1: .dict(). Removed in v2 -> .model_dump().
    return user.dict()


def serialize_user_json(user: UserOut) -> str:
    # v1: .json(). Removed in v2 -> .model_dump_json().
    return user.json()
