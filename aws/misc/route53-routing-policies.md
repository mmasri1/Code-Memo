## Route 53 routing policies

Route 53 routing policy decides **which DNS answer** to return.

## Common policies

| Policy | What it does | Use for |
| --- | --- | --- |
| Simple | single record | basic setups |
| Weighted | split traffic by % | A/B, gradual migrations |
| Latency-based | lowest latency region | multi-region apps |
| Failover | primary/secondary | DR, active-passive |
| Geolocation / Geoproximity | based on user location | compliance / regional routing |
| Multi-value | returns multiple healthy records | simple load spreading |

## Health checks

- Route 53 can health-check endpoints and avoid unhealthy targets, depending on policy.

## Common trade-offs

- DNS caching, TTL, slows instant failover.
- Confusing DNS-level routing with load balancer behavior.

