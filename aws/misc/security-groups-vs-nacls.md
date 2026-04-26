## Security groups vs NACLs

Both are network filters, but they behave differently.

## Key differences

| Feature | Security Group | NACL |
| --- | --- | --- |
| Applies to | ENI / instance | subnet |
| Stateful | **Yes**, return traffic allowed | **No**, must allow both directions |
| Rules | allow-only | allow + deny |
| Typical use | main firewall | coarse subnet guardrails |

## Rules of thumb

- Prefer **security groups** for most control.
- Use NACLs when you need **subnet-wide** deny rules or extra defense-in-depth.