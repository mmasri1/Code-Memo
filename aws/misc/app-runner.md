## App Runner

App Runner is a managed way to run a web service from:

- a container image in ECR
- or source code, builds for you

Think PaaS for containers.

## When to use it

- Small team, you want **fast deploys** and **low ops**
- Simple HTTP services
- You don’t need deep VPC/network customizations

## When not to

- You need complex networking like private subnets, NLB patterns, and advanced routing
- You want maximum cost control at high steady utilization

## Cost model

- You pay for **compute**, vCPU and RAM, while the service runs
- You may also pay for build and traffic-related costs

Rule of thumb:

- App Runner can be worth it for speed, but may not be the cheapest for always-on high load.