import json
import sqlite3

DB_PATH = "data/processed.db"
RAW_PATH = "data/raw_events.json"


def create_table(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS telemetry (
        event_id INTEGER,
        event_type TEXT,
        timestamp TEXT,
        service TEXT,
        status TEXT,
        latency_ms INTEGER
    )
    """)
    conn.commit()


def ingest():
    conn = sqlite3.connect(DB_PATH)
    create_table(conn)

    with open(RAW_PATH, "r") as f:
        events = json.load(f)

    rows = [
        (
            e["event_id"],
            e["event_type"],
            e["timestamp"],
            e["service"],
            e["status"],
            e["latency_ms"]
        )
        for e in events
    ]

    conn.executemany("""
        INSERT INTO telemetry VALUES (?, ?, ?, ?, ?, ?)
    """, rows)

    conn.commit()
    conn.close()

    print(f"Ingested {len(rows)} records into SQLite DB")


if __name__ == "__main__":
    ingest()