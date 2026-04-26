## RDS Multi-AZ vs read replicas

They solve different problems.

## What you get

| Feature | Multi-AZ | Read replica |
| --- | --- | --- |
| Goal | **high availability** | **scale reads** |
| Writes | on primary | replicas are read-only |
| Failover | automatic, managed | manual, promote replica |
| Latency | same region/AZ design | replication lag possible |
| Cost | ~2× compute+storage | pay per replica instance+storage |

## Rules of thumb

- If downtime hurts: **Multi-AZ** first.
- If reads are the bottleneck: add **read replicas**.
- Don’t expect replicas to fix writes.

## Common trade-offs

- Thinking replicas are HA, they can help but not the same as Multi-AZ.
- Ignoring replication lag when reading from replicas.

