import sqlite3
from pathlib import Path

DATA_DIR = Path("Data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

DB_Path = DATA_DIR / "intelligence_platform.db"

def connect_database(db_path=DB_Path):
    """
    connect to the SQLite database.
    Creates the DB file if it doesn't exist.
    """
    return sqlite3.connect(str(db_path))