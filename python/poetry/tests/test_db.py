import pytest

from store.db import add_user, get_user, init_db, make_engine, make_session, ping


@pytest.fixture()
def session():
    engine = make_engine()
    init_db(engine)
    sess = make_session(engine)
    sess._engine = engine  # keep a handle for ping test
    yield sess
    sess.close()


def test_ping_raw_string():
    engine = make_engine()
    assert ping(engine) == 1


def test_add_and_get_user(session):
    created = add_user(session, "Ada", "ada@example.com")
    fetched = get_user(session, created.id)
    assert fetched is not None
    assert fetched.name == "Ada"
    assert fetched.email == "ada@example.com"


def test_get_missing_user(session):
    assert get_user(session, 999) is None
