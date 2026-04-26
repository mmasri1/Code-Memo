## Blue/green vs rolling deploys

Deploy strategies are about risk vs speed.

## Rolling deploy

- Replace instances/tasks gradually
- Pros: simple, low extra capacity
- Cons: you run mixed versions; rollback can be slow

## Blue/green deploy

- Two environments: blue is current, green is new
- Switch traffic when green is healthy
- Pros: fast rollback, safer releases
- Cons: needs extra capacity during deploy

## AWS implementations

- ECS: CodeDeploy blue/green or rolling update
- EC2/ASG: CodeDeploy + ALB target groups
- Lambda: alias traffic shifting
