## AWS pricing comparisons

AWS pricing changes often. This page is for **decision-making**, not exact billing.

**All examples below assume**:

- Region: **`us-east-1`** style pricing
- Pricing model: **On-Demand** (no Savings Plans / RIs)
- Month: **730 hours**
- You’ll still have extra costs (tax, support, backups, etc.)

## The real cost model

| Category | What you pay for | Surprise cost drivers |
| --- | --- | --- |
| Compute | vCPU + RAM over time | idle capacity, overprovisioning |
| Networking | LBs + NAT + data transfer | **NAT Gateway**, cross-AZ traffic, egress |
| Data | DB + storage + IOPS | Multi-AZ, read replicas, backups |
| Observability | logs + metrics + traces | **log volume**, retention |
| Delivery | CDN/cache | cache misses, dynamic content |

## Unit prices used in examples

These are common reference numbers people use for back-of-the-napkin estimates:

| Item | Price |
| --- | --- |
| EC2 `t4g.small` | ~$0.0168 / hour |
| ALB | ~$0.0225 / hour + ~$0.008 / LCU-hour |
| NAT Gateway | ~$0.045 / hour + ~$0.045 / GB processed |
| Fargate | ~$0.04048 / vCPU-hour + ~$0.004445 / GB-hour |
| Lambda | $0.20 / 1M requests + ~$0.0000166667 / GB-second |
| API Gateway HTTP API | ~$1.00 / 1M requests |
| API Gateway REST API | ~$3.50 / 1M requests |
| CloudWatch Logs ingest | ~$0.50 / GB ingested |
| CloudFront (US) | ~$0.09 / GB egress (first ~10TB) |

## Traffic profiles

| Profile | Requests / second | Requests / month | Notes |
| --- | --- | --- | --- |
| Small | 10 RPS | 26M | small API / startup |
| Medium | 100 RPS | 262M | real product traffic |
| Bursty | avg 10, peak 200 | ~26M | spiky workloads (cron/events) |

## Compute: EC2+ASG+ALB vs ECS vs Beanstalk vs serverless

### What you’re comparing

This section compares how you run the app, not the DB.

| Option | What it is | What you pay for | When it’s a good default |
| --- | --- | --- | --- |
| EC2 + ASG + ALB | classic VMs | EC2 hours + ALB + ops | steady traffic, simple stack |
| ECS (EC2) | containers on your nodes | EC2 hours + some ops | teams want containers, cost-sensitive |
| ECS (Fargate) | serverless containers | vCPU+RAM time | small team, spiky-ish traffic |
| EKS | Kubernetes | control plane + nodes + ops | you **need** k8s ecosystem |
| Elastic Beanstalk | managed-ish platform | still EC2 + ALB + RDS | fastest PaaS-like path on AWS |
| Lambda + API GW | serverless functions | per-request + duration | very spiky, event-driven, low ops |
| App Runner | managed containers | vCPU+RAM (platform) | Heroku-like experience |

### Example A: steady 100 RPS API (always on)

Assume your app needs ~**2 vCPU and 4 GB RAM** continuously.

| Option | Rough monthly compute cost | What’s included / missing |
| --- | --- | --- |
| EC2 (2× `t4g.small`) | \(2 \times 0.0168 \times 730 \approx\) **$24.5/mo** | compute only (no ALB, no NAT) |
| Fargate (2 vCPU, 4 GB) | \(2 \times 0.04048 \times 730\) + \(4 \times 0.004445 \times 730\) \(\approx\) **$72/mo** | compute only |
| Lambda | can be cheap or very expensive | depends on duration + memory + concurrency |

Takeaway:

- **If you run hot 24/7**, EC2/ECS-on-EC2 often wins on raw compute $.
- Fargate wins when **ops simplicity** is worth the premium.

### Example B: bursty workloads (avg 10 RPS, peak 200)

If you provision for peaks on EC2, you pay for idle.

| Option | Typical outcome |
| --- | --- |
| EC2/ASG | you’ll overprovision unless scale-in is aggressive |
| Fargate | you pay closer to used if you scale tasks by demand |
| Lambda | best fit if work is short-lived and parallel |

## Load balancing: ALB vs API Gateway vs CloudFront

| Front door | Pricing shape | Good for | Common mistake |
| --- | --- | --- | --- |
| ALB | hourly + LCU | container/EC2 apps, path routing | ignoring LCU (bytes/conn) |
| API Gateway | per-request | serverless + simple APIs | REST API costs at high RPS |
| CloudFront | per-GB egress | static + cacheable dynamic | not caching enough |

Rule of thumb:

- **High RPS + small payload**: ALB can be cheaper than API Gateway.
- **Low/medium RPS + spiky + auth features**: API Gateway (HTTP API) is fine.

## Networking: NAT Gateway is the silent killer

If you put private subnets behind NAT, you pay **hourly + per GB processed**.

| Item | Typical monthly base |
| --- | --- |
| 1× NAT Gateway hourly | \(0.045 \times 730 \approx\) **$32.9/mo** |
| 100 GB processed | \(100 \times 0.045 =\) **$4.5/mo** |
| 1 TB processed | \(1024 \times 0.045 \approx\) **$46/mo** |

How to reduce NAT pain:

- Use **VPC endpoints** (S3/DynamoDB/etc.)
- Keep traffic inside VPC where possible
- Cache and batch external calls

## Databases: RDS vs Aurora vs DynamoDB (cost shape)

| DB | Pricing shape | Good for | Cost pitfall |
| --- | --- | --- | --- |
| RDS | instance-hours + storage + I/O | most apps | Multi-AZ doubles compute |
| Aurora | higher $/hr, elastic storage | high throughput | you pay for nice defaults |
| DynamoDB | request-based + storage | key/value + scale | wrong access pattern = $$$ |

## Storage: S3 vs EBS vs EFS (cost shape)

| Storage | Pay for | When it’s right |
| --- | --- | --- |
| S3 | GB-month + requests + egress | objects, static/media, backups |
| EBS | provisioned GB + IOPS (if provisioned) | EC2 disks |
| EFS | GB-month + throughput | shared POSIX filesystem |

## Observability: logs can cost more than compute

| Source | Why it explodes | Fix |
| --- | --- | --- |
| CloudWatch Logs | chatty apps + debug logs | sampling, levels, retention |
| ALB access logs | high RPS | sample, shorten retention |
| VPC Flow Logs | very noisy | enable selectively |

## Decision cheatsheet

| You care most about… | Start with… |
| --- | --- |
| lowest steady-state compute cost | **EC2 + ASG + ALB** or **ECS on EC2** |
| fastest deploys + standardization | **ECS**  |
| lowest ops burden | **Fargate** or **Beanstalk** |
| extreme spikiness / event workloads | **Lambda + HTTP API** |
| global latency | **CloudFront** first, then multi-region |