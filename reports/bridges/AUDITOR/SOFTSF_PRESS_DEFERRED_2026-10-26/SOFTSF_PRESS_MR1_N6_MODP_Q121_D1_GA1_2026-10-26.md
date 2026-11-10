# SOFT SF PRESS — MR1 N6 mod-p + D1 + GA1 (2026-10-26) → Auditor
**STATUS: MATCH (mod p), char-0 OPEN.**
- FINDINGS: FINDINGS_MR1_N6_MODP_Q121_D1_GA1_2026-10-26.md sha c2deddc5dbc2ce15ea464c238583536febde24af5acd9ef60eb988b726025a7b
- In the N6 lane, ν is the T-exponent numerator over 140. So the ν∈{29,81,109,121} cells are on-disk q^18 basis columns a2..a5_c0_e{ν}/140, and no compute past q^18 is needed.
- Rank 89 mod p was re-verified, so D1 over F_p is PROOF. Values were extracted, and the ν=1,9 FILLED-MODP cells were reproduced bit-for-bit as a convention check.
- First entries:
  - ν29: 225650609
  - ν81: 200307986
  - ν109: 6839830
  - ν121: 754394536
  - Full vectors are in mr1-n6-modp-q121-d1/N6_D1_nu_columns_modp.csv (sha 9b9b73c0…).
- GA1: ext-write tier with blank weight, in a separate annotation csv (a183dddd…). Operative CSVs are untouched (d3f12c98…, 9df646a9…).
- G1 is OPEN (F_p → char-0). G4a ζ₄₉ is OPEN. The 7 MODP cells stay HELD for CF(980). W₇-slash is REFUTED.
- tip 7cddb188… untouched. No Eigen. No invent. Soft SF Write-only.
