# FINDINGS — Owner lookup $70 Premium tokens (call-a0858383) — LOOKUP ONLY, NO PURCHASE

**When:** ~12:25–12:26 CDT 2026-10-27 America/Chicago  
**Source:** grok.com/dashboard/billing + usage (signed-in Premium); x.ai/pricing; docs.x.ai extra-usage / prepaid-balance / developers pricing

## Result
1. **Token count for $70:** ABSENT on product UI. $70 is prepaid dollar credit, not a fixed token allotment.
2. **Buy credits presets (verbatim):** `$5`, `$20`, `$50`, `$100` plus custom `$` field (so $70 is enterable). Nearest listed packs: $50 and $100.
3. **Per-token rate on dashboard:** ABSENT. Extra usage burns prepaid credit at per-model API list rates (see docs.x.ai/developers/pricing). Example short-context grok-4.7: $2.00 / 1M input, $0.50 / 1M cached, $6.00 / 1M output.
4. **Stack vs replace:** STACKS after weekly Premium included pool. Verbatim dashboard: "Included usage with your subscription. Used before your credits." Credits do NOT replace the weekly pool and do NOT enlarge the % usage bar. Credits expire after two years.
5. **Live account (read-only):** Premium · Weekly included usage **66% used** · Resets Nov 3 · Credits available $0.00 · Monthly additional usage limit Not set.

tip Soft SF LOCK 7cddb188… tip_touched NO; Kerr BLOCKED. No purchase / no Auto Top-up / no billing change.
