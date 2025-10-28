import sqlite3
from pathlib import Path

class EventStore:
    def __init__(self, db_path="events.db"):
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS events (
          ts   TEXT DEFAULT (datetime('now')),
          rule_id TEXT,
          line TEXT
        )""")
        self.conn.commit()

    def record(self, rule_id: str, line: str):
        self.conn.execute("INSERT INTO events(rule_id, line) VALUES(?,?)", (rule_id, line))
        self.conn.commit()
