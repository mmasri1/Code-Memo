## DLQs and retry strategy

Retries are not optional. DLQs prevent infinite retry loops.

## The simple model

- Message fails → retry with backoff
- If it keeps failing → send to **DLQ**
- DLQ is a **work queue for humans/tools** to inspect/replay

## Good defaults

- **Retry with jitter/backoff**
- **Cap max retries**
- Use **idempotency keys** for handlers so replay is safe

## Common trade-offs

- Infinite retries, cost and noise.
- No visibility timeout tuning, duplicates.
- Non-idempotent consumers, double charges and double emails.
