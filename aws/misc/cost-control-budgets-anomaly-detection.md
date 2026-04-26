## Cost control: AWS Budgets + Anomaly Detection

Cost control is part of production readiness.

## AWS Budgets

Use budgets to set alerts on:

- total monthly spend
- service-level spend, RDS, NAT, CloudWatch Logs
- account-level spend, prod vs dev

## Cost Anomaly Detection

Useful for:

- something suddenly got 10× more expensive
- unexpected egress or NAT usage
- log storms

## Practical defaults

- Budget for:
  - total account spend
  - NAT Gateway
  - CloudWatch Logs
  - data transfer
- Alert thresholds:
  - 50%, 80%, 100% of monthly budget

## Common trade-offs

- No tagging strategy → hard to attribute cost.
- Only looking at EC2 cost while NAT/logs dominate.

