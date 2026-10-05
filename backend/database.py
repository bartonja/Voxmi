"""
Database connection setup

This model creates a connection to the PostgreSQL database and
provides a reusable database session dependency for API routes
"""

from sqlmodel import Session, SQLModel, create_engine
from collections.abc import Generator
from app.core.config import settings

engine = create_engine(
    settings.postgres_url,
    echo=True,
)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session