## EC2 pricing models

EC2 cost is mostly **instance-hours** × rate, but the rate depends on the purchase model.

## Options

| Model | Discount | Tradeoff | Best for |
| --- | --- | --- | --- |
| **On-Demand** | none | simplest | new workloads, unknown usage |
| **Reserved Instances** | big | commitment to family and region | stable baseline, legacy setups |
| **Savings Plans** | big | commitment to **$ / hour** spend | stable baseline, modern default |
| **Spot** | huge | can be interrupted | stateless workers, batch, queues |

## What I usually do

- **Start On-Demand**
- Once usage stabilizes: buy **Compute Savings Plan** for the baseline
- Add **Spot** where interruption is acceptable

## Spot

- Spot instances can be reclaimed with short notice, design for it.
- Use for:
  - queue workers
  - CI runners
  - batch jobs
  - horizontally-scaled stateless services with enough capacity buffer