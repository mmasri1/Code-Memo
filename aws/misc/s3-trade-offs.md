## S3 consistency + common trade-offs

S3 is simple, but the trade-offs are usually around security, naming, and access patterns.

## Common trade-offs

- **Public access**:
  - Block Public Access can override bucket policy expectations, good but surprising.
- **Bucket policies vs IAM**:
  - you often need both to allow an action, and any explicit deny wins.
- **Static website hosting**:
  - uses the website endpoint, different behavior than REST endpoint.
- **Too many small objects**:
  - request costs + listing patterns matter at scale.
- **Egress**:
  - S3 → internet data transfer out can dominate costs.

## Rule of thumb

- Keep buckets private, use CloudFront for public delivery.
- Use lifecycle rules early, delete and transition.

