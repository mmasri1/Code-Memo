## Auto Scaling basics

Auto Scaling is about scaling **capacity units** based on metrics.

## What you can autoscale

- **EC2**, ASG: number of instances
- **ECS services**: number of tasks
- **Lambda**: scales automatically, you mainly manage concurrency limits
- **DynamoDB**: read and write capacity, or on-demand

## The 3 knobs

| Knob | Meaning |
| --- | --- |
| Desired | target capacity right now |
| Min | never go below this |
| Max | never exceed this |

## Scaling policies

- **Target tracking**: keep CPU at 50%
- **Step scaling**: if queue depth > X, add N
- **Scheduled**: predictable daily patterns

## Trade-offs

- **Scale out is faster than scale in**, especially for cold starts.
- CPU-only policies miss the real bottleneck, DB, queue, external APIs.
- If you’re behind an ALB, scale on **request count** or **latency** can be better than CPU.