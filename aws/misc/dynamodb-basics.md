## DynamoDB basics

DynamoDB is a managed NoSQL key-value/document store.

## Core ideas

- You design around **access patterns**.
- Data is distributed by **partition key**.
- Hot partitions = pain.

## Capacity modes

| Mode | Pricing shape | Best for |
| --- | --- | --- |
| Provisioned | you set RCU/WCU | predictable traffic |
| On-demand | pay per request | spiky/unknown traffic |

## Terms

- **RCU**: read capacity units
- **WCU**: write capacity units
- **GSI**: global secondary index, extra cost and extra writes

## Common trade-offs

- Using a low-cardinality partition key, hot partition.
- Adding many GSIs without understanding write amplification.
- Treating it like a cheaper RDS.
