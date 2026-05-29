"""Minimal FastAPI app wiring the v1-era models together."""
from datetime import datetime

from fastapi import FastAPI

from app.models import UserIn, UserOut, serialize_user

app = FastAPI(title="demo-uv")

_DB: dict[int, UserOut] = {}
_SEQ = {"id": 0}


@app.post("/users")
def create_user(payload: UserIn) -> dict:
    _SEQ["id"] += 1
    user = UserOut(
        id=_SEQ["id"],
        name=payload.name,
        email=payload.email,
        created_at=datetime(2024, 1, 1),
    )
    _DB[user.id] = user
    # serialize_user uses .dict() under the hood (v1 API).
    return serialize_user(user)
