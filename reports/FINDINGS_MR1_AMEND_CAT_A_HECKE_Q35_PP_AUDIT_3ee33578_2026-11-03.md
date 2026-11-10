# Soft SF FINDINGS AMEND — MR1 Cat A Hecke/ℚ(√35) absorb PP-AUDIT 3ee33578… — 2026-11-03
Write-only → Auditor. REPORTS ONLY; No RECS; No CERT. tip_touched NO.
Amends: FINDINGS_MR1_CAT_A_HECKE_Q35_RESIDUAL_C_CITE_HUNT_2026-11-03.md sha `6eb9713e03e01a2feef3c0797f1dc97ddd8a4d2097dd7af245eef048ce506b13`
PP Soft SF audit: PP-AUDIT `3ee33578…` (Professor Proof).

## Live-checks this AMEND
| Claim | Live result |
|---|---|
| LMFDB HMF search `https://www.lmfdb.org/ModularForm/GL2/TotallyReal/?field_label=2.2.140.1` | HTTP 200; title “Hilbert modular form search results”; **Results (1–50 of 137 matches)** for field 2.2.140.1. Prior FINDINGS X4 URL was wrong form → corrected. |
| LMFDB NumberField `https://www.lmfdb.org/NumberField/2.2.140.1` | HTTP 200; ℚ(√35); Discriminant 140; **Class number 2**. |
| arXiv:1608.00392 Aribam | MATCH — Chandrakant Aribam, “Noncommutative Iwasawa theory arising from Hecke algebras”. |
| arXiv:1710.05324 Bergdall–Hansen | MATCH — John Bergdall, David Hansen, “On p-adic L-functions for Hilbert modular forms”. |

## Absorb by item
1. **Item1 FLAG → AMEND:** Field-specific Hilbert modular forms over ℚ(√35) are **PRESENT in LMFDB data** (137 HMF weight [2,2] search hits at the corrected URL). Soft-literature framework remains PARTIAL (L1–L3). Class number 2 is live-checked and matters for T_𝔭 at non-principal primes (PP note absorbed). Rank for “standard references / Hecke setup”: still **PARTIAL** for textbook/arXiv exposition specific to this field; **PRESENT** for LMFDB enumerated forms over 2.2.140.1.
2. **Item2 CONFIRM:** stands PRESENT (unchanged).
3. **Item3 FLAG wording → AMEND:** The asked object T_p·exp(Θ) / T_p+εΘ remains **ABSENT**. Named standard (different) deformation objects now live-checked and listed as PARTIAL framework only — not the asked form: Hida families (standard name); Aribam arXiv:1608.00392; Bergdall–Hansen arXiv:1710.05324. These do **not** upgrade Item3 to PRESENT for T_p·exp(Θ)/T_p+εΘ.
4. **Item4 CONFIRM:** stands PARTIAL framework / ABSENT as-asked (unchanged).
5. **Zwegers note:** thesis Utrecht 2002; arXiv:0807.4834 remains MATCH (absorbed).
6. **Decoy / BOR:** 0712.0574 exclusion and BOR arXiv:0802.0963 correct (PP CONFIRM; unchanged).

## Counts after AMEND
PRESENT: Item2; LMFDB ℚ(√35) HMF enumeration (under Item1 data).
PARTIAL: Item1 textbook/arXiv setup; Item4; Item3 nearest named deformations (Hida/Aribam/Bergdall–Hansen) as different objects.
ABSENT: Item3 as asked (T_p·exp(Θ) / T_p+εΘ); Item4 as-asked project C.
GAP: transfer element C / Bridge Series C / residual_slash / V₃₅ unchanged.

tip Soft-SF LOCK tip_pre `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` tip_touched NO. No invent into Cat A. No CERT. No RECS.
