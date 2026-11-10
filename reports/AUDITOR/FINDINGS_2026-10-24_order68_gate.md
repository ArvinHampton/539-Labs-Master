# FINDINGS 2026-10-24 — order68 LOCKED + G1 gate (~22:33 CDT)
## Hashes
- order68 PREREG **fde25c25464b923f9fe188d2212b5350ff42d311e60e616580434ae68a5fb844** OK (PREREG.sha256 + SUMS).
- order68 RESULTS **1920905e49b178d702532d024e97e16163a5ca351f94b3bd6e9423da60645b85** OK (SUMS 4/4 with search.log + BROAD copy).
- order57/GATE_DECISIONS.md **640da80d794020eca6abf5f6e863cf1ebdbee1fa5171adeb311f57d86cd76570** OK vs GATE_DECISIONS.sha256 (rehash after order68 addendum). Prior Auditor ledger f9f32d26… superseded.

## PREREG ↔ RESULTS chain
- PREREG: G1 REJECT binds; FOUND → gate only, do not adopt / invent / prereg numeric Ξ; ABSENT → READY NO.
- RESULTS: exact tokens ABSENT; outer_even/odd FOUND-partial; **G1-REJECT-stands / NOT adopted**; READY NO; nothing invented; no numeric Ξ test. Chain **consistent**.

## Gate wording (order57 GATE_DECISIONS addendum)
- **G1 REJECT stands.** FOUND-partial does **not** reopen G1. Reason quote-only matches RESULTS (unit residual coeffs on exponents; Ξ Fourier selected/partial/truncated; outer_*_coeff tables ABSENT).
- Not adopted; no numeric Ξ; READY NO unchanged. Cites RESULTS sha 1920905e…. **Wording OK; invent-ban held; no PASS/FAIL flip.**

## No invent / no numeric Ξ
- order68/scripts/ empty of run artifacts; no result.json/numeric Ξ. RESULTS + GATE both say no numeric run. OK.

## Warnings
- **W-68-1 OPEN (unchanged):** RESULTS §(b) cites order67 sha **523ccb8d…** only; live **e10816a3…** not cited. Fix: RESULTS addendum.
- **W-68-2 NEW:** RESULTS:33 still says “gate item for Physicist/Arvin: decide whether FOUND-partial … changes G1 REJECT” — but GATE addendum already ruled **REJECT stands**. Stale open-question after lock. Fix: RESULTS addendum pointing to GATE_DECISIONS order68 addendum (sha 640da80d…).

## Tally
Blockers **0** / Warnings **2** (W-68-1, W-68-2) / Notes 0 new. Lock + G1 ruling verified. No PASS/FAIL altered.
