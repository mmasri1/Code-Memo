## Secrets Manager vs SSM Parameter Store

Both store configuration values. The difference is usually rotation + pricing + UX.

## Comparison

| Feature | Secrets Manager | SSM Parameter Store |
| --- | --- | --- |
| Best for | passwords/api keys | config + some secrets |
| Rotation | built-in workflows | DIY |
| Encryption | KMS | KMS SecureString |
| Pricing | higher | usually cheaper |

## Rule of thumb

- If you need **rotation** and secret lifecycle: choose **Secrets Manager**.
- If you need lots of config values and some secrets: **SSM Parameter Store** is often enough.

## Common trade-offs

- Fetching secrets on every request, latency and cost. Cache them.
- Storing secrets in plain env vars in logs or CI output.

