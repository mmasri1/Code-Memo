## Burstable instances, T family, and CPU credits for t3 and t4g

T instances are burstable and run on **shared CPU**.

- You get a **baseline** CPU level continuously.
- You can **burst** above baseline by spending **CPU credits**.
- If you run hot for long, you either **throttle** in Standard mode or **pay extra** in Unlimited mode.

Good for: dev, small APIs, mostly idle servers, background workers with spikes.  
Bad for: steady high CPU services like encoding, heavy compute, and sustained load.

## Mental model

- **Credits** are like CPU battery.
- Idle time charges the battery.
- Bursting drains it.

If your workload is steady, the battery never recharges → you either throttle or pay.

## Standard vs Unlimited

| Mode | What happens when credits run out | When to use |
| --- | --- | --- |
| **Standard** | CPU is throttled down to baseline | predictable bills, dev, non-critical |
| **Unlimited** | you can keep bursting, **but pay for surplus credits** | short periods of sustained CPU where throttling is worse |

Pricing gotcha:

- Unlimited can look cheap… until you run **high CPU for hours**.

## What to monitor so you don’t get surprised

On EC2 / CloudWatch:

- **`CPUCreditBalance`**: your battery level
- **`CPUCreditUsage`**: how fast you drain it
- **`CPUSurplusCreditBalance` / `CPUSurplusCreditsCharged`**: Unlimited mode, shows extra billed credits

Rule of thumb:

- If `CPUCreditBalance` trends to **0** during normal operation, you chose the wrong instance class.

## Common patterns

### Pattern A: small API

- Mostly idle
- occasional spikes
- low p95 CPU

T instances are usually great here.

### Pattern B: worker that runs 24/7 at 70–90% CPU

- Credits drain
- You either throttle or pay extra in Unlimited mode

Move to `m*`/`c*`, or scale out.

## Cost notes

T instances are cheap **because** you’re buying shared CPU.

- For sustained CPU, a more expensive `m*`/`c*` can be **cheaper overall** than Unlimited surplus credits.