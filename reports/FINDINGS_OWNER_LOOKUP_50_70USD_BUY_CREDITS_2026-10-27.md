# FINDINGS — Owner lookup $50 / $70 Buy credits conversion (call-a0858383) — LOOKUP ONLY, NO PURCHASE

**When:** ~12:28–12:29 CDT 2026-10-27 America/Chicago  
**URLs:** https://grok.com/dashboard/billing (Buy credits dialog); https://grok.com/dashboard/usage  
**Docs:** cursor.com/docs/models-and-pricing; docs.x.ai prepaid-balance / extra-usage

## Result
1. **Conversion on Buy credits UI:** ABSENT. Dialog shows dollar Amount only — no tokens, no credits-received count, no $/token rate preview for $50 or $70.
2. **What $50 / $70 purchases:** $50.00 / $70.00 of prepaid credit balance (1:1 dollar credit). Presets `$5` `$20` `$50` `$100` + custom Amount field (typed 70 accepted; typed 1,000,000 accepted with no cap error).
3. **Min / max:** No labeled min/max. Smallest preset `$5`. Custom accepted `1,000,000` with no error shown.
4. **Burn rate (docs, not dialog):** After weekly included pool. Cursor/Grok 4.7 standard (short): $2 / 1M input, $0.50 / 1M cache read, $6 / 1M output. Rough: $50 ≈ 25M input XOR ~8.3M output; $70 ≈ 35M input XOR ~11.7M output (mix-dependent).
5. **Stack:** Weekly pool used first ("Used before your credits"). Credits do not replace or enlarge the % bar. Credits expire after two years (dashboard).
6. **Live account (read-only):** Premium · Weekly **69% used** · Resets Nov 3 · Credits available $0.00 · Monthly additional usage limit Not set.

Screenshots (box): $50 select …/ff74b1bc….png; $70 typed …/81ea1936….png.

tip Soft SF LOCK 7cddb188… tip_touched NO; Kerr BLOCKED. No purchase / no Auto Top-up / no billing change.
