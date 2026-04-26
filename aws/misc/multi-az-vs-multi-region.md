## Multi-AZ vs multi-region

These are different levels of resilience.

## Multi-AZ

- Same region, multiple availability zones
- Protects against: **AZ failures**
- Typical: ALB across AZs + RDS Multi-AZ

## Multi-region

- Two or more regions
- Protects against: **regional outages**
- Requires: DNS failover, data replication, DR runbooks

## Cost/complexity

| Option | Cost | Complexity |
| --- | --- | --- |
| Multi-AZ | medium | medium |
| Multi-region | high | high |

## Rule of thumb

- Start with Multi-AZ for production reliability.
- Go multi-region only when a regional outage is unacceptable to the business.

