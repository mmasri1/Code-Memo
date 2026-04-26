## Elastic Beanstalk

Elastic Beanstalk, EB, is a platform wrapper that provisions AWS resources for you.

## What EB typically creates

- **EC2 instances** 
- **Auto Scaling Group**
- **Load balancer**
- **Security groups** + IAM roles
- **CloudWatch logs/metrics**

You still pay for those underlying resources. EB itself is not the expensive part.

## When it’s great

- You want a **Heroku-like** experience on AWS
- You don’t want to design infra yet
- You’re okay with AWS standard patterns

## When it hurts

- You need custom networking/security patterns
- You want full control over ALB rules, target groups, deployments, scaling

## Cost trade-offs

- EB environments often include an **ALB + multiple instances** → baseline cost floor.
- If you enable enhanced health/log streaming, logs volume can grow.