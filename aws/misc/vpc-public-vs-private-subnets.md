## VPC: public vs private subnets

Public subnet does **not** mean open to the internet.

## Definition

- **Public subnet**: route table has a route to an **Internet Gateway**, IGW
- **Private subnet**: no route to IGW

## Inbound vs outbound

- Public subnet instances can be reachable from the internet **only if**:
  - they have a public IP / EIP
  - security group allows it
  - NACL allows it
- Private subnet instances can still reach the internet **outbound** via NAT.

## Cost trade-offs

- **NAT Gateway** adds a baseline monthly cost plus per-GB processed.