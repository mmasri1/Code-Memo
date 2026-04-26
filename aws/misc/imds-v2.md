## IMDSv2

IMDS = Instance Metadata Service at `169.254.169.254` for EC2 instance info and credentials.

IMDSv2 adds a **session token** and prevents some SSRF-style attacks.

## Why it matters

- If your app has SSRF, an attacker can try to hit metadata and steal credentials.
- IMDSv2 makes that harder by requiring a token obtained via PUT + hop limit controls.

## Best practice

- Require **IMDSv2 only**
- Set **hop limit = 1** unless you explicitly need otherwise
