-- Build success rate
SELECT
    COUNT(*) AS total_builds,
    SUM(CASE WHEN status='success' THEN 1 ELSE 0 END) AS success_builds,
    ROUND(1.0 * SUM(CASE WHEN status='success' THEN 1 ELSE 0 END) / COUNT(*), 3) AS success_rate
FROM telemetry
WHERE event_type = 'build';


-- Deployment frequency by service
SELECT
    service,
    COUNT(*) AS deployments
FROM telemetry
WHERE event_type = 'deployment'
GROUP BY service
ORDER BY deployments DESC;


-- Average latency per service
SELECT
    service,
    AVG(latency_ms) AS avg_latency
FROM telemetry
GROUP BY service;