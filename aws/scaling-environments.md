## Scaling environments on AWS

- **Default**: stay simple as long as you can.
- **Always measure**: traffic, latency, error rate, and *cost per request*.

## Quick map

Traffic numbers are intentionally rough. Use them to reason, not to benchmark.

| Stage | Goal | Typical traffic | AWS building blocks | Cost profile | Trigger to move |
| --- | --- | --- | --- | --- | --- |
| 0 | Launch fast | 0–10 RPS | 1× EC2 + local app + DB (often same box) | Cheapest infra, most toil | Downtime / deploy pain |
| 1 | Basic HA | 10–200 RPS | ALB + Auto Scaling (EC2) + RDS | Higher baseline cost (always-on) | Too much ops / config drift |
| 2 | Standardize deploys | 50–500 RPS | Docker + ECS (EC2) or EKS + CI/CD | Pay for cluster nodes + control plane (EKS) | Stop managing servers |
| 3 | Reduce ops | 50–1000+ RPS (bursty) | ECS on Fargate or Lambda + API GW | Easy scaling, can cost more at steady high load | Cost becomes a problem |
| 4 | Team scaling | Depends | Split services + service discovery + IAM boundaries | More infra + observability spend | Teams block each other |
| 5 | Performance at scale | 200–10k+ RPS | CloudFront + ElastiCache + SQS + read replicas | Spend shifts to cache/CDN/data | Latency is business-critical |
| 6 | Global resilience | Global | Multi-region + Route 53 + DR + data replication | Most expensive + complex | Region outage unacceptable |

## Stage 0:  Just make it work

### Setup

- Single EC2 instance (monolith)
- DB on the same machine (or small RDS if you want backups/managed)

### What to optimize

- Put static assets on S3 later CloudFront
- Add basic monitoring (CloudWatch metrics + alarms)

### Cost notes

- **EC2**: lowest baseline cost, but you pay in **manual ops**
- If you can’t tolerate data loss, avoid DB on same instance

## Stage 1:  Stop the bleeding

### Upgrade

- **ALB** in front
- **Auto Scaling Group** (EC2)
- **RDS** (Multi-AZ if downtime hurts)

### What changes

- No more deploy and pray
- One instance can die without taking prod down

### Cost notes

- **ALB** hourly + LCU (traffic-dependent)
- **RDS** (Multi-AZ roughly doubles DB compute)
- You now have a **baseline** (always-on) cost floor

## Stage 2:  Standardize everything

### Upgrade → containers + repeatable deployments

- Containerize
- Pick one:
  - **ECS on EC2**: simpler + cheaper control plane
  - **EKS**: Kubernetes ecosystem, more moving parts

### Good defaults

- Start with **ECS** unless you *need* Kubernetes features/org-standard
- Keep 1–2 services until you feel real coupling pain

### Cost notes

- ECS: you mostly pay for **EC2 capacity**
- EKS: you pay for **control plane** + nodes + more ops overhead

## Stage 3:  Abstract infrastructure (serverless compute)

### Upgrade → stop managing nodes

- **ECS on Fargate** (containers without servers)
- Or **Lambda + API Gateway** (event-driven / spiky)

### When it wins

- Bursty traffic
- Small team, you want to move fast with less ops

### Cost notes

- Fargate/Lambda can be **more expensive** at steady high utilization than tuned EC2
- You trade control for speed: fewer knobs, simpler ops

## Stage 4:  Break the monolith (microservices, carefully)

Split only when you have **real team/org pressure**:

- independent deploys
- clear domain boundaries (Auth, Billing, Notifications)
- different scaling profiles

### Required upgrades

- Distributed tracing (OpenTelemetry → X-Ray/CloudWatch traces)
- Centralized logs + correlation IDs
- Contracts: versioned APIs/events

### Cost notes

- Infra grows (more ALBs, NAT, logs, metrics, queues, replicas)
- Observability spend can become a big line item

## Stage 5:  Optimize for scale (performance + cost)

### Add the usual big levers

- **CDN**: CloudFront (cache static + even some dynamic)
- **Caching**: ElastiCache (Redis) for hot reads / rate limits / sessions
- **Async work**: SQS + workers (ECS/Lambda) for slow tasks
- **DB scaling**: read replicas, indexing, partitioning choices

### Cost notes

- You spend more on **data transfer + cache + replicas**
- But you buy back compute/DB headroom and reduce p95 latency

## Stage 6:  Global + resilient (multi-region)

### Patterns

- **Active-passive**: cheaper, simpler DR
- **Active-active**: best availability, hardest correctness

### Required thinking

- Data replication model (eventual vs strong consistency)
- Failover automation + game days

## What actually drives cost (the knobs)

| Cost driver | What you see | Typical fix |
| --- | --- | --- |
| Always-on compute | High baseline monthly bill | Rightsize, autoscaling, Spot (where safe), schedule non-prod |
| NAT Gateway + data transfer | Why is networking so expensive? | Reduce cross-AZ/region chatter, prefer VPC endpoints, cache |
| ALB/CloudFront | Costs scale with traffic | Cache more, compress, reduce headers, optimize origins |
| RDS | CPU/storage/IO spikes | Indexing, query fixes, read replicas, scale storage/IO class |
| Logs/metrics/traces | Observability bill climbs | Sampling, retention policies, log levels, targeted dashboards |