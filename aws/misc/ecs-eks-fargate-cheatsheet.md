## ECS vs EKS vs Fargate

This is about running **containers**.

## The fast decision

- **ECS on EC2**: best default if you want containers and care about cost/control.
- **ECS on Fargate**: best default if you care about speed/ops simplicity.
- **EKS**: pick when you truly need Kubernetes, ecosystem, portability, org standards.

## Comparison table

| Option | You manage | You pay for | Pros | Cons |
| --- | --- | --- | --- | --- |
| ECS on EC2 | nodes + capacity | EC2 + EBS + ALB/NLB | cheaper at steady load | patching, AMIs, cluster ops |
| ECS Fargate | almost nothing | vCPU+RAM time plus extras | simplest ops | can be pricey at 24/7 high utilization |
| EKS | Kubernetes + nodes | control plane + nodes | k8s ecosystem | complexity tax, time and money |

## Cost trade-offs

- EKS has a **control plane** cost even if idle.
- Fargate can be surprisingly expensive for always-on services that run hot.
- Networking + NAT + logs can dominate container compute.