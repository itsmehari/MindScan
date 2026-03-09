-- MindScan SQLite schema (prototype)
CREATE TABLE IF NOT EXISTS journal_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entry_text TEXT,
    sentiment_score REAL,
    sentiment_label TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
