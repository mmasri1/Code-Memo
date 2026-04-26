## NAT Gateway vs VPC endpoints

If your private subnets need to talk to AWS services, the default is often NAT.
That can be expensive.

## What they are

- **NAT Gateway**: outbound internet access for private subnets, general purpose
- **VPC Endpoint**:
  - **Gateway endpoint**: S3 and DynamoDB, routes privately without NAT
  - **Interface endpoint**: PrivateLink, private ENI to AWS service or SaaS

## Cost shape

| Option | Costs | Notes |
| --- | --- | --- |
| NAT Gateway | hourly + **per GB processed** | can dominate small bills |
| VPC Endpoint | per-endpoint hourly for interface endpoints + data | S3 and DynamoDB gateway endpoints are usually cheap wins |

## Rule of thumb

- If most outbound is to **S3/DynamoDB**: add endpoints and reduce NAT usage.
- If you need general outbound internet: NAT remains necessary.

## Common trade-offs

- Paying NAT for S3 traffic, logs, artifacts, backups.
- Forgetting cross-AZ traffic costs when endpoints/NAT are in one AZ pattern.
