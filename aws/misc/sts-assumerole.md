## STS + AssumeRole

STS issues **temporary credentials**.

The common flow:

1. Principal in Account A calls `AssumeRole` on a role in Account B
2. Role’s **trust policy** allows that principal
3. STS returns short-lived creds
4. You use those creds to access resources in Account B, limited by role policies

## Two policies matter

| Policy | Answers |
| --- | --- |
| Trust policy | who can assume this role? |
| Permissions policy | what can the role do after assumed? |

## When to use

- Cross-account deployments, CI/CD
- Central security/logging accounts
- Third-party integrations with tight permissions

## Common trade-offs

- Forgetting `ExternalId` for third-party access patterns.
- Overly broad trust policies like `Principal: "*"` without conditions.

