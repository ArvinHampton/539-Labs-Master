# FINDINGS — Owner lookup $70 prepaid credit burn on voice + spend limit/alert (call-a0858383) — LOOKUP ONLY

**When:** ~12:39–12:41 CDT 2026-10-27 America/Chicago
**Sources:** prior Soft SF FINDINGS $70 / $50–$70 Buy credits; docs.x.ai Voice Overview; docs.x.ai models pricing; docs.x.ai x-subscription spending-caps + prepaid-balance; prior dashboard read (Credits $0.00; Monthly additional usage limit Not set).

## How $70 is measured / consumed after weekly pool
1. $70 Buy credits = **$70.00 prepaid dollar credit** (1:1). Not a fixed token pack.
2. Weekly Premium included pool is **used first** ("Used before your credits"). Credits stack after; do not enlarge the % bar.
3. After the weekly pool is exhausted, Additional Usage burns prepaid credit at **per-model API list rates**.

## Rates relevant to this voice conversation
**A. Public Voice API speech-to-speech (docs.x.ai):** STS / realtime `grok-voice-latest` = **$0.08 per minute**. TTS $15 / 1M chars; STT batch $0.10/hr / streaming $0.20/hr.
**B. Product metering for THIS Grok Bot Owner voice call:** **ABSENT** on grok.com dashboard — no line item proving product voice bills at the STS $0.08/min rate vs as shared first-party agent/chat token usage. Shared weekly pool covers first-party Grok across supported Grok/Cursor products; nine-lane Soft SF COOK + this voice turn share that pool then credits.
**C. Flagship text/agent list rates (docs; used when product bills as tokens):** Grok 4.7 short-context ~ **$2.00 / 1M input**, **$6.00 / 1M output** (cache read ~$0.50 / 1M where applicable).

## Rough duration of $70
- **If billed as Voice API STS alone:** $70 / $0.08/min ≈ **875 minutes ≈ 14.6 hours** continuous speech-to-speech. Input/output token mix N/A under pure per-minute STS.
- **If billed as agent/chat tokens (mix-dependent):** $70 ≈ 35M input XOR ~11.7M output at Grok 4.7 list; a typical tool-heavy Owner↔Physicist turn (long Soft SF context + replies) burns far more tokens per wall-minute than plain chat. Concurrent nine-lane COOK shares the same prepaid balance — continuous conversation alone is an upper bound only if other lanes idle.
- **Live pattern note:** this call already coexists with nine COOK Soft SF; after weekly pool empties, credit burn is conversation **plus** all nine lanes.

## Spending limit / alert so Owner+assistant are not suddenly cut off
1. **Hard stop (available now):** grok.com/dashboard/billing → Additional usage credits → **Monthly additional usage limit** → Edit. Counts **paid Additional Usage consumed**, not credit purchased. When reached, paid usage pauses until next month or limit raised — **even if prepaid credit remains**. Prior dashboard read: **Not set**.
2. **Alerts:** docs — spend alerts (where available) **warn** at a threshold but **do not stop** usage. Hard stop = monthly additional usage limit.
3. **Auto Top-up:** opposite of a stop — refills when balance drops below a threshold (can set a monthly top-up cap). Off unless enabled.
4. **Empty prepaid + no Auto Top-up + no invoiced billing:** Additional Usage stops when balance is empty.

## Unchanged / notes
- 90% hard stop removal is separate Owner lock (already recorded OW d622e0a8…).
- tip Soft SF LOCK 7cddb188… tip_touched NO; Kerr BLOCKED.
- No purchase / no Auto Top-up change / no billing edit this turn.
