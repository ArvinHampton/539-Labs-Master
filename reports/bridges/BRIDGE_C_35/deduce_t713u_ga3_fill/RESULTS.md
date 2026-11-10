# deduce_t713u_ga3_fill — RESULTS
PREREG 49bd0b24fa2bd488a25d93293b47ec02d114b8c1d77d3bf7973234a8119e425b (hashed before this file and before the table; unchanged). Authority t712s4471 (G-A3 compute, class C); t713s4484 (ψ); t713s4497 (defaults P1–P7). Schema filled: 8d247feb… (unaltered). Supersedes BLOCKED t712u (PREREG 25341d71… / RESULTS 333fa5bc… / SUMS 565d4270…) on Auditor CONFIRM.

## RG-F0 Input gate — PASS
All ingredients located Written/ACCEPT-sourced: Θ_{3/2}(·;a)=Σ(n+a)q^{(n+a)²} (552541cf L24); outer_even=35m²+7m (m≥1), outer_odd=35m²+42m+49/4 (m≥0) as q^{outer} with unit coeff (e60cad9b L16–22; 1bab65c4 L16–18); ψ (1be7f7d1…, fastkappa 70f605a4…); path/branch P2/P3; N=106 P5; leading factor 1 P7. n≥0 forced (full-ℤ sum ≡0). Ledger Ξ 7dbd63af… not used.

## RG-F1 Filled table — FILLED (NOT Cat A)
author_candidates/AUTHOR_CANDIDATE_GA3_h_table_FILLED_N106_2026-10-25.md sha 4da09dec14b6881583bfd685e1c44eb3563bd649f25d05e6f8e91cd618e49d39. Regenerated Ξ data/Xi_regen_N106.tsv sha 35b186f9df70c2bf247432edcef946e5f66f0ddf1bbca2f4454a30b210707197.

| x | W₇x | ψ(x) | h(x) | h(W₇x) | slash | δ(x) | abs δ | tol |
|---|---|---|---|---|---|---|---|---|
| 1/7 | −1 | 5.65e-5−1.102e-3i | 1.57057−0.14738i | −2.20756−2.21730i | 19.80118 | 45.2829+43.7577i | 62.970 | 1.1e-2 |
| 3/7 | −1/3 | 1.108e-3−8.997e-3i | −1.27840+1.42842i | 2.90364−0.65617i | 1.82483 | −6.5771+2.6258i | 7.082 | 1.7e-3 |
| 5/7 | −1/5 | 3.549e-3−2.209e-2i | −0.40749+1.12166i | −0.62523+0.27618i | 9.24175 | 5.3707−1.4307i | 5.558 | 1.1e-3 |
| 1 | −1/7 | 6.884e-3−3.826e-2i | −2.26167−2.27141i | −0.14574+1.57205i | 20.90222 | 0.7846−35.1307i | 35.139 | 6.3e-3 |

Sensitivity: V-P (partials 43/58/67, c=1): abs δ = 57.25, 7.32, 7.40, 32.44. N=150: abs δ = 64.80, 7.52, 14.34, 31.88. Quadrature check 2.0e-9. Note: ψ contributes ≤4e-2 in magnitude; h is dominated by the Ξ_N integral.

## RG-F2 Force criteria
- F1: FAIL (abs δ ≫ tol at all 4 points; robust under V-P and N=150).
- F2: δ≡0 NOT forced (samples never force; here samples actively show δ≠0 under these conventions).
- F3: PASS (nonzero defect recorded) — but NOT "controlled": δ is O(10) and N_trunc-sensitive (Ξ series non-convergent on ℝ), so obstruction is refined only as "δ≠0 at samples under locked P1–P7 conventions, N=106".
- Soft: Written 78:6 and partials 43/58/67 not reproduced by product form; ψ is an S-cocycle used under W₇ by ACCEPT (t713s4484); slash coeffs 4-decimal.

Verdict: G-A3 FILLED (class C, NOT Cat A) | F1 FAIL / F2 not forced / F3 PASS (uncontrolled defect) | Bridge PARTIAL | READY NO | residual-C OPEN. Bridge YES / δ≡0 / residual-C newly forced: NO/NO/NO. No order78.
