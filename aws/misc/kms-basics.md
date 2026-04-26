## KMS basics

KMS manages encryption keys, also called CMKs or KMS keys, and performs cryptographic operations.

## Envelope encryption

- KMS encrypts a **data key**
- your service uses the data key to encrypt data, for example S3, EBS, RDS, and app data
- KMS stores and controls the master key; you don’t handle raw key material in most setups

## Two permission layers

| Layer | Controls |
| --- | --- |
| **Key policy** | who can use/admin the KMS key |
| **IAM policy** | who is allowed to call KMS APIs |

If either denies, access fails.

## Cost shape

- You pay per **KMS request**: Encrypt, Decrypt, GenerateDataKey
- High-throughput workloads can generate a surprising KMS bill if you decrypt on every request

## Common trade-offs

- Using KMS decrypt in hot path without caching/data-key reuse.
- Forgetting cross-account access must be allowed in the **key policy**.