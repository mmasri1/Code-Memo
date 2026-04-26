## IAM users vs roles vs policies

IAM is who can do what on which resources.

## The objects

| Thing | What it is | Use it for |
| --- | --- | --- |
| **Policy** | JSON permissions document | attach to identities/resources |
| **User** | long-lived identity | humans, rarely recommended now |
| **Role** | assumed identity, temporary creds | EC2, ECS, Lambda, cross-account |
| **Group** | collection of users | legacy convenience |

## Best practice defaults

- Use **roles** for workloads like EC2, ECS, and Lambda.
- Use **IAM Identity Center**, SSO, for humans instead of IAM users.
- Grant least privilege; use managed policies cautiously.

## Common trade-offs

- Giving `AdministratorAccess` to everything temporarily.
- Confusing **role trust policy**, who can assume, vs **permissions policy**, what it can do.

