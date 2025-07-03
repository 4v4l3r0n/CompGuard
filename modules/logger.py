# modules/logger.py

import sqlite3
import os
from datetime import datetime

class Logger:
    def __init__(self, db_path="logs/events.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                module TEXT,
                message TEXT
            )
        """)
        self.conn.commit()

    def log_event(self, module, message):
        timestamp = datetime.utcnow().isoformat()
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO events (timestamp, module, message) VALUES (?, ?, ?)",
                       (timestamp, module, message))
        self.conn.commit()

    def close(self):
        self.conn.close()
