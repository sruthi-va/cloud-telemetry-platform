import streamlit as st
import sqlite3
import pandas as pd

DB_PATH = "data/processed.db"

def query_db(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

st.title("Cloud Telemetry Analytics Dashboard")

st.subheader("Build Success Rate")

df = query_db("""
SELECT
    COUNT(*) AS total,
    SUM(CASE WHEN status='success' THEN 1 ELSE 0 END) AS success,
    ROUND(1.0 * SUM(CASE WHEN status='success' THEN 1 ELSE 0 END)/COUNT(*),3) AS rate
FROM telemetry
WHERE event_type='build'
""")

st.dataframe(df)

st.subheader("Service Latency")

lat = query_db("""
SELECT service, AVG(latency_ms) AS avg_latency
FROM telemetry
GROUP BY service
""")

st.bar_chart(lat.set_index("service"))