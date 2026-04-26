## CloudFront basics

CloudFront is a CDN: it caches content closer to users to reduce latency and origin load.

## The 3 levers that matter

### Cache key

What makes two requests different for caching:

- path
- query string
- headers, be careful
- cookies, be careful

Small cache key = high hit rate. Huge cache key = expensive cache misses.

### TTLs

- short TTLs → fresher, more origin traffic
- long TTLs → cheaper/faster, but harder updates

### Invalidations

- Invalidation clears cached objects.
- Too many invalidations can cost and can hide bad TTL design.

## Cost model

- Mostly **data transfer out** + **requests**
- Cache misses also cost you at the **origin**, compute and DB

## Common trade-offs

- Caching personalized responses like cookies and authorization headers accidentally.
- Not compressing responses like gzip and brotli, paying more egress.