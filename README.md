# Cloud Telemetry Mining & Analytics Platform

An end-to-end data engineering pipeline that simulates and analyzes large-scale engineering telemetry events such as pull requests, CI/CD builds, deployments, and issue tracking activity.

The system demonstrates how modern engineering organizations collect, process, and analyze operational data to measure system reliability, developer productivity, and deployment performance.

---

## Overview

This project simulates a **real-world observability and engineering analytics platform** similar to systems used in production environments (Datadog-style telemetry + GitHub Insights).

It includes:

- Synthetic telemetry event generation
- ETL pipeline (ingestion + transformation)
- SQLite-based analytical warehouse
- SQL-driven metrics computation
- Interactive Streamlit dashboard

---

## Architecture

```

```
            ┌──────────────────────────────┐
            │   Synthetic Event Generator  │
            │ (GitHub, CI/CD, Issues, etc) │
            └──────────────┬───────────────┘
                           │
                           ▼
            ┌──────────────────────────────┐
            │     Raw JSON Event Store     │
            │       (raw_events.json)      │
            └──────────────┬───────────────┘
                           │
                           ▼
            ┌──────────────────────────────┐
            │       ETL Pipeline           │
            │  - Validation               │
            │  - Cleaning                 │
            │  - Normalization            │
            └──────────────┬───────────────┘
                           │
                           ▼
            ┌──────────────────────────────┐
            │   SQLite Analytical Store    │
            │      (processed.db)          │
            └──────────────┬───────────────┘
                           │
                           ▼
            ┌──────────────────────────────┐
            │   Analytics Layer (SQL/Py)   │
            │ - Build success rate         │
            │ - Latency metrics            │
            │ - Deployment frequency       │
            └──────────────┬───────────────┘
                           │
                           ▼
            ┌──────────────────────────────┐
            │   Streamlit Dashboard        │
            │   Visual insights layer      │
            └──────────────────────────────┘
```

````

---

## Key Features

### Event Simulation
Generates 1M+ realistic engineering telemetry events:
- Pull Requests
- Commits
- CI/CD Builds
- Deployments
- Issue tracking

---

### ETL Pipeline
- Schema validation
- Deduplication
- Time-series normalization
- Incremental ingestion support (extendable)

---

### Analytics Layer
Computes:
- Build success rate
- Deployment frequency per service
- System latency averages
- Failure trend analysis

---

### Dashboard
Interactive Streamlit dashboard showing:
- Engineering throughput
- Build reliability trends
- Service latency comparisons

---

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
````

---

### 2. Generate synthetic events

```bash
python etl/generator.py
```

---

### 3. Ingest data into SQLite

```bash
python etl/ingest.py
```

---

### 4. Run analytics

```bash
python analytics/metrics.py
```

---

### 5. Launch dashboard

```bash
streamlit run dashboard/app.py
```

---

## Example Metrics

* Build success rate
* Deployment frequency by service
* Average system latency
* Failure rate trends

---

## Future Improvements

* Kafka-based streaming ingestion
* AWS S3 + Athena warehouse
* Airflow orchestration
* Real-time anomaly detection
* FastAPI service layer
* Grafana dashboards

---