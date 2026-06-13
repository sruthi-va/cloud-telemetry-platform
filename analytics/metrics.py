import sqlite3
import pandas as pd

DB_PATH = "data/processed.db"

def run_query(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


if __name__ == "__main__":

    build_query = """
    SELECT
        COUNT(*) AS total,
        SUM(CASE WHEN status='success' THEN 1 ELSE 0 END) AS success,
        ROUND(1.0 * SUM(CASE WHEN status='success' THEN 1 ELSE 0 END) / COUNT(*), 3) AS rate
    FROM telemetry
    WHERE event_type='build'
    """

    df = run_query(build_query)
    print("\nBuild Metrics:")
    print(df)

    latency_query = """
    SELECT service, AVG(latency_ms) AS avg_latency
    FROM telemetry
    GROUP BY service
    """

    print("\nLatency:")
    print(run_query(latency_query))
