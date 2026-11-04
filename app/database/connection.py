import sqlite3

DB_NAME = "solicitudes.db"


def conectar():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn