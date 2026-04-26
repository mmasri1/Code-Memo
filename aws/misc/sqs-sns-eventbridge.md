## SQS vs SNS vs EventBridge

These are different messaging patterns.

## Quick comparison

| Service | Pattern | Best for |
| --- | --- | --- |
| **SQS** | queue, 1 consumer processes a message | async work, buffering, backpressure |
| **SNS** | pub/sub fan-out | notifications to many subscribers |
| **EventBridge** | event bus + rules | decoupled event routing across services/accounts |

## Rules of thumb

- Use **SQS** to do work later.
- Use **SNS** to tell many things something happened.
- Use **EventBridge** when you want routing rules, schema evolution, and multi-service eventing.

## Cost trade-offs

- Request-based pricing means high-throughput can add up.
- Retries + poison messages multiply costs if you don’t use DLQs.

