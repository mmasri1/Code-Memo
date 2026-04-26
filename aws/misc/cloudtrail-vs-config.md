## CloudTrail vs Config

Both help with governance, but they answer different questions.

## CloudTrail

- Records **API calls**, who did what, when, and from where
- Useful for security investigations and audit trails

## AWS Config

- Records **resource configuration state** over time
- Answers what does this resource look like now vs last week?
- Enables compliance rules, for example S3 buckets must not be public

## Quick comparison

| Question | Use |
| --- | --- |
| Who changed this security group? | **CloudTrail** |
| Is this bucket currently public? | **Config** |
| Did this resource drift from baseline? | **Config** |

## Cost trade-offs

- Both can generate lots of data at scale; scope them intentionally.

