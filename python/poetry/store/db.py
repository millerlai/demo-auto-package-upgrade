"""Data layer written against the SQLAlchemy 1.4 API.

Every idiom below changes in SQLAlchemy 2.0:
- `declarative_base` import path moved.
- `engine.execute(<raw string>)` was removed (no implicit autocommit / autobegin).
- `session.query(Model).get(pk)` is legacy; replaced by `session.get(Model, pk)`.
"""
from sqlalchemy import Column, Integer, String, create_engine

# 1.4: import path. In 2.0 this is `from sqlalchemy.orm import declarative_base`.
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)


def make_engine(url: str = "sqlite:///:memory:"):
    return create_engine(url)


def init_db(engine):
    Base.metadata.create_all(engine)


def make_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()


def ping(engine) -> int:
    # 1.4: implicit execution of a raw string on the Engine.
    # Removed in 2.0 -> must use `connection.execute(text("SELECT 1"))`.
    result = engine.execute("SELECT 1")
    return result.scalar()


def get_user(session, user_id: int):
    # 1.4 legacy Query.get(). 2.0 -> session.get(User, user_id).
    return session.query(User).get(user_id)


def add_user(session, name: str, email: str) -> User:
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    return user
