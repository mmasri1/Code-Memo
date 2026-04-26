## S3 storage classes

S3 storage class is basically how cheap is storage vs how painful is retrieval.

## Common classes

| Class | Best for | Tradeoff |
| --- | --- | --- |
| Standard | hot objects | higher $/GB |
| Intelligent-Tiering | unknown access patterns | monitoring fee, but avoids guessing |
| Standard-IA | infrequent access | retrieval fees + min storage duration |
| One Zone-IA | cheaper IA | no multi-AZ resilience |
| Glacier Instant / Flexible / Deep Archive | archive | slower retrieval + fees |

## Rules of thumb

- Default: **Standard** or **Intelligent-Tiering**.
- If you can re-create the data: consider **One Zone-IA**.
- If you won’t touch it for months: Glacier tiers.

## Common trade-offs

- Moving to IA/Glacier without understanding retrieval patterns → surprise bills.
- Forgetting minimum storage duration charges for some classes.

