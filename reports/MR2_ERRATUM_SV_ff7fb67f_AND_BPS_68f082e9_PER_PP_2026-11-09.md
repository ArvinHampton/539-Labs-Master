# MR2 erratum: scalars/vectors (ff7fb67f) per PP 3f1749e1, and BPS cross-check (1aa88a30 / erratum 68f082e9) per PP 5abd02c6
2026-11-09, written 21:35 CST (America/Chicago, box clock). Author: MR2. Text-only, additive. No existing file edited, no new computation. Nothing adopted. Junction **UNSOLVED**; count gap unchanged. No CERT, no Gemini, nothing sent, no agent messaged. Naming: resonant algebra. Authority: OW d5eaeef3, OW 8b26c786 (Group A = Aut⁺(48) × wall ℤ₂), OW t4436 (32881263…, "Let the math lead the pursuits on all open paths"; sidecar MATCH, Owner's words on line 3).

## Inputs (sha256 recomputed 21:29 CST; every one = its sidecar)
| role | file | sha256 |
|---|---|---|
| target A | MR2_MN2_KK_A_S4_SCALARS_VECTORS_COMPUTED_AUT48_2026-11-09.md | ff7fb67fb3bafc49ad7a8480a24b196bc800eb9c5e1b6908282547ee8311df50 |
| target A empty log | MR2_MN2_KK_A_S4_SCALARS_VECTORS_COMPUTED_AUT48_2026-11-09.log | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 (0 B) |
| target A real log | MR2_MN2_KK_A_S4_SCALARS_VECTORS_COMPUTED_AUT48_2026-11-09_RUN2.log | 82a3d9478376a1a5a941990b4aff3fbd96f1b00efd4d126c8b3113eea4902646 |
| status file | MR2_MN2_KK_A_SCALAR_VECTOR_STATUS_AND_ERRATA_2026-11-09.md | bd32b4e24e10c54cab1c22a7fb394522ae283ee05143990eff757bee8205da22 |
| PP audit A | FINDINGS_PP_AUDIT_MR2_SCALARS_VECTORS_ff7fb67f_2026-11-09_2045.md | 3f1749e18de6e25445cfc3bbce6394bac915a78b62980b75a9024c97b8167753 |
| target B | MR2_CROSSCHECK_NL_BPS_CALIBRATED_WALL_2026-11-09.md | 1aa88a305d0573d954e687fdb3c5bf50d44f0bb4d14fe1472f2a485e9c44a957 |
| target B erratum | MR2_ERRATUM_CROSSCHECK_NL_BPS_PER_PP_0a82cf18_2026-11-09.md | 68f082e9d8225e86f19b4f279aa892ac4601a3b6730fcdf6ccd7897601d6140c |
| PP confirm B | FINDINGS_PP_CONFIRM_MR2_ERRATUM_68f082e9_2026-11-09_2039.md | 5abd02c6a05aa92b4ef9b075638d0940b80160c345b0c41d5fba85065138d473 |
| NL E19 | NL_ERRATUM19_ACCEPT_PP_5f2de6f9_e12589a5_2026-11-09_2029.md | d3dd5a4c9f51d325e9adfda5427d8e8f27f5e9bd9ffa240900d777bc885c18d5 |
| NL E20 | NL_ERRATUM20_ACCEPT_PP_8c57e68b_0a82cf18_2026-11-09_2056.md | 6b10854d0b83439f8a19f12a1466ef28e7456f9bc3ee8fab32982948cc000ffe |
| PP audit of E20/D6 | FINDINGS_PP_AUDIT_NL_E20_AND_D6_2026-11-09_2123.md | 2252cafc7b2281372dce5f30d71b1d62dc0977f64ffd2ab2e91bdc76aafb6eb3 |
| PP 6-basis D5 script | /workspace/pp_e68_2040/d5basis.py | 726852ba316f88cfc8709a2f5e2e12c74e255cb6da77251f817a490e9857fc80 (recomputed; no sidecar checked) |

## Part A — ff7fb67f per PP 3f1749e1 (all seven fixes ACCEPTED, none disputed)
- **A1 (fix 1, tally).** The header "8/5/2/0 = 15" was a slip; ff7fb67f's own row labels give **9/4/2/0 = 15**. Adopting PP's grade: row 9 (|Aut⁺| = 48, GL(2,3) order statistics {1:1, 2:13, 3:8, 4:6, 6:8, 8:12}; H⁰(K²)^{Aut⁺} = 0) moves **COND → PROVED** on PP's exact ℚ(ζ₈) closure (3f1749e1) plus eb979fda. MR2's own float run alone stays COND evidence. **Corrected tally: PROVED 10 · COND 3 · OPEN 2 · REF 0 = 15.** PROVED: 1, 2, 3, 4, 5, 7, 8, 9, 10 (decomposition), 11 (identity); COND: 6, 12, 13; OPEN: 14, 15.
- **A2 (fix 2, D3).** D3 is replaced by: "Boundary falloffs z^{4−Δ} and z^{Δ} (z → 0). For the 12 mode (Δ = 6), 4−Δ = −2. For w (m²L² = 0, Δ = 4), the second-order exponents are {0, 4}." The [N4] log label "{Delta-4? i.e. 4-Delta, -Delta}" (RUN2 lines 8–9) and the [Z1] template text (line 14) are **cosmetic**; no claim uses them.
- **A3 (fix 3, row 7).** Row 7 reads "**PROVED as implication of (P1)–(P2)**". The J-sign table (−1)^{m−q} (K^m ⊗ V^q ≅ K^{m−q}, V ≅ TΣ ≅ K⁻¹, dJ = −1) is a **necessary condition at J-fixed (Weierstrass) points**, not a global invariance criterion. "All truncation modes survive" is not unconditional; it holds given (P1)–(P2).
- **A4 (fix 4, row 11) split.**
  - 11a **PROVED (identity):** 4 + 2j(j+3) + 2j(j+1) = 4(j+1)², hence Δ₂ = 2j+4. (Check: LHS = 4 + 4j² + 8j = 4(j+1)².)
  - 11b **COND:** identification of this family with the Chen–Gutperle–Uhlemann n = 0 universal family (arXiv 1903.07109; citation, not derived).
  - Row count unchanged (15): row 11 counts by 11a; 11b is recorded as an attached COND sub-statement and is not a 16th row. (If PP prefers a separate row, the tally becomes 10/4/2/0 = 16.)
- **A5 (fix 5, row 13 / RA-6).** Truncation statement **PROVED (implication of the CGR Lagrangian):** min m²L² = −4 = −d²/4 at d = 4, so the BF bound is **saturated, not violated**; lowest vector 0. **Full-spectrum statement COND** (cited SUSY ⇒ unitarity). Row 13 keeps COND for the tally (its full-spectrum part).
- **A6 (fix 6, row 10).** Decomposition (invariant 1-forms = df ⊕ *dg, f, g Aut⁺-invariant) **PROVED**. Lowest invariant Laplace value 23.0786 **COND (FEM)**. The **5D masses of these Σ-vectors are OPEN** (they belong to row 14).
- **A7 (fix 7, row 5).** Row 5 now lists as a **stated premise** CGR's χ decoupling (CGR (B.7)/(B.12)/(6.3)), not re-derived by MR2 or PP. Row 5 stays PROVED as an implication of CGR (3.7), (6.3) and that premise: 4 massless (A(1) + 3 F^{αβ}), χ triplet at m²L² = 8 (Δ = 5).
- **A8 (logs).** The empty file …_2026-11-09.log (e3b0c442…, 0 B, the empty-string hash; mtime 20:39:56.518, 8 ms after the .py) is from a first invocation that never ran (exit 127). It **supports no claim** and is kept under the never-overwrite rule. The real run log is …_RUN2.log (82a3d947…), which PP reproduced byte-identically.
- **A9 (bd32b4e2 header time).** MR2_MN2_KK_A_SCALAR_VECTOR_STATUS_AND_ERRATA_2026-11-09.md says "Written 20:33 CST"; its mtime is **20:31:32 CST**. Read it as "≈20:31". No content change.

## Part B — 1aa88a30 / 68f082e9 per PP 5abd02c6 (R1–R3 ACCEPTED)
- **R1 (D5 attribution).** In 68f082e9 (B2, D5 bullet), "This agrees with PP G6, against NL's −σ/2" is replaced by: "**+σ/2, agreeing with PP G6 and with NL E19-15 (d3dd5a4c), which corrected the 2017 −σ/2**." NL E19 (20:29:37) predates 68f082e9 (20:37:46), so the old attribution was stale. Per-NL D5 row (1aa88a30 line 158 and 68f082e9 line 92) now reads: "**D5 | NL: COND on H_Σ, sign +σ/2 (E19-15 PROVED; NL E20-3 restates its analytic chain) | MR2: concur**." No grade changes (NL's D5 stays COND on H_Σ; MR2's N18 sign result stays PROVED).
- **R2 (B3 notation).** In 68f082e9 B3 and 1aa88a30 N8 (b), the constituent tensions are renamed **τ_i**: a_eff := ∂_φ ln τ_i, to avoid a clash with the scalar matrix T = diag(e^{−6λ}, e^{−6λ}, e^{4λ+w}, e^{4λ+w}, e^{4λ−2w}). Content unchanged: ∂_φT = 0, ∂_φΔ = 0, det T = 1, so a_eff ≤ −2 carries over; N8 PROVED as an implication.
- **R3 (N18 evidence).** N18 (D5 = +σ/2) is PROVED on the hand derivation. Confirmation evidence: MR2's 3 random-ω exact Clifford trials (3 of 6 dimensions) **and PP's exact check on all 6 basis 2-forms ω_ij, 0 failures** (/workspace/pp_e68_2040/d5basis.py, 726852ba316f88cf…; the identity is linear in ω, so the basis check covers all ω).
- **B-note (NL E20 and PP 2252cafc).** NL E20 (6b10854d) **accepted Z1** (E20-5, PROVED, exact; PP rerun byte-identical: m²L² = {12, −4, 0}, w exponents {0, 4}, ∂³_wV = −24·2^{2/3}g²) and **Z2** (E20-6, OPEN: one-sided centre-manifold flows w ≈ −1/(2^{2/3}g²L·r), not W-flows). Under E20-7 (PP: PROVED as a scoping implication) NL **re-scoped P1, P3, D3, B6 and the K7 / E19-9 no-wall result to "level 0 with W-flow kept sides"**; outside that scope they are OPEN, in both [χU] and [χS]. This matches MR2's N8 restriction (W₃-flow kept sides) and N16 (Z2 OPEN). PP's D6-6 adds c = 2^{4/3}g (= 2^{2/3}g²L) > 0 and the exact slaving (δφ, δλ) = (1/5, 13/30)w², leading order PROVED with existence via the cited centre-manifold theorem as a premise; Z2 stays OPEN. MR2 grades unchanged.

## Tallies after this erratum
- ff7fb67f: **10 / 3 / 2 / 0 = 15** (was header 8/5/2/0, rows 9/4/2/0).
- BPS cross-check (1aa88a30 + 68f082e9): **14 / 2 / 1 / 1 = 18**, unchanged (PP 5abd02c6 confirmed). R1–R3 are wording/evidence only.
- This file's own new claims: none beyond the A4 split (11a PROVED identity, 11b COND citation) and A5's split (truncation PROVED / full COND), both counted inside ff7fb67f's 15 rows.

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (checked 21:28 CST), untouched.
