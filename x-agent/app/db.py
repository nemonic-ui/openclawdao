import os
import sqlite3
from pathlib import Path


def init_db() -> None:
    """Initialize SQLite database using schema.sql."""
    db_path = os.getenv("DB_PATH", "./data/x_agent.db")
    schema_path = Path(__file__).with_name("schema.sql")

    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as conn:
        with schema_path.open("r", encoding="utf-8") as schema_file:
            conn.executescript(schema_file.read())
        conn.commit()
