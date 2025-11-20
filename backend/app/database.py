# backend/app/database.py

from sqlmodel import SQLModel, create_engine, Session
from app.config import get_settings

settings = get_settings()

# -----------------------
# DATABASE ENGINE
# -----------------------
engine = create_engine(
    settings.DATABASE_URL,
    echo=True  # Set False in production
)


# -----------------------
# CREATE DB TABLES
# -----------------------
def init_db() -> None:
    """
    Creates all SQLModel tables in the database.
    Should be called from main.py during startup.
    """
    SQLModel.metadata.create_all(engine)


# -----------------------
# DB SESSION DEPENDENCY
# -----------------------
def get_session():
    """
    Provides a new database session for each request.
    FastAPI will automatically close it after request.
    """
    with Session(engine) as session:
        yield session
