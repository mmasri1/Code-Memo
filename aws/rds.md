## Amazon RDS

RDS is a **managed relational database** (Postgres/MySQL/MariaDB + others) where AWS runs the boring parts:

- backups + snapshots
- patching (you still choose windows/versions)
- monitoring hooks (CloudWatch)
- Multi-AZ failover (if enabled)

It’s often **more expensive than DB on EC2**, but usually worth it once downtime + ops time hurt.

## What you pay for

| Component | What it means | Common surprises |
| --- | --- | --- |
| **DB instance** | compute hours (vCPU/RAM) | Multi-AZ ~= **2×** compute |
| **Storage (GB-month)** | gp3/io1/io2 volume size | io* is pricey; gp3 often enough |
| **IO / IOPS** | depends on storage type | provisioned IOPS adds a line item |
| **Backups/snapshots** | stored backup GB-month | free up to DB size only for automated backups (rules vary) |
| **Data transfer** | mainly **egress** | cross-AZ / internet egress costs |

## A few anchor prices

Use these for quick math. Verify in the pricing calculator for production decisions.

| Item | Price (approx) |
| --- | --- |
| `db.t4g.micro` (Single-AZ) | ~$0.016 / hour (~$12 / mo) |
| `db.t4g.small` (Single-AZ) | ~$0.032 / hour (~$23 / mo) |
| **Multi-AZ** | roughly **doubles** compute + storage |
| gp3 storage | ~$0.115 / GB-month |
| io1/io2 storage | ~$0.125 / GB-month (+ provisioned IOPS) |
| Data transfer out (internet) | ~first 1 GB free, then ~**$0.09/GB** (tiered) |

## Worked example: small production Postgres

Assume:

- Engine: Postgres
- Instance: `db.t4g.small` (2 vCPU / 2 GB)
- Storage: 100 GB gp3
- Single-AZ (no HA)
- 100 GB/month internet egress

| Component | Rough monthly | Notes |
| --- | --- | --- |
| DB instance | \(0.032 \times 730 \approx\) **$23** | compute |
| Storage (100 GB gp3) | \(100 \times 0.115 =\) **$11.5** | storage |
| Data transfer out (100 GB) | \(\approx 100 \times 0.09 =\) **$9** | very rough |
| Total | **~$40–$60/mo** | before backups/IO extras |

## Worked example: same DB with Multi-AZ

Rule of thumb: Multi-AZ roughly **doubles** the big parts.

| Component | Rough monthly |
| --- | --- |
| DB instance (Multi-AZ) | **~$46** |
| Storage (Multi-AZ) | **~$23** |
| Total (very rough) | **~$70–$120/mo** |

## Quick comparison table (dev vs prod vs scaled)

| Setup | Typical choices | Typical monthly cost |
| --- | --- | --- |
| Dev | micro/small, Single-AZ, small storage | ~$20–$60 |
| Small prod | small/medium, gp3, backups, maybe Multi-AZ | ~$80–$250 |
| Scaling | replicas, Multi-AZ, bigger instances, more storage | $300–$1000+ |

## Why DB on EC2 is cheaper

Roughly:

| Option | What you pay | What you don’t get |
| --- | --- | --- |
| Postgres on EC2 | EC2 + EBS | managed backups, failover, easy scaling, patching |
| RDS | same infra + managed layer | you pay for **reliability + time** |

If the DB is important, you’ll re-build a lot of RDS features yourself on EC2.

## Operational features that change cost

### Multi-AZ

- **Purpose**: high availability + automatic failover
- **Cost**: roughly **2×** instance + storage
- **Default**: enable for production DBs where downtime hurts

### Read replicas

- **Purpose**: scale reads, reduce load on primary
- **Cost**: each replica is basically another DB instance (+ storage)
- **Gotcha**: replication lag is real; design for it

### Storage type choice (gp3 vs io1/io2)

- **Default**: start with **gp3**
- Use io1/io2 when you truly need consistent, high IOPS (and can pay for it)