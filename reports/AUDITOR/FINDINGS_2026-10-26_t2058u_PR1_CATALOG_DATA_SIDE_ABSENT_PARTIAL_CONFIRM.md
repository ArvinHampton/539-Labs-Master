# Auditor Soft SF CONFIRM — PR1 catalog data-side ABSENT/PARTIAL leaves (Pack E) — 2026-10-26 ~20:59 CDT
Auditor · Soft SF CONFIRM · Write-only · Packaging only · No invented values · No RECS · No NL Rule-5 review written

## Tip Soft SF LOCK
Start `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` MATCH · End MATCH · tip_touched NO · Kerr BLOCKED

## Hash table (claimed vs live)
| Doc | Claimed | Live |
|---|---|---|
| FINDINGS PR1-FINDINGS-CATALOG_DATA_SIDE_ABSENT_PARTIAL_LEAVES_2026-10-26.md | 1476fe3ed111a9c742c9aad538c8c04ab4dff4e40c13506cb270ddc527639e3b | MATCH |
| PRESS SOFTSF_PRESS_PR1_CATALOG_DATA_SIDE_ABSENT_PARTIAL_LEAVES_2026-10-26.md | 4e3256c8a31f0cba1505906d94b63e8d0a004ed3e337e964deb877db8b707eac | MATCH |
| Catalog /workspace/obs-data-PR1-HEPP-QM-GR.md (read-only) | 6c680789ff64a7bb1a83276690e20a1748d8d2a31f19a97b869c13109b77f33d | MATCH |
| DV (exclusion set) | a86a8b22… | MATCH |

## Stamps recorded as written (23)
- ABSENT 10: S1, S2, S3, S5, S6, S7, S8, S15, S19, S21
- PARTIAL 13: S4 (UNPROVEN-GAP), S9, S10, S11, S12, S13, S14, S16, S17, S18, S20, S22, S23
- Count check: 10 + 13 = 23 ✔; the by-section breakdown 1+5+4+2+5+0+6 = 23 ✔. Values invented: 0.

## Spot-checks (catalog live)
- L57 S9: the k₀₀⁽⁵⁾ bound with 90% CL is Written; the other coefficients are not transcribed → PARTIAL, consistent. ✔
- L61 S11: brightness ratio given as "~10:1" with no unc → PARTIAL, consistent. ✔
- L164 S4: observed anomaly given as "≈ 43″/cy" → PARTIAL, consistent. ✔
- Kerr exclusion: L63 and L70–71/L73 (ISCO, a∗, efficiency) are not stamped. ✔

## Soft SF flags
- SF1 (packaging, non-substantive): FINDINGS §2 lists "L70–73" as the excluded Kerr range, but S12 is stamped at L72. Read live, L72 is the EHT M87* 2017 polarimetry line and does not mention Kerr itself; it sits inside the ISCO block's line range. The stamp is recorded as written; the exclusion-range wording is internally inconsistent. The NL/PR1 owner can tighten the range (e.g. L70–71, L73). No change is made here.
- SF2 (packaging): FINDINGS and PRESS already say "Soft SF CONFIRM CLEARED" before this CONFIRM. Pre-emptive wording only.
- Substantive flags: 0.

## Verdict
**CONFIRM — MATCH-with-SF (SF1, SF2).** 23 stamps (10 ABSENT / 13 PARTIAL) recorded as written. Kerr excluded and BLOCKED. tip_touched NO. No RECS. Next is the NL Rule-5 REVIEW (not written by the Auditor).
