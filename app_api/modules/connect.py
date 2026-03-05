import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DB_URL = os.getenv("DB_URL", "sqlite:///./app.db")  # SQLite по умолчанию
engine = create_engine(DB_URL, connect_args={"check_same_thread": False}, echo=True)

if "PYTEST_CURRENT_TEST" in os.environ:
    DB_URL = "sqlite:///:memory:"

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Get DB."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
