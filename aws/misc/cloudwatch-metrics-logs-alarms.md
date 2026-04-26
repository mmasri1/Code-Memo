## CloudWatch: metrics vs logs vs alarms

CloudWatch is AWS’s default observability toolkit.

## The 3 primitives

| Thing | What it is | Example |
| --- | --- | --- |
| **Metrics** | time-series numbers | CPUUtilization, latency p95 |
| **Logs** | text/events | app logs, ALB access logs |
| **Alarms** | thresholds on metrics | 5xx > 1% for 5 min |

## Cost trade-offs

- Logs can get expensive fast: **ingest + storage + queries**.
- High-cardinality metrics, many dimensions, increase cost and complexity.

## Good defaults

- Alarm on user pain:
  - 5xx rate
  - latency
  - queue depth
  - DB connections / free storage
