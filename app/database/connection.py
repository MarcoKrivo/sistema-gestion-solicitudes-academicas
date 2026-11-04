import sqlite3
from pathlib import Path

DB_NAME = Path(__file__).resolve().parents[2] / "solicitudes.db"


def conectar():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn