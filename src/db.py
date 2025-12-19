from sqlmodel import SQLModel, create_engine, Session
from pathlib import Path

DB_FILE = Path(__file__).parent.parent / "mergington.db"
DATABASE_URL = f"sqlite:///{DB_FILE}"

# SQLite specific: allow multithreaded access for FastAPI test client
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
