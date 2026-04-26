## ALB vs NLB vs GWLB

Pick the load balancer based on **protocol** and **features**.

## Quick comparison

| LB | Layer | Best for | Features |
| --- | --- | --- | --- |
| **ALB** | L7, HTTP and HTTPS | web apps, APIs | path and host routing, auth integrations |
| **NLB** | L4, TCP UDP TLS | low latency, non-HTTP | static IPs, huge throughput |
| **GWLB** | L3 and L4, appliance | security appliances | traffic inspection and firewalls |

## Rules of thumb

- If it’s HTTP: start with **ALB**.
- If you need raw TCP/UDP or static IP: use **NLB**.
- If you’re inserting network appliances: **GWLB**.

## Cost trade-offs

- ALB costs include LCU, bytes, connections, and rules.
- NLB can be cheaper for some patterns but lacks L7 routing features.

