"""Database manager for MindScan – SQLite persistence."""
import sqlite3
import os

DB_NAME = "mindscan.db"
# Store DB in project root (parent of database/)
DB_PATH = os.path.join(os.path.dirname(__file__), "..", DB_NAME)


def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def init_db():
    """Create tables from schema if not present."""
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    with open(schema_path, "r") as f:
        sql = f.read()
    conn = get_connection()
    conn.executescript(sql)
    conn.commit()
    conn.close()


def insert_journal_entry(entry_text: str, sentiment_score: float, sentiment_label: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO journal_entries (entry_text, sentiment_score, sentiment_label)
           VALUES (?, ?, ?)""",
        (entry_text, sentiment_score, sentiment_label),
    )
    conn.commit()
    row_id = cur.lastrowid
    conn.close()
    return row_id


def get_recent_journal_entries(limit: int = 10):
    """Fetch recent entries for dashboard (optional use)."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """SELECT id, entry_text, sentiment_score, sentiment_label, created_at
           FROM journal_entries ORDER BY created_at DESC LIMIT ?""",
        (limit,),
    )
    rows = cur.fetchall()
    conn.close()
    return rows
