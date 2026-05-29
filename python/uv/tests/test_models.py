import json
from datetime import datetime

import pytest
from pydantic import ValidationError

from app.models import UserIn, UserOut, serialize_user, serialize_user_json


def test_email_validator_normalizes():
    u = UserIn(name="Ada", email="ADA@Example.com")
    assert u.email == "ada@example.com"


def test_invalid_email_rejected():
    with pytest.raises(ValidationError):
        UserIn(name="x", email="not-an-email")


def test_negative_age_rejected():
    with pytest.raises(ValidationError):
        UserIn(name="x", email="x@y.z", age=-1)


def test_serialize_user_uses_dict():
    out = UserOut(id=1, name="Ada", email="a@b.c", created_at=datetime(2024, 1, 1))
    data = serialize_user(out)
    assert data["id"] == 1
    assert data["name"] == "Ada"


def test_serialize_user_json():
    out = UserOut(id=1, name="Ada", email="a@b.c", created_at=datetime(2024, 1, 1))
    # Parse instead of matching raw text: pydantic v2 emits compact JSON, so the
    # exact spacing differs from v1 but the serialized value is what matters.
    assert json.loads(serialize_user_json(out))["id"] == 1


def test_config_orm_mode_enabled():
    # v2 surfaces the (renamed) orm_mode via model_config["from_attributes"].
    assert UserOut.model_config["from_attributes"] is True
